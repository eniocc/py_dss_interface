# -*- coding: utf-8 -*-
# @Time    : 8/17/2021 10:15 AM
# @Author  : Rodolfo Londero
# @Email   : rodolfpl@gmail.com
# @File    : test_linecodes.py
# @Software: PyCharm

import pytest


class TestLineCodes13Bus:

    @pytest.fixture(scope='function')
    def dss(self, solve_snap_13bus):
        dss = solve_snap_13bus
        dss.name_write('1')

        return dss

    # ===================================================================
    # Integer methods
    # ===================================================================
    def test_linecodes_count(self, dss):
        expected = 36
        actual = dss.count()
        assert actual == expected

    def test_linecodes_first(self, dss):
        expected = 1
        actual = dss.first()
        assert actual == expected

    def test_linecodes_next(self, dss):
        expected = 2
        actual = dss.next()
        assert actual == expected

    def test_linecodes_read_units(self, dss):
        expected = 0
        actual = dss.units_read()
        assert actual == expected

    def test_linecodes_write_units(self, dss):
        expected = 5
        dss.units_write(expected)
        actual = dss.units_read()
        assert actual == expected

    def test_linecodes_read_phases(self, dss):
        expected = 3
        actual = dss.phases_read()
        assert actual == expected

    def test_linecodes_write_phases(self, dss):
        expected = 2
        dss.phases_write(expected)
        actual = dss.phases_read()
        assert actual == expected

    def test_linecodes_is_z1z0(self, dss):
        expected = 0
        actual = dss.is_z1z0()
        assert actual == expected

    # ===================================================================
    # String methods
    # ===================================================================
    def test_linecodes_read_name(self, dss):
        expected = '1'
        actual = dss.name_read()
        assert actual == expected

    def test_linecodes_write_name(self, dss):
        expected = '2'
        dss.name_write(expected)
        actual = dss.name_read()
        assert actual == expected

    # ===================================================================
    # Float methods
    # ===================================================================
    def test_linecodes_read_r1(self, dss):
        expected = 0.058
        actual = dss.r1_read()
        assert actual == expected

    def test_linecodes_write_r1(self, dss):
        expected = 0.1
        dss.r1_write(expected)
        actual = dss.r1_read()
        assert actual == expected

    def test_linecodes_read_x1(self, dss):
        expected = 0.1206
        actual = dss.x1_read()
        assert actual == expected

    def test_linecodes_write_x1(self, dss):
        expected = 0.1
        dss.x1_write(expected)
        actual = dss.x1_read()
        assert actual == expected

    def test_linecodes_read_c1(self, dss):
        expected = 3.4
        actual = dss.c1_read()
        assert actual == expected

    def test_linecodes_write_c1(self, dss):
        expected = 1.0
        dss.c1_write(expected)
        actual = dss.c1_read()
        assert actual == expected

    def test_linecodes_read_r0(self, dss):
        expected = 0.1784
        actual = dss.r0_read()
        assert actual == expected

    def test_linecodes_write_r0(self, dss):
        expected = 0.1
        dss.r0_write(expected)
        actual = dss.r0_read()
        assert actual == expected

    def test_linecodes_read_x0(self, dss):
        expected = 0.4047
        actual = dss.x0_read()
        assert actual == expected

    def test_linecodes_write_x0(self, dss):
        expected = 0.1
        dss.x0_write(expected)
        actual = dss.x0_read()
        assert actual == expected

    def test_linecodes_read_c0(self, dss):
        expected = 1.6
        actual = dss.c0_read()
        assert actual == expected

    def test_linecodes_write_c0(self, dss):
        expected = 2.0
        dss.c0_write(expected)
        actual = dss.c0_read()
        assert actual == expected

    def test_linecodes_read_norm_amps(self, dss):
        expected = 400
        actual = dss.norm_amps_read()
        assert actual == expected

    def test_linecodes_write_norm_amps(self, dss):
        expected = 300
        dss.norm_amps_write(expected)
        actual = dss.norm_amps_read()
        assert actual == expected

    def test_linecodes_read_emerg_amps(self, dss):
        expected = 600
        actual = dss.emerg_amps_read()
        assert actual == expected

    def test_linecodes_write_emerg_amps(self, dss):
        expected = 300
        dss.emerg_amps_write(expected)
        actual = dss.emerg_amps_read()
        assert actual == expected

    # ===================================================================
    # Variant methods
    # ===================================================================
    def test_linecodes_read_rmatrix(self, dss):
        expected = [0.086666667, 0.029545455, 0.02907197, 0.029545455, 0.088371212, 0.029924242, 0.02907197,
                    0.029924242, 0.08740530]
        expected = [truncate(x, 6) for x in expected]
        actual = dss.rmatrix_read()
        actual = [truncate(x, 6) for x in actual]
        assert actual == expected

    def test_linecodes_write_rmatrix(self, dss):
        expected_list = [0.791721, 0.31, 0.781649, 0.28345, 0.32, 0.791721]
        expected = format_matrix(expected_list)
        expected_str = format_matrix_str(expected)

        dss.rmatrix_write(expected_str)
        actual = dss.rmatrix_read()

        actual = [truncate(x, 6) for x in actual]
        expected = [truncate(x, 6) for x in expected]

        assert actual == expected

    def test_linecodes_read_xmatrix(self, dss):
        expected = [0.20416667, 0.09501894, 0.07289773, 0.09501894, 0.19852273, 0.08022727, 0.07289773, 0.08022727,
                    0.20172349]
        expected = [truncate(x, 6) for x in expected]

        actual = dss.xmatrix_read()
        actual = [truncate(x, 6) for x in actual]

        assert actual == expected

    def test_linecodes_write_xmatrix(self, dss):
        expected_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
        expected = format_matrix(expected_list)
        expected_str = format_matrix_str(expected)

        dss.xmatrix_write(expected_str)
        actual = dss.xmatrix_read()

        actual = [truncate(x, 9) for x in actual]
        expected = [truncate(x, 9) for x in expected]

        assert actual == expected

    def test_linecodes_read_cmatrix(self, dss):
        expected = [2.85171007, -0.92029379, -0.35075557, -0.92029379, 3.00463186, -0.58501125, -0.35075557,
                    -0.58501125, 2.71134756]

        actual = dss.cmatrix_read()
        actual = [truncate(x, 6) for x in actual]
        expected = [truncate(x, 6) for x in expected]

        assert actual == expected

    def test_linecodes_write_cmatrix(self, dss):
        expected_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
        expected = format_matrix(expected_list)
        expected_str = format_matrix_str(expected)
        dss.cmatrix_write(expected_str)
        actual = dss.cmatrix_read()

        actual = [truncate(x, 9) for x in actual]
        expected = [truncate(x, 9) for x in expected]

        assert actual == expected

    def test_linecodes_all_names(self, dss):
        expected = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '300', '301', '302', '303', '304',
                    '400', '601', '602', '603', '604', '605', '606', '607', '721', '722', '723', '724', 'mtx601',
                    'mtx602', 'mtx603', 'mtx604', 'mtx605', 'mtx606', 'mtx607']
        actual = dss.names()
        assert actual == expected


def truncate(num, n):
    # Return a truncated version of a floating point number
    temp = str(num)
    for x in range(len(temp)):
        if temp[x] == '.':
            try:
                return float(temp[:x + n + 1])
            except Exception as e:
                print(e)
                return float(temp)
    return float(temp)


def format_matrix(expected_list):
    # Return a full matrix from expected list from lower triangle
    matrix = []
    for i in range(3):
        if i == 0:
            matrix.extend((expected_list[0], expected_list[1], expected_list[3]))
        elif i == 1:
            matrix.extend((expected_list[1], expected_list[2], expected_list[4]))
        else:
            matrix.extend((expected_list[3], expected_list[4], expected_list[5]))
    return matrix


def format_matrix_str(expected_list):
    # Return the matrix converted to string with delimiters used in OpenDSS
    matrix_str = '['
    for i, val in enumerate(expected_list):
        matrix_str += f"{str(val)} "
        if i in [2, 5]:
            matrix_str += ' | '
    return f'{matrix_str[:-1]}]'
