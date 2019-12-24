ARCH_SEC_ADDR = "https://security.archlinux.org/"
ARCH_SEC_ADDR_JSON = ARCH_SEC_ADDR + "vulnerable.json"
ARCH_SEC_ADDR_ALL_JSON = ARCH_SEC_ADDR + "issues.json"
ARCH_BUG_ADDR = "https://bugs.archlinux.org/task/"
PACMAN_LOCAL_CMD = "pacman -Qi"
PACMAN_ALL_CMD = "pacman -Sii"
PACMAN_INSTALLED_CMD = "pacman -Qq"     # Used to be pacman -Qnq
PACMAN_INSTALLED_VER_CMD = "pacman -Q"  # Used to be pacman -Qn
PACMAN_ALL_PKGS_CMD = "pacman -Ssq"
PACMAN_VERCMP_CMD = "vercmp"
REGEX = "(?<=Required By     : )(.+)"
ATTRIBUTES = ["name", "affected", "severity", "type", "ticket", "advisories"]

USER_CONFIG = "/etc/taps.conf"
VERSION = "1.0.0"
