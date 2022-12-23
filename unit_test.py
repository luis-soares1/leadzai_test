from pagination import Pagination
import unittest

class TestPagination(unittest.TestCase):

    def test_current_page_bigger_than_total_pages(self):
        p = Pagination(current_page=10, total_pages=2, boundaries=3, around=4)
        with self.assertRaises(Exception) as e:
            p.execute()
            self.assertRaises("Current page is bigger than the total number of pages", str(e.exception))

    def test_two_dots_first(self):
        p = Pagination(current_page=5, total_pages=7, boundaries=0, around=2)
        p.execute()
        self.assertEqual(p.page_container, ['...', 3, 4, 5, 6, 7])

    def test_two_dots_first_and_end(self):
        p = Pagination(current_page=5, total_pages=10, boundaries=0, around=2)
        p.execute()
        self.assertEqual(p.page_container, ['...', 3, 4, 5, 6, 7, '...'])

    def test_two_dots_end(self):
        p = Pagination(current_page=3, total_pages=10, boundaries=0, around=2)
        p.execute()
        self.assertEqual(p.page_container, [1, 2, 3, 4, 5, '...'])

    def test_1_element_dots_first(self):
        p = Pagination(current_page=13, total_pages=13, boundaries=0, around=0)
        p.execute()
        self.assertEqual(p.page_container, ['...', 13])

    def test_1_element_dots_last(self):
        p = Pagination(current_page=1, total_pages=13, boundaries=0, around=0)
        p.execute()
        self.assertEqual(p.page_container, [1, '...'])

    def test_property_not_integer(self):
        p = Pagination(current_page="1", total_pages=2, boundaries=3, around=4)
        with self.assertRaises(Exception) as e:
            p.execute()
            self.assertRaises("Not an integer", str(e.exception))

    def test_big_around_lower_limit(self):
        p = Pagination(current_page=5, total_pages=11, boundaries=0, around=6)
        p.execute()
        self.assertEqual(p.page_container, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_big_around_upper_limit(self):
        p = Pagination(current_page=10, total_pages=14, boundaries=0, around=5)
        p.execute()
        self.assertEqual(p.page_container, ['...', 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_total_pages_zero(self):
        p = Pagination(current_page=5, total_pages=0, boundaries=1, around=1)
        with self.assertRaises(Exception) as e:
            p.execute()
            self.assertRaises("Properties have values below 0 or total pages are 0", str(e.exception))

    def test_big_boundaries(self):
        p = Pagination(current_page=1, total_pages=11, boundaries=10000, around=0)
        p.execute()
        self.assertEqual(p.page_container, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_negative_current_page(self):
        p1 = Pagination(current_page=-1, total_pages=5, boundaries=0, around=0)
        with self.assertRaises(Exception) as e:
            p1.execute()
            self.assertRaises("Properties have values below 0 or total pages are 0", str(e.exception))

    def test_negative_total_pages(self):
        p2 = Pagination(current_page=1, total_pages=-1, boundaries=0, around=0)
        with self.assertRaises(Exception) as e:
            p2.execute()
            self.assertRaises("Properties have values below 0 or total pages are 0", str(e.exception))

    def test_negative_boundaries(self):
        p3 = Pagination(current_page=1, total_pages=5, boundaries=-1, around=0)
        with self.assertRaises(Exception) as e:
            p3.execute()
            self.assertRaises("Properties have values below 0 or total pages are 0", str(e.exception))

    def test_negative_around(self):
        p4 = Pagination(current_page=1, total_pages=5, boundaries=6, around=-1)
        with self.assertRaises(Exception) as e:
            p4.execute()
            self.assertRaises("Properties have values below 0 or total pages are 0", str(e.exception))

    def test_big_numbers(self):
        p1 = Pagination(15000, 30000, 3, 6)
        p1.execute()
        self.assertEqual(p1.page_container, [1, 2, 3, "...", 14994, 14995, 14996,
                                             14997, 14998, 14999, 15000, 15001,
                                             15002, 15003, 15004, 15005, 15006, "...",
                                             29998, 29999, 30000])

    def test_current_number_last_position(self):
        p1 = Pagination(10, 10, 3, 0)
        p1.execute()
        self.assertEqual(p1.page_container, [1, 2, 3, "...", 8, 9, 10])

    def test_current_number_first_position(self):
        p1 = Pagination(10, 10, 3, 0)
        p1.execute()
        self.assertEqual(p1.page_container, [1, 2, 3, "...", 8, 9, 10])


if __name__ == "__main__":
    unittest.main()