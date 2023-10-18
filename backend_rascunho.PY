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





