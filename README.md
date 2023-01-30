# RT  - Uma api de diversas funcionalidades

Criei essa api para fins de estudos e praticidade na hora de executar algumas tarefas em meu emprego atual na área de suporte e certificados.

##  Como usar

Você pode acessar a página `/docs` para ver a documentação da api gerada automaticamente pela lib FastAPI.


## Rotas

'/' (root)
|
|_'v1/'
    |
    |
    |__'validar/'
	   |
	   |
	   |____'cpf/{cpf:string}'
	   |
	   |____'cnpj/{cnpj:string}'
	   |
	   |____'cnh/{cnh:string}'
	   |
	   |____'certidao/{certidao:string}'
	   |
	   |____'titulo/{titulo:string}'
	   |
	   |____'renavam/{renavam:string}'
	   |
	   |____'pis/{pis:string}'