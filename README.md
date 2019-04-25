# word2vecで色々やってみる

# 2019/04
## word2vec
### 実行手順
- sourceディレクトリ内にテキストデータorソースコードなどが入ったディレクトリを用意します
```
word2vec/source/hoge/***.txt
word2vec/source/hoge/***.class
```
- mainで実行するか個別で実行します
```
$ python main.py
# source内のディレクトリを指定
# 類似度検索をしたい単語を入力
```
### 個別実行
- merge_source.pyでsourceディレクトリ内のソースorテキストをまとめる
```
$ python merge_source.py
#source内のディレクトリを指定
```
- textディレクトリ内にまとめられたテキストファイルが生成される
- ソースコードなら`replace.py`をテキストデータなら`mecab.py`を実行
```
$ python replace.py
```
- 対応ソースコードをコーパスとしてモデリング
```
$ python model.py
#ソースコードが入っているsource内のディレクトリを指定
# optionを適宜設定してモデリングを実行
```
- 生成されたモデルから類似
```
$ python result.py
```
- プロット
```
$ python plot.py
```
