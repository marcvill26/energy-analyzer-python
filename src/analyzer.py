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


def calculate_energy_cost(consumption,price):
  
    cost = consumption * price
    cost = round(cost,2)
    return cost


def find_power_p1(text):
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        if 'término potencia p1' in line.lower():
            power_p1 = lines[i + 1]
            
           
            power_p1 = power_p1.replace('kW','')
            power_p1 = power_p1.strip()
            power_p1 = power_p1.replace(',','.')
            power_p1 = float(power_p1)
            return power_p1
            
            
def find_power_p2(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'término potencia p2' in line.lower():
            power_p2 = lines[i + 1]
            
            power_p2 = power_p2.replace('kW','')
            power_p2 = power_p2.strip()
            power_p2 = power_p2.replace(',','.')
            power_p2 = float(power_p2)
            return power_p2
            
            
def find_total(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if'total a pagar' in line.lower():
            total = lines[i + 2]
            
            total = total.replace('€','')
            total = total.strip()
            total = total.replace(',','.')
            total = float(total)
            
            return total            