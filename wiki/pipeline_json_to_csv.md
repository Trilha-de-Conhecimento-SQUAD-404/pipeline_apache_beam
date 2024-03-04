
# Explicação do Pipeline de Transformação de dados

Neste documento, vamos discutir sobre a estrutura e funcionamento do pipeline de transformação de dados de JSON para CSV com o Apache Beam. 

## Contexto: 
Antes de entrarmos nos detalhes do pipeline em si, é importante entendermos o contexto em que ela opera.


###  [Public APIs](https://api.publicapis.org/entries):
A API public API oferece acesso a uma lista abrangente de outras APIs públicas disponíveis na internet. Ao acessa-lá, os desenvolvedores podem obter informações sobre diversas APIs disponíveis, como seus nomes, descrições, categorias, URLs base, entre outros detalhes relevantes. Nesse projeto, essa API constitui-se como a origem dos dados.

### Função *Pardo* 
A função usada para fazer a requisição para a API é conhecida como ParDo, abreviação de "Parallel Do". Essa função é capaz de processar dados em paralelo, o que significa que pode executar várias tarefas ou operações simultaneamente. No contexto do pipeline de dados, o ParDo é utilizado para aplicar uma transformação em **cada elemento JSON** da lista de dados de forma independente e paralela.

<img width="100" alt="image" src="https://github.com/AnaJuliaMM/pipeline_apache_beam/blob/feature/creating_wiki/wiki/media/others/pardo.png">

## Fluxo de trabalho
Este código utiliza o Apache Beam para criar um pipeline de transformação de dados. O pipeline inclui uma etapa em que os dados são obtidos através de uma função ParDo, que transforma o formato dos dados de JSON para CSV. Em seguida, os dados transformados são gravados em um arquivo CSV chamado "public_apis"

## Código

### 1. App 
Cria o objeto Pipeline e estrutura as seguintes tarefas:
1. Cria uma instância do Pipeline Apache Beam
2. Obtém uma lista de objetos JSON
3. Transforma cada objeto JSON para CSV
4. Grava os dados transformados em um arquivo CSV chamado "public_apis"
<img width="900" alt="image" src="https://github.com/AnaJuliaMM/pipeline_apache_beam/blob/feature/creating_wiki/wiki/media/code/app-img.png">

### 2. ParDo

Neste código a classe PublicApis estende a classe DoFn, e realiza uma requisição HTTP para uma API pública, extrai os dados JSON e retorna cada API individualmente para o pipeline do Apache Beam, tratando os erros adequadamente e registrando as informações no log, no arquivo "json_to_csv.log"
<img width="900" alt="image" src="https://github.com/AnaJuliaMM/pipeline_apache_beam/blob/feature/creating_wiki/wiki/media/code/pardo-img.png">


### 3. Method
Esse código define uma função chamada `json_to_csv_row` que é chamada pelo PTransform Map para transformar um objeto JSON em uma linha em formato CSV e retorna essa linha como uma string

Por exemplo, se o objeto JSON fosse:
 ```
{
 "nome": "João",
 "idade": 30,
 "cidade": "São Paulo"
 }
```

A função retornaria uma string CSV como 
```
"João,30,São Paulo"
```
<img width="900" alt="image" src="https://github.com/AnaJuliaMM/pipeline_apache_beam/blob/feature/creating_wiki/wiki/media/code/method-img.png">

### 4. Resultado
https://github.com/AnaJuliaMM/pipeline_apache_beam/assets/123522605/48d23ed0-fb43-43bd-81b6-82932d4b2336

## Conclusão 

Esperamos que esta explicação tenha fornecido uma compreensão clara da estrutura e do funcionamento deste fluxo de trabalho específico, que utiliza o pipeline de transformação de dados do Apache Beam para processar uma lista de objetos JSON provenientes da API Public APIs e transformar em um arquivo  CSV. 😄
