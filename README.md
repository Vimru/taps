# taps
### True arch package security

taps aims to make it easier to see the vulnerability status & details for your packages, query packages for past vulnerabilities, and make official Arch security data easier to access.

 - [Features](#features)
 - [Installation](#installation)
 - [Usage](#usage)
 - [Examples, tips & tricks](#examples-tips--tricks)
 - [Dependencies](#dependencies)
 - [FAQ](#faq--possible-questions-about-why-taps-works-as-it-does)
 - [False positives & false negatives](#false-positives--false-negatives)

## Features
 - Easy-to-read overview of your vulnerable packages
 - Show past vulnerabilities of packages
 - Search package(s) for current or past vulnerabilities, view multiple items at once
 - Includes links to AVGs, Arch Security Advisories, tickets and CVEs
 - Identify if patches are available for a vulnerable installed package
 - Identify packages which have vulnerable dependencies
 - Show CVE information
 - Hide attributes you don't want to see
 - Optional color output
 - Simple, quick and easy to use
   - [audit mode takes around 500ms - 3s](https://github.com/Vimru/taps/blob/master/README.md#faq--possible-questions-about-why-taps-works-as-it-does)
   - query mode takes around 500 - 1000ms
 - Show as little or as much information as you need

## Installation
**Stable release with pip:**

As a non-root user:

	$ pip install --user taps
	$ sudo ln -s ~/.local/bin/taps /usr/bin/taps

As root:

(This is a security risk as you are running `setup.py` as root).

	# pip install taps

**Development version:**

(This is an unreleasable version likely to be unstable).

	$ git clone https://github.com/Vimru/taps && cd taps
	$ pip install --user .
	$ ln -s ~/.local/bin/taps /usr/bin/taps

### Config file

You can make a config file by copying the template file in the repository (taps.conf) to /etc/taps.conf with the appropriate read permissions. The individual colors have to be valid names for use with 'colorful'.

If you don't make a config file or its contents cannot be interpreted, taps will use its default settings from the template config file.

## Usage
	$ taps -h
	usage: taps.py [-h] [-r] [-n NUM_OUTPUT] [--hide HIDE] [-q] [-c] [-v] [-m] [-o] {audit,query} ...

	Find your vulnerable packages, information from security.archlinux.org, and more!

	optional arguments:
	  -h, --help            show this help message and exit
	  -r, --required        Show the 'required by' attribute of the packages (dependencies)
	  -n NUM_OUTPUT, --num-output NUM_OUTPUT
							The number of vulnerability items to print out
	  --hide HIDE           The attributes to hide, separated by commas (no spaces).
	  -q, --quiet           Only print package names.
	  -c, --cve             Show CVE names and links. Use with -v for detailed information.
	  -v, --verbose         Output information about specific versions where possible, CVE descriptions and links to
				references for CVEs if -c option used. WARNING: passing both -v and -c options will take
				significantly longer to process due to fetching individual CVE data.
	  -m, --monochrome      Don't use colors.
	  -o, --one-at-time     Show one item at a time, press enter to show next.

	Available modes:
	  {audit,query}
		audit               Identify any installed packages with vulnerabilities, determine if patches are available.
							Use -h for more information.
		query               Query past and existing package vulnerabilities. Use -h for more information.<br>
<br>

	$ taps audit -h
	usage: taps.py audit [-h] [-p]

	Show whether any installed packages have vulnerabilities and determine if
	patches are available. Versions are checked in case you haven't updated in a
	while and have missed security updates.

	optional arguments:
	  -h, --help         show this help message and exit
	  -p, --patched      Show only packages with available patch updates
	  -s, --skip-checks  Skip checks for available patches, will only check current vulnerabilities. This will increase
			     the speed of audit mode, but could potentially miss vulnerabilities and can only be used safely
			     after a -Syu upgrade.
<br>
	 
	$ taps query -h
	usage: taps.py query [-h] [-p PACKAGES [PACKAGES ...]] [-i] [-f]

	Show information for vulnerable (or fixed) packages from
	security.archlinux.org. Without any arguments, 'query' will show current
	vulnerabilities for all arch packages.

	optional arguments:
	  -h, --help            show this help message and exit
	  -p PACKAGES [PACKAGES ...], --packages PACKAGES [PACKAGES ...]
				Package(s) to show vulnerabilities for.
	  -i, --installed       Only show vulnerabilities for installed packages.
	  -f, --fixed           Show fixed vulnerablities as well as current
				vulnerabilities.

## Examples, tips & tricks

taps has two modes:

**audit**: used to audit the security of installed packages, identify vulnerabilities and detect available patches.

**query**: query past and existing package vulnerabilities with https://security.archlinux.org and search specific packages

Each mode is used as follows ("optional arguments" for both modes (`taps -h`) have to be put *before* the mode):

    $ taps -q audit
    $ taps -q query
    
See the help pages for more information:

    $ taps audit -h
    $ taps query -h

**View overview of your vulnerable packages:**
	
	$ taps audit
	nasm 
	   => group          : AVG-903 (https://security.archlinux.org/AVG-903
	   => affected       : 2.14.02-1 (2.14.02-1 installed)
	   => severity       : High
	   => type           : arbitrary code execution

	openjpeg2 
	   => group          : AVG-864 (https://security.archlinux.org/AVG-864
	   => affected       : 2.3.1-1 (2.3.1-1 installed)
	   => severity       : Low
	   => type           : denial of service

	[...]
    
**Only show vulnerable packages with available patches:**

    $ taps audit -p
    
**View current vulnerabilities for all packages (not just installed ones):**
    
    $ taps query
    
**View current vulnerabilities only for installed packages:**
    
    $ taps query -i
    
**Show one vulnerability item at a time, press enter for next:**

    $ taps -o query

**View the number of total vulnerabilites a package has had:**
	
    $ taps -q query -fp firefox | wc -l
    32

**Find current vulnerabilities for specified packages:**
 
    $ taps query -p glibc firefox
   
**Show which packages installed on your system use a vulnerable package as a dependency / the package's "required" by data:**

	$ taps -r audit
	openjpeg2 
	   => group          : AVG-864 (https://security.archlinux.org/AVG-864
	   => affected       : 2.3.1-1 (2.3.1-1 installed)
	   => severity       : Low
	   => type           : denial of service
	   => required by    : 
	       => openjpeg2: ffmpeg  ghostscript  gst-plugins-bad  poppler  webkit2gtk

	libmp4v2 
	   => group          : AVG-848 (https://security.archlinux.org/AVG-848
	   => affected       : 2.0.0-5 (2.0.0-5 installed)
	   => severity       : Low
	   => type           : denial of service
	   => required by    : 
	       => libmp4v2: faac
	[...]

**Show the first 2 vulnerability items:**

	$ taps -n2 audit
	nasm 
	   => group          : AVG-903 (https://security.archlinux.org/AVG-903
	   => affected       : 2.14.02-1 (2.14.02-1 installed)
	   => severity       : High
	   => type           : arbitrary code execution

	openjpeg2 
	   => group          : AVG-864 (https://security.archlinux.org/AVG-864
	   => affected       : 2.3.1-1 (2.3.1-1 installed)
	   => severity       : Low
	   => type           : denial of service

   
**Find current & fixed vulnerabilities for specified packages:**

(-n4 used here to limit output)

	$ taps -n4 query -fp glibc sudo
	glibc 
	   => group          : AVG-368 (https://security.archlinux.org/AVG-368
	   => affected       : 2.25-7 (2.30-3 installed)
	   => severity       : Critical
	   => type           : multiple issues

	sudo 
	   => group          : AVG-1047 (https://security.archlinux.org/AVG-1047
	   => affected       : 1.8.27-1 (1.8.29-1 installed)
	   => severity       : High
	   => type           : privilege escalation
	   => advisories     : https://security.archlinux.org/ASA-201910-9

	glibc 
	   => group          : AVG-855 (https://security.archlinux.org/AVG-855
	   => affected       : 2.29-4 (2.30-3 installed)
	   => severity       : High
	   => type           : information disclosure
	   => advisories     : https://security.archlinux.org/ASA-201911-3

	lib32-glibc, glibc 
	   => group          : AVG-590 (https://security.archlinux.org/AVG-590
	   => affected       : 2.26-10
	   => severity       : High
	   => type           : privilege escalation
	   => advisories     : https://security.archlinux.org/ASA-201801-18
			       https://security.archlinux.org/ASA-201801-19
		       
**Use the verbose option, -v or --verbose, to show the version which fixed a vulnerability (or if not fixed, say it's vulnerable):**

This could be useful if you wanted to find every vulnerability a package has had, and taps can show you which of the vulnerabilities are fixed or not.

	$ taps -v query -fp nasm
	nasm (vulnerable)
	   => group          : AVG-903 (https://security.archlinux.org/AVG-903
	   => affected       : 2.14.02-1 (2.14.02-1 installed)
	   => severity       : High
	   => type           : arbitrary code execution

	nasm (fixed in 2.14.02-1)
	   => group          : AVG-852 (https://security.archlinux.org/AVG-852
	   => affected       : 2.14-1 (2.14.02-1 installed)
	   => severity       : Medium
	   => type           : denial of service
	   => advisories     : https://security.archlinux.org/ASA-201901-16

**Use -v and -c together to show detailed information about CVEs:**

	$ taps -vc query -p python-django
	python-django (vulnerable)
	   => group          : AVG-1070 (https://security.archlinux.org/AVG-1070
	   => affected       : 2.2.6-2
	   => severity       : Low
	   => type           : privilege escalation
	   => issues         : 
	   => CVE-2019-19118 (https://security.archlinux.org/CVE-2019-19118)
	       => description : A privilege escalation issue has been found in Django since 2.1 and before 2.2.8 or 2.1.15, where a user who lacks permission to edit a model should not be able to trigger its save-related signals.
	       => references : https://www.djangoproject.com/weblog/2019/dec/02/security-releases/
			       https://github.com/django/django/commit/36f580a17f0b3cb087deadf3b65eea024f479c21

**Be alerted if a package version is outdated and a patch is available:**

(For demonstration purposes taps thinks glibc version 1.0 is installed)

	taps audit
	glibc 
	   => group          : AVG-368 (https://security.archlinux.org/AVG-368
	   => affected       : 2.25-7 (1.0 installed)
	   => severity       : Critical
	   => type           : multiple issues
	   => fixed          : vulnerability was patched in 2.26-1 (1.0 installed)

	glibc 
	   => group          : AVG-855 (https://security.archlinux.org/AVG-855
	   => affected       : 2.29-4 (1.0 installed)
	   => severity       : High
	   => type           : information disclosure
	   => advisories     : https://security.archlinux.org/ASA-201911-3
	   => fixed          : vulnerability was patched in 2.30-1 (1.0 installed)

Where possible, taps will show links (like above) for AVGs, advisories, tickets and CVEs.

**Hide attributes you don't want to see:**

	$ taps --hide name,type,affected audit
	nasm 
	   => severity       : High

	openjpeg2 
	   => severity       : Low

	libmp4v2 
	   => severity       : Low

	unzip 
	   => severity       : Low

## Dependencies
**Python modules:**

PyPI packages:

 - [colorful](https://pypi.org/project/colorful/)
 - [setuptools](https://pypi.org/project/setuptools/)

## FAQ & possible questions about why taps works as it does

**Why is audit mode slower than query mode?**

In order for audit mode to reliably determine if patches are available (an installed package version is older than the patched version), `vercmp` has to be used for many packages which is not particularly efficient. Libraries do exist for this such as [cmp_version](https://pypi.org/project/cmp_version/) and [rpm-vercmp](https://pypi.org/project/rpm-vercmp/), however they are unable to deal with some unusual version number cases, such as comparing 3.1.3pre1-1 with 3.1.3-1 and 1:3.34.0-2 with 3.20.1-1. If these libraries were used, you could come across false positives.

If you have just -Syu'd, you can probably skip these checks with -s for increased speed.

 - Default audit mode takes around 1s - 3s
 - Audit mode with skipped checks takes around 500ms - 1000ms

**Why is `pacman -Q` and `pacman -Qq` used when `pacman -Qn` would only list native packages and be more efficient?**

For *some* reason, when using the `-n` option with pacman to ignore foreign packages, pacman takes significantly longer (a few 100ms longer) to fetch results. For this reason, it is faster to iterate over some foreign packages than use `-n`.

**Which repositories are supported?**

Only the official stable repositories should be used to ensure you receive accurate information. You *can* use testing repositories, however you are likely to run into problems due to official data from security.archlinux.org only supporting official stable respositories.

## False positives & false negatives

If you think you've found a false positive or false negative being reported by taps, first check it isn't due to security.archlinux.org being outdated. Once you've checked with security.archlinux.org and confirmed the problem is with taps, feel free to [open a new issue](https://github.com/Vimru/taps/issues/new) or make a pull request.
