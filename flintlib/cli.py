# flint - Sam's general purpose resume generation tool
# Copyright (C) 2010 Sam Hart (hartsn@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import getopt
import cli_util
import os

from flintlib.config import Config as flintConfig

# Callbacks

def cli_help(pre_options, pre_args, command, post_options):
    """
    Given a flint command, will print detailed help for that
    command from the option_dispatch.
    """
    # FIXME
    # The following assumes the user entered a valid command
    # and will crash if an invalid command is given
    # Additionally, do we really want to allow for multiple
    # helps in one command line?
    if post_options:
        for com in post_options:
            print option_dispatch[com].usage
            print
            print option_dispatch[com].summary
            print
            for line in option_dispatch[com].desc:
                print line
    else:
        print option_dispatch[None].usage
        print option_dispatch[None].summary
        print
        for line in option_dispatch[None].desc:
            print line
        print
        for com in option_dispatch.keys():
            if com:
                print "   %s%s%s" % (com, cli_util.space_filler(com, 20),
                        option_dispatch[com].summary)

def cli_init(pre_options, pre_args, command, post_options):
    '''
    Command line init method
    '''
    verbose = 0
    force = False
    working_dir = os.getcwd()
    resume_name =  os.path.split(working_dir)[-1]
    if post_options:
        working_dir = post_options[0]
        resume_name = working_dir

    for o, a in pre_options:
        if o in ("-v", "--verbose"):
            verbose = verbose + 1
        if o in ("-f", "--force"):
            force = True

    config = flintConfig(working_dir, force)
    config.create(resume_name)
    # Now, edit the config file
    (bhash, ahash, bsize, asize) = cli_util.launch_editor(config.config_file)

class Command:
    def __init__(self, short_opts, long_opts, usage, summary, desc, callback):
        self.short_opts = short_opts
        self.long_opts = long_opts
        self.usage = usage
        self.summary = summary
        self.desc = desc
        self.callback = callback

option_dispatch = {
    None : Command(
        None,
        None,
        'Flint',
        'Flint resume generation tool',
        ['basic commands, use "help" to get more details.'],
        cli_help),
    'init' : Command(
        ['v', 'f'],
        ['verbose', 'force'],
        'flint [OPTIONS] init [DEST]',
        'Initialize a flint source archive in given directory',
        ['  Initializes a flint source archive. Will use the',
         '  [DEST] directory for the archive, or the current',
         '   directory if nothing is specified.',
         '',
         '  OPTIONS:',
         '  -v|--verbose    Be verbose about actions',
         "  -f|--force      Force even if directory isn't empty"],
        cli_init),
    'help' : Command(
        None,
        None,
        'flint help [COMMAND]',
        'Gives help for flint',
        ['   If called with no [COMMAND], will give general help',
         '   and exit. Otherwise, will print help for [COMMAND].'],
         cli_help),

}

def cli_parse(argv):
    """
    Parse the command line options
    """
    pre_opt = []
    command = None
    post_opt = []
    stage = 0
    for option in argv:
        if stage == 0:
            if option in option_dispatch.keys():
                stage = 1
                command = option
            else:
                pre_opt.append(option)
        else:
            post_opt.append(option)

    short_opts = ''
    long_opts = []
    if option_dispatch[command].short_opts:
        for a in option_dispatch[command].short_opts:
            short_opts = short_opts + a

    if option_dispatch[command].long_opts:
        long_opts = option_dispatch[command].long_opts

    opts, args = getopt.getopt(pre_opt, short_opts, long_opts)

    return (opts, args, command, post_opt)

def run(argv):
    '''
    Main entrance to the flint cli
    '''
    (pre_options, pre_args, command, post_options)= cli_parse(argv)
    option_dispatch[command].callback(pre_options, pre_args, command, post_options)
