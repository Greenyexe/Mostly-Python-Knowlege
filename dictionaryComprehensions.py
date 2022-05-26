# dictionary comprehension = create dictionaryies using and expression
# can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

#citiesInF = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

#citiesInC = {key: (round((value - 32)*(5/9))) for (key, value) in citiesInF.items()}
#print(citiesInC)

#weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}
#sunnyWeather = {key: value for (key, value) in weather.items() if value == "sunny"}

#print(sunnyWeather)

#citiesInF = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
#warmOrCold = {key: ("Warm" if value >= 50 else "Cold") for (key, value) in citiesInF.items()}

#print(warmOrCold)

def checkTemp(value):
    if value >= 70:
        return "Hot"
    elif 69 >= value >=40:
        return "Warm"
    else:
        return "Cold"

citiesInF = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
warmOrCold = {key: checkTemp(value) for (key, value) in citiesInF.items()}
print(warmOrCold)