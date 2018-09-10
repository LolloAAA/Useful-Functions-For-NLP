def deleteLaughter(sentence):
  #Split sentence in words
  lst = sentence.split()

  #List of letters most used in the laughs
  vowels = ["a", "e", "i", "o", "u"]

  #For each word in the sentence...
  for i in lst:
    for k in vowels:
      #Control if letter "h" is in the word and if the length word is equal or longer than 4. This final condition can be edited as necessary
      if ("h" in i) and (len(i) >= 4):
        #I count how many "h" and vower (a or e or i or ...) are in the words and control if is equal to the length word. I put an offset of 2
        #typing errors (like "ahah1ahah", "ehehyehjehe"). This offset can be edited if you don't want consider an offest or consider a larger offset
        if (len(i) - 2) <= (i.count(k) + i.count('h')):
          sentence = sentence.replace(i, "")
  return sentence

print(deleteLaughter("I'm joking ahahaha eheheheh ihihihihi ohhoohohoho uhuhuhu"))
