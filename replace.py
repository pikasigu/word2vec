import re
import os
import shutil


def main():

    print("please input project name in text directory")
    project = input()

    # subに元ファイルが存在するか
    if not os.path.exists('./text/sub/' + project + ".txt"):
        shutil.copyfile('./text/' + project + ".txt",
                        './text/sub/' + project + ".txt")
    path = './text/sub/' + project + ".txt"

    with open(path) as f:
        # 改行で区切って取得
        source = f.read().split('\n')

    # 正規表現のパターン
    pattern1 = r"//.*|\t|^import.*"
    pattern2 = r"[\{\};]"
    pattern3 = r'["\.,\(\)]'

    result = ""

    for s in source:
        t_res = re.sub(pattern1, "", s)
        t_res = re.sub(pattern2, "", t_res)
        t_res = re.sub(pattern3, " ", t_res)
        if not t_res == "":
            result += t_res + "\n"

    # 結果を書き込み
    with open("./text/" + project + ".txt", mode="w") as f:
        f.write(result)
    print("export {}".format("./text/" + project + ".txt"))


if __name__ == '__main__':
    main()
