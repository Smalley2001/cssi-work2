#To use you must press in the command line pip install translate


# This is a language converter from english to another language

# from translate import Translator
# translator= Translator(to_lang="German")
# translation = translator.translate("Good Morning!")
# print translation


#This is a translator from two different languages other than english
from translate import Translator
translator= Translator(from_lang="german",to_lang="spanish")
translation = translator.translate("Guten Morgen")
print translation
