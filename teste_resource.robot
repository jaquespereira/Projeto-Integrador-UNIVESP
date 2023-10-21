*** Settings ***
Library    SeleniumLibrary

***Variables***

*** Keywords ***
Abrir o navegador
    Open Browser    browser=chrome
    Maximize Browser Window

Fechar o navegador
    Capture Page Screenshot
    Close Browser


Dado que usuario entrar na pagina inicial
    Go To    url=file:///C:/Users/maria/OneDrive/%C3%81rea%20de%20Trabalho/Projeto-Integrador-UNIVESP/index1(pagina_inicial).html
    Wait Until Element Contains    //button[contains(.,'Vamos começar !')]    Vamos começar

Entao clicar no botao Vamos começar 
    Click Element    //button[contains(.,'Vamos começar !')]
    Sleep    5s

Quando chegar na pagina o que voce encontra nessa plataforma, usuario explorara as paginas  
    Wait Until Element Is Visible    //p[@class='plataforma'][contains(.,'O que você encontra nessa plataforma')]


Entao Clicar conheca nossa Missao, Visao valores E voltar 
    Click Element                    //div[@class='linkar text-body-secondary'][contains(.,'Conheça nossa missão, visão e valores')]
    Sleep    5s
    Wait Until Element Is Visible    //h1[contains(.,'Quem Somos')]
    Click Element                    //button[@class='voltar'][contains(.,'Voltar')]
    Sleep    5s



Entao Clicar conheca Nossa Marca E voltar 
    Click Element                    //div[@class='linkar text-body-secondary'][contains(.,'Conheça mais sobre a platarfoma')]
    Sleep    5s
    Wait Until Element Is Visible    //h1[contains(.,'Nossa Marca')]
    Click Element                    //button[@class='voltar'][contains(.,'Voltar')]    
    Sleep    5s

Entao Clicar Conheça mais sobre os investimentos e simule aqui Marca
    Click Element                    //div[@class='linkar text-body-secondary'][contains(.,'Conheça mais sobre os investimentos e simule aqui!')]
    Sleep    5s
    Wait Until Element Is Visible    //h1[contains(.,'Conheça Mais')]
    Sleep    10s


Dado que usuario esta na pagina de investimentos 
    Go To    url=file:///C:/Users/maria/OneDrive/%C3%81rea%20de%20Trabalho/Projeto-Integrador-UNIVESP/index7.html

Entao preencher os valores e calcular
    Input Text        //input[contains(@name,'Investimento Inicial')]           1000
    Input Text        //input[contains(@name,'Investimento Mensal(aporte)')]    100
    Input Text        //input[contains(@name,'Prazo(Meses)')]                   12
    Click Element     //button[@onclick='calcularRendaFixa()'][contains(.,'Calcular REVER')]
    





