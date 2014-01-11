#   Copyright (C) 2011 Jason Anderson
#
#
# This file is part of PseudoTV.
#
# PseudoTV is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PseudoTV is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PseudoTV.  If not, see <http://www.gnu.org/licenses/>.

import os
import xbmc, xbmcgui
import xbmcaddon
import httplib
import urllib
import urllib2 
import sys, re
import shutil

from resources.lib.Globals import *
from urllib import urlopen

# Script constants
__scriptname__ = "PseudoTV Live"
__author__     = "Lunatixz, Jason102 & Angrycamel"
__url__        = "https://github.com/Lunatixz/script.pseudotv.live"
__settings__   = xbmcaddon.Addon(id='script.pseudotv.live')
__cwd__        = __settings__.getAddonInfo('path')


# Adapting a solution from ronie (http://forum.xbmc.org/showthread.php?t=97353)
if xbmcgui.Window(10000).getProperty("PseudoTVRunning") != "True":
    xbmcgui.Window(10000).setProperty("PseudoTVRunning", "True")
    shouldrestart = False

#    if xbmc.executehttpapi("GetGuiSetting(1, services.webserver)")[4:] == "False":
#        try:
#            forcedserver = __settings__.getSetting("ForcedWebServer") == "True"
#        except:
#            forcedserver = False

#        if forcedserver == False:
#            dlg = xbmcgui.Dialog()
#            retval = dlg.yesno('PseudoTV', 'PseudoTV will run more efficiently with the web', 'server enabled.  Would you like to turn it on?')
#            __settings__.setSetting("ForcedWebServer", "True")

#            if retval:
#                xbmc.executehttpapi("SetGUISetting(3, services.webserverport, 8152)")
#                xbmc.executehttpapi("SetGUISetting(1, services.webserver, true)")
#                dlg.ok('PseudoTV', 'XBMC needs to shutdown in order to apply the', 'changes.')
#                xbmc.executebuiltin("RestartApp()")
#                shouldrestart = True

    if shouldrestart == False:
        if REAL_SETTINGS.getSetting("ClearBCT") == "true":
            Path1 = (xbmc.translatePath(os.path.join(BCT_LOC)))
            
            if os.path.exists(Path1):
                shutil.rmtree(BCT_LOC)
                REAL_SETTINGS.setSetting('ClearBCT', "false")
            else:
                REAL_SETTINGS.setSetting('ClearBCT', "false")

                
        if REAL_SETTINGS.getSetting("Donor_Enabled") == "true" and REAL_SETTINGS.getSetting("Donor_Update") == "true":   
            try:
                UserPass = REAL_SETTINGS.getSetting('Donor_UP')
                flename1 = 'Donor.py'
                flename2 = 'Donor.pyo'
                URL = ('http://'+UserPass+'@ptvl.comeze.com/strms/')
                Path1 = (xbmc.translatePath(os.path.join('special://home/addons/script.pseudotv.live/resources/lib/')))
                Path2 = (xbmc.translatePath(os.path.join('special://home/addons/script.pseudotv.live-master/resources/lib/')))
                urlPath = (URL + flename2)
                
                if os.path.exists(Path1):
                    flePath1 = (Path1 + flename1)
                else:
                    flePath1 = (Path2 + flename1)
                
                if os.path.exists(Path1):
                    flePath2 = (Path1 + flename2)
                else:
                    flePath2 = (Path2 + flename2)
                try:
                    os.remove(flePath1)
                    os.remove(flePath2)
                except:
                    pass
                urllib.urlretrieve(urlPath, flePath2)
                xbmc.log('script.pseudotv.live - Updating Donor.pyo')
                REAL_SETTINGS.setSetting('Donor_Update', "false")
                xbmc.executebuiltin('RunScript("' + __cwd__ + '/pseudotv.py' + '")')
            except:
                xbmc.executebuiltin('RunScript("' + __cwd__ + '/pseudotv.py' + '")')
                xbmc.log('script.pseudotv.live - Updating Donor.py - ::EXCEPTION::', xbmc.LOGERROR)
        else:
            xbmc.executebuiltin('RunScript("' + __cwd__ + '/pseudotv.py' + '")')
    else:
        xbmc.log('script.pseudotv.live - Already running, exiting', xbmc.LOGERROR)
