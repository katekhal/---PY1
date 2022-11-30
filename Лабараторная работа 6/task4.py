import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(name) -> list[dict]:
    list_dict = []  # TODO реализовать конвертер из csv в json
    list_rows = []
    with open(name, 'r') as f:
        result = f.readlines()
        headings = result[0].rstrip().split(sep=',')
        for row in result[1:]:
            list_rows.append(row.rstrip().split(sep=','))

        for element in list_rows:
            list_dict.append(dict(zip(headings, element)))
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))