from dataclasses import dataclass, field
from decimal import Decimal
from datetime import date

from .quote_item import QuoteItem
from domain.customer import Customer
from domain.offer_details import OfferDetails


@dataclass
class Quote:
    id: int
    customer: Customer = field(default_factory=Customer)
    details: OfferDetails = field(default_factory=OfferDetails)
    items: list[QuoteItem] = field(default_factory=list)

    def add_item(self, item: QuoteItem) -> None:
        for existing_item in self.items:
            if existing_item.product.id == item.product.id:
                existing_item.quantity += item.quantity
                return

        self.items.append(item)

    def remove_item(self, product_id: int) -> None:
        self.items = [
            item
            for item in self.items
            if item.product.id != product_id
        ]

    def total_price(self) -> Decimal:
        return sum((item.total_price() for item in self.items), Decimal("0"))

    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def change_quantity(self, product_id: int, delta: int) -> None:
        for item in self.items:
            if item.product.id == product_id:
                item.quantity += delta

                if item.quantity <= 0:
                    self.remove_item(product_id)

                return
            
    def set_quantity(self, product_id: int, quantity: int) -> None:
        for item in self.items:
            if item.product.id == product_id:

                if quantity <= 0:
                    self.remove_item(product_id)
                else:
                    item.quantity = quantity

                return
    
    def validation_errors(self) -> list[str]:
        errors = []

        if self.is_empty():
            errors.append("Oferta musi zawierać co najmniej jeden produkt.")

        if not self.customer.company_name.strip():
            errors.append("Nazwa klienta jest wymagana.")

        if not self.details.offer_number.strip():
            errors.append("Numer oferty jest wymagany.")

        if self.details.valid_until < date.today():
            errors.append("Data ważności oferty nie może być wcześniejsza niż dzisiaj.")

        return errors
    
    def can_generate_pdf(self) -> bool:
        return len(self.validation_errors()) == 0