from fastapi import FastAPI
from routers import router_validar

app = FastAPI()
app.title = "RT-API"
app.description = "API de validação de documentos"
app.version = "1.0.0"
app.docs_url = "/v1/docs"
app.redoc_url = "/v1/redoc"
app.openapi_url = "/v1/openapi.json"
# Root route
@app.get("/")
def routes():
    return {'Versões disponíveis': ['v1'], 'Versão atual': 'v1'}


# V1 route
@app.get("/v1/")
def read_root():
    return {'Status': 'OK', 'Versão': '1.0.0', 'Mensagem': 'Bem-vindo à RT-API!'}

# V1 - Validar routes
app.include_router(router_validar.router, prefix="/v1/validar", tags=["Validar"])

