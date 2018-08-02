def convert_data(json_object_data):
    json_file_as_dictionary = load_json_file(json_object_data)
    for key, value in json_file_as_dictionary.items():
        print(key, value)
        avg_dict = round(get_average(value),2)
        print(avg_dict)

    get_median(json_file_as_dictionary)
    get_mode(json_file_as_dictionary)
    # final_result = write_json_format(json_file_as_dictionary)
    # return final_result


def load_json_file(json_object_data):
    sorted_data = {}
    # Loop through each item in the array
    for element in json_object_data:
        if element["id"] not in sorted_data.keys():
            sorted_data[element["id"]] = [element["temperature"]]
        else:
            sorted_data[element["id"]].append(element["temperature"])
    return sorted_data


def get_average(json_file_as_dictionary):
    for value in json_file_as_dictionary:
        sum_of_values = sum(json_file_as_dictionary)
        num_of_values = len(json_file_as_dictionary)
        average = sum_of_values / num_of_values
    return average


def get_median(json_file_as_dictionary):
    for key, value in json_file_as_dictionary.items():
        # sort values into smallest to largest
        value.sort()
        array_length = len(value)
        remainder = array_length % 2
        if remainder == 1:
            median_number = array_length // 2
            median_number = round(median_number, 2)
            print(key, value[median_number])
            return key, value[median_number]
        else:
            median_number = (value[array_length // 2] + value[array_length // 2 - 1]) / 2
            median_number = round(median_number, 2)
            print(key, median_number)
            # find number on either side of this position -1 and +1 then add the 2 values together and divide


def get_mode(json_file_as_dictionary):
    for key, value in json_file_as_dictionary.items():
        calc = {}
        for item in value:
            if item not in calc.keys():
                calc[item] = 0
            else:
                calc[item] += 1
        maximum_value = max(calc.values())
        modes = [key for key in calc.keys() if calc[key] == maximum_value]
        print(key, modes)


def main():
    json_object_data = [{"id": "a", "timestamp": 1509493641, "temperature": 3.53},
                        {"id": "b", "timestamp": 1509493642, "temperature": 4.13},
                        {"id": "c", "timestamp": 1509493643, "temperature": 3.96},
                        {"id": "a", "timestamp": 1509493644, "temperature": 3.63},
                        {"id": "c", "timestamp": 1509493645, "temperature": 3.96},
                        {"id": "a", "timestamp": 1509493645, "temperature": 4.63},
                        {"id": "a", "timestamp": 1509493646, "temperature": 3.53},
                        {"id": "b", "timestamp": 1509493647, "temperature": 4.15},
                        {"id": "c", "timestamp": 1509493655, "temperature": 3.95},
                        {"id": "a", "timestamp": 1509493677, "temperature": 3.66},
                        {"id": "b", "timestamp": 1510113646, "temperature": 4.15},
                        {"id": "c", "timestamp": 1510127886, "temperature": 3.36},
                        {"id": "c", "timestamp": 1510127892, "temperature": 3.36},
                        {"id": "a", "timestamp": 1510128112, "temperature": 3.67},
                        {"id": "b", "timestamp": 1510128115, "temperature": 3.88}]
    final_result = convert_data(json_object_data)
    # print(final_result)


main()
