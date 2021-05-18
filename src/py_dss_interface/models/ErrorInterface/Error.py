# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/05/2021
"""
import ctypes
from py_dss_interface.models.ErrorInterface.ErrorCode import ErrorCode
from py_dss_interface.models.ErrorInterface.ErrorDesc import ErrorDesc


class Error(ErrorCode, ErrorDesc):
    """
    This interface implements the Error interface of OpenDSS by declaring 2 procedures for accessing the different
    properties included in this interface.
    """
    pass
