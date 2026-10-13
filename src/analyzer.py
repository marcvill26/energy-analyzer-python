def find_consumption(text):
    lines = text.splitlines()

    for i, line in enumerate(lines):

        if "consumo electricidad" in line.lower():

            consumption = lines[i + 1]

            consumption = consumption.replace("kWh", "")
            consumption = consumption.strip()
            consumption = int(consumption)

            return consumption


def find_price(text):
    lines = text.splitlines()

    for i, line in enumerate(lines):

        if "consumo electricidad" in line.lower():

            price = lines[i + 2]

            price = price.replace("x", "")
            price = price.replace("€/kWh", "")
            price = price.strip()
            price = price.replace(",", ".")
            price = float(price)

            return price


def calculate_energy_cost(consumption, price):
    cost = consumption * price
    cost = round(cost, 2)

    return cost


def find_power_p1(text):
    lines = text.splitlines()

    for i, line in enumerate(lines):

        if "término potencia p1" in line.lower():

            power_p1 = lines[i + 1]

            power_p1 = power_p1.replace("kW", "")
            power_p1 = power_p1.strip()
            power_p1 = power_p1.replace(",", ".")
            power_p1 = float(power_p1)

            return power_p1
        
        

def find_power_p1_cost(text):
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        if 'término potencia p1' in line.lower():
            power_p1_cost = lines[i + 3]
            power_p1_cost = power_p1_cost.replace('€','')
            power_p1_cost = power_p1_cost.strip()
            power_p1_cost = power_p1_cost.replace(',','.')
            power_p1_cost = float(power_p1_cost)
            
            return power_p1_cost
    
    
    
    
    
def find_power_p2(text):
    lines = text.splitlines()

    for i, line in enumerate(lines):

        if "término potencia p2" in line.lower():

            power_p2 = lines[i + 1]

            power_p2 = power_p2.replace("kW", "")
            power_p2 = power_p2.strip()
            power_p2 = power_p2.replace(",", ".")
            power_p2 = float(power_p2)

            return power_p2



def find_power_p2_cost(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if"término potencia p2" in line.lower():
            power_p2_cost = lines [i + 3]
            power_p2_cost = power_p2_cost.replace('€','')
            power_p2_cost = power_p2_cost.strip()
            power_p2_cost = power_p2_cost.replace(',','.')
            power_p2_cost = float(power_p2_cost)
            return power_p2_cost
        

def find_total(text):
    lines = text.splitlines()

    for i, line in enumerate(lines):

        if "total a pagar" in line.lower():

            total = lines[i + 2]

            total = total.replace("€", "")
            total = total.strip()
            total = total.replace(",", ".")
            total = float(total)
            return total


def analyzer_price(price):

    if price < 0.12:
        return "Precio bajo"

    elif price <= 0.18:
        return "Precio medio"

    else:
        return "Precio alto"


def calculate_other_costs(total, energy_cost):
    other_costs = total - energy_cost
    other_costs = round(other_costs, 2)

    return other_costs


def calculate_energy_percentage(energy_cost, total):
    percentage = (energy_cost / total) * 100
    percentage = round(percentage, 2)

    return percentage


def calculate_other_cost_percentage(other_costs, total):
    percentage = (other_costs / total) * 100
    percentage = round(percentage, 2)
    return total            


def analyzer_price(price):
    if price < 0.12:
        return 'Precio bajo'
    elif price <= 0.18:
        return 'Precio medio'
    else:
        return 'Precio alto'        

    
def calculate_other_costs(total, energy_cost):
    other_costs = total - energy_cost
    other_costs = round(other_costs,2)
    return other_costs

def calculate_energy_percentage(energy_cost,total):
    percentage = (energy_cost / total) *100
    percentage = round(percentage,2)
    return percentage

def calculate_other_cost_percentage(other_costs, total):
    percentage = (other_costs / total) *100
    percentage = round(percentage,2)
    return percentage


def find_socilal_bonus_cost (text):
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        if 'financiación de bono social' in line.lower():
            social_bonus_cost = lines[i + 3]
            social_bonus_cost = social_bonus_cost.replace('€','')
            social_bonus_cost = social_bonus_cost.strip()
            social_bonus_cost = social_bonus_cost.replace(',','.')
            social_bonus_cost = float(social_bonus_cost)
            
            return social_bonus_cost
        
def find_electricity_tax (text):
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        if 'impuesto electricidad' in line.lower():
            tax_electricity = lines [i + 3]
            tax_electricity = tax_electricity.replace('€','')
            tax_electricity = tax_electricity.strip()
            tax_electricity = tax_electricity.replace(',','.')
            tax_electricity = float(tax_electricity)
            
            return tax_electricity
        
def find_meter_rental_cost(text):
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if 'alquiler de contador' in line.lower():
                meter_rental_cost = lines[i + 3]

                meter_rental_cost = meter_rental_cost.replace('€', '')
                meter_rental_cost = meter_rental_cost.strip()
                meter_rental_cost = meter_rental_cost.replace(',', '.')
                meter_rental_cost = float(meter_rental_cost)

                return meter_rental_cost
            
def find_total_electricity (text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'total electricidad' in line.lower():
            
            
           
            total_electricity = lines [ i + 1]
            total_electricity = total_electricity.replace('€','')
            total_electricity = total_electricity.strip()
            total_electricity = total_electricity.replace(',','.')
            total_electricity = float(total_electricity)
            
            return total_electricity           
        
def calculate_total_electricity(
    
    energy_cost,
    power_p1_cost,
    power_p2_cost,
    social_bonus_cost,
    tax_electricity,
    meter_rental_cost
):
    total= (
        energy_cost
        +power_p1_cost
        +power_p2_cost
        +social_bonus_cost
        +tax_electricity
        +meter_rental_cost
    )
    
    total = round(total,2)
    
    return total


def find_total_service(text):
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        if 'total servicios' in line.lower():
            total_services = lines [i + 1]
            total_services = total_services.replace('€','')
            total_services = total_services.strip()
            total_services = total_services.replace(',','.')
            total_services = float(total_services)
            
            return total_services
        
def find_iva(text):
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        if 'iva' in line.lower():
            iva = lines [i  + 1]
            iva = iva.replace('€','')
            iva = iva.strip()
            iva = iva.replace(',','.')
            iva = float(iva)
            
            return iva
        
        
def calculate_invoice_total(
    total_electricity,
    total_services,
    iva
):
    total = (
        total_electricity
        + total_services
        + iva
    )

    total = round(total, 2)

    return total