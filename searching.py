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
        count = 0
        for n in sequence:
            if n == number:
                positions.append(sequence.index(n) + 1)
                count += 1
            else:
                continue

        output = { "positions" : positions, "count" : count }
        if positions == [] and count == 0:
            return "Hledané číslo není v sekvenci.", output
        return output

        # asymptotická složitost nejlepší scénář big O(1), nejhorší scénář big O(n)


def pattern_search(seq, vzor):
    positions = []
    for i in range(len(seq) - len(vzor) + 1):
        win = seq[i:i+len(vzor)]
        if win == vzor:
            positions.append(i)
        else:
            continue
    return set(positions)


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    # print(sequential_data)
    number = 63
    linearni_hledani = linear_search(sequential_data, number)
    # print(linearni_hledani)
    hledani_vzoru = pattern_search(read_data("sequential.json", "dna_sequence"), "ATA")
    print(hledani_vzoru)

if __name__ == '__main__':
    main()