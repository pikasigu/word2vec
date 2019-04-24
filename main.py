import merge_source
import model
import result


def main():
    print("Start word2vec")
    print("Input source name")
    project = input()
    merge_source.sub(project)
    model.sub(project)
    result.sub(project)


if __name__ == '__main__':
    main()
