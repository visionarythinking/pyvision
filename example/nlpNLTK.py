from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hallo Hr. Anass, wie geht es dir heute? das Wetter ist sehr schön heute"
print(sent_tokenize(example_text))
print(word_tokenize(example_text))
