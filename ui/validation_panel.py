import streamlit as st

from domain.quote import Quote


def render_validation_panel(quote: Quote) -> None:
    errors = quote.validation_errors()

    if not errors:
        st.success("✅ Oferta jest kompletna i gotowa do wygenerowania PDF.")
        return

    st.warning("Przed wygenerowaniem oferty uzupełnij:")

    for error in errors:
        st.write(f"• {error}")