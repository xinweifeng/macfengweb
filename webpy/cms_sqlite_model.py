#!/usr/bin/python
# MVC cms model
# Only DB methods
# for sqlite3 version

import web

from config_define import SysConfig 
import helper

sqlitedbfile = SysConfig().SqliteDB_Prod
# SysConfig().SqliteDB_Dev
# SysConfig().SqliteDB_Prod
db = web.database(dbn='sqlite', db=sqlitedbfile)

def get_top_contents(topcount):
    return db.select('cms_content', order='id DESC',limit=topcount)
    
def get_all_contents_lite():
    return db.select('cms_content',what='id,url,title,pagetype,author,updatetime', order='id DESC')

def get_all_contents():
    return db.select('cms_content', order='id DESC')

def get_content_by_url(url):
    try:
        return db.select('cms_content', where='url=$url', vars=locals())[0]
    except IndexError:
        return None

def get_content_by_id(id):
    try:
        return db.select('cms_content', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_content(url, title, text, author='macfeng admin', pagetype=0):
    db.insert('cms_content', url=url, title=title, content=text,pagetype=pagetype,author=author,updatetime = helper.now_str())

def update_content(id, url, title, text, author, pagetype):
    db.update('cms_content', where="id=$id", vars=locals(),
        url=url, title=title, content=text, pagetype=pagetype,
        author = author, updatetime = helper.now_str())

def del_content(id):
    db.delete('cms_content', where="id=$id", vars=locals())