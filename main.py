import CSVreaderClass
import UnsortedTermListGeneratorClass


# entry point of the interpreter
def main():
    dictionary, list_structure = index("tweets.csv")


# returns the dictionary and the inverted index list structure
def index(filename):
    reader = CSVreaderClass.CSVreader()  # converter CSV to List
    raw_list = reader.get_list_from_path(filename)  # returns a list sorted by tweet ids
    unsorted_term_list_generator = UnsortedTermListGeneratorClass.UnsortedTermListGenerator()
    unsorted_list = unsorted_term_list_generator.generate_from_list(raw_list)
    unsorted_list.sort()  # sort the global term list
    for each in unsorted_list:
        print(each[0], each[1])
    dictionary = None
    list_structure = None
    return dictionary, list_structure


if __name__ == '__main__':
    main()
