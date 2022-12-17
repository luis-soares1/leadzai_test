from pagination import Pagination
import unittest


class TestPagination(unittest.TestCase):

    def test_current_page_bigger_than_total_pages(self):
        p = Pagination(current_page=10, total_pages=2, boundaries=3, around=4)
        with self.assertRaises(Exception):
            p.execute()

    def test_property_not_integer(self):
        p = Pagination(current_page="1", total_pages=2, boundaries=3, around=4)
        with self.assertRaises(Exception):
            p.execute()

    def test_big_around_lower_limit(self):
        p = Pagination(current_page=5, total_pages=11, boundaries=0, around=6)
        with self.assertRaises(Exception):
            p.execute()

    def test_big_around_upper_limit(self):
        p = Pagination(current_page=10, total_pages=14, boundaries=0, around=5)
        with self.assertRaises(Exception):
            p.execute()

    def test_total_pages_zero(self):
        p = Pagination(current_page=5, total_pages=0, boundaries=1, around=1)
        with self.assertRaises(Exception):
            p.execute()

    def test_big_boundaries(self):
        p = Pagination(current_page=1, total_pages=11, boundaries=6, around=0)
        with self.assertRaises(Exception):
            p.execute()
    
    def test_negative_current_page(self):
        p1 = Pagination(current_page=-1, total_pages=5, boundaries=0, around=0)
        with self.assertRaises(Exception):
            p1.execute()
    
    def test_negative_total_pages(self):
        p2 = Pagination(current_page=1, total_pages=-1, boundaries=0, around=0)
        with self.assertRaises(Exception):
            p2.execute()

    def test_negative_boundaries(self):
        p3 = Pagination(current_page=1, total_pages=5, boundaries=-1, around=0)
        with self.assertRaises(Exception):
            p3.execute()

    def test_negative_around(self):
        p4 = Pagination(current_page=1, total_pages=5, boundaries=6, around=-1)
        with self.assertRaises(Exception):
            p4.execute()

    def test_double_three_dots(self):
        p1 = Pagination(10, 50, 2, 2)
        p1.execute()
        self.assertEqual(p1.page_container, [1, 2, 8, 9, 10, 11, 12, 49, 50])

    def test_big_numbers(self):
        p1 = Pagination(15000, 30000, 3, 6)
        p1.execute()
        self.assertEqual(p1.page_container, [1, 2, 3, 14994, 14995, 14996,
                                             14997, 14998, 14999, 15000, 15001,
                                             15002, 15003, 15004, 15005, 15006,
                                             29998, 29999, 30000])
    
    def test_current_number_last_position(self):
        p1 = Pagination(10, 10, 3, 0)
        self.assertEqual(p1.page_container, [1, 2, 3, 8, 9, 10])
    
    def test_current_number_last_position_with_around_non_zero(self):
        p1 = Pagination(10, 10, 3, 1)
        with self.assertRaises(Exception):
            p1.execute()

    def test_current_number_first_position_with_around_non_zero(self):
        p1 = Pagination(1, 10, 3, 1)
        with self.assertRaises(Exception):
            p1.execute()
    




if __name__ == "__main__":
    unittest.main()