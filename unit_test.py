from pagination import Pagination
import unittest


class TestPagination(unittest.TestCase):

    def test_current_page_bigger_than_total_pages(self):
        p = Pagination(current_page=10, total_pages=2, boundaries=3, around=4)
        with self.assertRaises(Exception) as e:
            p.execute()
        self.assertEqual(str(e.exception),
                         "Current page is bigger than the total number of pages")

    def test_property_not_integer(self):
        p = Pagination(current_page="1", total_pages=2, boundaries=3, around=4)
        with self.assertRaises(Exception) as e:
            p.execute()
        self.assertEqual("Not an integer", str(e.exception))

    def test_total_pages_zero(self):
        p = Pagination(current_page=5, total_pages=0, boundaries=1, around=1)
        with self.assertRaises(Exception) as e:
            p.execute()
        self.assertEqual(
            "Properties have values below 0 or total pages are 0", str(
                e.exception))

    def test_negative_current_page(self):
        p1 = Pagination(current_page=-1, total_pages=5, boundaries=0, around=0)
        with self.assertRaises(Exception) as e:
            p1.execute()
        self.assertEqual(
            "Properties have values below 0 or total pages are 0", str(
                e.exception))

    def test_current_page_zero(self):
        p1 = Pagination(current_page=0, total_pages=5, boundaries=0, around=0)
        with self.assertRaises(Exception) as e:
            p1.execute()
        self.assertEqual(str(e.exception),
                         "Properties have values below 0 or total pages are 0")

    def test_negative_total_pages(self):
        p2 = Pagination(current_page=1, total_pages=-1, boundaries=0, around=0)
        with self.assertRaises(Exception) as e:
            p2.execute()
        self.assertEqual(
            "Properties have values below 0 or total pages are 0", str(
                e.exception))

    def test_negative_boundaries(self):
        p3 = Pagination(current_page=1, total_pages=5, boundaries=-1, around=0)
        with self.assertRaises(Exception) as e:
            p3.execute()
        self.assertEqual(
            "Properties have values below 0 or total pages are 0", str(
                e.exception))

    def test_negative_around(self):
        p4 = Pagination(current_page=1, total_pages=5, boundaries=6, around=-1)
        with self.assertRaises(Exception) as e:
            p4.execute()
        self.assertEqual(
            "Properties have values below 0 or total pages are 0", str(
                e.exception))

    def test_two_dots_first(self):
        self.assertEqual(
            Pagination(current_page=5, total_pages=7, boundaries=0, around=2).execute().page_container, [
                '...', 3, 4, 5, 6, 7])
        self.assertEqual(
            Pagination(100, 100, 0, 1).execute().page_container, [
                '...', 99, 100])

    def test_two_dots_first_and_end(self):
        self.assertEqual(
            Pagination(current_page=5, total_pages=10, boundaries=0, around=2).execute().page_container, [
                '...', 3, 4, 5, 6, 7, '...'])

    def test_two_dots_end(self):
        self.assertEqual(
            Pagination(
                current_page=3, total_pages=10, boundaries=0, around=2).execute().page_container, [
                1, 2, 3, 4, 5, '...'])
        self.assertEqual(
            Pagination(1, 1000, 0, 2).execute().page_container, [
                1, 2, 3, '...'])

    def test_three_dots_middle(self):
        self.assertEqual(
            Pagination(1, 1000, 3, 1).execute().page_container, [
                1, 2, 3, '...', 998, 999, 1000])
        self.assertEqual(
            Pagination(1000, 1000, 3, 1).execute().page_container, [
                1, 2, 3, '...', 998, 999, 1000])
        self.assertEqual(
            Pagination(100, 100, 1, 0).execute().page_container, [
                1, '...', 100])
        self.assertEqual(Pagination(100, 100, 5, 4).execute().page_container, [
                         1, 2, 3, 4, 5, '...', 96, 97, 98, 99, 100])

    def test_1_element_dots_first(self):
        self.assertEqual(
            Pagination(current_page=13, total_pages=13, boundaries=0, around=0).execute().page_container, [
                '...', 13])
        self.assertEqual(
            Pagination(100, 100, 0, 0).execute().page_container, [
                '...', 100])

    def test_1_element_dots_last(self):
        self.assertEqual(
            Pagination(current_page=1, total_pages=13, boundaries=0, around=0).execute().page_container, [
                1, '...'])

    def test_double_three_dots(self):
        self.assertEqual(
            Pagination(50, 100, 1, 0).execute().page_container, [
                1, '...', 50, '...', 100])
        self.assertEqual(Pagination(500, 1000, 2, 3).execute().page_container, [
                         1, 2, '...', 497, 498, 499, 500, 501, 502, 503, '...', 999, 1000])
        self.assertEqual(Pagination(7, 15, 3, 1).execute().page_container, [
                         1, 2, 3, '...', 6, 7, 8, '...', 13, 14, 15])

    def test_1_element_double_three_dots(self):
        self.assertEqual(Pagination(current_page=3, total_pages=10, boundaries=0,
                                    around=0).execute().page_container, ["...", 3, '...'])

    def current_page_equals_total_pages(self):
        self.assertEqual(
            Pagination(
                current_page=5, total_pages=5, boundaries=3, around=3).execute().page_container, [
                '...', 13])

    def test_big_around_lower_limit(self):
        self.assertEqual(
            Pagination(current_page=5, total_pages=11, boundaries=0, around=6).execute().page_container, [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_big_around_upper_limit(self):
        self.assertEqual(
            Pagination(current_page=10, total_pages=14, boundaries=0, around=5).execute().page_container, [
                '...', 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_big_boundaries(self):
        self.assertEqual(
            Pagination(current_page=1, total_pages=11, boundaries=10000, around=0).execute().page_container, [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_big_numbers(self):
        self.assertEqual(Pagination(15000,
                                    30000,
                                    3,
                                    6).execute().page_container,
                         [1,
                          2,
                          3,
                          "...",
                          14994,
                          14995,
                          14996,
                          14997,
                          14998,
                          14999,
                          15000,
                          15001,
                          15002,
                          15003,
                          15004,
                          15005,
                          15006,
                          "...",
                          29998,
                          29999,
                          30000])

    def test_current_number_last_position(self):
        self.assertEqual(
            Pagination(10, 10, 3, 0).execute().page_container, [
                1, 2, 3, "...", 8, 9, 10])

    def test_current_number_first_position(self):
        self.assertEqual(
            Pagination(10, 10, 3, 0).execute().page_container, [
                1, 2, 3, "...", 8, 9, 10])

    def test_boundary_and_around_overlap(self):
        self.assertEqual(
            Pagination(5, 10, 4, 4).execute().page_container, [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def total_pages_smaller_than_boundaries(self):
        self.assertEqual(
            Pagination(current_page=5, total_pages=5, boundaries=6, around=2).execute().page_container, [
                1, 2, 3, 4, 5])

    def single_page_total_page(self):
        self.assertEqual(Pagination(1, 1, 0, 0).execute().page_container, [1])

    def test_general_inputs(self):
        self.assertEqual(
            Pagination(5, 10, 2, 3).execute().page_container, [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(
            Pagination(5, 10, 3, 4).execute().page_container, [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(
            Pagination(4, 10, 2, 2).execute().page_container, [
                1, 2, 3, 4, 5, 6, '...', 9, 10])
        self.assertEqual(Pagination(6, 15, 3, 3).execute().page_container, [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, '...', 13, 14, 15])
        self.assertEqual(Pagination(7, 15, 3, 1).execute().page_container, [
                         1, 2, 3, '...', 6, 7, 8, '...', 13, 14, 15])
        self.assertEqual(
            Pagination(4, 10, 9, 10).execute().page_container, [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(Pagination(10, 20, 5, 1).execute().page_container, [
                         1, 2, 3, 4, 5, '...', 9, 10, 11, '...', 16, 17, 18, 19, 20])
        self.assertEqual(Pagination(10, 20, 1, 4).execute().page_container, [
                         1, '...', 6, 7, 8, 9, 10, 11, 12, 13, 14, '...', 20])


if __name__ == "__main__":
    unittest.main()
