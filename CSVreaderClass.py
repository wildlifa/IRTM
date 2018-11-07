import csv


class CSVreader:

    def __init__(self):
        self.__raw_list = []

    def get_list_from_path(self, path):
        self.__raw_list = []
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            doc_id_counter = 1
            for row in reader:
                dataset = (doc_id_counter, row[0], row[1], row[2], row[3], row[4])
                self.__raw_list.append(dataset)
                doc_id_counter = doc_id_counter + 1
        return self.__raw_list

