# Projeto ETL - Extração de Dados da API Coinbase

Este projeto é um pipeline ETL (Extract, Transform, Load) que extrai dados de preços de criptomoedas da API da Coinbase e os processa para análise.

## 🚀 Funcionalidades

- Extração de dados em tempo real da API Coinbase
- Processamento de preços spot de criptomoedas
- Armazenamento estruturado dos dados
- Interface de visualização dos dados

## 🛠️ Tecnologias Utilizadas

- Python
- Requests (para chamadas à API)
- Streamlit (para visualização de dados)
- SQLite (para armazenamento de dados)

## 📋 Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/ETLProjectAPIExtract.git
```

2. Instale as dependências:

```bash
pip install -r src/requirements.txt
```

## 💻 Como Usar

1. Execute o pipeline de extração:

```bash
python src/pipeline.py
```

2. Inicie o dashboard:

```bash
streamlit run app/dashboard.py
```

## 📊 Estrutura do Projeto

```
ETLProjectAPIExtract/
├── app/
│   └── dashboard.py
├── src/
│   ├── pipeline.py
│   ├── database.py
│   └── requirements.txt
└── README.md
```

## 🔄 Pipeline de Dados

O projeto segue um fluxo ETL:

1. **Extract**: Coleta dados da API Coinbase
2. **Transform**: Processa e estrutura os dados
3. **Load**: Armazena os dados em um banco de dados local

## 📈 Visualização de Dados

O dashboard permite visualizar:

- Preços spot em tempo real
- Histórico de preços
- Análises básicas dos dados

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

Glauber Bandeira - [glauberbandeira\_@hotmail.com](mailto:glauberbandeira_@hotmail.com)
Linkedin - [Glauber BAndeira](https://www.linkedin.com/in/glauberbandeira/)

---

⭐️ Se este projeto ajudou você, considere dar uma estrela!
