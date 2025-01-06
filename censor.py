def censor(text,word):
#this code  replaces a word inside a text with ***
  new_word = "*" * len(word)
  words = text.split()
  for i in range(len(words)):
    if words[i] == word:
      words[i]=new_word
  return " ".join(words)
