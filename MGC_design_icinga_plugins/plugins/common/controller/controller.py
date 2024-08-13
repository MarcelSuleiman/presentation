from abc import abstractmethod
from typing import Dict

from plugins.common.gateway.http_gateway import DnsGateway
from plugins.http_check.gateway.http_gateway import RequestGateway
from plugins.http_check.gateway.soup_gateway import SoupGateway
from plugins.http_check.model.service import Service


class Controller:
    def __init__(self, service: Service, http_gateway: RequestGateway | DnsGateway, soup_gateway: SoupGateway):
        self.service = service
        self.http_gateway = http_gateway
        self.soup_gateway = soup_gateway

    @abstractmethod
    def get_data(self) -> Service:
        ...


class ControllerIMPL(Controller):
    def get_data(self) -> Service:
        for page in self.service.pages:
            # response = page.get_response(self.http_gateway)
            response = page.universal_get(self.http_gateway)
            if isinstance(self.http_gateway, RequestGateway):
                item = self.soup_gateway.find_all(response, page.attributes)
                print(item)
                page.parse_response(item)
            else:
                response = page.get_answer(self.http_gateway)
                for r in response:
                    print(r)

    def something_else(self):
        pass


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