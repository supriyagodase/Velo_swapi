not_implemented_error_msg = "This method has not been implemented"


# TODO - you can also convert this class into abstract class and
# define methods as abstract methods


class ResourceBase(object):
    """
    Base class representing required methods to be implemented by all resource
    classes
    """

    # TODO - add all resources in this list
    resources = ["planets", "spaceships", "people", "vehicles"]

    def __init__(self):
        self.home_url = "https://swapi.dev/"
        self.planets = self.home_url + "api/people/"
    def get_count(self):
        raise NotImplementedError(not_implemented_error_msg)

    def get_resource_urls(self, resource):
        raise NotImplementedError(not_implemented_error_msg)

