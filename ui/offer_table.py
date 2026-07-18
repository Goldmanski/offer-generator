import streamlit as st

from domain.quote import Quote


def render_offer_table(quote: Quote) -> None:
    offer_data = []

    for item in quote.items:
        offer_data.append(
            {
                "ID": item.product.id,
                "Produkt": item.product.name,
                "Ilość": item.quantity,
                "Cena": float(item.product.price),
                "Wartość": float(item.total_price()),
                "Usuń": False,
            }
        )

    if not offer_data:
        st.info("🛒 Oferta jest pusta. Dodaj pierwszy produkt.")
        return

    edited_offer = st.data_editor(
        offer_data,
        hide_index=True,
        disabled=["ID", "Produkt", "Cena", "Wartość"],
        column_config={
            "ID": None,
            "Cena": st.column_config.NumberColumn(
                "Cena",
                format="%.2f zł",
                width="small",
            ),
            "Wartość": st.column_config.NumberColumn(
                "Wartość",
                format="%.2f zł",
                width="small",
            ),
            "Usuń": st.column_config.CheckboxColumn(
                "Usuń",
            ),
        },
        use_container_width=True,
    )

    for row, item in zip(edited_offer, quote.items.copy()):
        if row["Usuń"]:
            quote.remove_item(item.product.id)
            st.rerun()

        if row["Ilość"] != item.quantity:
            quote.set_quantity(
                item.product.id,
                int(row["Ilość"]),
            )
            st.rerun()