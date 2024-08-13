from abc import abstractmethod

from bs4 import ResultSet, BeautifulSoup

from plugins.http_check.gateway.http_gateway import HttpResponse


class SoupGateway:
    @staticmethod
    @abstractmethod
    def find_all(response: HttpResponse, attributes: dict[str, str]) -> ResultSet:
        ...


class SoupGatewayIMPL(SoupGateway):
    def find_all(self, response: str, attributes: dict[str, str]) -> ResultSet:
        soup = BeautifulSoup(response.text, 'html.parser')
        d = soup.find_all(**attributes)
        return d
