from fastapi import FastAPI
from routers import router_validar

app = FastAPI()

# Root route
@app.get("/")
def routes():
    return {'Versões disponíveis': ['v1'], 'Versão atual': 'v1'}


# V1 route
@app.get("/v1/")
def read_root():
    return {'Status': 'OK', 'Versão': '1.0.0', 'Mensagem': 'Bem-vindo à RT-API!'}

# V1 - Validar routes
app.add_route("/v1/validar", router_validar.router)