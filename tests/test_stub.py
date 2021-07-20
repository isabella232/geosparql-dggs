"""
This Python 3.3 code tests the ``processing.processing`` module.
Beware, these tests cover only some functions and only some scenarios.
Keep adding tests!
CHANGELOG:
- 2021-03-17:   David Habgood (DH): Initial version
"""
import unittest
from source import *
from source.dggs_classes import *


class CellValid(unittest.TestCase):

    def test_dggs_geom_format_invalid_1(self):
        with self.assertRaises(AssertionError):
            Cell('H123', kind='rHEALPix')

    def test_dggs_geom_format_invalid_2(self):
        with self.assertRaises(ValueError):
            Cell('HH', kind='rHEALPix')

    # def test_dggs_geom_compression_1(self):
    #     assert Cell(['P012', 'N013'], kind='rHEALPix').suid == ['N013', 'P012']

    def test_dggs_geom_single_cell(self):
        assert Cell('P012', kind='rHEALPix').suid == ('P', 0, 1, 2)


class CellNeighbour(unittest.TestCase):

    def test_neighbour_up(self):
        self.assertEqual(
            Cell('R41', kind='rHEALPix').neighbour('up').suid, ('R', 1, 7))

    def test_neighbour_down(self):
        self.assertEqual(
            Cell('R47', kind='rHEALPix').neighbour('down').suid, ('R', 7, 1))

    def test_neighbour_left(self):
        self.assertEqual(
            Cell('R43', kind='rHEALPix').neighbour('left').suid, ('R', 3, 5))

    def test_neighbour_right(self):
        self.assertEqual(
            Cell('R45', kind='rHEALPix').neighbour('right').suid, ('R', 5, 3))


class CellNeighbours(unittest.TestCase):

    def test_neighbours(self):
        self.assertEqual(
            Cell('R4', kind='rHEALPix').neighbours_suids(),
            {('R', 1), ('R', 3), ('R', 5), ('R', 7)}
            )


class CellCollections(unittest.TestCase):

    def test_collection(self):
        assert CellCollection([Cell('R4'), Cell('R1'), Cell('R5')])

    def test_deduplication(self):
        self.assertEqual((CellCollection([Cell('R4'), Cell('R1'), Cell('R5'), Cell('R5')]).cell_suids),
                         ['R1', 'R4', 'R5'])


class SFRelationships(unittest.TestCase):

    def test_sf_equals(self):
        self.assertTrue(sfEquals('P1', 'P1'))

    def test_sf_not_equals(self):
        self.assertFalse(sfEquals('P1', 'P2'))

    def test_sf_overlaps(self):
        self.assertTrue(sfOverlaps('P1', 'P1'))

    def test_sf_not_overlaps(self):
        self.assertFalse(sfOverlaps('P1', 'P2'))

    def test_sf_overlaps_different_res(self):
        self.assertTrue(sfOverlaps('P100', 'P1'))

    def test_sf_overlaps_list_str(self):
        self.assertTrue(sfOverlaps(['P1', 'P2'], 'P100'))

    def test_sf_not_overlaps_list_str(self):
        self.assertFalse(sfOverlaps(['P1', 'P2'], 'P3'))

    def test_sf_disjoint(self):
        self.assertFalse(sfDisjoint('P1', 'P1'))

    def test_sf_not_disjoint(self):
        self.assertTrue(sfDisjoint('P1', 'P2'))

    def test_sf_disjoint_different_res(self):
        self.assertFalse(sfDisjoint('P100', 'P1'))

    def test_sf_disjoint_list_str(self):
        self.assertFalse(sfDisjoint(['P1', 'P2'], 'P100'))

    def test_sf_disjoint_list_str(self):
        self.assertTrue(sfDisjoint(['P1', 'P2'], 'P3'))

if __name__ == "__main__":
    unittest.main()
