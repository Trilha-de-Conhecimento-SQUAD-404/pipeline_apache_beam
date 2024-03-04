# Pipeline de tranformação de dados
Este repositório contém um pipeline batch no Apache Beam, que transforma dados JSON em um arquivo CSV

Acesse a documentação: 🔗
- [Apache Beam](./wiki/apache.md)
- [Execução do Pipeline](./wiki/execucao.md)

## Estrutura do projeto: 
- `pipeline`: scripts para a criação do pipeline
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
![Captura de tela 2024-03-04 142926](https://github.com/AnaJuliaMM/pipeline_apache_beam/assets/123522605/56baadb7-1c2f-4c9e-91a2-4867d9f48a84)


