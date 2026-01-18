# 🚗 Borali API

API backend do **Borali**, um aplicativo de transporte inspirado no modelo Uber, desenvolvido com foco em **boas práticas de engenharia de software**, **arquitetura escalável** e **aprendizado profissional**.

Este projeto faz parte do meu processo de evolução como desenvolvedora, simulando um ambiente real de empresa, com versionamento, organização modular e uso de Git de forma profissional.

---

## 📌 Tecnologias Utilizadas

* **Python 3.12**
* **FastAPI**
* **Uvicorn**
* **Pydantic v2**
* **pydantic-settings**
* **Git & GitHub**
* (Em breve) PostgreSQL, SQLAlchemy, Docker

---

## 🏗️ Estrutura do Projeto

```
backend/
├── app/
│   ├── main.py            # Ponto de entrada da aplicação
│   ├── core/              # Configurações centrais do projeto
│   │   └── config.py
│   ├── routes/            # Rotas da API
│   │   └── health.py
│   └── __init__.py
├── venv/                  # Ambiente virtual
└── requirements.txt
```

---

## 🚀 Como executar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Jaquelinesf2/borali.git
cd borali/backend
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o servidor

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Endpoints disponíveis

### Health Check

```
GET /api/v1/health
```

Resposta:

```json
{
  "status": "ok",
  "service": "Borali API"
}
```

---

## 📖 Documentação automática

* Swagger UI:
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* ReDoc:
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧠 Boas práticas aplicadas

* Versionamento de API (`/api/v1`)
* Separação de responsabilidades
* Configuração centralizada
* Estrutura modular de rotas
* Commits semânticos
* Simulação de fluxo de trabalho de empresa

---

## 🛣️ Próximos passos

* Cadastro de usuários (passageiro e motorista)
* Autenticação e autorização
* Integração com banco de dados
* Integração com app mobile
* Deploy em ambiente cloud

---

## 👩‍💻 Desenvolvido por

**Jaqueline da Silva Freitas**

* GitHub: [https://github.com/Jaquelinesf2](https://github.com/Jaquelinesf2)
* Área de interesse: Backend, APIs, Full Stack Development
