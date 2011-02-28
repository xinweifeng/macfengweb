#!/usr/bin/python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)

import web
#import json
from twitter import Twitter,OAuth
from twapiconfig import TwApiConfig
#web.config.debug = True

#tempaltes engine
#render = web.template.render('templates/',base='default_layout')
#render = web.template.render('templates/')
tproxy_render = web.template.render('templates/tproxy/')


urls = (
        '','retproxyindex',
        '/ti/(.*)','tproxyinterface',
        '/(.*)', 'tproxyindex',
)
apiConfig = TwApiConfig()
twitter_CONSUMER_KEY= apiConfig.CONSUMER_KEY
twitter_CONSUMER_SECRET=apiConfig.CONSUMER_SECRET
twitter_OAuthToken = apiConfig.OAuthToken
twitter_OAuthTokenKey = apiConfig.OAuthTokenKey
#json interface
class tproxyinterface:
    def GET(self,path):
        #web.header('Content-Type', 'application/json')
        #if (path[]'friends.list.html')
        #return "{\"firstName\": \"John\",\"lastName\": \"Smith\",\"path\":\"" + path.find('friends.list.html') +"\"}"
        #return "{\"firstName\": \"John\",\"lastName\": \"Smith\",\"path\":\"" + path +"\"}" 
        mtptwitter = Twitter(auth=OAuth(twitter_OAuthToken,twitter_OAuthTokenKey,twitter_CONSUMER_KEY,twitter_CONSUMER_SECRET),secure=True,api_version='1',domain='api.twitter.com')
        if path.find('friends.list.html')>=0:
            return tproxy_render.jqm_base('friends timeline',
            tproxy_render.jqm_tproxy_friends_list(
                mtptwitter.statuses.friends_timeline(count=30)
            )
            )
#return tproxy_render.tproxy_friends_list(mtptwitter.statuses.friends_timeline(count=30))
        else:
            #web.header('Content-Type', 'application/json')
            #twitterresult = reversed(mtptwitter.statuses.friends_timeline(count=15))
            #return mtptwitter.statuses.friends_timeline(count=1)
            return tproxy_render.jqm_content_test()



#class tproxy:
#    def GET(self):
#        return render.tproxy()

class retproxyindex:
    def GET(self): raise web.seeother('/')
    
class tproxyindex:
    def GET(self, path):
        return tproxy_render.jqm_base('tproxy',tproxy_render.jqm_tproxy()) #return tproxy_render.tproxy()

app_tproxy = web.application(urls, globals())