import TermGeneratorClass


class UnsortedTermListGenerator:

    def __init__(self):
        self.__unsorted_list = []

    def generate_from_list(self, mylist):
        self.__unsorted_list = []
        term_generator = TermGeneratorClass.TermGenerator()  # object that generates terms from tweets
        for each in mylist:
            local_term_list = term_generator.\
                get_terms_from_string(each[4])  # returns a list of normalized terms from a string
            for local_term in local_term_list:   # adds a tuple of term and doc ID to the global list
                item = (local_term, each[1])
                self.__unsorted_list.append(item)
        return self.__unsorted_list

