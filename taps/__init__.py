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
elif os.path.exists(PKG_DATA_CONF):
    user_config.read(PKG_DATA_CONF)
else:
    print("Fatal: Template config file not found at install location.")
    exit()
