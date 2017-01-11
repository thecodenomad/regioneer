#!/usr/bin/python
""" Main module for starting regioneer program """

import json
import os
import sys

from regioneer.core import constants
from regioneer.core.models import load_models_from_configuration

def load_configuration_file(loc):
    """ Load a given configuration file based on the passed in location """

    if not loc:
        print("'{}' is not supported (yet?)...".format(curr_sys))
        sys.exit(1)

    # Load configuration file if exist
    if os.path.exists(conf_loc):
        with open(loc, 'r') as infile:
            conf = json.loads(infile)
            return load_models_from_configuration(conf)

    # Else Create simple configuration file
    else:
        # TODO: when a configuration file doesn't alrady exist copy over the base configuration
        pass

if __name__ == "__main__":

    # See what type of system this is
    curr_sys = os.uname().sysname.lower()
    conf_loc = constants.BASE_CONFIGS.get(curr_sys, None)

    # Load the configuration
    profiles = load_configuration_file(conf_loc)

    guessed_profiles = []
    for profile in profiles:
        if profile.is_active():
            guessed_profiles.append(profile)

    print("Guessed the following active profiles: ")
    for profile in guessed_profiles:
        print("{}".format(profile.name()))
