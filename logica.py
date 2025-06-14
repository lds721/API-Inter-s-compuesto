from modelos import InversionEntrada, ResultadoReparto

def calcular_reparto(data: InversionEntrada) -> ResultadoReparto:
    A = data.aportaciones
    r = data.interes
    n = data.periodos

    # Cálculo del valor futuro individual y total
    VF_individuales = [round(c * (1 + r) ** n, 2) for c in A]
    VF_total = round(sum(VF_individuales), 2)
    capital_total = round(sum(A), 2)
    beneficio_total = round(VF_total - capital_total, 2)

    # Reparto proporcional
    proporciones = [a / capital_total for a in A]
    beneficios = [round(p * beneficio_total, 2) for p in proporciones]

    # Diccionario de resultados
    beneficios_dict = {f"beneficio_{i+1}": beneficios[i] for i in range(len(A))}

    explicacion = (
        f"Con un interés del {r*100:.2f}% durante {n} períodos, "
        f"la inversión total genera un valor futuro de {VF_total}.\n\n"
        f"El beneficio total es {beneficio_total} y se reparte proporcionalmente según las aportaciones iniciales:\n" +
        "\n".join([f"Inversor {i+1} aporta {A[i]} y gana {beneficios[i]}" for i in range(len(A))])
    )

    return ResultadoReparto(
        valor_futuro_total=VF_total,
        beneficio_total=beneficio_total,
        beneficios_individuales=beneficios_dict,
        explicacion=explicacion
    )
