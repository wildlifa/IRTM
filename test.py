import csv


def main():
    data = []
    with open('tweets.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            dataset = (row[0], row[1], row[2], row[3], row[4])
            data.append(dataset)

    print(data[0][4])


if __name__ == '__main__':
    main()
