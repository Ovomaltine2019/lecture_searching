import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)


    # načtení povolených klíčů ze souboru
    with open("sequential.json", "r") as f:
        allowed_key = json.load(f)

    # ověření, zda je klíč (field) v množině povolených klíčů
    if field not in allowed_key:
        return None

    with open(file_name, "r") as f:
        data = json.load(f)

    return data.get(field)


def linear_search(sequence, number):
        positions = []
        for n in sequence:
            if n == number:
                positions.append(sequence.index(n))
            else:
                continue

        count = len(positions)
        output = { "positions" : positions, "count" : count }
        if positions == [] and count == 0:
            return "Hledané číslo není v sekvenci.", output
        return output


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    # print(sequential_data)
    number = 15
    linearni_hledani = linear_search(sequential_data, number)
    print(linearni_hledani)


if __name__ == '__main__':
    main()