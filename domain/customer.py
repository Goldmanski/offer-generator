from dataclasses import dataclass


@dataclass
class Customer:
    company_name: str = ""
    nip: str = ""
    address: str = ""
    contact_person: str = ""
    email: str = ""
    phone: str = ""