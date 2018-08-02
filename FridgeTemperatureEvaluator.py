def convert_data(json_array):
    """
    Passes Json array to be sorted and then run calculations

    :param json_array: Json Array
    :return: Json Array
    """
    sorted_fridge_data = sort_json_array(json_array, "id", "temperature")
    return json_array_output(sorted_fridge_data)


def json_array_output(sorted_fridge_data):
    """
    Passes the sorted data to each calculation method and returns the final Json array

    :param sorted_fridge_data: Dictionary
    :return: Json array
    """
    output_as_array = []
    for key, value in sorted_fridge_data.items():
        average = round(get_average(value), 2)
        median = round(get_median(value), 2)
        mode = get_mode(value)
        output_as_array.append({"id": "{}".format(key), "average": average, "median": median, "mode": mode})
    return output_as_array


def sort_json_array(json_array, id, key):
    """
    Sorts the data with the same id into a dictionary with all values in a list

    :param json_array:
    :param id: String
    :param key: String
    :return: Dictionary
    """
    sorted_data = {}
    for element in json_array:
        if element[id] not in sorted_data.keys():
            sorted_data[element[id]] = [element[key]]
        else:
            sorted_data[element[id]].append(element[key])
    return sorted_data


def get_average(sorted_fridge_data):
    """
    Gets the average number from the array it is passed

    :param sorted_fridge_data:
    :return: average as float
    """
    num_of_values = len(sorted_fridge_data)
    if num_of_values == 0:
        return None
    else:
        sum_of_values = sum(sorted_fridge_data)
        num_of_values = len(sorted_fridge_data)
        average = sum_of_values / num_of_values
        return average


def get_median(sorted_fridge_data):
    """
    Gets the median value from the array it is passed

    :param sorted_fridge_data:
    :return: median as float
    """
    array_length = len(sorted_fridge_data)
    if array_length == 0:
        return None
    else:
        sorted_fridge_data.sort()
        remainder = array_length % 2
        if remainder == 1:
            median_number = sorted_fridge_data[array_length // 2]
        else:
            median_number = (sorted_fridge_data[array_length // 2] + sorted_fridge_data[array_length // 2 - 1]) / 2
        return median_number


def get_mode(sorted_fridge_data):
    """
    Gets the mode value from the array it is passed

    :param sorted_fridge_data:
    :return: mode as array
    """
    if len(sorted_fridge_data) == 0:
        return None
    else:
        calc = {}
        for item in sorted_fridge_data:
            if item not in calc.keys():
                calc[item] = 0
            else:
                calc[item] += 1
        maximum_value = max(calc.values())
        mode = [key for key in calc.keys() if calc[key] == maximum_value]
        return mode


def main():
    """
    The main function in this instance is simply calling the convert data function
    """
    json_array = [{"id": "a", "timestamp": 1509493641, "temperature": 3.53},
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
    output = convert_data(json_array)
    print(output)


main()
