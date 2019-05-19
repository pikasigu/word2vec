import urllib.request
from bs4 import BeautifulSoup
import csv
from janome.tokenizer import Tokenizer
from collections import defaultdict

print('yahoo news search : ')
input_search = input()
search_word = urllib.parse.quote(input_search)
print(search_word)

url = "https://news.yahoo.co.jp/search/?p=" + search_word + "&st=n&ei=UTF-8&b="

title = ""

for i in range(20):
    search_url = url + str(i*10+1)
    html = urllib.request.urlopen(search_url)

    soup = BeautifulSoup(html, "lxml")

    headline = soup.find_all(attrs={"class": "t"})

    for item in headline:
        print(item.get_text())
        title += item.get_text()

f = open('yahoo_title.txt', "w")
f.write(title)
f.close()


# 名詞だけ抽出、単語をカウント
def counter(texts, get_pos):
    t = Tokenizer()
    words_count = defaultdict(int)
    words = []
    for text in texts:
        tokens = t.tokenize(text)
        for token in tokens:
            # 品詞から名詞だけ抽出
            pos = token.part_of_speech.split(',')[0]
            if pos == get_pos:
                words_count[token.base_form] += 1
                words.append(token.base_form)
    return words_count, words


with open('yahoo_title.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    texts = []
    for row in reader:
        if row:
            text = row[0].split('http')
            texts.append(text[0])

words_count, words = counter(texts, '名詞')

# sort
d = [(v, k) for k, v in words_count.items()]
d.sort()
d.reverse()
for count, word in d[:50]:
    print(count, word)
