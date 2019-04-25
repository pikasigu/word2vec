from gensim.models import word2vec
import logging


def main():
    # logging
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.INFO)

    print("please input project name in text directory")
    path = input()
    sentences = word2vec.Text8Corpus('./text/' + path + ".txt")
    print("please input modeling option")
    print('if not use default option, please input "option"')
    isOption = input()

    # use default option
    if isOption != "option":
        model = word2vec.Word2Vec(sentences,
                                  sg=1,
                                  size=500,
                                  min_count=10,
                                  window=5,
                                  batch_words=50)
        model.save("./model/" + path + ".model")

    else:
        print("WIP.....")


def sub(project):
    # logging
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.INFO)

    sentences = word2vec.LineSentence('./text/' + project + ".txt")
    print("modeling start")
    model = word2vec.Word2Vec(sentences,
                              sg=1,
                              size=200,
                              min_count=3,
                              window=5)
    model.save("./model/" + project + ".model")


if __name__ == '__main__':
    print("Start modeling")
    main()
