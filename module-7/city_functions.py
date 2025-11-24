# city_functions.py

def city_country(city, country, population=None, language=None):
    """
    Return a string in one of the following formats:
    - City, Country
    - City, Country - population xxx
    - City, Country - population xxx, Language
    """
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result


# City calls
print(city_country("santiago", "chile"))                          # City, Country
print(city_country("houston", "usa", 2310000))                    # City, Country - population
print(city_country("tokyo", "japan", 13960000, "japanese"))       # City, Country - population, Language
