#!/usr/bin/python

# Copyright Hugh Perkins 2009
# hughperkins@gmail.com http://manageddreams.com
#
# This program is free software; you can redistribute it and/or aiify it
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

import cgitb; cgitb.enable()
import cgi

from utils import *
from core import *

dbconnection.connectdb()

loginhelper.processCookie()

menu.printPageTop()

if loginhelper.gusername == '':
   print "You must login first"
else:
   botrunnername = formhelper.getValue('botrunnername')
   sharedsecret = formhelper.getValue('sharedsecret')

   if botrunnername != None and sharedsecret != None and botrunnername != '' and sharedsecret != '':

      rows = dbconnection.cursor.execute( "insert into botrunners "\
         "( botrunner_name,botrunner_owneraccountid, botrunner_sharedsecret ) "\
         " select %s, account_id, %s from "\
         " accounts where username = %s ",
         ( botrunnername,sharedsecret, loginhelper.gusername, ) )
      if rows == 1:
         print "Added ok"
      else:
         print "Something went wrong.  Please check your values and try again."
   else:
      print "Please fill in the fields and try again"

dbconnection.disconnectdb()

menu.printPageBottom()
