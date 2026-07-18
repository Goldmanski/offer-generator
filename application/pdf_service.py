from io import BytesIO
from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image
from utils.formatters import format_currency
from xml.sax.saxutils import escape

from domain.quote import Quote


class PdfService:

    def generate(self, quote: Quote) -> bytes:

        project_root = Path(__file__).resolve().parent.parent

        fonts_dir = project_root / "data" / "fonts"
        images_dir = project_root / "data" / "images"

        pdfmetrics.registerFont(
            TTFont(
                "DejaVu",
                str(fonts_dir / "DejaVuSans.ttf"),
            )
        )

        pdfmetrics.registerFont(
            TTFont(
                "DejaVu-Bold",
                str(fonts_dir / "DejaVuSans-Bold.ttf"),
            )
        )

        buffer = BytesIO()

        document = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        styles["Title"].fontName = "DejaVu-Bold"
        styles["Heading2"].fontName = "DejaVu-Bold"
        styles["Normal"].fontName = "DejaVu"

        story = []

        logo = Image(
            str(images_dir / "logo-C8rls40z_0.png"),
            width=220,
            height=55,
        )

        logo.hAlign = "CENTER"

        story.append(logo)

        story.append(Spacer(1, 0.2 * cm))

        story.append(
            Paragraph(
                "<b>OFERTA</b>",
                styles["Title"],
            )
        )

        story.append(Spacer(1, 0.4 * cm))

        offer_info = Table(
            [
                ["Numer oferty:", quote.details.offer_number],
                ["Data wystawienia:", quote.details.issue_date.strftime("%d.%m.%Y")],
                ["Ważna do:", quote.details.valid_until.strftime("%d.%m.%Y")],
                ["Sprzedawca:", quote.details.salesperson],
            ],
            colWidths=[140, 320],
        )

        offer_info.hAlign = "LEFT"

        offer_info.setStyle(
            TableStyle(
                [
                    ("FONTNAME", (0, 0), (0, -1), "DejaVu-Bold"),
                    ("FONTNAME", (1, 0), (1, -1), "DejaVu"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]
            )
        )

        story.append(offer_info)

        story.append(Spacer(1, 0.8 * cm))

        story.append(
            Paragraph("<b>Dane klienta</b>", styles["Heading2"])
        )

        customer_info = Table(
            [
                ["Nazwa firmy:", quote.customer.company_name],
                ["NIP:", quote.customer.nip],
                ["Adres:", quote.customer.address],
                ["Osoba kontaktowa:", quote.customer.contact_person],
                ["Email:", quote.customer.email],
                ["Telefon:", quote.customer.phone],
            ],
            colWidths=[140, 320],
        )

        customer_info.hAlign = "LEFT"

        customer_info.setStyle(
            TableStyle(
                [
                    ("FONTNAME", (0, 0), (0, -1), "DejaVu-Bold"),
                    ("FONTNAME", (1, 0), (1, -1), "DejaVu"),

                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]
            )
        )

        story.append(customer_info)

        story.append(Spacer(1, 0.5 * cm))

        table_data = [
            ["Lp.", "Produkt", "Ilość", "Cena", "Wartość"]
        ]

        for index, item in enumerate(quote.items, start=1):
            table_data.append(
                [
                    index,
                    item.product.name,
                    item.quantity,
                    format_currency(item.product.price),
                    format_currency(item.total_price()),
                ]
            )

        table = Table(
            table_data,
            colWidths=[40, 220, 60, 80, 80],
            repeatRows=1,
        )

        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8E8E8")),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),

                    ("FONTNAME", (0, 0), (-1, 0), "DejaVu-Bold"),
                    ("FONTNAME", (0, 1), (-1, -1), "DejaVu"),

                    ("ALIGN", (0, 0), (0, -1), "CENTER"),
                    ("ALIGN", (2, 0), (-1, -1), "CENTER"),

                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),

                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ]
            )
        )

        story.append(table)

        story.append(Spacer(1, 0.5 * cm))

        story.append(
            Paragraph(
                "<b>Podsumowanie</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                f"Łączna wartość oferty: <b>{format_currency(quote.total_price())}</b>",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                "<b>Uwagi</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                escape(quote.details.notes) if quote.details.notes else "-",
                styles["Normal"],
            )
        )

        story.append(Spacer(1, 1 * cm))

        story.append(
            Paragraph(
                "<font color='#777777' size='9'>Oferta wygenerowana automatycznie.</font>",
                styles["Normal"],
            )
        )

        story.append(Spacer(1, 1 * cm))

        document.build(story)

        pdf = buffer.getvalue()

        buffer.close()

        return pdf