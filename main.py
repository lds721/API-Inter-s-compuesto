from fastapi import FastAPI
from modelos import InversionEntrada, ResultadoReparto
from logica import calcular_reparto

app = FastAPI(title="API Reparto Proporcional", version="2.0")

@app.post("/reparto", response_model=ResultadoReparto)
def reparto_beneficios(data: InversionEntrada):
    return calcular_reparto(data)
