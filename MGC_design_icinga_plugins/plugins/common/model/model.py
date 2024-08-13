from abc import abstractmethod
from typing import Optional
import re

from bs4 import ResultSet
from pydantic import HttpUrl, Field

from plugins.common.gateway.http_gateway import DnsGateway, DnsResponse
from plugins.dns_check.model.model import Section
from plugins.common.gateway.http_gateway import RequestGateway, HttpResponse
from plugins.common.model.base import Model
from plugins.common.model.type_alias import DictAny


class Product(Model):
    name: str
    price: float


class WebPage(Model):
    name: str
    url: HttpUrl
    # url_host_name: str = re.findall(r'//(.*?)/', str(url))[0]
    attributes: DictAny = Field(exclude=True)
    headers: Optional[DictAny] = None
    url_host_name: Optional[str] = None

    def universal_get(self, client: RequestGateway | DnsGateway):
        """
        Very good documentation.
        :param client:
        :return:
        """
        if isinstance(client, RequestGateway):
            return client.get(url=self.url, headers=self.headers)

        if isinstance(client, DnsGateway):
            return client.get(url_host_name=self.url_host_name)

    def get_response(self, http_client: RequestGateway) -> HttpResponse:
        return http_client.get(url=self.url, headers=self.headers)

    def get_answer(self, dns_client: DnsGateway) -> DnsResponse:
        return dns_client.get(url_host_name=self.url_host_name)

    @property
    def url_host_name(self):
        return self._url_host_name

    @url_host_name.setter
    def url_host_name(self, value):
        self._url_host_name = re.findall(r'//(.*?)/', str(self.url))[0]



    # @abstractmethod
    def parse_response(self, response: ResultSet) -> None:
        ...


class Shop(WebPage):
    products: list[Product] = Field(default_factory=list)
    attributes: DictAny = Field(exclude=True)

    @abstractmethod
    def parse_response(self, response: ResultSet) -> None:
        data = self.get_answer()
