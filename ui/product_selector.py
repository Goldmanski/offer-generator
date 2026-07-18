from collections import defaultdict

import streamlit as st

from domain.product import Product
from domain.quote import Quote
from domain.quote_item import QuoteItem
from utils.formatters import format_currency


def render_product_selector(
    products: list[Product],
    quote: Quote,
) -> None:

    st.subheader("Produkty")

    grouped_products = defaultdict(list)

    for product in products:
        grouped_products[product.category.name].append(product)

    for category_name, category_products in grouped_products.items():

        with st.expander(
            f"{category_name} ({len(category_products)})",
            expanded=category_name == "Drzwi",
        ):

            selected_product = st.selectbox(
                "Wybierz produkt",
                category_products,
                key=f"product_{category_name}",
                format_func=lambda product: (
                    f"{product.name} — {format_currency(product.price)}"
                )
            )  

            if st.button(
                "Dodaj",
                key=f"add_{category_name}",
            ):
                quote.add_item(
                    QuoteItem(
                        product=selected_product,
                        quantity=1,
                    )
                )
                st.rerun()