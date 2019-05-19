#asahi news

import urllib.request, urllib.error,urllib.parse
import lxml.html
from bs4 import BeautifulSoup
import csv
from janome.tokenizer import Tokenizer
from collections import Counter, defaultdict

print('search : ')
input_search = input()
search_word = urllib.parse.quote(input_search)
print(search_word)

url = "https://sitesearch.asahi.com/sitesearch/index.php?sort=&Keywords=" + search_word + "&start="


title = ""

for i in range(20):
    search_url = url + str(i*10)
    html = urllib.request.urlopen(search_url)

    soup = BeautifulSoup(html, "lxml")

    headline = soup.find_all(attrs={"class":"SearchResult_Headline"})

    #print(headline)

    for item in headline:
        print(item.em.get_text())
        title += item.em.get_text()

    #print(title)

f = open('html.txt',"w")
f.write(title)
f.close()

#名詞だけ抽出、単語をカウント
def counter(texts,get_pos):
    t = Tokenizer()
    words_count = defaultdict(int)
    words = []
    for text in texts:
        tokens = t.tokenize(text)
        for token in tokens:
            #品詞から名詞だけ抽出
            pos = token.part_of_speech.split(',')[0]
            if pos == get_pos:
                words_count[token.base_form] += 1
                words.append(token.base_form)
    return words_count, words

with open('./asahi_title.txt','r') as f:
    reader = csv.reader(f, delimiter='\t')
    texts = []
    for row in reader:
        if row:
            text = row[0].split('http')
            texts.append(text[0])

words_count, words = counter(texts,'名詞')

#不要な要素を削除
words_count.pop('RT',None)
words_count.pop('@',None)
words_count.pop(':',None)
words_count.pop('_',None)
words_count.pop('の',None)
words_count.pop('ん',None)

#sort
d = [(v,k) for k,v in words_count.items()]
d.sort()
d.reverse()
for count, word in d[:50]:
    print (count, word)
