def load_data_from_file_into_list(filename: str):
    data_list = []
    file = open(filename, 'r')
    lines = file.read().splitlines()
    file.close()

    for line in lines:
        if line != "END":
            data_list.append(line)

    return data_list


def load_data_from_file_into_dictionary(filename: str):
    data_dict = {}
    current_key = None
    file = open(filename, 'r')
    lines = file.read().splitlines()
    file.close()

    for line in lines:
        if line.startswith("COLUMN"):
            current_key = line.split()[1]
            data_dict[current_key] = []
        elif line != "END":
            data_dict[current_key].append(line)

    return data_dict


def output_data_from_list(data_table: list):
    print(f"Displaying data from list...")
    for item in data_table:
        if item.startswith("COLUMN"):
            column_name = item.replace("COLUMN ", "")
            print(f"\n{'*' * 70}\n{column_name}\n{'*' * 70}")
        else:
            print(f"{item}")
            

def output_data_from_dictionary(data_table: dict):
    print(f"Displaying data from dictionary...")
    for column_name, values in data_table.items():
        print(f"\n{'*' * 70}\n{column_name}\n{'*' * 70}")
        for value in values:
            print(f"{value}")


def output_total_mean_median(data_table, total_column_name: str):
    total = 0
    values = []
    non_numeric_found = False
    data_type = "dictionary" if isinstance(data_table, dict) else "list"

    if isinstance(data_table, list):
        if f"COLUMN {total_column_name}" in data_table:
            index = data_table.index(f"COLUMN {total_column_name}") + 1
            while index < len(data_table) and not data_table[index].startswith("COLUMN"):
                if data_table[index].isdigit():
                    value = int(data_table[index])
                    total += value
                    values.append(value)
                else:
                    non_numeric_found = True
                index += 1
        else:
            print(f"Column: {total_column_name} could not be found")
            return

    elif isinstance(data_table, dict):
        if total_column_name in data_table:
            for value in data_table[total_column_name]:
                if value.isdigit():
                    numeric_value = int(value)
                    total += numeric_value
                    values.append(numeric_value)
                else:
                    non_numeric_found = True
        else:
            print(f"Column: {total_column_name} could not be found")
            return

    if non_numeric_found:
        print(f"One or more values in {total_column_name} could not be converted into numerical values")

    mean = total / len(values) if values else 0
    median = sorted(values)[len(values) // 2] if values else 0

    print(f"\nDisplaying total from column {total_column_name} from {data_type}...")
    print(f"Total from column {total_column_name} = {total}")
    print(f"The mean of column {total_column_name} = {mean}")
    print(f"The median of column {total_column_name} = {median}")

