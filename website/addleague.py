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
from core.tableclasses import *

sqlalchemysetup.setup()

loginhelper.processCookie()

if loginhelper.gusername == '':
   jinjahelper.message( "You must login first" )
else:
   leaguename = formhelper.getValue('leaguename')
   modname = formhelper.getValue('modname')
   mapname = formhelper.getValue('mapname')
   nummatchesperairpair = int(formhelper.getValue('nummatchesperairpair'))

   if leaguename != None and modname != None and mapname != None and leaguename != '' and modname != '' and mapname != '':
      account = accounthelper.getAccount( loginhelper.gusername )
      league = League( leaguename, account, modname, mapname, nummatchesperairpair )
      sqlalchemysetup.session.add( league )
      sqlalchemysetup.session.commit()
      jinjahelper.message("Added ok. You might want to schedule matches now")
   else:
      jinjahelper.message( "Please fill in the fields and try again" )

sqlalchemysetup.close()



