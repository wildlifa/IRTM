class TermGenerator:

    def __init__(self):
        self.__term_list = []

    # returns a list of normalized terms from a string
    def get_terms_from_string(self, my_string):
        self.__term_list = []
        my_string = my_string.replace("[NEWLINE]", "")  # removes newline symbols
        my_string = my_string.lower()   # lowers all letters to lower case
        my_string = my_string.replace("n't", ' not')  # splits words with n't
        tokens = my_string.split()
        for token in tokens:
            token = ''.join(e for e in token if e.isalnum())   # removes all garbage symbols
            https_index = token.find("https")  # removes https links from candidate list
            if https_index == 0:
                token = ""
            if token != "":
                not_on_the_list = True
                for each_result in self.__term_list:  # only add a term if its not already there
                    if each_result == token:
                        not_on_the_list = False
                if not_on_the_list:
                    self.__term_list.append(token)
        return self.__term_list
