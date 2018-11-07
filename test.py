import csv


def main():
    with open('tweets.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
