import unittest
import fridge_temperature_evaluator


class test_fridge_temp(unittest.TestCase):
    def test_average(self):
        self.assertEqual(fridge_temperature_evaluator.get_average([2, 10, 18, 1]), 7.75)
        self.assertEqual(fridge_temperature_evaluator.get_average(["a", 2, 3, 4]), None)
        self.assertEqual(fridge_temperature_evaluator.get_average(["a", "b", "c", "d"]), None)

    def test_median(self):
        self.assertEqual(fridge_temperature_evaluator.get_median([2, 10, 18, 1]), 6)
        self.assertEqual(fridge_temperature_evaluator.get_median([2, 10, 18, 1, 3]), 3)
        self.assertEqual(fridge_temperature_evaluator.get_median(["a", 2, 3, 4]), None)
        self.assertEqual(fridge_temperature_evaluator.get_median(["a", "b", "c", "d"]), None)

    def test_mode(self):
        self.assertEqual(fridge_temperature_evaluator.get_mode([2, 2, 10, 10, 18, 1]), [2, 10])
        self.assertEqual(fridge_temperature_evaluator.get_mode([2, 2, 18, 1, 3]), [2])
        self.assertEqual(fridge_temperature_evaluator.get_mode([2, 18, 1, 3]), None)
        self.assertEqual(fridge_temperature_evaluator.get_mode(["a", 2, 3, 4]), None)
        self.assertEqual(fridge_temperature_evaluator.get_mode(["a", "b", "c", "d"]), None)

    def test_convert_data(self):
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

        self.assertEqual(fridge_temperature_evaluator.convert_data(json_array),
                         [{'id': 'a', 'average': 3.77, 'median': 3.65, 'mode': [3.53]},
                          {'id': 'b', 'average': 4.08, 'median': 4.14, 'mode': [4.15]},
                          {'id': 'c', 'average': 3.72, 'median': 3.95, 'mode': [3.36, 3.96]}])

    def test_sort_json_array(self):
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
        self.assertEqual(fridge_temperature_evaluator.sort_json_array(json_array, "id", "temperature"),
                         {'a': [3.53, 3.63, 4.63, 3.53, 3.66, 3.67], 'b': [4.13, 4.15, 4.15, 3.88],
                          'c': [3.96, 3.96, 3.95, 3.36, 3.36]})
        self.assertEqual(fridge_temperature_evaluator.sort_json_array(json_array, "id", "timestamp"),
                         {'a': [1509493641, 1509493644, 1509493645, 1509493646, 1509493677, 1510128112],
                          'b': [1509493642, 1509493647, 1510113646, 1510128115],
                          'c': [1509493643, 1509493645, 1509493655, 1510127886, 1510127892]})

    def test_json_array_output(self):
        sorted_dictionary = {'a': [3.53, 3.63, 4.63, 3.53, 3.66, 3.67], 'b': [4.13, 4.15, 4.15, 3.88],
                             'c': [3.96, 3.96, 3.95, 3.36, 3.36]}
        self.assertEqual(fridge_temperature_evaluator.json_array_output(sorted_dictionary),
                         [{'id': 'a', 'average': 3.77, 'median': 3.65, 'mode': [3.53]},
                          {'id': 'b', 'average': 4.08, 'median': 4.14, 'mode': [4.15]},
                          {'id': 'c', 'average': 3.72, 'median': 3.95, 'mode': [3.36, 3.96]}])


if __name__ == '__main__':
    unittest.main()
