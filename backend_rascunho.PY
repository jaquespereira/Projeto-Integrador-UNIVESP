import requests
import json

# URL da API do Banco Central para a taxa Selic
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

# Função para obter a taxa Selic atual
def obter_taxa_selic_atual():
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if dados:
            # A API retorna os dados em ordem cronológica reversa, então o primeiro registro é o mais recente.
            taxa_atual = float(dados[0]['valor'])
            return taxa_atual
    return None

# Chama a função para obter a taxa Selic atual
taxa_atual = obter_taxa_selic_atual()

if taxa_atual is not None:
    print(f"A taxa Selic atual é de: {taxa_atual:.2f}%")
else:
    print("Não foi possível obter a taxa Selic atual. Verifique a URL da API ou a conexão com a internet.")





import mysql.connector

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
cursor = conn.cursor()

# Função para inserir um novo investimento no banco de dados
def inserir_investimento(nome, principal, taxa_juros, prazo, data_vencimento):
    sql = "INSERT INTO investments (name, principal, interest_rate, term, maturity_date) VALUES (%s, %s, %s, %s, %s)"
    values = (nome, principal, taxa_juros, prazo, data_vencimento)
    cursor.execute(sql, values)
    conn.commit()
    print("Investimento inserido com sucesso!")

# Função para calcular o rendimento de um investimento
def calcular_rendimento(investimento_id):
    sql = "SELECT principal, interest_rate, term FROM investments WHERE id = %s"
    cursor.execute(sql, (investimento_id,))
    result = cursor.fetchone()
    
    if result:
        principal, taxa_juros, prazo = result
        montante = principal * (1 + taxa_juros/100) ** prazo
        rendimento = montante - principal
        return rendimento
    else:
        return None

