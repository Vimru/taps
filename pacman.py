from config import *
from text_format import printColor
import subprocess

def pacmanCommand(cmd):
    try:
        command_output = subprocess.run(cmd.split(), capture_output=True)
    except Exception as e:
        printColor("Fatal error while using pacman:", RED)
        printColor(e, RED)
        exit()

    # Check for errors.
    if command_output.stderr:
        printColor("Error occurred while running " + cmd + ": " + command_output.stderr.decode("utf-8"), RED)
        if "was not found" in command_output.stderr.decode("utf-8"):
            printColor("This might have been caused by the package belonging to the multilib repository: https://wiki.archlinux.org/index.php/Official_repositories#Enabling_multilib", AMBER)
        return
    return command_output.stdout.decode("utf-8")

def installedPackagesVersions():
    return pacmanCommand(PACMAN_INSTALLED_VER_CMD).split("\n")

def installedPackages():
    return pacmanCommand(PACMAN_INSTALLED_CMD).split("\n")

def allRepoPackages():
    return pacmanCommand(PACMAN_ALL_PKGS_CMD).split("\n")

def vercmp(version1, version2):
    return int(pacmanCommand(PACMAN_VERCMP_CMD + " " + version1 + " " + version2))

