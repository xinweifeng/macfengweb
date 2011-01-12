#!/usr/bin/python
'''
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import web
import markdown

### wiki model
db = web.database(dbn='mysql', user='dbuser', pw='******', db='webpy')

def get_pages():
    return db.select('pages', order='id DESC')

def get_page_by_url(url):
    try:
        return db.select('pages', where='url=$url', vars=locals())[0]
    except IndexError:
        return None

def get_page_by_id(id):
    try:
        return db.select('pages', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_page(url, title, text,pagetype=0):
    db.insert('pages', url=url, title=title, content=text,pagetype=pagetype)

def del_page(id):
    db.delete('pages', where="id=$id", vars=locals())

def update_page(id, url, title, text,pagetype):
    db.update('pages', where="id=$id", vars=locals(),
        url=url, title=title, content=text,pagetype=pagetype)

### wiki test post password 
postpass = u'wikipass'

### Url mappings
urls = (
    "", "Rewiki",
    '/', 'Index',
    '/new', 'New',
    '/edit/(\d+)', 'Edit',
    '/delete/(\d+)', 'Delete',
    '/(.*)', 'Page',
)

### Templates
t_globals = {
    'datestr': web.datestr,
    'markdown': markdown.markdown,
}
render = web.template.render('templates/wiki/', base='base', globals=t_globals)
#render = web.template.render('templates/wiki/')

class Rewiki:
    def GET(self): raise web.seeother('/')

class Index:

    def GET(self):
        """ Show page """
        pages = get_pages()
        return render.index(pages)


class Page:

    def GET(self, url):
        """ View single page """
        page = get_page_by_url(url)
        if not page:
            raise web.seeother('/new?url=%s' % web.websafe(url))
        return render.view(page)


class New:

    def not_page_exists(url):
        return not bool(get_page_by_url(url))
    
    def input_mustnumber(pagetype):
        return is_intnumber(pagetype)

    page_exists_validator = web.form.Validator('Page already exists', 
                                not_page_exists)
                                
    input_isnotnumber_validator = web.form.Validator('Input must a number', 
                                input_mustnumber)
                                
    form = web.form.Form(
        web.form.Textbox('url', web.form.notnull, page_exists_validator,
            size=30,
            description="Location:"),
        web.form.Textbox('title', web.form.notnull, 
            size=30,
            description="Page title:"),
        web.form.Textbox('pagetype',web.form.notnull, input_isnotnumber_validator,
            size=5,
            description="Page Type:"),
        web.form.Textarea('content', web.form.notnull, 
            rows=30, cols=80,
            description="Page content:", post="Use markdown syntax"),
        web.form.Textbox('password',web.form.notnull,
            size=5,
            description="Password:"),
        web.form.Button('Create page'),
    )

    def GET(self):
        url = web.input(url='').url
        form = self.form()
        form.fill({'url':url})
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        
        if not is_current_password(form.d.password):
            return render.new(form)
        
        if not is_intnumber(form.d.pagetype):
            return render.new(form)
            
        new_page(form.d.url, form.d.title, form.d.content,int(form.d.pagetype))
        
        raise web.seeother('/' + form.d.url)

def is_current_password(upass):
    return upass == postpass

def is_intnumber(uchar):
    try:
        int(uchar)
        return True
    except:
        return False

class Delete:

    def POST(self, id):
        del_page(int(id))
        raise web.seeother('/')


class Edit:

    form = web.form.Form(
        web.form.Textbox('url', web.form.notnull, 
            size=30,
            description="Location:"),
        web.form.Textbox('title', web.form.notnull, 
            size=30,
            description="Page title:"),
        web.form.Textbox('pagetype',web.form.notnull,
            size=5,
            description="Page Type:"),
        web.form.Textarea('content', web.form.notnull, 
            rows=30, cols=80,
            description="Page content:", post="Use markdown syntax"),
        web.form.Textbox('password',web.form.notnull,
            size=5,
            description="Password:"),
        web.form.Button('Update page'),
    )

    def GET(self, id):
        page = get_page_by_id(int(id))
        form = self.form()
        form.fill(page)
        return render.edit(page, form)


    def POST(self, id):
        form = self.form()
        page = get_page_by_id(int(id))
        if not form.validates():
            return render.edit(page, form)
        
        if not is_current_password(form.d.password):
            return render.edit(page, form)
        
        if not is_intnumber(form.d.pagetype):
            return render.edit(page, form)
            
        update_page(int(id), form.d.url, form.d.title, form.d.content,int(form.d.pagetype))
        raise web.seeother('/')

### retrun app_wiki
app_wiki = web.application(urls, globals())
'''