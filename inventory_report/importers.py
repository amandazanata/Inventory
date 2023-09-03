from typing import Dict, Type
from abc import ABC, abstractmethod
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

            list_prod = list()
            for product in data:
                itens_prod = Product(
                    product["product_name"],
                    product["id"],
                    product["company_name"],
                    product["serial_number"],
                    product["expiration_date"],
                    product["manufacturing_date"],
                    product["storage_instructions"],)
                list_prod.append(itens_prod)
            return list_prod


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
