# ソースコードを1つのテキストファイルにまとめる
import glob
import os
import codecs # UnicodeDecodeError回避

def main():
    # get file list
    print("please input files path in source directory")
    path = input()
    paths = glob.glob("./source/" + path + "/*")

    mergedSource = ""
    # file open
    print(paths)
    print("merge start")
    for p in paths:
        print(p)
        # with codecs.open(p,"r",'utf-8','ignore') as f:
        # 事前に書き換えておく
        with open(p,"r") as f:
            mergedSource += f.read()

    print("finishd!")

    # 結果を書き込み
    with open("./text/"+ path +".txt", mode="w") as f:
        f.write(mergedSource)
    print("export {}".format(path))

if __name__ == '__main__':
    print("Start if merge source")
    main()
