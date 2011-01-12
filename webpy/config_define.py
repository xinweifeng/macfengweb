#!/usr/bin/python

class SysConfig:
    SqliteDB_Prod = '/var/sqlite/devdb.sqlite'
    SqliteDB_Dev ='/Users/xinweifeng/Documents/dev/sqlitedb/devdb.sqlite'
    CMS_MODIFY_PASSWORD = '********'
    CMS_DELETE_PASSWORD = '********'


##########themeconfig  start##########
class ThemeConfig:
    StaticPath =''
    CurrentPath ='index'
    def getStaticImagesPath(self):
        return self.StaticPath + '/images'
    def getStaticCssPath(self):
        return self.StaticPath+'/css'
    def liCheckCurrent(self,checkPath='index'):
        if (self.CurrentPath.find(checkPath)>=0):
            return 'id="current"'
        else:
            return ''
##########themeconfig  end##########
