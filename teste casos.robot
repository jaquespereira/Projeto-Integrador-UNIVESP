
*** Settings ***
Resource         teste_resource.robot
Test Setup       Abrir o navegador 
Test Teardown    Fechar o navegador

*** Test Cases ***

Caso 01 - Navegar a pagina inicial 
    Dado que usuario entrar na pagina inicial
    Entao clicar no botao Vamos começar 
    Quando chegar na pagina o que voce encontra nessa plataforma, usuario explorara as paginas 
    Entao Clicar no botao conhecer investimentos
    Entao Clicar Calculadora 

Caso 02 - Investir 
    Dado que usuario esta na pagina de investimentos 
    Entao preencher os valores e calcular
    
