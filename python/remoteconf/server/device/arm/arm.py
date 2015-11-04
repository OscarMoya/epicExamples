import json


class ARM:

    def __init__(self):
        self.in_port1_lambda = None
        self.in_port2_lambda = None

        self.out_port1_lambda = None
        self.out_port2_lambda = None
        self.client_1_services = None
        self.client_2_services = None

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
