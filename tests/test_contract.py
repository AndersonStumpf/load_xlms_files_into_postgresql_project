import pytest
from datetime import datetime
from src.contract import Sales
from pydantic import ValidationError

# Testing if the examples match with contract defined
def test_valid_sales_data():

    valid_data = {
        "email": "test@examle.com",
        "data": datetime.now(),
        "valor": 100.5,
        "produto": "Produto X",
        "quantidade": 3,
        "categoria": "categoria1"
    }

    sale = Sales(**valid_data)

    assert sale.email == valid_data["email"]
    assert sale.data == valid_data["data"]
    assert sale.valor == valid_data["valor"]
    assert sale.produto == valid_data["produto"]
    assert sale.quantidade == valid_data["quantidade"]
    assert sale.categoria == valid_data["categoria"]


# Testing if the examples don't match with contract defined
def test_invalid_sales_data_test():
    invalid_data = {
        "email": "tester@example.com",
        "data": "data",
        "valor": -100,
        "produto": "",
        "quantidade": "",
        "categoria": "categoria"
    }

    with pytest.raises(ValidationError):
        Sales(**invalid_data)