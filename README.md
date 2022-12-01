# PythonAPI-FASTAPI

Implementação de uma API para consultas simples utilizando REST.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[instalação](#-instala%C3%A7%C3%A3o)** para saber como instalar o projeto.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software?
* Python 3 ou superior
* MySQL

### 🔧 Instalação

Antes de tudo, é necessário baixar o **[codigo-fonte](https://github.com/eduardo92005-debug/PythonAPI-FASTAPI/archive/refs/heads/main.zip)**  da API. Daí, basta
seguir os passos abaixo:
* Extraia o zip da API dentro de uma pasta que desejar.
* Abra um terminal dentro da pasta.
* Se necessário instale o pacote de ambientes virtuais do python, use: ``` python -m pip install venv ```
* Escreva o seguinte comando no terminal e aguarde: ``` python -m venv api_venv ```
* Se estiver no sistema operacional Windows use: ``` api_venv\Scripts\Activate ```
* Caso esteja num sistema Linux use: ``` source  api_venv/bin/activate```
* Feito isso, agora é necessário instalar os pacotes para o funcionamento correto da api
* Para isso, use o comando: ``` pip install requirements.txt ```
* Se tudo ocorreu bem, no arquivo env.py, substitua ENV_USER pelo usuário do banco, ENV_PASS pela senha do banco e ENV_TABLE pela tabela a ser utilizada.
* Agora para subir um servidor web, utilize o uvicorn, sendo assim, utilize o seguinte comando: ``` uvicorn main:app --reload ```

## ⚙️ Arquitetura de pastas

* __Dependencies__ ->  Pasta que agloba todas as dependencias necessárias para a API.
* __Models__ -> Conjunto de arquivos que responsável pelos modelos/entidades do ORM SQLAlchemy.
* __Schemas__ -> Conjunto de arquivos especializados para validar os modelos.
* __Services__ -> Conjunto de arquivos especializados em fornecer utilidades gerais para o aplicativo.
* __v1/endpoints__ -> Conjunto de arquivos responsáveis por controlar as rotas e suas funcionalidades.


## 🛠️ Construído com

* [Python](https://www.php.net/docs.php) - Python
* [FastAPI](https://fastapi.tiangolo.com/) - Framework para criação de API's
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
