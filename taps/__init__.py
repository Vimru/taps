import configparser
from taps.config import *
import os
import pkg_resources

# Read config file. If doesn't exist, use defaults.
user_config = configparser.ConfigParser()

# Package data file location.
PKG_DATA_CONF = pkg_resources.resource_filename("taps", "taps.conf")

if os.path.exists(USER_CONFIG):
    user_config.read(USER_CONFIG)
    # Check /etc/taps.conf config is correct.
    for setting in ["Color", "White", "Amber", "Green", "Red"]:
        if setting not in user_config["COLORS"]:
            print("Invalid configuration file format. Defaulting to template.")
            user_config.read(PKG_DATA_CONF)
            break
elif os.path.exists(PKG_DATA_CONF):
    user_config.read(PKG_DATA_CONF)
else:
    print("Fatal: Template config file not found at install location.")
    exit()


