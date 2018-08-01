
def load_json_file():
    sorted_data = {}
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
    # Loop through each item in the array
    for element in json_object_data:
        if element["id"] not in sorted_data.keys():
            sorted_data[element["id"]] = [element["temperature"]]
        else:
            sorted_data[element["id"]].append(element["temperature"])
    return sorted_data


def calculate_average(json_file_as_dictionary):
    for key, value in json_file_as_dictionary.items():
        sum_of_values = sum(value)
        num_of_values = len(value)
        average = sum_of_values / num_of_values
        average = round(average, 2)
        print(key, average)
        #       need to consider how to return this either as a dictionary or variable


def calculate_median(json_file_as_dictionary):
    for key, value in json_file_as_dictionary.items():
        # sort values into smallest to largest
        value.sort()
        array_length = len(value)
        remainder = array_length % 2
        if remainder == 1:
            median_number = array_length// 2
            median_number = round(median_number, 2)
            print(key, value[median_number])
            return key, value[median_number]
        else:
            median_number = (value[array_length //2] + value[array_length // 2 - 1]) / 2
            median_number = round(median_number, 2)
            print(key, median_number)

            # find number on either side of this position -1 and +1 then add the 2 values together and divide


# calculate the median for each Id
# def calculate_mode(jason_file_as_list):
#
#
# # calculate the mode for each Id
#
# def write_json_format(jason_file_as_dictionary):


def main():
    json_file_as_dictionary = load_json_file()
    calculate_average(json_file_as_dictionary)
    calculate_median(json_file_as_dictionary)
    # calculate_mode(json_file_as_dictionary)
    # write_json_format(json_file_as_dictionary)
    #


main()