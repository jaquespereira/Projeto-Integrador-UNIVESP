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
    Go To    url=file:///C:/Users/SAMSUNG/Desktop/Jaques/Projeto-Integrador-UNIVESP/index1(pagina_inicial).html 
    Wait Until Element Contains    //button[contains(.,'Vamos começar !')]    Vamos começar

Entao clicar no botao Vamos começar 
    Click Element    //button[contains(.,'Vamos começar !')]
    Sleep    5s

Quando chegar na pagina o que voce encontra nessa plataforma, usuario explorara as paginas  
    Wait Until Element Is Visible    locator=//a[contains(.,'Conheça mais sobre a platarfoma')]
    Sleep     3s
    Click Element                    locator=//a[contains(.,'Conheça mais sobre a platarfoma')]
    Scroll Element Into View        locator=//button[@class='voltar'][contains(.,'Voltar')]
    Sleep     3s
    Click Element                   locator=//button[@class='voltar'][contains(.,'Voltar')]

Entao Clicar no botao conhecer investimentos
    Click Element                    //div[@class='linkar text-body-secondary'][contains(.,'Sobre Investimentos')]
    Sleep     3s    
    Scroll Element Into View        locator=//button[@class='voltar'][contains(.,'Voltar')]
    Sleep     3s    
    Click Element                    locator=//button[@class='voltar'][contains(.,'Voltar')]
    Sleep    5s
    Scroll Element Into View         //div[@class='linkar text-body-secondary'][contains(.,'Conheça mais sobre os investimentos previdenciarios !')]

Entao Clicar Calculadora 
    Click Element                    //div[@class='linkar text-body-secondary'][contains(.,'Conheça mais sobre os investimentos previdenciarios !')]
    Sleep    5s
    Click Element                    //a[@class='buton-previdencia'][contains(.,'TESOURO RENDA MAIS')]
    Sleep     3s
    Scroll Element Into View          //button[@class='voltar'][contains(.,'Ir para o próximo investimento --->')]
    Click Element                     //button[@class='voltar'][contains(.,'Ir para o próximo investimento --->')] 
   

Entao Clicar Conheça mais sobre os investimentos e simule aqui Marca
    Click Element                    //div[@class='linkar text-body-secondary'][contains(.,'Conheça mais sobre os investimentos e simule aqui!')]
    Sleep    5s
    Wait Until Element Is Visible    //h1[contains(.,'Conheça Mais')]
    Sleep    s

Entao Clicar Conheça mais sobre os investimentos
    Click Element    //div[@class='linkar text-body-secondary'][contains(.,'Conheça mais sobre os investimentos e simule aqui!')]
    Sleep    5s
    Click Element    //th[@scope='row'][contains(.,'CDB (Certificado de Depósito Bancário)')]
    Sleep    5s
    


Dado que usuario esta na pagina de investimentos 
    Go To    url=file:///C:/Users/SAMSUNG/Desktop/Jaques/Projeto-Integrador-UNIVESP/index10(calculadora_renda_fixa).html
    
Entao preencher os valores e calcular
    Input Text        //input[contains(@name,'valorInicial')]           1000
    Input Text        //input[contains(@name,'InvestimentoMensal')]    100
    Input Text        //input[contains(@name,'tempoDeInvestimento')]                   12
    Scroll Element Into View    locator=//button[contains(.,'Calcular')]
    Sleep    4s
    
    Go To    url=file:///C:/Users/SAMSUNG/Desktop/Jaques/Projeto-Integrador-UNIVESP/index10(calculadora_renda_fixa)2.html
    Sleep    4s
    
    Scroll Element Into View    //button[@class='voltar'][contains(.,'Voltar')]
    Input Text     //input[contains(@type,'number')]     100
    Sleep    4s


