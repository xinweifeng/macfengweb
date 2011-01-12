import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import web
import blog

render = web.template.render('templates/')
web.config.debug = True

db = web.database(dbn='mysql', user='dbuser', pw='******', db='webpy')
       
urls = (
  "/blog", blog.app_blog,
  "/list",'list',
  "/add",'add',
  "/(.*)", 'index'
)

class index:
    def GET(self, path):
        return "hello " + path

class list:
    def GET(self):
    	name = 'macfeng'
       	todos = db.select('todo')
       	return render.demo_list(todos)
    	
    	    	
class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/list')
				
app = web.application(urls, globals())

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

app.internalerror = internalerror


application = app.wsgifunc()