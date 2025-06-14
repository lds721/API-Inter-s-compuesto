from pydantic import BaseModel
from typing import List, Dict

class InversionEntrada(BaseModel):
    aportaciones: List[float]
    interes: float
    periodos: int

class ResultadoReparto(BaseModel):
    valor_futuro_total: float
    beneficio_total: float
    beneficios_individuales: Dict[str, float]
    explicacion: str
