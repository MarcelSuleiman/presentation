from abc import abstractmethod, ABC
from http import HTTPStatus
from typing import Protocol

import requests
from requests import Response

from plugins.http_check.gateway.exceptions import ForbiddenError, ResponseError


class HttpResponse(Protocol):
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
