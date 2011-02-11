#!/usr/bin/python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
#import time
import web

# import config
from config_define import ThemeConfig

# import theme
from theme_define import ThemeCoolblue

# import entity
from entity_list_define import ListDataLite


# import sub app
import blog
import wiki
import cms
#import cms_model

import cms_sqlite_model

#import blog

##########config region start##########
#debug on/off release to set False
web.config.debug = True

#tempaltes engine
#render = web.template.render('templates/',base='default_layout')
#render = web.template.render('templates/')


#dbconfig
#db = web.database(dbn='mysql', user='dbuser', pw='*****', db='webpy')

##########config region end##########   


#subapp remark:'/blog', blog.app_blog,
path_prefix = '/webpy'
urls = (
        '/', 'reindex',
        '/home','reindex',
        '/child','child',
        '/demo','demo',
        '/list','defaultarchiveslist',
        '/list/(\d+)','archiveslist',
        '/about','about',
        '/blog',blog.app_blog,
        '/cms',cms.app_cms,
        '/test','test',
        #prefix
        path_prefix+'/', 'reindex',
        path_prefix+'/home','reindex',
        path_prefix+'/child','child',
        path_prefix+'/demo','demo',
        path_prefix+'/list','defaultarchiveslist',
        path_prefix+'/list/(\d+)','archiveslist',
        path_prefix+'/about','about',
        path_prefix+'/blog',blog.app_blog,
        path_prefix+'/cms',cms.app_cms,
        path_prefix+'/test','test',
        
        '/(.*)', 'index',
)

themerender = ThemeCoolblue()

class test:
    def GET(self):
        contents = cms_sqlite_model.get_top_contents(10)
        params = {'listdata':contents}
        return themerender.render('test','test','','',params=params)

class reindex:
    def GET(self): raise web.seeother('/index')
    
class child:
    def GET(self):
        return themerender.render('child','child')    

class demo:
    def GET(self):
        return themerender.render('demo','demo')

class defaultarchiveslist:
    def GET(self):
        querystringPageNum = web.input(pagenum='0').pagenum
        return archiveslist().GET(querystringPageNum)
    
class archiveslist:
    def GET(self,pagenum):
        #listdata = [] #init listdata
        #i = 0
        #listdata.append(ListDataLite(i,'Index','2010-10-04 21:43:00'))
        #i=i+1
        #listdata.append(ListDataLite(i,'About this site','2010-10-05 10:58:00','/webpy/about'))
        #i=i+1
        #listdata.append(ListDataLite(i,'Shi','2010-10-05 16:47:10','/webpy/index'))
        #params = {'pagenum':int(pagenum),'listdata':listdata}
        #return themerender.render('list','archiveslist','','',params)
        contentslite = cms_sqlite_model.get_all_contents_lite()
        params = {'listdata':contentslite}
        return themerender.render('list','list','','',params)
      
class about:
    def GET(self):
        return themerender.render('about','about')  

class index:
    def GET(self, path):
        contents = cms_sqlite_model.get_top_contents(10)
        params = {'listdata':contents}
        return themerender.render(path,params=params)

app = web.application(urls, globals())

##########web customs output region start##########
#customs  not found
def notfound():
    return web.notfound("404:Sorry, the page you were looking for was not found.")

    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))
app.notfound = notfound

#customs internalerror
def internalerror():
    return web.internalerror("502:Bad Request.")

#app.internalerror = internalerror
##########web customs output region end##########

application = app.wsgifunc()