import streamlit as st
from datetime import date

from domain.offer_details import OfferDetails


def render_offer_details_form(details: OfferDetails) -> None:
    st.subheader("Dane oferty")

    col1, col2 = st.columns(2)

    with col1:
        details.offer_number = st.text_input(
            "Numer oferty",
            value=details.offer_number,
        )

        details.issue_date = st.date_input(
            "Data wystawienia",
            value=details.issue_date,
        )

    with col2:
        details.salesperson = st.text_input(
            "Sprzedawca",
            value=details.salesperson,
        )

        details.valid_until = st.date_input(
            "Oferta ważna do",
            value=details.valid_until,
            min_value=date.today(),
        )

        details.notes = st.text_area(
            "Uwagi",
            value=details.notes,
            height=100,
        )