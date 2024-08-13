from abc import abstractmethod

from plugins.http_check.model.base import Model
from plugins.http_check.model.model import WebPage, Shop
from plugins.http_check.model.type_alias import DictAny


class Service(Model):
    pages: list[WebPage]

    @classmethod
    @abstractmethod
    def compose(cls, list_of_pages: list[WebPage]):
        ...


class ServiceIMPL(Service):
    pages: list[WebPage]

    @classmethod
    def compose(cls, list_of_pages):
        # TODO add list comprehention from -C argparse
        return cls(pages=list_of_pages)

