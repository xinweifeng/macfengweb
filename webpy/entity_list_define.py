#!/usr/bin/python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import helper

### ListDataLite 
class ListDataLite:
    ID = 0
    Title = ''
    PostDate = ''
    Author = ''
    Url = ''
    
    def __init__(self,Id=0,title='no title',postdate=helper.now_str(),url='/webpy/index',author='macfeng admin'):
        self.ID = Id
        self.Title = title
        self.PostDate = postdate
        self.Author = author
        self.Url = url

### ListDataCmsContent
class ListDataCmsContent(ListDataLite):
    Content = ''
    PageType = 0
    
    def __init__(self,Id=0,title='no title',postdate=helper.now_str(),url='/webpy/index',author='macfeng admin',content='',pagetype=0):
        super.__init__(Id,title,postdate,author,url)
        self.Content = content
        self.PageType = pagetype

