# Refridgerator Temperature Evaluator

### Assumptions

#### The main two assumptions for this project were:
* The output was only required to be in the same format as a Json array and not output as a Json object
* The only inputs are going to be Json arrays in the same form as the example given on the task sheet and not reading
from Json objects
```

                                    Example input format

                  [{"id": "a", "timestamp": 1509493641, "temperature": 3.53},
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
```

### How to Run the Code

To run the program using pycharm just simply run the application, it already has a Json Array passed in through main to
the functions so it will return and print out the correct output of the calculations for each fridge id.

However if the code was to be implemented into an existing code base the main function can be removed and then the
convert_data() needs to be called from another function passing in a Json Array for it to return a new Json Array.

### How to Test the Code


### Explanation of Functions


#### json_array_output

* Takes in the sorted fridge data which goes through a for loop and runs all of the calculations for each key and their
values one key at a time
* The results from the calculations are then rounded to 2nd decimal point as specified and then appended to an empty
Json array with their specific ids


#### convert_data()

* The Json array is passed in to this function and then is passed to sort_json_array
* The sort_json_array returns a dictionary containing a list for each id and the values related to these keys
* The dictionary is then passed to the json_array_output function which does all of the calculations and returns
a Json array for main to print


#### sort_json_array()

* The initial design for the method only required the Json array and would statically implement the id and key, however
after some refinement i found that i could create this function to be able to be used for other sets of numerical data
* The key and id are now passed in as strings to this function along with the Json array
* The expected output is a dictionary
```
E.g. "timestamp" could be passed in instead of "temperature" as the key, so now it will only use the timestamp
data instead of temperature
```


#### get_average()

* The get_average function takes in an array which contains Integer values for the current key in the current
 json_array_output iteration.
* Error handling for empty arrays
* Calculates the average by summing the array values and dividing them by the length of the array


#### get_median()

*The get_median function takes in an array which contains Integer values for the current key in the
current json_array_output iteration
* Error handling for empty arrays
* The median function works similar to how a human would calculate the median by hand
* The array is sorted in ascending order and then modulo 2 is applied on the length of the array which tells us whether
its an even (0) or odd number (1).
* If the number is odd the floor division operand (//) is used to divide the length of the array and give a integer which
is then used as the position where the median value is
* If the number is even the median is found by using the same floor division operand to retrieve the first intgeer
 and by moving one position to the left in the array (-1) you can retrieve the second integer. These two integers are then
 added together and divided by 2


#### get_mode()

The design for this function was yet again based off of how we as humans would calculate the mode, which is to count
each value and keep a score of how many times each value has appeared, the highest score being the mode. With that
in mind the get_mode function takes in an array that contains all values for the current key in the json_array_output
iteration. The first step is to check if the array is empty and if it is then nothing is returned to add error
checking and to also optimize speeds for possible larger data. If the array has values in it, it will then create an
empty dictionary and begin looping through the array adding the values as keys with 0 as the value if they are not
already in the new dictionary, however if there is already a key in the dictionary of the same value it will simply
add 1 to the keys value. Once the loop has finished it will calculate the maximum value of the keys and then use that
value to find the mode. This is done by creating an array containing the keys that have values that meet the maximum
value. For instance if there are a max of 3 values of the same type it will only add the keys (which are the values
from the array passed in just converted to keys) which meet the minimum value of 3. Thus returning the most frequent
numbers that appear in the array. Expected value for input is an array containing integers and the expected output is an
array of integers.


#### main()

In this instance the main function is used to simply pass a Json array to the
convert data function which then handles all of the conversion of the data
and returns a Json array. Most of the work is handled by the convert data function
so that if it were implemented into an up and running code base it could simply be
called with the required arguments passed in, this also allows the function to be tested.