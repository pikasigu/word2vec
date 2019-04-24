from gensim.models import word2vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib
import warnings


def main(project):
    matplotlib.use('tkagg')

    # Future warning 対策
    warnings.filterwarnings('ignore')

    # Load
    model = word2vec.Word2Vec.load("./model/" + project + ".model")

    print("input main word")
    word = input()
    topn = 30

    # Get Similar word
    words = [x[0] for x in sorted(model.most_similar(word, topn=topn))]
    words.append(word)

    # Get from model
    data = []
    for w in words:
        data.append(model[w])

    # PCA
    pca = PCA(n_components=2)
    pca.fit(data)
    data_pca = pca.transform(data)

    # plot
    loop = 0
    for p in data_pca:
        plt.plot(p[0], p[1], ms=5.0, zorder=2, marker="x")
        plt.annotate(words[loop], (p[0], p[1]), size=9)
        loop += 1
    plt.show()


if __name__ == '__main__':
    print("input project name")
    project = input()
    main(project)
