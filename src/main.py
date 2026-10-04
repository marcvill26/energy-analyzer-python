from pdf_reader import read_pdf
from analyzer import find_consumption
from analyzer import find_price
from analyzer import calculate_energy_cost
from analyzer import find_power_p1
from analyzer import find_power_p2
from analyzer import find_total

file_path = "invoices/Documento_Naturgy_5_.pdf"

invoice_text = read_pdf(file_path)



consumption = find_consumption(invoice_text)
price = find_price(invoice_text)
energy_cost = calculate_energy_cost(consumption, price)
power_p1 = find_power_p1(invoice_text)
power_p2 = find_power_p2(invoice_text)
total = find_total(invoice_text)

invoice = {
    'consumption_kwh': consumption,
    'price_kwh':price,
    'energy_cost': energy_cost,
    'power_p1_kw': power_p1,
    'power_p2_kw': power_p2,
    'total':total
}
print(invoice)

print('Consumo encontrado:',consumption, 'KWh')
print('Tipo de dato:', type(consumption))
print('Precio encontrado:', price, '€/KWh')
print('Tipo de dato:', type(price))
print('Costo de energía encontrado:', energy_cost, '€')
print('Potencia P1 encontrada:', power_p1, 'kW')
print('Potencia P2 encontrada:', power_p2, 'kW')
print('Total a pagar encontrado:', total, '€')