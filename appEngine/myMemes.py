from google.appengine.ext import ndb

class MemeInfo(ndb.Model):
    meme_top_line = ndb.StringProperty(required=True)
    meme_image =  ndb.StringProperty(required=True)
    meme_bottom_line= ndb.StringProperty(required=True)

#     def printMemeInfo(self):
#         print(self.meme_top_line + " " + self.meme_image + " " + self.meme_bottom_line)
#
# meme1 = MemeInfo(meme_top_line= "distracted boyfriend",meme_image= meme_bottom_line= "What are you doing? ")
# meme2 = MemeInfo(meme_top_line= "jealous", meme_image= meme_bottom_line= "girlfriend")
#
# meme1.MemeInfo()
# meme2.MemeInfo()
# all_Memes= MemeInfo.query().fetch()
# print(all_Memes)
