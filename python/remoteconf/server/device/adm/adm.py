import json


class ADM:

    def __init__(self):

        self.port1_lambda = None
        self.port2_lambda = None
        self.port3_lambda = None
        self.port4_lambda = None

        self.routes = list()

    def configure(self, **kwargs):

        for attribute in kwargs.keys():
            setattr(self, attribute, kwargs[attribute])

    def show_configuration(self):
        return_dict = dict()
        for attribute in self.__dict__:
            if attribute.startswith("__"):
                pass
            return_dict[attribute] = getattr(attribute, self.__dict__[attribute])

        return json.dumps(return_dict)



