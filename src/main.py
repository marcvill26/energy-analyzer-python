import os

from pdf_reader import read_pdf

from analyzer import find_consumption
from analyzer import find_price
from analyzer import calculate_energy_cost
from analyzer import find_power_p1
from analyzer import find_power_p2
from analyzer import find_total

from analyzer import analyzer_price

from analyzer import calculate_other_costs
from analyzer import calculate_energy_percentage
from analyzer import calculate_other_cost_percentage

from analyzer import find_power_p1_cost
from analyzer import find_power_p2_cost
from analyzer import find_socilal_bonus_cost
from analyzer import find_electricity_tax
from analyzer import find_meter_rental_cost
from analyzer import find_total_electricity

from analyzer import find_total_service
from analyzer import find_iva

from analyzer import calculate_total_electricity
from analyzer import calculate_invoice_total

from report import generate_report


invoice_files = [
    file
    for file in os.listdir("invoices")
    if file.lower().endswith(".pdf")
]


for file_name in invoice_files:

    print()
    print("=" * 60)
    print("FACTURA:", file_name)
    print("=" * 60)

    file_path = os.path.join("invoices", file_name)

    invoice_text = read_pdf(file_path)

    consumption = find_consumption(invoice_text)
    price = find_price(invoice_text)

    energy_cost = calculate_energy_cost(
        consumption,
        price
    )

    power_p1 = find_power_p1(invoice_text)
    power_p2 = find_power_p2(invoice_text)

    power_p1_cost = find_power_p1_cost(invoice_text)
    power_p2_cost = find_power_p2_cost(invoice_text)

    social_bonus_cost = find_socilal_bonus_cost(invoice_text)

    tax_electricity = find_electricity_tax(invoice_text)

    meter_rental_cost = find_meter_rental_cost(
        invoice_text
    )

    total_electricity = find_total_electricity(
        invoice_text
    )

    total_services = find_total_service(
        invoice_text
    )

    iva = find_iva(invoice_text)

    total = find_total(invoice_text)

    calculated_total_electricity = (
        calculate_total_electricity(
            energy_cost,
            power_p1_cost,
            power_p2_cost,
            social_bonus_cost,
            tax_electricity,
            meter_rental_cost
        )
    )

    electricity_difference = round(
        total_electricity -
        calculated_total_electricity,
        2
    )

    electricity_validation = (
        calculated_total_electricity
        == total_electricity
    )

    calculated_invoice_total = (
        calculate_invoice_total(
            total_electricity,
            total_services,
            iva
        )
    )

    invoice_difference = round(
        total -
        calculated_invoice_total,
        2
    )

    invoice_validation = (
        calculated_invoice_total
        == total
    )

    calculated_other_cost = (
        calculate_other_costs(
            total,
            energy_cost
        )
    )

    calculated_energy_percentage = (
        calculate_energy_percentage(
            energy_cost,
            total
        )
    )

    calculated_other_cost_percentage = (
        calculate_other_cost_percentage(
            calculated_other_cost,
            total
        )
    )

    price_category = analyzer_price(price)

    invoice = {
        "consumption_kwh": consumption,
        "price_kwh": price,

        "energy_cost": energy_cost,

        "power_p1_kw": power_p1,
        "power_p2_kw": power_p2,

        "power_p1_cost": power_p1_cost,
        "power_p2_cost": power_p2_cost,

        "social_bonus_cost": social_bonus_cost,
        "tax_electricity": tax_electricity,
        "meter_rental_cost": meter_rental_cost,

        "total_electricity": total_electricity,

        "calculated_total_electricity":
            calculated_total_electricity,

        "electricity_difference":
            electricity_difference,

        "electricity_validation":
            electricity_validation,

        "total_services": total_services,
        "iva": iva,

        "calculated_invoice_total":
            calculated_invoice_total,

        "invoice_difference":
            invoice_difference,

        "invoice_validation":
            invoice_validation,

        "total": total,

        "price_category": price_category,

        "other_costs":
            calculated_other_cost,

        "energy_percentage":
            calculated_energy_percentage,

        "other_cost_percentage":
            calculated_other_cost_percentage
    }

    generate_report(invoice)