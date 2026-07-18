import streamlit as st

from application.product_service import ProductService
from application.quote_service import QuoteService
from ui.offer_table import render_offer_table
from ui.customer_form import render_customer_form
from ui.product_selector import render_product_selector
from ui.offer_details_form import render_offer_details_form
from ui.validation_panel import render_validation_panel
from application.pdf_service import PdfService
from utils.formatters import format_currency

st.title("Generator ofert PDF")

if "offer_confirmed" not in st.session_state:
    st.session_state.offer_confirmed = False

product_service = ProductService()
products = product_service.load_products()


quote_service = QuoteService()

if "quote" not in st.session_state:
    st.session_state.quote = quote_service.create_quote()

with st.form("offer_data_form"):

    render_offer_details_form(
        st.session_state.quote.details
    )

    st.divider()

    render_customer_form(
        st.session_state.quote.customer
    )

    submitted = st.form_submit_button(
        "✅ Zatwierdź dane"
    )

    if submitted:
        st.session_state.offer_confirmed = True
        st.success("Dane zostały zapisane.")

st.divider()

render_product_selector(
    products,
    st.session_state.quote,
)

st.subheader("Oferta")

render_offer_table(st.session_state.quote)

st.subheader("Podsumowanie")

st.write(
    f"Łączna wartość oferty: {format_currency(st.session_state.quote.total_price())}"
)

st.divider()

render_validation_panel(
    st.session_state.quote
)

pdf_service = PdfService()

if (
    st.session_state.offer_confirmed
    and st.session_state.quote.can_generate_pdf()
):
    pdf_bytes = pdf_service.generate(
        st.session_state.quote
    )

    st.download_button(
        label="📄 Pobierz PDF",
        data=pdf_bytes,
        file_name=f"{st.session_state.quote.details.offer_number}.pdf",
        mime="application/pdf",
    )
    
