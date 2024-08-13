from abc import abstractmethod

from plugins.common.gateway.http_gateway import DnsGateway
from plugins.http_check.gateway.http_gateway import RequestGateway
from plugins.http_check.gateway.soup_gateway import SoupGateway
from plugins.http_check.model.service import Service


class Controller:
    def __init__(self, service: Service, http_gateway: RequestGateway, soup_gateway: SoupGateway):
        self.service = service
        self.http_gateway = http_gateway
        self.soup_gateway = soup_gateway

    @abstractmethod
    def get_data(self) -> Service:
        ...


class ControllerIMPL(Controller):
    def get_data(self) -> Service:
        for page in self.service.pages:
            response = page.get_response(self.http_gateway)
            item = self.soup_gateway.find_all(response, page.attributes)
            print(item)
            page.parse_response(item)

    def something_else(self):
        pass
