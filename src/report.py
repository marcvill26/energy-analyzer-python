def generate_report(invoice):

    print("==============================")
    print("     ANALISIS DE FACTURA")
    print("==============================")

    print()
    print("Consumo:", invoice["consumption_kwh"], "kWh")
    print("Precio:", invoice["price_kwh"], "€/kWh")

    print()
    print("Potencia P1:", invoice["power_p1_kw"], "kW")
    print("Potencia P2:", invoice["power_p2_kw"], "kW")

    print()
    print("Coste de energía:", invoice["energy_cost"], "€")
    print("Otros costes:", invoice["other_costs"], "€")
    print("Total:", invoice["total"], "€")

    print()
    print("Categoría:", invoice["price_category"])

    print()
    print(
        "Porcentaje destinado a energía:",
        invoice["energy_percentage"],
        "%"
    )

    print(
        "Porcentaje destinado a otros costes:",
        invoice["other_cost_percentage"],
        "%"
    )

    print()
    print("==============================")