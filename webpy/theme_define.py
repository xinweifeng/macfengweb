#!/usr/bin/python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import web
# import config
from config_define import ThemeConfig

render = web.template.render('templates/')
##########coolblue theme start##########
class ThemeCoolblue:
    def __init__(self,themeconfig=None):	
        if themeconfig == None:
            self.themeconfig = ThemeConfig()
        else:
            self.themeconfig = themeconfig
    
    def getContentRender(self,contenttype,subapp='',siderbar=''):
        if contenttype == 'index' or contenttype == '':
            return render.coolblue_content(self.themeconfig,
                                    render.coolblue_sidebar(self.themeconfig)
                                    )
        else:
            if subapp == '':
                contentrender = web.template.frender('templates/coolblue_'+contenttype+'.html')
            else:
                contentrender = web.template.frender('templates/'+ subapp+'/coolblue_'+contenttype+'.html')
            
            if siderbar == '':
                return contentrender(self.themeconfig,
                                    render.coolblue_sidebar(self.themeconfig)
                                    )
            else:
                contentsiderrender = web.template.frender('templates/'+siderbar+'.html')
                return contentrender(self.themeconfig,
                                    contentsiderrender(self.themeconfig)
                                    )
        	
    def render(self,currentpath,contenttype='index',subapp='',siderbar='',params={}):
        self.themeconfig.StaticPath = '/webpy/static/coolblue'
        self.themeconfig.CurrentPath  = currentpath
        self.themeconfig.Params = params
        contentrender = self.getContentRender(contenttype,subapp,siderbar)
        return render.coolblue_base(self.themeconfig,
                                    render.coolblue_header(self.themeconfig),
                                    contentrender,
                                    render.coolblue_footer(self.themeconfig))  
##########coolblue theme end##########  