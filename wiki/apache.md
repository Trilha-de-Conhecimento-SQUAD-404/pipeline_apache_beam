# Apache Beam
O Apache Beam é um modelo de programação unificado de código aberto para pipelines de processamento de dados em lote e em streaming que simplifica a dinâmica de processamento de dados em grande escala.

### Vantagens ✅

- É uma tecnologia versátil que oferece suporte as seguintes linguagens de programação: Java, Python, Go
- Conta com uma variedade de executores de pipeline (runners), permitindo que os usuários escolham a melhor opção para suas necessidades de execução.
- Capacidade de integrar dados de diversas fontes, proporcionando uma flexibilidade maior no desenvolvimento de pipelines de processamento de dados.

<img width="600" alt="image" src="https://github.com/AnaJuliaMM/pipeline_apache_beam/blob/feature/creating_wiki/wiki/media/apache/beam_img2.png">


## Arquitetura

### 1. Beam SDK (Software Development Kit)
O SDK do Beam, ou Kit de Desenvolvimento de Software do Beam, é um conjunto de ferramentas e bibliotecas específicas de uma linguagem de programação que permite aos desenvolvedores criar pipelines de processamento de dados usando o Apache Beam. Ele fornece APIs para definir fontes de dados, transformações e saídas, além de oferecer suporte para execução em diferentes runners (executores) de pipeline.
Atualmente, o Apache Beam possue as seguintes SDKs:
- Java SDK
- Python SDK
- GO SDK

### 2. Ferramentas de execução (Runners)
São os componentes responsáveis por executar os pipelines em um sistema de processamento de dados definidos com o Apache Beam. Existem diferentes ferramentas de execução disponíveis, como:
- Direct Runner (para execução local)
- Apache Flink
- Apache Spark
- Google Cloud Dataflow
- entre outros.


![diagrama](./media/apache/beam_img.png)

## Conceitos

### 1. Pipeline

O Pipeline é um objeto no Apache Beam que encapsula todas as tarefas de processamento de dados, do início ao fim. Isso inclui a leitura de dados de entrada, a transformação desses dados e a gravação de dados de saída.

- **Pipeline Linear**
![image](https://github.com/AnaJuliaMM/pipeline_apache_beam/assets/123522605/d3bad427-6f4e-4f04-99c9-0ea44485a11c)

- **Pipeline Ramificada**
  ![image](https://github.com/AnaJuliaMM/pipeline_apache_beam/assets/123522605/65bdfb8f-3e45-4c57-aaaa-9644b528b7cd)

### 2. PCollection

Um "PCollection" representa um conjunto de dados distribuídos no qual o pipeline do Apache Beam opera. Esse conjunto de dados pode ser limitado, originando-se de uma fonte fixa como um arquivo, ou ilimitado, vindo de uma fonte de atualização contínua (streaming). Os "PCollections" são as entradas e saídas de cada etapa do pipeline.

### 3. PTransform

Uma "PTransform" representa uma operação de processamento de dados, ou uma etapa, em seu pipeline. Todo "PTransform" recebe um ou mais PCollection objetos como entrada, executa uma função de processamento, e produz zero ou mais PCollectionobjetos de saída.


## [Exemplo de Pipeline no Apache Beam](./execucao.md)
Temos um exemplo de pipeline de tranformação de dados escrita utilizando o Apache Beam com execução local. Esse pipeline recebe dados JSON de uma API  e os transforma em um arquivo CSV.
