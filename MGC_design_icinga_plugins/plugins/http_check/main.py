import json
import re
import sys
import os
from pprint import pprint

from plugins.common.gateway.http_gateway import DnsGatewayIMPL
from plugins.common.controller.controller import DnsControllerIMPL
# from plugins.http_check.controller.controller import ControllerIMPL
from plugins.common.controller.controller import ControllerIMPL
from plugins.http_check.gateway.http_gateway import RequestGatewayIMPL
from plugins.http_check.gateway.soup_gateway import SoupGatewayIMPL
from plugins.http_check.model.service import ServiceIMPL

local_dir = os.path.dirname(__file__)
# sys.path.insert(0, local_dir)

from plugins.common.get_icinga_output import compose_icinga_output
from plugins.http_check.model.model import WebPage


def compose_config(c, custom_class: WebPage) -> list[WebPage]:
    if c is None or c == "" or c == "null":
        raise ValueError("Config is missing.")

    try:
        config_raw = c.replace("'", '\"')
        config_json = json.loads(config_raw)
        # return config_json
        return [custom_class(**v) for k, v in config_json.items()]

    except ValueError as ve:
        raise ValueError(str(ve))

    except KeyError as ke:
        raise KeyError(str(ke.args[0]))

    except TypeError as te:
        raise TypeError(str(te))

    except Exception as ex:
        raise Exception(str(ex))


if __name__ == "__main__":
    args = compose_icinga_output()
    config = compose_config(args.config, custom_class=WebPage)

    for c in config:
        c.url_host_name = re.findall(r'//(.*?)/', str(c.url))[0]

    # print(config)

    service = ServiceIMPL.compose(config)
    request_gateway = RequestGatewayIMPL()
    soup_gateway = SoupGatewayIMPL()
    dns_gateway = DnsGatewayIMPL()

    controller = ControllerIMPL(service=service, http_gateway=request_gateway, soup_gateway=soup_gateway)
    dns_controller = DnsControllerIMPL(service=service, http_gateway=dns_gateway)

    data = controller.get_data()
    # dns_data = dns_controller.get_data()
    dns_controller.get_data()
    print(dns_controller.basket)
