from typing import Dict, Type
from abc import ABC, abstractmethod
import csv
import json

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)
            product_list = list()
            for product in data:
                itens = Product(
                    product["id"], product["product_name"],
                    product["company_name"], product["manufacturing_date"],
                    product["expiration_date"], product["serial_number"],
                    product["storage_instructions"],)
                product_list.append(itens)
            return product_list


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
