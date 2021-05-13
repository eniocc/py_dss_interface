# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
from py_dss_interface.models.PD_Elements.Lines.LinesV import LinesV
from py_dss_interface.models.PD_Elements.Lines.LinesS import LinesS
from py_dss_interface.models.PD_Elements.Lines.LinesI import LinesI
from py_dss_interface.models.PD_Elements.Lines.LinesF import LinesF


class Lines(LinesV, LinesS, LinesI, LinesF):
    """
    This interface implements the Lines (ILines) interface of OpenDSS by declaring 4 procedures for accessing the
    different properties included in this interface: LinesV, LinesS, LinesI, LinesF.
    """
    pass
