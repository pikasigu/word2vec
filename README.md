# word2vecで色々やってみる

# 2019/04
## ソースコードに対してword2vec
- ソースコードに対してword2vec処理をしてみる
### 実行手順
- 一発ならこっち
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
- 生成されたモデルから類似とかを色々弄ってみる
```
$ python result.py
```
