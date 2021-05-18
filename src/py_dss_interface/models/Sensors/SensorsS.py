# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class SensorsS(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows: CStr SensorsS(int32_t Parameter, CStr Argument); This interface
    returns a string with the result of the query according to the value of the variable Parameter, which can be one
    of the following.
    """

    def sensors_read_name(self):
        """Gets the name of the active sensor object."""
        result = ctypes.c_char_p(self.dss_obj.SensorsS(ctypes.c_int32(0), ctypes.c_int32(0)))
        return result.value.decode('ascii')

    def sensors_write_name(self, argument):
        """Sets the name of the active sensor object."""
        argument = Base.check_string_param(argument)
        result = ctypes.c_char_p(self.dss_obj.SensorsS(ctypes.c_int32(1), argument.encode('ascii')))
        return result.value.decode('ascii')

    def sensors_read_meteredelement(self):
        """Gets the full name of the measured element."""
        result = ctypes.c_char_p(self.dss_obj.SensorsS(ctypes.c_int32(2), ctypes.c_int32(0)))
        return result.value.decode('ascii')

    def sensors_write_meteredelement(self, argument):
        """Sets the full name of the measured element."""
        argument = Base.check_string_param(argument)
        result = ctypes.c_char_p(self.dss_obj.SensorsS(ctypes.c_int32(3), argument.encode('ascii')))
        return result.value.decode('ascii')
