#  DevOps Lab Ana 

API REST desenvolvida em Python (Flask) focada em práticas modernas de **DevOps**. Este projeto demonstra um ciclo completo de desenvolvimento de software, desde a containerização até o deploy contínuo automatizado.

## 📋 Funcionalidades

* **API RESTful:** Endpoints para listagem de itens e verificação de status.
* **Autenticação JWT:** Segurança implementada com *Json Web Tokens*.
* **Documentação Automática:** Swagger UI integrado para testar rotas.
* **Containerização:** Ambiente padronizado com Docker e Docker Compose.
* **Testes Automatizados:** Verificação de qualidade com `unittest`.
* **CI/CD Completo:** Pipeline de Integração e Entrega Contínua com GitHub Actions.

---

## 🤖 GitHub Actions

A "mágica" deste projeto acontece no arquivo `.github/workflows/workflow.yaml`. Toda vez que um código é enviado (`push`) para o repositório, uma esteira automática é iniciada:

### 1. 🏗️ Build
O GitHub prepara o ambiente (Ubuntu), instala o Python e baixa todas as dependências listadas no `requirements.txt`. Isso garante que o código não tem erros básicos de instalação.

### 2. 🧪 Testes Automatizados
Antes de qualquer coisa ir para o ar, o sistema roda a bateria de testes definida em `teste_app.py`.
* Se **um** teste falhar, a esteira para imediatamente.
* Isso impede que código quebrado chegue em produção.

### 3. 🚀 Deploy Automático 
Se (e somente se) os testes passarem, o GitHub Actions:
1.  Instala a CLI da Vercel.
2.  Autentica usando tokens seguros (`SECRETS`).
3.  Faz o deploy da aplicação para a nuvem da Vercel automaticamente.

**Segredos necessários no GitHub (Settings > Secrets):**
* `VERCEL_TOKEN`

---

## 🛠️ Tecnologias

* [Python 3.9+](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)
* [Docker](https://www.docker.com/)
* [GitHub Actions](https://github.com/features/actions)
* [Vercel](https://vercel.com/) (Hospedagem Serverless)

---

# ⚙️ Como Rodar Localmente

### Criar venv
```
python -m venv venv
```
### Ativar venv 
```
(Windows)
.\venv\Scripts\activate

Ativar venv (Linux/Mac):
source venv/bin/activate

Desativar venv:
deactivate
```

### Instale as dependências 
```
pip install -r requirements.txt
python app.py
``` 
---

# 🐳 Via Docker (Recomendado)
A maneira mais simples de rodar, garantindo que tudo funcione igual ao servidor.

```bash
# Subir a aplicação
docker-compose up --build

# Rodar os testes dentro do container
docker-compose run api python -m unittest discover
```