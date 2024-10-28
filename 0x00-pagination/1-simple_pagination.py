#!/usr/bin/env python3
"""Simple pagination"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index."""
    start = (page - 1) * page_size
    return (start, start + page_size)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a specific page of the dataset
        based on pagination parameters.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows representing the page.
        """
        assert type(page) == int and type(page_size) == int, "Arguments must
        be integers"
        assert page > 0 and page_size > 0, "Arguments must be greater than 0"

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        # Return an empty list if start is out of range
        return dataset[start:end] if start < len(dataset) else []