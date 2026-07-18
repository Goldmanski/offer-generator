from decimal import Decimal

from domain.category import Category
from domain.product import Product


class ProductService:
    def load_products(self) -> list[Product]:
        doors = Category(
            id=1,
            name="Drzwi"
        )

        frames = Category(
            id=2,
            name="Ościeżnice"
        )

        handles = Category(
            id=3,
            name="Klamki"
        )

        return [
            # ===== Drzwi =====

            Product(
                id=1,
                name="DRE Soho",
                manufacturer="DRE",
                category=doors,
                price=Decimal("1899.00")
            ),
            Product(
                id=2,
                name="DRE Hampton",
                manufacturer="DRE",
                category=doors,
                price=Decimal("2499.00")
            ),
            Product(
                id=3,
                name="DRE Vetro D",
                manufacturer="DRE",
                category=doors,
                price=Decimal("1799.00")
            ),
            Product(
                id=4,
                name="DRE Nova",
                manufacturer="DRE",
                category=doors,
                price=Decimal("1599.00")
            ),
            Product(
                id=5,
                name="DRE Enter",
                manufacturer="DRE",
                category=doors,
                price=Decimal("2899.00")
            ),
            Product(
                id=6,
                name="DRE Binito",
                manufacturer="DRE",
                category=doors,
                price=Decimal("2199.00")
            ),
            Product(
                id=7,
                name="DRE Estra",
                manufacturer="DRE",
                category=doors,
                price=Decimal("2399.00")
            ),
            Product(
                id=8,
                name="DRE Vetro E",
                manufacturer="DRE",
                category=doors,
                price=Decimal("1999.00")
            ),
            Product(
                id=9,
                name="DRE Scala",
                manufacturer="DRE",
                category=doors,
                price=Decimal("2099.00")
            ),
            Product(
                id=10,
                name="DRE Auri",
                manufacturer="DRE",
                category=doors,
                price=Decimal("2599.00")
            ),

            # ===== Ościeżnice =====

            Product(
                id=11,
                name="Ościeżnica regulowana DRE",
                manufacturer="DRE",
                category=frames,
                price=Decimal("499.00")
            ),
            Product(
                id=12,
                name="Ościeżnica stała DRE",
                manufacturer="DRE",
                category=frames,
                price=Decimal("349.00")
            ),
            Product(
                id=13,
                name="Ościeżnica ukryta DRE Sara Pro",
                manufacturer="DRE",
                category=frames,
                price=Decimal("899.00")
            ),

            # ===== Klamki =====

            Product(
                id=14,
                name="Klamka TOM",
                manufacturer="DRE",
                category=handles,
                price=Decimal("119.00")
            ),
            Product(
                id=15,
                name="Klamka PORTO",
                manufacturer="DRE",
                category=handles,
                price=Decimal("99.00")
            ),
            Product(
                id=16,
                name="Klamka SOLLER",
                manufacturer="DRE",
                category=handles,
                price=Decimal("129.00")
            ),
            Product(
                id=17,
                name="Klamka TELESTA",
                manufacturer="DRE",
                category=handles,
                price=Decimal("149.00")
            ),
            Product(
                id=18,
                name="Klamka LIMA FIT",
                manufacturer="DRE",
                category=handles,
                price=Decimal("139.00")
            ),
        ]