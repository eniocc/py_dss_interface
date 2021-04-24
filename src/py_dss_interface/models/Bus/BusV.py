# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes
from comtypes import automation
from py_dss_interface.models.Base import Base


class BusV(Base):
    def bus_variant(self, first):
        variant_pointer = ctypes.pointer(automation.VARIANT())
        self.dss_obj.BUSV(ctypes.c_int32(first), variant_pointer)
        return variant_pointer.contents.value

    def bus_voltages(self):
        """Returns a complex array of voltages at this bus."""
        return self.bus_variant(0)

    # TODO: Checar duplicidade com o método desta classe nomeado sequence_voltages
    def bus_seqvoltages(self):
        """Returns a complex array of Sequence voltages at this bus."""
        return self.bus_variant(1)

    def bus_nodes(self):
        """Returns an integer array of node numbers defined at the bus in same order as the voltages."""
        return self.bus_variant(2)

    def bus_voc(self):
        """Returns the open circuit voltage as complex array."""
        return self.bus_variant(3)

    def bus_isc(self):
        """Returns the short circuit current as complex array."""
        return self.bus_variant(4)

    def bus_pu_voltages(self):
        """Returns the voltages in per unit at bus as complex array."""
        return self.bus_variant(5)

    def bus_zsc_matrix(self):
        """Returns the complex array of Zsc matrix at bus, column by column."""
        return self.bus_variant(6)

    def bus_zsc1(self):
        """Returns the complex array of Zsc matrix at bus, column by column."""
        return self.bus_variant(7)

    def bus_zsc0(self):
        """Returns the complex zero-sequence short circuit impedance at bus."""
        return self.bus_variant(8)

    def bus_ysc_matrix(self):
        """Returns the complex array of Ysc matrix at bus, column by column."""
        return self.bus_variant(9)

    def bus_sequence_voltages(self):
        """Returns the complex double array of sequence voltages (0, 1, 2) at this bus."""
        return self.bus_variant(10)

    def bus_vll(self):
        """For 2 and 3 phase buses, returns a variant array of complex numbers representing L-L voltages in volts.
        Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3."""
        return self.bus_variant(11)

    def bus_pu_vll(self):
        """Returns a variant array of complex numbers representing L-L voltages in per unit. Returns -1.0 for 1-phase bus.
        If more than 3 phases, returns only first 3.."""
        return self.bus_variant(12)

    def bus_vmag_angle(self):
        """Returns a variant array of doubles containing voltages in magnitude (VLN), angle (deg)."""
        return self.bus_variant(13)

    def bus_pu_vmag_angle(self):
        """Returns a variant array of doubles containing voltages in per unit and angles in degrees."""
        return self.bus_variant(14)
