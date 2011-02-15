import os
from flintlib import *
from flintlib.config import Config as flintConfig

def repo_init(pre_options, pre_args, command, post_options):
    '''
    Initializes a flint repo
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

    # Check if the directory exists
    if not os.path.isdir(working_dir):
        # Go ahead and create it then
        os.mkdir(working_dir)

    config = flintConfig(working_dir, force)
    if not os.path.isdir(config.config_dir):
        os.mkdir(config.config_dir)
    config.create(resume_name)
    # Now, edit the config file
    (bhash, ahash, bsize, asize) = cli_util.launch_editor(config.config_file)

    # Make the directories
    for d in [TEMPLATE_DIRECTORY, TEMPLATE_HTML, TEMPLATE_DOCX, TEMPLATE_PDF,
              OUTPUT_DIRECTORY, OUTPUT_HTML, OUTPUT_DOCX, OUTPUT_PDF,
              ENTRY_DIRECTORY]:
        full_dir = "%s/%s" % (working_dir, d)
        if not os.path.isdir(full_dir):
            os.mkdir(full_dir)
