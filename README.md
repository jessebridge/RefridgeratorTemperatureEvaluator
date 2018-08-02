# Refridgerator Temperature Evaluator

## Explanation of Functions

### json_array_output
The json_array_output function takes the sorted fridge data and puts it through a for loop which runs
all of the calculations for each key and their values. The for loop gets the all of values for 1 key at a time as an array and
passes them to the calculation functions, which then append the id and the results for each function to an empty array, it then
repeats this loop for each key in the dictionary from the sorted fridge data. The results that are returned are then rounded to
2nd decimal point as specified here so that the math functions were seperated to doing only math.

### convert_data()
The Json array is passed to this function and then it is passed to the sort_jason_array
function where it is then returned as a dictionary containing a list for each id and then
it is passed to the json_array_output function which is then returned to main as a Json list.
The main idea was to have the data in an easy to read format that could be easily used in the following
calculation methods such as median, mode and average, whereas if the data was not formatted it would require
further steps to gather all data and compute the outputs for each id
(eg. getting all temperatures for the fridge with id 'a').

### sort_json_array()
The sort_json_array function takes in a Json array, a string as the id and a string as the key. The initial design
for the method only required the Json array and would statically implement what id and key was required, however
after some refinement i found that i could create this function to be able to be used for other sets of numerical
data. The id and key are now passed in as strings so that in future this function could be used on other data.
For example if the task required the use of the timestamp instead of the temperature then "timestamp" could be
passed in insteadof "temperature" which will provide details on the timestamp instead, this also works for the id as
the task may not require the data to be grouped by an 'id'.

### get_average()
The get_average function takes in an array which contains values for the current key in the json_array_output
iteration, it then checks to see if the array is empty if it is it will return nothing, this is to provide error
checking and to provide optimization/speed as it will not execute the code below it if array is empty. To calculate
the average the sum of the array was divided by the length of the array to always provide a precise calculation no
matter the size of the array or the numerical data within.

### get_median()
The get_median function takes in an array which contains values for the current key in the json_array_output
iteration, it then checks to see if the array is empty if it is it will return nothing, this is to provide error
checking and to provide optimization/speed as it will not execute the code below it if array is empty. If the array
however does have values inside it will sort the array values from smallest to largest and run modulo 2 on the
length of the array which will provide insight to if there is an even or odd number of values. If there are an odd
amount of variables it will return with a remainder of 1 which an if statement checks for, and will set the median
number to the centre position of the array using the floor division operand (//2) which will divide the array by two
and round down if necessary to make sure that the position is a whole number. The median number is then set to the
value of this position. However if the remainder is 0 it means it is an even which requires some extra calculations.
The median number is found by using the same floor division operand and then adding it to the position on its left
which is to subtract 1 from the position found in the centre, these 2 values are then added together and divided by
2 to provide the median number. The idea of how to find the median was mainly through how we as humans would
calculate the median on paper, by finding the 2 centre values, adding them together and then dividing them by 2.

### get_mode()
The design for this function was yet again based off of how we as humans would calculate the mode, which is to count
each value and keep a score of how many times each value has appeared, the highest score being the mode. With that
in mind the get_mode function takes in an array that contains all values for the current key in the json_array_output
iteration. The first step is to check if the array is empty and if it is then nothing is returned to add error
checking and to also optimize speeds for possible larger data. If the array has values in it, it will then create an
empty dictionary and begin looping through the array adding the values as keys with 0 as the value if they are not
already in the new dictionary, however if there is already a key in the dictionary of the same value it will simply
add 1 to the keys value. Once the loop has finished it will calculte the maximum value of the keys and then use that
value to find the mode. This is done by creating an array containing the keys that have values that meet the maximum
value. For instance if there are a max of 3 values of the same type it will only add the keys (which are the values
from the array passed in just converted to keys) which meet the minimum value of 3. Thus returning the most frequent
numbers that appear in the array.

### main()
In this instance the main function is used to simply pass a Json array to the
convert data function which then handles all of the conversion of the data
and returns a Json array. Most of the work is handled by the convert data function
so that if it were implemented into an up and running code base it could simply be
called with the required arguments passed in, this also allows the function to be tested.