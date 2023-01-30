from fastapi import APIRouter
from functions import Validadores, Formatacoes

router = APIRouter()

@router.get("/cpf/{cpf:str}")
def valida_cpf(cpf: str) -> dict:
    cpf_formatado = Formatacoes.formata_cpf(cpf)
    if Validadores.valida_cpf(cpf):
        response = {"cpf": cpf_formatado, "Status": 'Válido'}
    else:
        response = {"cpf": cpf_formatado, "Status": 'Inexistente'}
        
    return response

@router.get("/cnpj/{cnpj:str}")
def valida_cnpj(cnpj: str) -> dict:
    cnpj_formatado = Formatacoes.formata_cnpj(cnpj)
    if Validadores.valida_cnpj(cnpj):
        response = {"cnpj": cnpj_formatado, "Status": 'Válido'}
    else:
        response = {"cnpj": cnpj_formatado, "Status": 'Inexistente'}
        
    return response

@router.get("/cnh/{cnh:str}")
def valida_cnh(cnh: str) -> dict:
    
    if Validadores.valida_cnh(cnh):
        response = {"cnh": cnh, "Status": 'Válido'}
    else:
        response = {"cnh": cnh, "Status": 'Inexistente'}
        
    return response

@router.get("/certidao/{certidao:str}")
def valida_certidao(certidao: str) -> dict:
    
    if Validadores.valida_certidao(certidao):
        response = {"certidao": certidao, "Status": 'Válido'}
    else:
        response = {"certidao": certidao, "Status": 'Inexistente'}
        
    return response

@router.get("/titulo/{titulo:str}")
def valida_titulo(titulo: str) -> dict:
    
    if Validadores.valida_titulo(titulo):
        response = {"titulo": titulo, "Status": 'Válido'}
    else:
        response = {"titulo": titulo, "Status": 'Inexistente'}
        
    return response

@router.get("/renavam/{renavam:str}")
def valida_renavam(renavam: str) -> dict:
    
    if Validadores.valida_renavam(renavam):
        response = {"renavam": renavam, "Status": 'Válido'}
    else:
        response = {"renavam": renavam, "Status": 'Inexistente'}
        
    return response

@router.get("/pis/{pis:str}")
def valida_pis(pis: str) -> dict:
    
    if Validadores.valida_pis(pis):
        response = {"pis": pis, "Status": 'Válido'}
    else:
        response = {"pis": pis, "Status": 'Inexistente'}
        
    return response
