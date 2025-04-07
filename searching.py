import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """


    if field not in {"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        sekvencia = json.load(json_file)

    return sekvencia[field]


def linear_search(sekvencia, cislo):
    pozicie = []
    count = 0
    index = 0

    while index < len(sekvencia):
        if sekvencia[index] == cislo:
            pozicie.append(index)
            count = count + 1
        index = index + 1

    return {"positions":pozicie,
            "count": count}

#     slovnik = {}
#     zoznam_pozic = []
#     sucet = 0
#     for i in sekvencia:
#         if i == cislo:
#             zoznam_pozic = zoznam_pozic.append(sekvencia[i])
#             slovnik["positions"] = zoznam_pozic
#             sucet = sucet + 1
#             slovnik["count"] = sucet
#
#     return slovnik
# print(linear_search([54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5], 2))


def  pattern_search(sekvencia, vzor):
    # i = 0
    # mnozina_indexov = set()
    # for i in sekvencia:
    #     if sekvencia[i:i+3] == vzor:
    #         mnozina_indexov.append(i + 2)
    # return mnozina_indexov

    mnozina_indexov = set()
    velkost_vzoru = len(vzor)

    left_index = 0
    right_index = velkost_vzoru

    while right_index < len(sekvencia):
        for i in range(velkost_vzoru):
            if vzor[i] != sekvencia[left_index + i]:
                break
        else:
            mnozina_indexov.add(left_index + velkost_vzoru // 2)

        left_index = left_index + 1
        right_index = right_index + 1

    return mnozina_indexov

def binary_search(zoznam, cislo):
    i = 0
    while i < len(zoznam):
        if len(zoznam) % 2 == 0:
            zoznam[i]



    return i


def main():
    file_name = "sequential.json"

    sekvencia = read_data(file_name, field="unordered_numbers")
    print(sekvencia)

    search = linear_search(sekvencia, 2)
    print(search)

    dna = read_data(file_name, field="dna_sequence")
    print(dna)
    pattern = pattern_search(dna, "ATA")
    print(pattern)

    zoradeny_zoznam = read_data(file_name, field="ordered_numbers")
    print(zoradeny_zoznam)
    binary = binary_search(zoradeny_zoznam, 25)
    print(binary)

if __name__ == '__main__':
    main()