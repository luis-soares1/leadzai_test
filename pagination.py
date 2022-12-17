from math import floor

# SUMMARY

# The numbers that are to be printed in the end, will be added to the set.
# I choose the set because the boundaries and around will sometimes overlap,
# which using a list would mean I would had repeated page values.

class Pagination:
    def __init__(self, current_page: int, total_pages: int, boundaries: int,
                 around: int):

        self.current_page: int = current_page
        self.total_pages: int = total_pages
        self.boundaries: int = boundaries
        self.around: int = around
        self.page_container: set = set()

    def _add_elements(self, start_idx: int, end_idx: int):
        for page in range(start_idx, end_idx + 1):
            self.page_container.add(page)

    def exec_boundaries(self, start: bool = True):
        if start:
            self._add_elements(1, self.boundaries)
            return
        self._add_elements(self.total_pages-self.boundaries+1, self.total_pages)

    def exec_around(self, backwards: bool = True):
        if backwards:
            self._add_elements(self.current_page-self.around, self.current_page)
            return
        self._add_elements(self.current_page+1, self.current_page + self.around)

    def print_pagination(self):
        self.page_container.add(self.current_page)
        self.page_container = sorted(self.page_container)
        for idx, n in enumerate(self.page_container):
            if idx == 0:
                print(n, end=" ")
                continue
            elif self.page_container[idx] - self.page_container[idx-1] > 1:
                print("...", end=" ")
            print(n, end=" ")

    def validation(self):
        if not all([
            isinstance(self.current_page, int), isinstance(self.around, int),
            isinstance(self.boundaries, int), isinstance(self.total_pages, int)]):
            raise Exception("Not an integer")

        elif not all([self.current_page > 0, self.around >= 0, self.boundaries >= 0, self.total_pages > 0]):
            raise Exception("Properties have values below 0 or total pages are 0")

        elif self.current_page > self.total_pages:
            raise Exception("Current page is bigger than the total number of pages")

        elif self.boundaries > floor(self.total_pages/2):
            raise Exception(f"No space left for boundaries. Total pages: {self.total_pages}, Boundaries: {self.boundaries}")

        elif self.current_page-self.around < 1 or self.current_page + self.around > self.total_pages:
            raise Exception(f"Around value ({self.around}) goes below or upwards delimitations")


    def execute(self):
        self.validation()
        self.exec_boundaries()
        self.exec_boundaries(False)
        self.exec_around()
        self.exec_around(False)
        self.print_pagination()


if __name__ == "__main__":
    p = Pagination(current_page=1, total_pages=0, boundaries=2, around=2)
    p.execute()
