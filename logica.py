from modelos import InversionEntrada, ResultadoReparto

def calcular_reparto(data: InversionEntrada) -> ResultadoReparto:
    aportaciones = data.aportaciones
    interes = data.interes
    periodos = data.periodos

    # 🚫 Validaciones
    if not aportaciones or len(aportaciones) < 2:
        raise ValueError("Debe haber al menos dos inversores.")
    
    if any(a <= 0 for a in aportaciones):
        raise ValueError("Todas las aportaciones deben ser mayores que cero.")

    if interes <= 0:
        raise ValueError("El interés debe ser un valor positivo.")

    if periodos <= 0:
        raise ValueError("El número de periodos debe ser un valor entero positivo.")

    # ✅ Cálculo
    valor_futuro_total = sum(a * (1 + interes) ** periodos for a in aportaciones)
    total_aportado = sum(aportaciones)
    beneficio_total = valor_futuro_total - total_aportado

    beneficios = {}
    explicacion = f"Con un interés del {interes:.2%} durante {periodos} períodos, la inversión total genera un valor futuro de {valor_futuro_total:.1f}.\n\n"
    explicacion += f"El beneficio total es {beneficio_total:.1f} y se reparte proporcionalmente según las aportaciones iniciales:\n"

    for i, a in enumerate(aportaciones, 1):
        proporcion = a / total_aportado
        beneficio = proporcion * beneficio_total
        beneficios[f"beneficio_{i}"] = round(beneficio, 2)
        explicacion += f"Inversor {i} aporta {a:.1f} y gana {beneficio:.2f}\n"

    return ResultadoReparto(
        valor_futuro_total=round(valor_futuro_total, 2),
        beneficio_total=round(beneficio_total, 2),
        beneficios_individuales=beneficios,
        explicacion=explicacion
    )
