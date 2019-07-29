import webapp2
import jinja2
import os

from myMemes import MemeInfo
from google.appengine.api import urlfetch
import json
#This initializes the jinja2 environment
#This is the same for almost every app you build
#This is a constructor
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions= ["jinja2.ext.autoescape"],
    autoescape= True
)

# curl -d 'template_id=112126428&username=danielkelleycssi&password=cssirocks&text0=thisisthetop&text1=thisisthebottom' https://api.imgflip.com/caption_image  
meme_templates = ["https://i.imgflip.com/2/1h7in3.jpg",
"https://i.imgflip.com/2/1otk96.jpg", "https://i.imgflip.com/2/1yxkcp.jpg"]
#the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):
        api_url= "https://api.imgflip.com/get_memes"
        imgflip_response= urlfetch.fetch(api_url).content
        imgflip_response_json= json.loads(imgflip_response)
        meme_templates = ["url"]
        for meme_template in imgflip_response_json["data"]["memes"][0:100]:
            meme_templates.append(meme_template["url"])
        meme_dict= {
        "imgs": meme_templates
        }

        # self.response.headers["Content-Type"]= "text/html"
        # self.response.write("<h1>Google 2019</h1>")
        welcome_template= jinja_env.get_template("appengine.html")
        self.response.write(welcome_template.render(meme_dict))

    def post(self):
        top_line= self.request.get("top-line")
        print(top_line)

class ResultPage(webapp2.RequestHandler):

    def post(self):
        top_line= self.request.get("top-line")
        bottom_line= self.request.get("bottom-line")
        meme_url =self.request.get("template")
        data_dict = {
            "top": top_line,
            "bottom": bottom_line,
            "url": meme_url
        }
        Meme1= MemeInfo(meme_top_line= top_line, meme_image = meme_url, meme_bottom_line = bottom_line)
        Meme1.put()
        content = MemeInfo.query().fetch()
        firstMemeInfo = content[0]
        print(firstMemeInfo)
        result_template= jinja_env.get_template("result.html")
        self.response.write(result_template.render(data_dict))

class AllMemes(webapp2.RequestHandler):
    def get(self):
        all_Memes= MemeInfo.query().fetch()
        allmemesdict= {
        "mymemes": all_Memes
        }
        result_template= jinja_env.get_template("allMemes.html")
        self.response.write(result_template.render(allmemesdict))


class SleepingPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers ["Content-Type"] = "text/plain"
        self.response.write(" Happy Day")
#the app configuration section
app= webapp2.WSGIApplication(
[
    ("/",MainPage),
    ("/result", ResultPage),
    ("/allMemes", AllMemes),
    ("/sleep", SleepingPage)
],
debug=True
)
