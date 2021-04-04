"""
    Plugin for to factory restore osmc user password
"""

# -*- coding: UTF-8 -*-
# main imports
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon
import time

# plugin constants
__plugin__ = "Factory restore osmc user password "
__author__ = "Zjoasan"
__url__ = "https://osmc.tv/"
__git_url__ = "https://https://github.com/zjoasan/osmc_passwd_restore"
__credits__ = "Zjoasan"
__version__ = "0.0.1"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.OSMC_pw_restore')

os.system("/bin/echo -e 'osmc\nosmc' | /usr/bin/sudo /usr/bin/passwd osmc")
time.sleep(5)
dialog.ok("Password restored", "Now the password for osmc user has been restored to factory default.")
