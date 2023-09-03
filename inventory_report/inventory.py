from typing import Optional

from inventory_report.product import Product


class Inventory:

    def __init__(self, data: Optional[list[Product]] = None):
        self._data = data or list()

    @property
    def data(self) -> list[Product]:
        return self._data

    def add_data(self, data: list[Product]):
        self._data.extend(data)
