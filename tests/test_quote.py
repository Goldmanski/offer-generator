from domain.quote import Quote
from domain.quote_item import QuoteItem
from domain.product import Product
from domain.category import Category

from decimal import Decimal


def create_product():
    return Product(
        id=1,
        name="Drzwi wewnętrzne DRE Vetro E",
        manufacturer="DRE",
        category=Category(1, "Drzwi wewnętrzne"),
        price=Decimal("1899"),
    )


def test_empty_quote_is_invalid():
    quote = Quote(id=1)

    assert not quote.can_generate_pdf()


def test_quote_with_required_data_is_valid():
    quote = Quote(id=1)

    quote.customer.company_name = "OpenAI"

    quote.details.offer_number = "OF/001"

    quote.add_item(
        QuoteItem(
            product=create_product(),
            quantity=1,
        )
    )

    assert quote.can_generate_pdf()

def test_total_price_returns_sum_of_all_items():
    quote = Quote(id=1)

    product = create_product()

    quote.add_item(
        QuoteItem(product=product, quantity=2)
    )

    assert quote.total_price() == Decimal("3798")

def test_adding_same_product_increases_quantity():
    quote = Quote(id=1)

    product = create_product()

    quote.add_item(
        QuoteItem(product=product, quantity=1)
    )

    quote.add_item(
        QuoteItem(product=product, quantity=2)
    )

    assert len(quote.items) == 1
    assert quote.items[0].quantity == 3

def test_set_quantity_changes_item_quantity():
    quote = Quote(id=1)

    product = create_product()

    quote.add_item(
        QuoteItem(product=product, quantity=1)
    )

    quote.set_quantity(product.id, 5)

    assert quote.items[0].quantity == 5

def test_remove_item_removes_product():
    quote = Quote(id=1)

    product = create_product()

    quote.add_item(
        QuoteItem(product=product, quantity=1)
    )

    quote.remove_item(product.id)

    assert len(quote.items) == 0