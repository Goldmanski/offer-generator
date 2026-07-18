import streamlit as st

from domain.customer import Customer


def render_customer_form(customer: Customer) -> None:
    st.subheader("Dane klienta")

    customer.company_name = st.text_input(
        "Nazwa firmy",
        value=customer.company_name,
    )

    customer.nip = st.text_input(
        "NIP",
        value=customer.nip,
    )

    customer.address = st.text_area(
        "Adres",
        value=customer.address,
        height=80,
    )

    customer.contact_person = st.text_input(
        "Osoba kontaktowa",
        value=customer.contact_person,
    )

    customer.email = st.text_input(
        "Email",
        value=customer.email,
    )

    customer.phone = st.text_input(
        "Telefon",
        value=customer.phone,
    )