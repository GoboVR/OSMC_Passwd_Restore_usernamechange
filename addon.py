"""
    Plugin for to factory restore gobo user password
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
__plugin__ = "Factory restore gobo user password "
__author__ = "Orignail: Zjoasan Fork: Gobo and Gemini AI"
__url__ = "https://osmc.tv/"
__git_url__ = "https://github.com/GoboVR/OSMC_Passwd_Restore_usernamechange"
__credits__ = "Orignail: Zjoasan Fork: Gobo and Gemini AI"
__version__ = "0.0.1"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.Gobo_pw_restore')

os.system("/bin/echo -e 'gobo\ngobo' | /usr/bin/sudo /usr/bin/passwd gobo") # Changed line
time.sleep(5)
dialog.ok("Password restored", "Now the password for gobo user has been restored to factory default.") # Changed dialog message
