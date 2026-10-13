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

    print("Coste potencia P1:", invoice["power_p1_cost"], "€")
    print("Coste potencia P2:", invoice["power_p2_cost"], "€")

    print("Bono Social:", invoice["social_bonus_cost"], "€")
    print("Impuesto Electricidad:", invoice["tax_electricity"], "€")
    print("Alquiler de Contador:", invoice["meter_rental_cost"], "€")
    print("Total Electricidad:", invoice["total_electricity"], "€")

    print()
    print("----- VALIDACION ELECTRICIDAD -----")
    print()

    print(
        "Total electricidad factura:",
        invoice["total_electricity"],
        "€"
    )

    print(
        "Total electricidad calculado:",
        invoice["calculated_total_electricity"],
        "€"
    )

    print(
        "Diferencia:",
        invoice["electricity_difference"],
        "€"
    )

    print()

    if invoice["electricity_validation"]:
        print("✅ Total electricidad validado")
    else:
        print("❌ Diferencia detectada")

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
    print("Total Servicios:", invoice["total_services"], "€")
    print("IVA:", invoice["iva"], "€")

    print()
    print("----- VALIDACION FACTURA -----")
    print()

    print(
        "Total factura PDF:",
        invoice["total"],
        "€"
    )

    print(
        "Total factura calculado:",
        invoice["calculated_invoice_total"],
        "€"
    )

    print(
        "Diferencia:",
        invoice["invoice_difference"],
        "€"
    )

    print()

    if invoice["invoice_validation"]:
        print("✅ FACTURA VALIDADA")
    else:
        print("❌ DIFERENCIA DETECTADA")

    print()
    print("==============================")
