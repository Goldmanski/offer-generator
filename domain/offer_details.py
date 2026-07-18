from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class OfferDetails:
    offer_number: str = ""
    issue_date: date = field(default_factory=date.today)
    valid_until: date = field(
        default_factory=lambda: date.today() + timedelta(days=30)
    )
    salesperson: str = ""
    notes: str = ""