# Interface de usuário
while True:
    print("Escolha uma opção:")
    print("1. Inserir novo investimento")
    print("2. Calcular rendimento de um investimento")
    print("3. Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        nome = input("Nome do investimento: ")
        principal = float(input("Principal: "))
        taxa_juros = float(input("Taxa de juros (em %): ")
        prazo = int(input("Prazo (em anos): "))
        data_vencimento = input("Data de vencimento (AAAA-MM-DD): ")
        inserir_investimento(nome, principal, taxa_juros, prazo, data_vencimento)
    
    elif opcao == "2":
        investimento_id = int(input("ID do investimento: "))
        rendimento = calcular_rendimento(investimento_id)
        
        if rendimento is not None:
            print(f"O rendimento do investimento é: R$ {rendimento:.2f}")
        else:
            print("Investimento não encontrado.")
    
    elif opcao == "3":
        break

# Fechar a conexão com o banco de dados
conn.close()



const mysql = require('mysql2');
const readline = require('readline');

// Configurações do banco de dados MySQL
const db = mysql.createConnection({
  host: 'localhost',
  user: 'seu_usuario',
  password: 'sua_senha',
  database: 'seu_banco_de_dados'
});

// Criação da tabela para investimentos
db.query(`
  CREATE TABLE IF NOT EXISTS investments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    principal DECIMAL(10, 2),
    interest_rate DECIMAL(5, 2),
    term INT,
    maturity_date DATE
  )
`, (err) => {
  if (err) {
    console.error('Erro na criação da tabela:', err);
    return;
  }

  console.log('Tabela criada com sucesso.');

  // Iniciar a aplicação após a criação da tabela
  startApplication();
});

// Função para inserir um novo investimento no banco de dados
function inserirInvestimento(nome, principal, taxaJuros, prazo, dataVencimento) {
  const sql = `
    INSERT INTO investments (name, principal, interest_rate, term, maturity_date)
    VALUES (?, ?, ?, ?, ?)
  `;

  const values = [nome, principal, taxaJuros, prazo, dataVencimento];

  db.query(sql, values, (err, result) => {
    if (err) {
      console.error('Erro ao inserir investimento:', err);
      return;
    }

    console.log('Investimento inserido com sucesso!');
  });
}

// Função para calcular o rendimento de um investimento
function calcularRendimento(investimentoId) {
  const sql = 'SELECT principal, interest_rate, term FROM investments WHERE id = ?';

  db.query(sql, [investimentoId], (err, results) => {
    if (err) {
      console.error('Erro ao buscar investimento:', err);
      return;
    }

    if (results.length > 0) {
      const { principal, interest_rate, term } = results[0];
      const montante = principal * (1 + interest_rate / 100) ** term;
      const rendimento = montante - principal;
      console.log(`O rendimento do investimento é: R$ ${rendimento.toFixed(2)}`);
    } else {
      console.log('Investimento não encontrado.');
    }
  });
}

// Inicializar a interface de linha de comando
function startApplication() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.question('Escolha uma opção:\n1. Inserir novo investimento\n2. Calcular rendimento de um investimento\n3. Sair\n', (opcao) => {
    if (opcao === '1') {
      rl.question('Nome do investimento: ', (nome) => {
        rl.question('Principal: ', (principal) => {
          rl.question('Taxa de juros (em %): ', (taxaJuros) => {
            rl.question('Prazo (em anos): ', (prazo) => {
              rl.question('Data de vencimento (AAAA-MM-DD): ', (dataVencimento) => {
                inserirInvestimento(nome, principal, taxaJuros, prazo, dataVencimento);
                rl.close();
              });
            });
          });
        });
      });
    } else if (opcao === '2') {
      rl.question('ID do investimento: ', (investimentoId) => {
        calcularRendimento(investimentoId);
        rl.close();
      });
    } else if (opcao === '3') {
      rl.close();
    }
  });
}

Certifique-se de substituir 'seu_usuario', 'sua_senha' e 'seu_banco_de_dados' pelas informações de autenticação e nome do banco de dados corretos. Este código cria uma aplicação de linha de comando para inserir investimentos no banco de dados e calcular o rendimento com base no ID do investimento. Certifique-se de que o servidor MySQL esteja em execução e acessível a partir deste código.





<!DOCTYPE html>
<html>
<head>
    <title>Calculadora da Poupança</title>
</head>
<body>
    <h1>Calculadora da Poupança</h1>
    <p>Informe o valor inicial e o período de investimento:</p>
    <label for="valorInicial">Valor Inicial:</label>
    <input type="number" id="valorInicial" step="0.01" placeholder="Informe o valor inicial"><br><br>
    <label for="periodoInvestimento">Período de Investimento (em meses):</label>
    <input type="number" id="periodoInvestimento" placeholder="Informe o período de investimento"><br><br>
    <button id="calcular">Calcular Rendimento</button>
    <p id="resultado"></p>

    <script>
        document.getElementById("calcular").addEventListener("click", function () {
            const valorInicial = parseFloat(document.getElementById("valorInicial").value);
            const periodoInvestimento = parseInt(document.getElementById("periodoInvestimento").value);
            const apiUrl = `https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/${new Date().getFullYear()}&dataFinal=01/12/${new Date().getFullYear()}`;

            fetch(apiUrl)
                .then((response) => response.json())
                .then((data) => {
                    // Encontrar a taxa de rendimento da poupança no último mês disponível
                    const ultimaTaxa = data[data.length - 1].valor / 100;

                    // Calcular o rendimento da poupança
                    const rendimento = valorInicial * Math.pow(1 + ultimaTaxa, periodoInvestimento / 12) - valorInicial;

                    document.getElementById("resultado").textContent = `Seu rendimento estimado é de R$ ${rendimento.toFixed(2)}`;
                })
                .catch((error) => {
                    console.error("Erro ao buscar a taxa de rendimento da poupança: " + error);
                });
        });
    </script>
</body>
</html>


A construção da plataforma nos permitiu reforçar tanto a teoria como a prática de alguns elementos trabalhados no PI anterior, tais como HTML, CSS e o framework Bootstrap, o versionamento de código via GitHub. Além disso, pudemos nos aprofundar em alguns elementos que apenas tínhamos tido um contato mais inicial, porém que não eram o escopo central do último projeto como a parte de banco de dado ou o uso do Javascript.  

Aprendemos e trabalhamos com novos conceitos e práticas relacionados ao desenvolvimento. Entendemos sobre o uso da nuvem na construção da plataforma, bem como trabalhar com APIs de forma dar novas possiblidades para o back-end, acessibilidade como dado fundamental de equidade, uso de testes como meio de garantia da qualidade no desenvolvimento do produto.  

Procuramos trabalhar com boas práticas, a fim de que o código seja mais acessível para futuras refatorações ou mesmo para entendimento facilitado do código e como ele está estruturado. Acreditamos também que há possibilidades de melhoria e amadurecimento, deixando em aberto próximo projeto a possiblidade de implementar novas funcionalidades, fluxos a fim de procurar a melhoria contínua da mesma. 