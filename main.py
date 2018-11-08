import CSVreaderClass
import UnsortedTermListGeneratorClass
import FrequencyVectorClass
import QueryProcesserClass


# entry point of the interpreter
def main():
    dictionary, list_structure = index("tweets.csv")
    query_processor = QueryProcesserClass.QueryProcessor(dictionary)
    query_processor.print_posting_list_by_term("nacht")
    query_processor.print_posting_list_by_term("schlafen")


# returns the dictionary and the inverted index list structure
def index(filename):
    dictionary = {}
    list_structure = []
    reader = CSVreaderClass.CSVreader()  # converter CSV to List
    raw_list = reader.get_list_from_path(filename)  # returns a list sorted by tweet ids
    unsorted_term_list_generator = UnsortedTermListGeneratorClass.UnsortedTermListGenerator()  # term generator object
    my_list = unsorted_term_list_generator.\
        generate_from_list(raw_list)  # generate a global term list from raw list data
    print("sorting by terms...")
    my_list.sort()  # sort the global term list
    frequency_generator = FrequencyVectorClass.FrequencyVector()
    frequency_vector = frequency_generator.generate_vector_from_list(my_list)
    counter = 0
    for frequency_value in frequency_vector:
        posting_list = []
        for each in range(counter, counter + frequency_value[0]):
            posting_list.append(my_list[each][1])
        dict_value = (frequency_value[0], frequency_value[1], posting_list)
        list_structure.append(dict_value)
        dictionary[frequency_value[1]] = dict_value
        counter = counter + frequency_value[0]
    return dictionary, list_structure


if __name__ == '__main__':
    main()
