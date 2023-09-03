from inventory_report.product import Product


def test_product_report() -> None:
    product_list = Product(
        id="farinha",
        product_name="Farinha de Trigo",
        manufacturing_date="01-05-2021",
        company_name="Farinini",
        serial_number="TY68 409C JJ43 ASD1 PL2F",
        expiration_date="02-06-2023",
        storage_instructions="armazenar em local protegido da luz.",
    )

    report_inv = str(product_list)

    assert "The product farinha - Farinha de Trigo" in report_inv
    assert "with serial number TY68 409C JJ43 ASD1 PL2F" in report_inv
    assert "manufactured on 01-05-2021" in report_inv
    assert "by the company Farinini" in report_inv
    assert "valid until 02-06-2023" in report_inv
    assert (
        "must be stored according to the following instructions: "
        "armazenar em local protegido da luz." in report_inv
    )
