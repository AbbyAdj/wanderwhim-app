import requests

class City:
    def __init__(self, **city_data):
        self.city_name = city_data["name"]
        self.country = city_data["country"]
        # e.g. self.weather = WeatherData()

class GeneralData:
    def __init__(self, city_name):
        # Use Google Places API
        self.city = city_name

    def get_city_data(self):
        """This will get all city data including city name, lat-long, city id, city categories, geographical data"""
        pass


    def extra_information(self):
        """Fun facts about the location to be added to the city page"""
        pass


class TravelData:
    """This includes data about travel(train stations, airports, etc.) as well as weather data"""
    def __init__(self):
        pass

    def get_train_stations(self):
        pass

    def get_airports(self):
        pass

    def get_weather(self):
        pass


class CityActivities:
    # I might end up inputting these myself. But as the project gets larger, I would have to figure out a way to use
    # these methods.
    def __init__(self):
        pass

    def get_cultural(self):
        pass

    def get_historical(self):
        pass

    def get_fun(self):
        pass

    def get_intense(self):
        pass

    def get_relaxing(self):
        pass


class CityFood:
    # The foods are being classified by country/region. However, they will need tags to classify them as either mild,
    # spicy, savory, sweet, etc. Use the Google maps API to show their locations or to simply help with the search.
    def __init__(self):
        pass

    def get_asian(self):
        pass

    def get_african(self):
        pass

    def get_mexican(self):
        pass

    def get_continental(self):
        pass

    def get_american(self):
        pass

    def get_arabic(self):
        pass


class CityStay:
    # These are hotel stays and other accommodation.
    # These also need tags for later on in the project. For instance, cozy, contemporary, etc.
    def __init__(self):
        pass

    def get_hotels(self):
        pass

    def get_alternative(self):
        # i.e. anything other than a hotel
        pass

    def get_cheapest(self):
        # This and the one below are dependent on the choice of either a hotel or alternative accommodation or both.
        pass

    def get_expensive(self):
        pass



