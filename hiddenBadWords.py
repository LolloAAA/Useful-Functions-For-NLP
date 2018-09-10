def hiddenBadWords(sentence):
  #List of badWords that you want control. You can use a data-set of Bad Words to in csv format too.
  badWords = ["asshole"]

  #The sentence is splitted into words
  lst = sentence.split()

  separatore = ""
  sentence = " " + sentence + " "

  try:
    #For each word in the sentence...
    for i in lst:
      separatore = ""
      #Control if the first and last characters are letters and not numbers or symbols
      if (i[0].isalpha() and i[-1].isalpha()):
        #I take the word without first and last characters
        l = list(i[1:-1])

        #For each character...
        for k in l:
          #Control if is not a letter except "x" (because "x" can be used for hiding a bad word)
          if (not k.isalpha()) or "x" in k:
            #Separatore is a string that contains the middle substring of a bad words. 
            #e.g. --> for the word "you are an as./%%%...le", separatore = "./%%%..."
            separatore = separatore + k

        if(separatore != ""):
          #Split the word by substring separatore
          l = i.split(separatore)

          #Matching of "as.....le" with "asshole" with scan of the bad-words list
          for p in badWords:
            if p[:len(l[0])] == l[0] and p[-len(l[1]):] == l[1]:
              sentence = sentence.replace((" "+i+" "), " "+p+" ")
  except:
    pass
  return sentence

print(hiddenBadWords("You are an as.....le"))
