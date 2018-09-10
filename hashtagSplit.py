import csv
import operator

#Function used for sorting a list of words based their length
def sortLength(lst):
    lst2 = sorted(lst, key = len, reverse = 1)
    return lst2

def hashtagSplit(hashtag):
    hashtag = hashtag.replace("#","")
    hashtag = hashtag.lower()

    lista = []
    listaDaTogliere = []

    #Here we have to load the dictionary in ".csv" format
    spamReader = csv.reader(open('parole.csv', newline=''), delimiter=' ', quotechar='|')
    for row in spamReader:
      if row[0] in hashtag:
        #We do not consider words that have less than 2 letters, useless in the preprocessing of text data
        if len(row[0]) > 2:
          lista.extend([row[0]])

    lista = sortLength(lista)

    #This small block removes all the words found from the initial hashtag, thus obtaining the useless string to be removed
    #The words are deleted in decreasing length, so that smaller strings are not contained in the larger ones
    listaDaTogliere = []
    tmpstring = hashtag
    for i in range(0, len(lista)):
      if lista[i] in tmpstring:
        tmpstring = tmpstring.replace(lista[i],"#")
      else:
        listaDaTogliere.extend([lista[i]])
    tmpstring2 = hashtag
    for i in range(0, len(lista)):
      tmpstring2 = tmpstring2.replace(lista[i],"#"+lista[i]+"#")
    hashtag = tmpstring2.replace(tmpstring,"");
    hashtag = hashtag.replace("#","")
    lista = list(set(lista) - set(listaDaTogliere))

    listaDaTogliere = []
    for i in range(0, len(lista)):
      tmpstring = hashtag
      for k in range(0, len(lista)): 
        if i != k:
          tmpstring = tmpstring.replace(lista[k],"")
      if lista[i] not in tmpstring:
        listaDaTogliere.extend([lista[i]])
    lista = list(set(lista) - set(listaDaTogliere))

    #For each word found We find its position within the hashtag to sort the words
    posizioni = {}
    for i in range(0, len(lista)):
      posizioni.update({lista[i]:[hashtag.find(lista[i])]})

    #At the last We sort all the word
    posizioni = sorted(posizioni.items(), key = operator.itemgetter(1))
    for i in range(0, len(lista)):
      lista[i] = posizioni[i][0]

    final = " ".join(lista)

    return final


print(hashtagSplit("#nelMezzoDelCamminoDiNostraVita"))
