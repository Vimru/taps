import configparser
from taps.config import *
import os

# Read config file. If doesn't exist, use defaults.
user_config = configparser.ConfigParser()

if os.path.exists(USER_CONFIG):
    user_config.read(USER_CONFIG)
elif os.path.exists("taps.conf"):
    user_config.read("taps.conf")
else:
    print("Fatal: Template config file not found at install location.")
