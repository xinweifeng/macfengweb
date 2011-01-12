#!/usr/bin/python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import web

import helper

# import theme
from theme_define import ThemeCoolblue
from config_define import SysConfig


# import entity
from entity_list_define import ListDataLite

#import cms_model
import cms_sqlite_model

urls = (
    '', 'recms',
    '/', 'cmsalllist',
    '/alllist','cmsalllist',
    '/new', 'cmsnew',
    '/add', 'cmsnew',
    '/edit/(\d+)', 'cmsedit',
    '/delete/(\d+)', 'cmsdelete',
    '/(.*)', 'cmsview',
)

# render = web.template.render('templates/')

cms_themerender = ThemeCoolblue()
cmssidebar = 'cms/coolblue_cms_sidebar'
vpass = SysConfig.CMS_MODIFY_PASSWORD
dpass = SysConfig.CMS_DELETE_PASSWORD

class recms:
    def GET(self): raise web.seeother('/')
    
class cmsview:
    def GET(self, urlpath):
        """ View single page """
        if helper.is_int(urlpath):
            page = cms_sqlite_model.get_content_by_id(int(urlpath))
        else:
            page = cms_sqlite_model.get_content_by_url(urlpath)
            
        if not page:
            raise web.seeother('/')
        
        params = {'cmspagedata':page}
        
        return cms_themerender.render('/cms/view','cms_view',
        'cms','',params)

class cmsalllist:
    def GET(self):
        #get all cms content lite
        contentslite = cms_sqlite_model.get_all_contents_lite()
        params = {'listdata':contentslite}
        return cms_themerender.render('/cms/index','cms_alllist',
        'cms',cmssidebar,params)

class cmsnew:
    def GET(self):
        params = {'error':''}
        return cms_themerender.render('/cms/add','cms_add',
        'cms',cmssidebar,params)
        
    def POST(self):
        form_input = web.input()
        cmsurl = form_input.cms_url
        cmstitle = form_input.cms_title
        cmspagetype = form_input.cms_pagetype
        cmscontent = form_input.cms_content
        cmsauthor = form_input.cms_author
        cmspassword = form_input.cms_password
        
        params = {'error':''}
        bhaserror = False
        if (cmspassword!=vpass):
            params['error']='password error!'
            bhaserror = True
        elif (cmsurl==''):
            params['error']='url error!'
            bhaserror = True
        
        if (bhaserror==True):
            return cms_themerender.render('/cms/add','cms_add',
        'cms',cmssidebar,params)
        
        if (cmstitle==''):
            cmstitle = cmsurl
        if (cmspagetype==''):
            cmspagetype = '0'
        if (cmscontent==''):
            cmscontent = 'null content!'
        if (cmsauthor==''):
            cmsauthor = 'macfeng admin'
        #new_content(url, title, text, author='macfeng admin', pagetype=0):
        cms_sqlite_model.new_content(cmsurl,cmstitle,cmscontent,cmsauthor,int(cmspagetype))
        
        raise web.seeother('/')

class cmsedit:
    def GET(self,id):
        page = cms_sqlite_model.get_content_by_id(int(id))
        params = {'error':'','listdata':page}
        return cms_themerender.render('/cms/edit','cms_edit',
        'cms',cmssidebar,params)
        
    def POST(self,id):
        form_input = web.input()
        cmsurl = form_input.cms_url
        cmstitle = form_input.cms_title
        cmspagetype = form_input.cms_pagetype
        cmscontent = form_input.cms_content
        cmsauthor = form_input.cms_author
        cmspassword = form_input.cms_password
        
        params = {'error':''}
        bhaserror = False
        if (cmspassword!=vpass):
            params['error']='password error!'
            bhaserror = True
        elif (cmsurl==''):
            params['error']='url error!'
            bhaserror = True
            
        page = cms_sqlite_model.get_content_by_id(int(id))
        page.url = cmsurl
        page.title = cmstitle
        page.pagetype = cmspagetype
        page.content = cmscontent
        page.author = cmsauthor
        
        params['listdata'] = page
        
        if (bhaserror==True):
            return cms_themerender.render('/cms/edit','cms_edit',
        'cms',cmssidebar,params)
        
        if (cmstitle==''):
            cmstitle = cmsurl
        if (cmspagetype==''):
            cmspagetype = '0'
        if (cmscontent==''):
            cmscontent = 'null content!'
        if (cmsauthor==''):
            cmsauthor = 'macfeng admin'
        #new_content(url, title, text, author='macfeng admin', pagetype=0):
        cms_sqlite_model.update_content(int(id),cmsurl,cmstitle,cmscontent,cmsauthor,int(cmspagetype))
        
        raise web.seeother('/')
        
class cmsdelete:
    def POST(self,id):
        form_input = web.input()
        cmsdelpassword = form_input.cms_delpassword
        if (cmsdelpassword==dpass):
            cms_sqlite_model.del_content(int(id))
        raise web.seeother('/')
        
app_cms = web.application(urls, globals())