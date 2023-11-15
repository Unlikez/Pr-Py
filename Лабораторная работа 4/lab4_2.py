# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    line_ = []
    with open(INPUT_FILENAME) as f:
        read = csv.DictReader(f)
        [line_.append(rows) for rows in read]

    with open(OUTPUT_FILENAME, 'w') as d:
        json.dump(line_, d, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
