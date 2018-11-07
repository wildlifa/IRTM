import CSVreaderClass


# entry point of the interpreter
def main():
    dictionary, list_structure = index("tweets.csv")


# returns the dictionary and the inverted index list structure
def index(filename):
    reader = CSVreaderClass.CSVreader()
    raw_list = reader.get_list_from_path(filename)
    dictionary = None
    list_structure = None
    return dictionary, list_structure


if __name__ == '__main__':
    main()
