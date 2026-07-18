from dataclasses import dataclass
from decimal import Decimal
from .product import Product


@dataclass
class QuoteItem:
    product: Product
    quantity: int

    def total_price(self) -> Decimal:
        return self.product.price * self.quantity

    