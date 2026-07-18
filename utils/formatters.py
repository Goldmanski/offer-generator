from decimal import Decimal


def format_currency(value) -> str:
    value = Decimal(value)

    formatted = f"{value:,.2f}"
    formatted = formatted.replace(",", "X")
    formatted = formatted.replace(".", ",")
    formatted = formatted.replace("X", " ")

    return f"{formatted} zł"