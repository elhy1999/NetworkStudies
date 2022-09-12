import urllib.request
from bs4 import BeautifulSoup
import string
from time import time
import json
import csv

file = open("top100.csv")
top100 = csv.reader(file)
top100.__next__()
top_100_words = {}
for row in top100:
    word = row[0]
    part_of_speech = row[1]
    rank = row[2]
    top_100_words[word] = (part_of_speech, rank)

from_to_words = {}

def search(root):

    def look_up(word):

        global from_to_words
        print(word)

        if word == '' or word in from_to_words:
            return

        if word in top_100_words:
            from_to_words[word] = []
            return

        url = "https://www.vocabulary.com/dictionary/" + word
        htmlfile = urllib.request.urlopen(url)
        soup = BeautifulSoup(htmlfile, features="html.parser")

        # Print instances like Synonyms, Antonyms, etc.
        soup1 = soup.find(class_="definition") 
        txt = soup1.get_text()
        txt1 = txt.rstrip()
        words = [s.translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits)) for s in txt1.split()[1:]]

        from_to_words[word] = words

        for w in words:
            look_up(w)

    look_up(root)

root = input("What is the root word? ")
file_name = root + "_root.json"

t1 = time()
try:
    search(root)
except:
    print("Search stopped")
t2 = time()
print("time taken", t2 - t1)

with open(file_name, 'w') as outfile:
    json.dump(from_to_words, outfile)