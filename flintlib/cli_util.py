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

import os
import hashlib

def space_filler(text, size):
    """
    space_filler(text, size)
    Given text and a requested size, return empty space that,
    when added to text, will fill up to size.
    """
    a = " "
    if size > len(text):
        a = " " * (size - len(text))
    return a

class DataFileParseError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def parse_datafile(name, column_list):
    """
    Given a datafile (name) and a format for the columns (column_list) will parse
    the file and return a list of the data
    """

    parsed_list = []

    fd = file(name, 'rb')
    for line in fd.readlines():
        temp_line = line.strip()
        if len(temp_line):
            if temp_line[0] != '#':
                temp_split = temp_line.split('|')
                if len(temp_split) == len(column_list):
                    temp_parsed = {}
                    for a in range(len(column_list)):
                        temp_parsed[column_list[a]] = temp_split[a].strip()
                    parsed_list.append(temp_parsed)
                else:
                    raise DataFileParseError("Error parsing datafile %s" % name)
    fd.close()
    return parsed_list

def launch_editor(name):
    """
    Launch an external editor
    Returns:
    (bhash, ahash, bsize, asize)
    Where:
    asize = filesize after
    bsize = filesize before
    ahash = filehash after
    bhash = filehash before
    """

    bstat = os.stat(name)
    bsize = bstat.st_size
    fd = file(name, 'rb')
    bhash = md5.new(fd.read()).digest()
    fd.close()

    # TODO: Right now, we just use $EDITOR from the system environement, but later on
    # we will want to make this fancier
    editor = os.environ.get("EDITOR", "nano")
    cmd = "%s %s" % (editor, name)
    status = os.system(cmd)

    # TODO: Should do something with status

    astat = os.stat(name)
    asize = astat.st_size
    fd = file(name, 'rb')
    ahash = md5.new(fd.read()).digest()
    fd.close()

    return (bhash, ahash, bsize, asize)

def pager(name):
    """
    Given a filename, view it in some external pager
    """

    # TODO: This needs to be fixed, we ought to try various pagers
    # right now we just kind of assume less is available...
    # which is dumb :-P

    cmd = "less %s" % (name)
    status = os.system(cmd)
