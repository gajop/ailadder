#!/usr/bin/python

# Copyright Hugh Perkins 2009
# hughperkins@gmail.com http://manageddreams.com
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
# You should have received a copy of the GNU General Public License along
# with this program in the file licence.txt; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-
# 1307 USA
# You can find the licence also on the web at:
# http://www.opensource.org/licenses/gpl-license.php
#

# webservice for use through xmlrpclib

import SimpleXMLRPCServer
import sys
import os
import datetime

from utils import *
from core import *

import config

class AILadderService:
   # return (True,'') if goes ok, otherwise (False,message)
   def ping(self, botrunnername, sharedsecret, status):
      if not botrunnerhelper.validatesharedsecret(botrunnername, sharedsecret):
         return (False, "Not authenticated")

      dbconnection.dictcursor.execute("update botrunners " \
         " set botrunner_lastpingstatus = %s, "\
         " botrunner_lastpingtime = %s " \
         " where botrunners.botrunner_name = %s  ",
         ( status, dates.dateTimeToDateString( datetime.datetime.now() ), botrunnername ) )
      return (True,'')

   # return (True,'') if goes ok, otherwise (False,message)
   # needs to pass as string, since xmlrpc doesn't support long :-/
   def registersupportedmap( self, botrunnername, sharedsecret, mapname, maparchivechecksum_string ):
      if not botrunnerhelper.validatesharedsecret(botrunnername, sharedsecret):
         return (False, "Not authenticated")

      if not maphelper.addmapifdoesntexist(mapname, long(maparchivechecksum_string)):
         return (False, "Couldn't register map")

      if not maphelper.setbotrunnersupportsthismap( botrunnername, mapname ):
         return (False, "couldn't mark map as supported for botrunner")

      return (True,'')

   # return (True,'') if goes ok, otherwise (False,message)
   # needs to pass as string, since xmlrpc doesn't support long :-/
   def registersupportedmod( self, botrunnername, sharedsecret, modname, modarchivechecksum_string ):
      if not botrunnerhelper.validatesharedsecret(botrunnername, sharedsecret):
         return (False, "Not authenticated")

      if not modhelper.addmodifdoesntexist(modname, long(modarchivechecksum_string)):
         return (False, "Couldn't register mod")

      if not modhelper.setbotrunnersupportsthismod( botrunnername, modname ):
         return (False, "couldn't mark mod as supported for botrunner")

      return (True,'')

   def registersupportedai( self, botrunnername, sharedsecret, ainame, aiversion ):
      if not botrunnerhelper.validatesharedsecret(botrunnername, sharedsecret):
         return (False, "Not authenticated")

      if not aihelper.addaiifdoesntexist(ainame, aiversion):
         return (False, "Couldn't register ai")

      return (True,'')

   def getsupportedmods( self, botrunnername, sharedsecret ):
      return modhelper.getsupportedmods(botrunnername)

   def getsupportedmaps( self, botrunnername, sharedsecret ):
      return maphelper.getsupportedmaps(botrunnername)

   def getsupportedais( self, botrunnername, sharedsecret ):
      return aihelper.getsupportedais(botrunnername)

handler = SimpleXMLRPCServer.CGIXMLRPCRequestHandler()
handler.register_instance( AILadderService() )
handler.register_introspection_functions()

dbconnection.connectdb()
try:
   handler.handle_request()
except:
   print str( sys.exc_value )

dbconnection.disconnectdb()

