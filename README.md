# Pipeline de tranformação de dados
Este repositório contém uma pipeline batch no Apache Beam, que transforma dados JSON em um arquivo CSV

Acesse a documentação: 🔗
- [Apache Beam](./wiki/apache.md)
- [Execução da Pipeline](./wiki/execucao.md)

## Estrutura do projeto: 
- `pipeline`: scripts para a criação da pipeline
- `wiki`: documentação e recursos
- `Dockerfile`: definir e construir uma imagem Docker

## Pré- requisitos
- Python (versão 3.10 ou superior)
- Docker e docker-compose

## Como executar
### Localmente

Clone o projeto:

```bash
  git clone https://github.com/AnaJuliaMM/pipeline_apache_beam.git
```

Crie um ambiente virtual:

```bash
  python -m venv venv
```

Ative o ambiente virtual:

```bash
  .\venv\Scripts\activate
```

Instale os requirements.txt:

```bash
  pip install -r requirements.txt
```

Execute a pipeline
```
  cd ./pipeline/
  python app.py
```

### Com o Docker
Construção da imagem:
```
docker build -t apache-beam-json-to-csv .
```
Para rodar a imagem no Docker:

```
docker run -d apache-beam-json-to-csv
```

## Resultado
https://github.com/AnaJuliaMM/pipeline_apache_beam/assets/123522605/48d23ed0-fb43-43bd-81b6-82932d4b2336


