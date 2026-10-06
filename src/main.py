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
from report import generate_report


file_path = "invoices/Documento_Naturgy_5_.pdf"

invoice_text = read_pdf(file_path)

consumption = find_consumption(invoice_text)
price = find_price(invoice_text)
energy_cost = calculate_energy_cost(consumption, price)
power_p1 = find_power_p1(invoice_text)
power_p2 = find_power_p2(invoice_text)
total = find_total(invoice_text)

price_category = analyzer_price(price)

calculated_other_cost = calculate_other_costs(
    total,
    energy_cost
)

calculated_energy_percentage = calculate_energy_percentage(
    energy_cost,
    total
)

calculated_other_cost_percentage = calculate_other_cost_percentage(
    calculated_other_cost,
    total
)


invoice = {
    "consumption_kwh": consumption,
    "price_kwh": price,
    "energy_cost": energy_cost,
    "power_p1_kw": power_p1,
    "power_p2_kw": power_p2,
    "total": total,
    "price_category": price_category,
    "other_costs": calculated_other_cost,
    "energy_percentage": calculated_energy_percentage,
    "other_cost_percentage": calculated_other_cost_percentage
}


generate_report(invoice)