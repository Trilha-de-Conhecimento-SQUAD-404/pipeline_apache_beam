# Pipeline de transformação de dados

Este repositório contém um pipeline batch no Apache Beam, que transforma dados JSON em um arquivo CSV

Acesse a documentação: 🔗

- [Apache Beam](./wiki/apache_beam.md)
- [Execução do Pipeline](./wiki/pipeline_json_to_csv.md)

## Estrutura do projeto:

- `pipeline`: scripts para a criação do pipeline
- `wiki`: documentação e recursos
- `Dockerfile`: definir e construir uma imagem Docker

## Pré- requisitos

- Apache Beam (versão 2.54.0)
- Python (versão 3.10 ou superior)
- Docker (versão 24.0.6)
- docker-compose (version v2.21.0-desktop.1)

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

Para executar a imagem no Docker:

```
# Windows PowerShell
docker run -d --name beam_conteiner -v "${PWD}/pipeline/data:/opt/apache/beam/pipeline/data" apache-beam-json-to-csv

# Linux ou macOS
docker run -d --name beam_conteiner -v "$(pwd)/pipeline/data:/opt/apache/beam/pipeline/data" apache-beam-json-to-csv

```

Acesse o terminal *bash* do contêiner 

```
docker exec -it beam_conteiner /bin/bash
```

Execute a pipeline 

```
python app.py
```

## Resultado esperado

### Verifique o arquivo csv gerado na pasta `pipeline/data/` ✨

![Captura de tela 2024-03-04 142926](https://github.com/AnaJuliaMM/pipeline_apache_beam/assets/123522605/56baadb7-1c2f-4c9e-91a2-4867d9f48a84)
