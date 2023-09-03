from inventory_report.product import Product


def test_create_product() -> None:

    id = "1"
    product_name = "Test"
    manufacturing_date = "01-01-2021"
    company_name = "Test"
    expiration_date = "01-01-2022"
    storage_instructions = "Test o test"
    serial_number = "TEIT 1234 5678 9012 3456 7890 1234"

    product = {
        "id": id,
        "product_name": product_name,
        "manufacturing_date": manufacturing_date,
        "company_name": company_name,
        "expiration_date": expiration_date,
        "storage_instructions": storage_instructions,
        "serial_number": serial_number,
    }
    prod = Product(**product)
    print(prod)
    assert prod.id == id
    assert prod.company_name == company_name
    assert prod.product_name == product_name
    assert prod.manufacturing_date == manufacturing_date
    assert prod.expiration_date == expiration_date
    assert prod.serial_number == serial_number
    assert prod.storage_instructions == storage_instructions


test_create_product()
