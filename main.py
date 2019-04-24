import merge_source
import model
import result
import mecab
import replace
import plot


def main():
    print("Start word2vec")
    print("Input source name")
    project = input()
    merge_source.sub(project)
    print("is code? [y/n]")
    iscode = input()
    if iscode == "y":
        replace.sub(project)
    else:
        mecab.sub(project)
    model.sub(project)
    result.sub(project)
    print("plot? [y]")
    iscode = input()
    if iscode == "y":
        plot.main(project)


if __name__ == '__main__':
    main()
