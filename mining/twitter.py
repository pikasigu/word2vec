# coding:utf-8
import json
from requests_oauthlib import OAuth1Session
import csv
from janome.tokenizer import Tokenizer
from collections import defaultdict
import twitter_config
import time


def main():
    # difine_keys
    (access_token,
     access_token_secret,
     consumer_key,
     consumer_key_secret) = twitter_config.main()

    # TimeLine
    # url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    # Search
    url = "https://api.twitter.com/1.1/search/tweets.json"

    print('search word: ')
    input_search = input()

    print('save file name: ')
    save_name = input()

    # Search params
    params = {'q': input_search,
              'count': 200}

    # API
    twitter = OAuth1Session(consumer_key,
                            consumer_key_secret,
                            access_token,
                            access_token_secret)

    res = twitter.get(url, params=params)

    f_out = open('./text/' + save_name + '.txt', 'w')

    # 繰り返し回数
    for j in range(10):
        res = twitter.get(url, params=params)

        if res.status_code == 200:

            # API取得上限
            limit = res.headers['x-rate-limit-remaining']
            if limit == 1:
                print("get api limit")
                time.sleep(60*15)
            timeline = json.loads(res.text)
            for tweet in timeline['statuses']:
                f_out.write(tweet['text'])
        else:
            print("ERROR: %d" % res.status_code)

    f_out.close()

    with open('./text/' + save_name + '.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        texts = []
        for row in reader:
            if row:
                text = row[0].split('http')
                texts.append(text[0])

    words_count, words = counter(texts, '名詞')

    # 不要な要素を削除
    words_count.pop('RT', None)
    words_count.pop('@', None)
    words_count.pop(':', None)
    words_count.pop('_', None)
    words_count.pop('の', None)
    words_count.pop('ん', None)
    words_count.pop(input_search, None)

    # sort
    d = [(v, k) for k, v in words_count.items()]
    d.sort()
    d.reverse()
    for count, word in d[:30]:
        print(count, word)


def counter(texts, get_pos):
    # 名詞だけ抽出、単語をカウント
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


if __name__ == '__main__':
    main()
