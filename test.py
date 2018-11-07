import csv


def main():
    data = []
    posting_generator = []
    with open('tweets.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        doc_id_counter = 1
        for row in reader:
            dataset = (doc_id_counter, row[0], row[1], row[2], row[3], row[4])
            data.append(dataset)
            doc_id_counter = doc_id_counter + 1

    for each in data:
        tweet_text = each[5]
        doc_id = each[0]
        posting_generator.extend(get_terms_from_tweet_text(tweet_text, doc_id))

    posting_generator.sort()
    generate_structure(posting_generator)


def get_terms_from_tweet_text(input_string, doc_id):
    result_list = []
    tweet_tokens = input_string.split()
    for each in tweet_tokens:
        normalized_terms = normalize(each)
        for eachterm in normalized_terms:
            not_on_the_list = True
            for each_result in result_list:
                if each_result[0] == eachterm:
                    not_on_the_list = False
            if not_on_the_list:
                posting_tuple = (eachterm, doc_id)
                result_list.append(posting_tuple)
    return result_list


def generate_structure(unindexed_list):
    dict = {}
    list_container = []
    counter = 0
    while counter < len(unindexed_list):
        content = unindexed_list[counter][0]
        posting_list = []
        frequency = 1
        posting_list.append(unindexed_list[counter][1])
        for subcounter in range(counter + 1, len(unindexed_list)):
            nextcontent = unindexed_list[subcounter][0]
            if content == nextcontent:
                posting_list.append(unindexed_list[subcounter][1])
                frequency = frequency + 1
            else:
                break
        # todo tuple

    return None


def normalize(token):
    terms_from_token = []
    term = token.lower()
    if term.startswith('"'):
        term = term[1:]
    if term.startswith('#'):
        term = term[1:]
    if term.endswith('"'):
        term = term[:-1]
    if term.endswith('.'):
        term = term[:-1]
    if term.endswith(','):
        term = term[:-1]
    if term.startswith('@'):
        term = term[1:]
    if term.endswith('?'):
        term = term[:-1]
    if term.endswith('!'):
        term = term[:-1]

    terms_from_token.append(term)
    return terms_from_token


if __name__ == '__main__':
    main()
