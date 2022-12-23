
class Pagination:
    def __init__(self, current_page: int, total_pages: int, boundaries: int,
                 around: int):

        self.current_page: int = current_page
        self.total_pages: int = total_pages
        self.boundaries: int = boundaries
        self.around: int = around
        self.page_container: set = set()

    def __str__(self) -> str:
        return " ".join([str(page) for page in self.page_container])

    # Adds elements from start_idx to end_idx to the page container set
    def _add_elements(self, start_idx: int, end_idx: int):
        if end_idx > self.total_pages:
            end_idx = self.total_pages
        elif start_idx < 1:
            start_idx = 1

        for page in range(start_idx, end_idx + 1):
            self.page_container.add(page)

    # Add the boundary elements
    def exec_boundaries(self, start: bool = True):
        if start:
            self._add_elements(1, self.boundaries)
            return
        self._add_elements(self.total_pages-self.boundaries+1, self.total_pages)

    # Add the around elements
    def exec_around(self, backwards: bool = True):
        if backwards:
            self._add_elements(self.current_page-self.around, self.current_page)
            return
        self._add_elements(self.current_page+1, self.current_page + self.around)

    def _get_two_dots_idxs(self):
        self.page_container.add(self.current_page)
        self.page_container = sorted(self.page_container)
        two_dots_idxs = []

        for idx, n in enumerate(self.page_container):
            # check for middle, beginning and end three dots
            if idx == 0 and n != 1:
                two_dots_idxs.append(idx)
            if (idx == len(self.page_container) - 1) and n != self.total_pages:
                two_dots_idxs.append(idx+1)
            elif self.page_container[idx] - self.page_container[idx-1] > 1:
                two_dots_idxs.append(idx)
        return reversed(two_dots_idxs)

    # inserts the "..." in their place and prints the pagination
    def insert_three_dots(self):
        for idx in self._get_two_dots_idxs():
            self.page_container.insert(idx, "...")

    # Throws an exception for invalid inputs
    def validation(self):
        if not all([
            isinstance(self.current_page, int), isinstance(self.around, int),
            isinstance(self.boundaries, int), isinstance(self.total_pages, int)]):
            raise Exception("Not an integer")
        elif not all([self.current_page > 0, self.around >= 0, self.boundaries >= 0, self.total_pages > 0]):
            raise Exception("Properties have values below 0 or total pages are 0")
        elif self.current_page > self.total_pages:
            raise Exception("Current page is bigger than the total number of pages")

    def execute(self):
        self.validation()
        self.exec_boundaries()
        self.exec_boundaries(False)
        self.exec_around()
        self.exec_around(False)
        self.insert_three_dots()


if __name__ == "__main__":
    p = Pagination(3, 10, 0, 0)
    p.execute()
    print(p)
