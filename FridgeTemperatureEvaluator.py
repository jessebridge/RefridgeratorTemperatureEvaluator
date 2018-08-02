def convert_data(json_object_data):
    fridge_data_as_list = sort_json_array(json_object_data, "id", "temperature")
    return json_array_output(fridge_data_as_list)


def json_array_output(fridge_data_as_list):
    output_as_array = []
    for key, value in fridge_data_as_list.items():
        average = round(get_average(value), 2)
        median = round(get_median(value), 2)
        mode = get_mode(value)
        output_as_array.append({"id": "{}".format(key), "average": average, "median": median, "mode": mode})
    return output_as_array


def sort_json_array(json_object_data, id, key):
    sorted_data = {}
    # Loop through each item in the array
    for element in json_object_data:
        if element[id] not in sorted_data.keys():
            sorted_data[element[id]] = [element[key]]
        else:
            sorted_data[element[id]].append(element[key])
    return sorted_data


def get_average(fridge_data_as_list):
    num_of_values = len(fridge_data_as_list)
    if num_of_values == 0:
        return None
    else:
        sum_of_values = sum(fridge_data_as_list)
        num_of_values = len(fridge_data_as_list)
        average = sum_of_values / num_of_values
        return average


def get_median(fridge_data_as_list):
    array_length = len(fridge_data_as_list)
    if array_length == 0:
        return None
    else:
        fridge_data_as_list.sort()
    remainder = array_length % 2
    if remainder == 1:
        median_number = fridge_data_as_list[array_length // 2]
    else:
        median_number = (
                            fridge_data_as_list[array_length // 2] + fridge_data_as_list[array_length // 2 - 1]) / 2
    return median_number


def get_mode(fridge_data_as_list):
    if len(fridge_data_as_list) == 0:
        return None
    else:
        calc = {}
        for item in fridge_data_as_list:
            if item not in calc.keys():
                calc[item] = 0
            else:
                calc[item] += 1
        maximum_value = max(calc.values())
        mode = [key for key in calc.keys() if calc[key] == maximum_value]
        return mode


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
    output = convert_data(json_object_data)
    print(output)


main()
