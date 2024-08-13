from abc import abstractmethod

from plugins.common.model.base import Model
from plugins.common.model.model import WebPage, Shop
from plugins.common.model.type_alias import DictAny


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

