import requests
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
code = requests.get("https://httpstatuses.com/")
html = BeautifulSoup(code.text,"html.parser")
body = html.find("body").text
stop = stopwords.words("english")
Words = []
porter = PorterStemmer()
for word in word_tokenize(body):
    if porter.stem(word) not in Words and porter.stem(word) not in stop:
        Words.append(porter.stem(word))
print(Words)

