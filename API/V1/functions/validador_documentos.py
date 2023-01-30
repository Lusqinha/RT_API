from validate_docbr import CPF, CNPJ, CNH, Certidao, TituloEleitoral, RENAVAM, PIS

class Formatacoes:
    def formata_cpf(cpf):
        cpf_formatado = CPF().mask(cpf)
        return cpf_formatado

    def formata_cnpj(cnpj):
        cnpj_formatado = CNPJ().mask(cnpj)
        return cnpj_formatado


class Validadores:
    def valida_cpf(cpf):
        cpf_validado = CPF().validate(cpf)
        
        if cpf_validado:
            return True
        else:
            return False

    def valida_cnpj(cnpj):
        cnpj_validado = CNPJ().validate(cnpj)
        
        if cnpj_validado:
            return True
        else:
            return False

    def valida_cnh(cnh):
        cnh_validado = CNH().validate(cnh)
        
        if cnh_validado:
            return True
        else:
            return False

    def valida_certidao(certidao):
        certidao_validado = Certidao().validate(certidao)
        
        if certidao_validado:
            return True
        else:
            return False

    def valida_titulo(titulo):
        titulo_validado = TituloEleitoral().validate(titulo)
        
        if titulo_validado:
            return True
        else:
            return False
        
    def valida_renavam(renavam):
        renavam_validado = RENAVAM().validate(renavam)
        
        if renavam_validado:
            return True
        else:
            return False
        
    def valida_pis(pis):
        pis_validado = PIS().validate(pis)
        
        if pis_validado:
            return True
        else:
            return False