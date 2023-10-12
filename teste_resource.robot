*** Settings ***
Library    SeleniumLibrary

***Variables***

*** Keywords ***
Abrir o navegador
    Open Browser    browser=chrome
    Maximize Browser Window

Fechar o navegador
    Close Browser


Dado que usuario entrar na pagina inicial
    Go To    url=http://127.0.0.1:5500/Projeto-Integrador-UNIVESP/index.html
    Wait Until Element Contains    //button[contains(.,'Vamos começar !')]    Vamos começar

Entao clicar no botao Vamos começar 
    Click Element    //button[contains(.,'Vamos começar !')]

Quando chegar na pagina o que voce encontra nessa plataforma, usuario explorara as paginas  
    Wait Until Element Is Visible    //p[@class='plataforma'][contains(.,'O que você encontra nessa plataforma')]

Entao Clicar conheca nossa Missao, Visao valores E voltar 
    Click Element                    //div[@class='linkar text-body-secondary'][contains(.,'Conheça nossa missão, visão e valores')]
    Wait Until Element Is Visible    //h1[contains(.,'Quem Somos')]
    Click Element                    //button[@class='voltar'][contains(.,'Voltar')]

Entao Clicar conheca Nossa Marca E voltar 
    Click Element                    //div[@class='linkar text-body-secondary'][contains(.,'Conheça mais sobre a platarfoma')]
    Wait Until Element Is Visible    //h1[contains(.,'Nossa Marca')]
    Click Element                    //button[@class='voltar'][contains(.,'Voltar')]    

Entao Clicar Conheça mais sobre os investimentos e simule aqui Marca
    Click Element                    //div[@class='linkar text-body-secondary'][contains(.,'Conheça mais sobre os investimentos e simule aqui!')]
    Wait Until Element Is Visible    //h1[contains(.,'Conheça Mais')]


Dado que usuario esta na pagina de investimentos 
    Wait Until Element Is Visible    //h1[contains(.,'Conheça Mais')]

Entao clicar CBD liquidez diaria 
    Click Element    //h5[@class='card-title'][contains(.,'CBD Liquidez Diária  -Aplicação minima: 100,00  -Vencimento: 1 dia depois -Liquidez: 104% do CDI')]
    Wait Until Element Is Visible    //h1[contains(.,'Calculadora de Investimentos')]

Entao preencher os valores e calcular
    Input Text        //input[contains(@name,'Investimento Inicial')]           1000
    Input Text        //input[contains(@name,'Investimento Mensal(aporte)')]    100
    Input Text        //input[contains(@name,'Prazo(Meses)')]                   12
    Click Element     //button[@class='calculo'][contains(.,'Calcular')]
    





