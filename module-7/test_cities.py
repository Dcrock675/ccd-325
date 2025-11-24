# test_cities.py
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        # Test with just city and country
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

        # Test with city, country, and population
        result = city_country("houston", "usa", 2310000)
        self.assertEqual(result, "Houston, Usa - population 2310000")

        # Test with city, country, population, and language
        result = city_country("tokyo", "japan", 13960000, "japanese")
        self.assertEqual(result, "Tokyo, Japan - population 13960000, Japanese")

if __name__ == "__main__":
    unittest.main()
