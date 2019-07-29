
# https://pypi.org/project/pyspellchecker/

from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['zzzz', 'is', 'hapenning', 'herw'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))


# from spellchecker import SpellChecker
#
# spell = SpellChecker()  # loads default word frequency list
# spell.word_frequency.load_text_file('./PRACTICE.txt')
#
# # if I just want to make sure some words are not flagged as misspelled
# spell.word_frequency.load_words(['microsoft', 'apple', 'google'])
# spell.known(['microsoft', 'google'])  # will return both now!
