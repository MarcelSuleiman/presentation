from argparse import Namespace
from typing import List
import sys
import os

local_dir = os.path.dirname(__file__)
# lib_dir = os.path.dirname(os.path.dirname(__file__)) + "\\lib"
sys.path.insert(0, local_dir)
# sys.path.insert(1, lib_dir)

# from FIO.IcingaAlarm import IcingaAlarm
# from FIO import IcingaOutput
from plugins.common.get_cmd_args import compose_input_arguments


# from lib.FIO.IcingaAlarm import IcingaAlarm
# from lib.FIO.IcingaOutput import IcingaOutput

# from input_parser import compose_input_arguments


# class IcingaOutputWrap(IcingaOutput):
#     """
#     Singletone for IcingaOutput
#     """
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(IcingaOutput, cls).__new__(cls)
#         return cls._instance
#
#
# def get_fio_fields(without: List[str]) -> List[str]:
#     fio_fields = []
#     alarm = IcingaAlarm()
#     temp: List[str] = alarm.getHiddenFieldsShort()
#     for f in temp:
#         if f not in without:
#             fio_fields.append(f.lower())
#
#     return list(set(fio_fields))


def compose_icinga_output(): # -> tuple[IcingaOutputWrap, Namespace]:
    # a = IcingaOutputWrap()
    args = compose_input_arguments()

    # a.setDefaultMsgGroup('OSS-Icinga')
    # # a.setDefaultMsgGroup(args.plugin_default_msgg)
    #
    # a.setPluginErrorMsgGroup('OSS-Icinga')
    # # a.setPluginErrorMsgGroup(args.plugin_error_msgg)
    #
    # a.setFIOErrorMsgGroup('OSS-Icinga')
    # # a.setFIOErrorMsgGroup(args.fio_error_msgg)
    #
    # a.setPluginErrorSeverity('Minor')
    # # a.setPluginErrorSeverity(args.plugin_error_sev)
    #
    # a.setFIOErrorSeverity('Minor')
    # # a.setFIOErrorSeverity(args.fio_error_sev)

    # msv = args.maximum_severity
    #
    # if msv == "Major" or msv == "4":
    #     a.setMaxSeverityToMajor()
    # elif msv == "Minor" or msv == "3":
    #     a.setMaxSeverityToMinor()
    # elif msv == "Warning" or msv == "2":
    #     a.setMaxSeverityToWarning()

    return args
