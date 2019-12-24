from taps.config import *
from taps.text_format import genColorText
import taps.pacman as pacman
from taps import user_config
import re

def genString(vuln_item, attribute, optionalArg):
    color = user_config["COLORS"]["Green"]
    if vuln_item[attribute]:
        if attribute == "ticket":
            # Create URL.
            value = ARCH_BUG_ADDR + vuln_item[attribute]
        elif attribute == "advisories":
            # Create URL.
            value = "\n\t\t       ".join([ARCH_SEC_ADDR + ASA for ASA in vuln_item[attribute]])
        elif attribute == "name":
            # Create URL and output 'group' over 'name'.
            value = vuln_item["name"] + " (" + ARCH_SEC_ADDR + vuln_item[attribute] + ")"
            attribute = "group"
        elif attribute == "fixed":
            color = user_config["COLORS"]["Amber"]
            installed_pkgs = optionalArg
            # Package has patch. Find the installed package.
            for pkg in vuln_item["packages"]:
                if pkg in installed_pkgs:
                    value = "vulnerability was patched in " + vuln_item[attribute] + " (" + installed_pkgs[pkg] + " installed)"
                    break
        elif attribute == "issues":
            # Tabs and whitespace keep each CVE item inline.
            value = "\n\t\t       ".join([CVE + " (" + ARCH_SEC_ADDR + CVE + ")" for CVE in vuln_item[attribute]])
        elif attribute == "references":
            color = user_config["COLORS"]["White"]
            # Show CVEs, references and descriptions for each CVE. Requires to build a nested => output.
            output_lines = []
            for cve in vuln_item["issues"]:
                output_lines.append("\n   => " + cve + " (" + ARCH_SEC_ADDR + cve + ")")
                output_lines.append(("\t=> description : ").expandtabs(7) + vuln_item["issues"][cve]["description"])
                references = "\n\t\t       ".join([reference for reference in vuln_item["issues"][cve][attribute]])
                output_lines.append(("\t=> references : ").expandtabs(7) + references)
            value = "\n".join(output_lines)
            attribute = "issues"
        elif attribute == "required by":
            # Show the required by attribute of a package. Requires to build a nested => output.
            color = user_config["COLORS"]["White"]
            pacman_cmd = optionalArg
            value = ""
            for pkg in vuln_item["packages"]:
                command_output = pacman.pacmanCommand(pacman_cmd + " " + pkg)
                if command_output:
                    # Use regex to get packages form command_output.
                    requiredby_packages = re.findall(REGEX, command_output)
                    value += ("\n\t=> " + pkg + ": ").expandtabs(7) + " ".join(requiredby_packages)
        elif attribute == "affected":
            # Add current installed version to output.
            installed_pkgs = optionalArg
            # Find the installed package.
            for pkg in vuln_item["packages"]:
                if pkg in installed_pkgs:
                    value = vuln_item[attribute] + " (" + installed_pkgs[pkg] + " installed)"
                    break
                value = vuln_item[attribute]
        else:
            value = vuln_item[attribute]

        string = genColorText(("   => " + attribute + "\t : ").expandtabs(10) + value, color)
    else:
        string = None
    return string
