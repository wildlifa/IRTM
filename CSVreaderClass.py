import csv


class CSVreader:

    def __init__(self):
        self.__raw_list = []

    # turns an CSV file into a list of tuples which are sorted by ID
    def get_list_from_path(self, path):
        self.__raw_list = []
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for row in reader:
                dataset = (row[0], row[1], row[2], row[3], row[4])
                self.__raw_list.append(dataset)
            self.__raw_list.sort(key=by_tweet_id)
            return self.__raw_list


def by_tweet_id(elem):
    return elem[1]

