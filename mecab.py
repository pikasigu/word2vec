import MeCab
import os
import shutil


def sub(project):

    print("mecab start")

    # subに元ファイルが存在するか
    if not os.path.exists('./text/sub/' + project + ".txt"):
        shutil.copyfile('./text/' + project + ".txt",
                        './text/sub/' + project + ".txt")
    path = './text/sub/' + project + ".txt"

    with open(path) as f:
        # 改行で区切って取得
        source = f.read().split('\n')

    # 分かち書き
    # mt = MeCab.Tagger("-Ochasen -d '/path/mecab-ipadic~") #自分がインストールした辞書を指定
    mt = MeCab.Tagger()
    mt.parse("")  # unicodeでエラーが出ることがある

    with open('./text/' + project + ".txt", 'w', encoding='utf-8') as f:
        for text in source:
            tmp_lists = []

            # 検索単語の調整を行う場合は以下で行う
            # if '{near word}' in text:
            #    text = text.replace('{near word}','{word}')

            node = mt.parseToNode(text)
            while node:
                # 品詞の絞り込み
                if node.feature.startswith('名詞') \
                    or node.feature.startswith('形容詞') \
                        or node.feature.startswith('動詞'):
                    tmp_lists.append(node.surface)
                node = node.next
            print(tmp_lists)
            f.write(' '.join(tmp_lists) + '\n')

    print("mecab finish")


if __name__ == '__main__':
    print("Start mecab")
    print("input project name")
    project = input()
    sub(project)
