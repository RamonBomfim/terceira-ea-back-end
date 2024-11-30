# Instruções para instalação do projeto

## 1. Primeiro de tudo, faça o clone

```shell
  git clone https://github.com/RamonBomfim/terceira-ea-back-end.git
```

## 2. Crie uma virtual env com o python

Abra seu terminal e navegue até o projeto que acabou de clonar

```shell
  cd terceira-ea-back-end
```

Em seguida, use o comando:

```shell
  python -m venv venv
```

Com esse comando, você acabou de criar uma virtual env cahamada **venv**.

### 2.1. Ativando a virtual env

Se estiver usando Windows, basta usar o comando a seguir no seu terminal:

```shell
  .\venv\Scripts\Activate.ps1
```

Caso esteja utilizando Linux ou MacOS:

```shell
  source venv/bin/activate
```

## 3. Instalar os libs

Para instalar as bibliotecas/frameworks, basta utilizar o comando:

```shell
  pip install -r requirements.txt
```

## 4. Preparando para rodar o projeto

Antes de rodar o projeto, é preciso criar as migrations. Para isso, execute os seguintes comandos:

Supondo que você está dentro da pasta 'terceira-ea-back-end

```shell
  cd api_project
```

Em seguida, vamos criar as migrations

```shell
  python manage.py makemigrations
```

E por fim, executar as migrations criadas

```shell
  python manage.py migrate
```

Pronto, estamos prontos para rodar o projeto.

## 5. Rodando o projeto e consumindo as rotas

Para rodar o projeto, basta executar:

```shell
  python manage.py runserver
```

O projeto será iniciado em **http://127.0.0.1:8000**

### Testando as rotas

A primeira rota a ser testada contém dados fixos que correspondem ao **Passo 3** do exercício proposto.

Acesse a rota: `usuarios-fixos/` e verá o retorno:

```json
{
  "usuarios": [
    {
      "nome": "Carlos",
      "email": "carlos@email.com"
    },
    {
      "nome": "João",
      "email": "joão@email.com"
    }
  ]
}
```

As demais rotas, são referentes ao **Passo 4** do exercício proposto.

Acessando a rota: `register/` será possível registrar um novo usuário. Para isso, envie uma requisição do tipo **POST**, contendo:

```json
{
    "username": "novo_usuario",
    "password": "senha123",
    "email": "usuario@email.com"
}
```

Caso a requisição seja enviada com sucesso, a seguinte mensagem aparecerá:

```json
{
    "message": "User created successfully"
}
```

Para testar se de fato o JWT foi criado para o usuário recém criado, você deve enviar uma requisição do tipo **POST**
para a rota `api/token/`, contendo:

```json
{
    "username": "novo_usuario",
    "password": "senha123"
}
```

Caso a requisição seja enviada com sucesso, a seguinte mensagem aparecerá:

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```