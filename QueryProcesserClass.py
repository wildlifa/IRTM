class QueryProcessor:

    def __init__(self, dictionary):
        self.__dictionary = dictionary

    def print_posting_list_by_term(self, term):
        print("printing documents of word: " + term)
        x = self.__dictionary.get(term)
        x_list = x[2]
        for each in x_list:
            print(each)
        print("---done---")
