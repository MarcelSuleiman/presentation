from abc import abstractmethod
from typing import Dict

from plugins.http_check.gateway import http_gateway
from plugins.http_check.model import service


class DnsController:
    def __init__(self, service, http_gateway):
        self.service = service
        self.http_gateway = http_gateway

    @abstractmethod
    def get_data(self):
        ...


class DnsControllerIMPL(DnsController):
    def __init__(self, service, http_gateway):
        super().__init__(service, http_gateway)
        self.basket: Dict[str, list] = {}

    def get_data(self):
        for page in self.service.pages:
            response = page.get_answer(self.http_gateway)
            self.basket[page.name] = [r for r in response]

    #         for r in response:
    #             print(r)
    #
    #     return self.basket
    #
    # def print_ip(self):
    #     print(self.get_data())
