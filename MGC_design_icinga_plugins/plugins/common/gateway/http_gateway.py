from abc import abstractmethod, ABC
from http import HTTPStatus
from typing import Protocol

import dns
import dns.resolver
import requests
from requests import Response

from plugins.dns_check.model.model import Section
from plugins.common.gateway.exceptions import ForbiddenError, ResponseError


class HttpResponse(Protocol):
    @property
    @abstractmethod
    def text(self) -> str:
        ...


class DnsResponse(Protocol):
    @property
    @abstractmethod
    def text(self) -> str:
        ...


class RequestGateway(ABC):
    @abstractmethod
    def get(self, url, headers):
        ...


class RequestGatewayIMPL(RequestGateway):
    def get(self, url, headers) -> HttpResponse:
        response = requests.get(url=url, headers=headers)

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise ForbiddenError(f"Forbidden access to {url=}")
        elif not response.status_code == HTTPStatus.OK:
            raise ResponseError(f"Status code of response was not 200")

        return response


class DnsGateway(ABC):
    @abstractmethod
    def get(self, url_host_name):
        ...


class DnsGatewayIMPL(DnsGateway):
    def get(self, url_host_name: str) -> dns.resolver.Answer:
        my_resolver = dns.resolver.Resolver()
        my_resolver.nameservers = ['8.8.8.8'] # [section.dns_server]
        my_resolver.port = 53 # section.dns_port
        my_resolver.lifetime = 10 # section.timeout

        answer = my_resolver.resolve(
            qname=url_host_name, # section.dns_entry,
            rdtype='A', # section.dns_record_type,
            tcp=False, # section.dns_protocol,
            raise_on_no_answer=True
        )

        return answer
