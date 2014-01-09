#   Copyright (C) 2013 Lunatixz
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

import xbmc, xbmcgui, xbmcaddon
import subprocess, os
import time, threading
import datetime
import sys, re
import random
import httplib
import base64
import Globals
import urllib2 
import shutil

from urllib import unquote
from urllib import urlopen
from xml.etree import ElementTree as ET
from xml.dom.minidom import parse, parseString
from BeautifulSoup import BeautifulSoup
from Globals import *
from Channel import Channel
from FileAccess import FileLock, FileAccess

class Donor:


    def log(self, msg, level = xbmc.LOGDEBUG):
        log('ChannelList: ' + msg, level)

    
    def logDebug(self, msg, level = xbmc.LOGDEBUG):
        if REAL_SETTINGS.getSetting('enable_Debug') == "true":
            log('ChannelList: ' + msg, level)
    