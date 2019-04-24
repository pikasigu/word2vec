from gensim.models import word2vec
import warnings # Future warning 対策

def main():
    warnings.filterwarnings('ignore')
    # model import
    print("input project name")
    project = input()
    model = word2vec.Word2Vec.load("./model/" + project + ".model")

    # results
    print("input word")
    word = input()
    results = model.wv.most_similar(positive=[word])
    print("most similar words")
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
