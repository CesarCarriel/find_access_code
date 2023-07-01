# Find Acess Code

## Problema:
Um método de segurança comum no banco eletrônico consiste em solicitar ao usuário três caracteres
aleatórios de um código de acesso. Por exemplo, se o código de acesso for 531278, eles podem solicitar o 2o,
3o e 5o caracteres; a resposta esperada seria: 317.

## Solução:
Esse projeto contém uma solução que analisa varios desses caracteres aleatorios usados para chegar o mais proximo de uma
codigo de acesso.

Ao executar o projeto ficará disponivel um endpoint Rest do tipo PUT para upload de um arquivo de texto com as entradas 
keylogs e internamente é executado um algoritmo que procura a chave de acesso e retorna no seguinte formato.

## Como executar o projeto:

### Instalar dependencias:

Para executar o projeto é necessario instalar o **Pipenv** utilizando o **pip** para instalação das dependecias do 
projeto:

```
pip install --user pipenv
```

Agora para instalar as dependencias do projeto, execute:

```
pipenv sync --dev
```

Após a instalação das dependencias serem concluídas execute o seguinte comando para ativar o seu virtualenv:

```
pipenv shell
```

### Iniciar o projeto:

Para subir o servidor flask execute o comando:

```
flask --app app run
```
 
Como executar usando o cURL:

```
curl -X PUT -T caminho_do_arquivo http://localhost:5000/upload/nome_do_arquivo.txt
```

Exemplo de resposta:

```json
{
  "access_code": "111111"
}
```

