from utils.fetch_data import hit_url
from reso.base import ResourceBase
from utils.randgen import ProduceChars
from pprint import pprint

class Planets(ResourceBase):
    """
    Resource class (plural)
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/planets"  # plural
        self.__character_range = [1, 82]   # TODO implement setter method

    def get_count(self):
        plural_character_url = self.home_url + self.__relative_url
        response = hit_url(plural_character_url)
        result = response.json()
        return result

    def get_resource_urls(self):
        # TODO - implement this method similar to above
        number = ProduceChars(1, 83, 4)
        number_url = []
        num_url = {}
        for num in number:
            x = self.home_url + self.__relative_url + f"{num}"
            number_url.append(x)
        num_url.update({"url": number_url})
        return num_url

    def get_urls_random(self, number1):
        single_url ={}
        self.number1 = number1

        single =  self.home_url + self.__relative_url + f"{number1}"
        single_url.update({"url": single})
        return single_url


