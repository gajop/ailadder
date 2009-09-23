# Copyright Hugh Perkins 2004, 2009
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

import sys
import os
import MySQLdb

import config

connection = None
cursor = None

def connectdb():
   global connection, cursor
   connection = MySQLdb.connect( host = config.dbhost,
     user = config.dbuser,
     passwd = config.dbpassword,
     db = config.dbname )
   cursor = connection.cursor()
   return cursor

def disconnectdb():
   cursor.close()
   connection.close()

# returns a list(?) containing the results from the query
# which should return a single column of data
def querytolist( querysql ):
   cursor.execute( querysql )
   row = cursor.fetchone()
   resultlist = []
   while row != None:
      resultlist.append( row[0] )
      row = cursor.fetchone()
   return resultlist

