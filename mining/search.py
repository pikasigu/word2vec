import urllib.request
import urllib.error
import urllib.parse

from bs4 import BeautifulSoup, Comment
import csv
import os
import re
import sys
import ssl


def input_to_exp(input_search, engine):
    # 検索語 から search の title と url を取得
    search_word = urllib.parse.quote(input_search)  # encode

    # init
    url = ""
    titles = ""

    # get search url
    if engine == "google":
        print("use google search")
        url = "https://www.google.co.jp/search?q=" + search_word + "&start="

    elif engine == "yahoo":
        print("recognize yahoo engine")
        print("cannnot use this engine")
        url = ""
        sys.exit

    print("input save file name")
    save_name = input()

    print(">>>>> start export >>>>>")
    print(">>> get page titles & URL >>>")

    loop_count = 3

    # file init
    if os.path.exists('./search/search_url.txt'):
        os.remove('./search/search_url.txt')
    f = open('./search/search_url.txt', "w")  # urls file

    for i in range(loop_count):  # load pager count
        search_url = url + str(i*10)
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) "
            + "Gecko/20100101 Firefox/47.0",
        }
        request = urllib.request.Request(url=search_url, headers=headers)
        html = urllib.request.urlopen(request)

        soup = BeautifulSoup(html, "lxml")

        headline = soup.find_all(attrs={"class": "r"})

        for item in headline:
            titles += item.get_text()

        # 一旦飛ぶ先のURLのファイルに残しておく
        for a in soup.find_all(class_="r"):
            for i in a.find_all("a"):  # attrs={"class":"r" ,"href": "/link"}):
                if "webcache.googleusercontent" not in i.get("href"):
                    if "#" not in i.get("href"):
                        if "/search?" not in i.get("href"):

                            f = open('./search/search_url.txt', "a")
                            f.write(i.get("href") + ",")
                            f.close()

    f = open('./search/' + save_name + '.txt', "w")
    f.write(titles)
    f.close()

    print("<<< finish get titles & URL <<<")
    exp_body(save_name)
    print("<<<<< finish export <<<<<")


def exp_body(save_name):  # url file より body 取得のためのパイプ
    print(">>> start get body from URL >>>")

    # create new file
    if os.path.exists('./search/' + save_name + '.tsv'):
        os.remove('./search/' + save_name + '.tsv')
    f = open('./search/' + save_name + '.tsv', "w")
    f.close()

    with open('./search/search_url.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        texts = []
        for row in reader:
            if row:
                texts = row[0].split(',')

        for text in texts:
            if len(text) != 0:
                if "http://" or "https://" in text:
                    get_body_text(text, save_name)

    print("<<< finish get body from URL <<<")


def get_body_text(url, save_name):  # url から body 本文を抽出
    print("get from " + url)
    ssl._create_default_https_context = ssl._create_unverified_context
    f = open('./search/' + save_name + '.tsv', "a")
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) "
        + "Gecko/20100101 Firefox/47.0",
    }
    try:
        request = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(request)
        soup = BeautifulSoup(html, "lxml")
        # コメントタグの除去
        for comment in soup(text=lambda x: isinstance(x, Comment)):
            comment.extract()
        # scriptタグの除去
        for script in soup.find_all('script', src=False):
            script.decompose()
        # テキストだけの抽出
        for text in soup.find_all(text=True):
            if text.strip():

                # text に 余計な文字列が含まれるので取り除く
                # 後に配列処理に変更
                text = re.sub(r'[!-~]', "", text)  # 半角記号,数字,英字
                text = re.sub(r'[︰-＠]', "", text)  # 全角記号
                text = re.sub('\t', "", text)
                text = re.sub('税込', "", text)  # 改行文字
                text = re.sub('￥', "", text)
                text = re.sub('　', "", text)  # 全角空白
                text = re.sub(' ', "", text)  # 空白文字
                text = re.sub('\n', "", text)  # 改行文字

                f.write(text)

        f.write('\n')
        f.close()

    except (ZeroDivisionError, TypeError) as e:
        print(e)
        print("--- cannot open this page ---")


if __name__ == '__main__':
    print("input search word")
    word = input()
    input_to_exp(word, "google")
