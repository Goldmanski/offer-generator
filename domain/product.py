from dataclasses import dataclass
from decimal import Decimal
from .category import Category


@dataclass
class Product:
    id: int
    name: str
    manufacturer: str
    category: Category
    price: Decimal

