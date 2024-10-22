# My ORM
Biblioteca simples que facilita o desenvolvimento simples de **CRUDs** usando Python.

____

## Instalação

* Clonando o repositório

```bash
$ git clone git@github.com:paulindavzl/my-orm.git
$ pip install -r requirements.txt
```

Ou

```bash
$ pip install -e .[SGDB]
```

* Utilizando o PIP INSTALL

```bash
$ pip install my-orm[SGDB]
```

**Instalar usando `pip install -e .[SGDB]` ou  `pip install my-orm[SGDB]`é recomendado porque a biblioteca se comporta melhor!**

**O 'SGDB' é qual sistema será utilizado. Esta biblioteca tem suporte para:**

* sqlite - Usa o `sqlite3` como suporte.
* mysql - Usa o `mysql-connector-python` como suporte.
* postgres - Usa o `psycopg2-binary` como suporte.

____

## Primeiros passos

Importe todas as funcionalidades da biblioteca:

```python
from my_orm import *
```

Dependendo do SGDB escolhido, a configuração muda:

* SQLITE:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")
```

**_dbs_** é o tipo de SGDB

**_url_** é o caminho para o arquivo

**OBS: Após a definição do banco de dados, todos os métodos e funções são universais, independente do SGDB escolhido!**

**Veja mais atributos que podem ser definidos ao instanciar a classe `MyORM` em [`ATRIBUTOS`](##Atributos)**

____

## Criar tabela

Para criar tabelas utiliza-se o método **`MyORM.make()`**:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")
orm.make(
    "Order", # nome da tabela
    id = (integer(), prop("pri_key")), # nome da coluna = tipo/propriedade
    user_id = (integer(), prop("n_null")), # nome da coluna = tipo/propriedade
    f_key = ("user_id", "Users(id)") # chave estrageira define-se usando f_key = (chave estrangeira, tabela(chave primária))   
)
```

O resultado deste método seria:

```sql
CREATE TABLE IF NOT EXISTS
    Order(
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    );
```

**Veja mais sobre `foreign key` e outras propriedades em [`PROPRIEDADES`](##Propiedades)**

___

## Inserir

Para inserir dados em uma tabela, usa-se o método **`MyORM.add()`**:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

# adicionar somente um registro por vez
orm.add(
    "Users", # nome da tabela
    name = "Example", # coluna = "valor"
    email = "ex@example.com" # coluna = "valor"
)

# adicionar vários registros de uma vez
orm.add(
    "Users", # nome da tabela
    columns = ["name", "email"], # chave columns = lista[colunas]
    values = [["Example1", "ex1@example.com"], ["Example2", "ex2@example.com"]] # chave values = lista[lista[valores]]
)
```

O resultado deste método seria:

```sql
INSERTO INTO Users (name, email) VALUES (?, ?);
```

**OBS: Inserir mais de um registro por vez não alteraria o código `SQL` em si, apenas na hora de executá-lo!**

**Nota-se que para inserir vários registros de uma vez, define-se uma chave (columns) como uma lista de colunas e uma chave (values) como uma lista com outras listas dentro. Caso a quantidade de valores seja diferente da quantidade de colunas, um erro será exibido!**

____

## Selecionar

Para selecionar dados é utilizado o método **`MyORM.get()`**:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

# selecionar todas as colunas
orm.get(
    "Users", # nome da tabela
    "all", # todas as colunas
)

# selecionar colunas específicas
orm.get(
    "Users", # nome da tabela
    columns = ["id"], # coluna(s) que serão retornadas, podem ter o parâmetro columns ou não
    whe_("name = 'example'") # condição, opcional
)
```

**O retorno deste método por padrão é em formato de dicionário. Esta funcionalidade pode ser desativada definindo o argumento `in_dict` como `False`:**

```python
orm.get(in_dict=False)
```

Desta forma, o retorno será no formado padrão do SGDB, geralmente em listas!

**OBS: Sempre deve-se informar as colunas (ou "all"), caso contrário resultará em erro!**

**Veja mais sobre WHERE (whe_()) e outras condições em [`CONDIÇÕES`](##Condições)**

## Atualizar

Para atualizar dados, é o utilizado o método **`MyORM.edit()`**:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.edit(
    "Users", # nome da tabela
    whe_("name = 'User1'"), # condição/condições
    name = "User2" # alteração/alterações
)
```

**Por padrão, alterar registros exige uma condição para evitar alterar todos os registros por acidente. Esta funcionalidade pode ser desativada ao instanciar a classe MyORM:**

```python
# True permite / False não permite (padrão)
orm = MyORM(alter_all=True)
```

Desta forma, não será obrigatório uma condição!

**Este atributo também é válido no método [`DELETE`](##Deletar)**

**Veja mais atributos que podem ser definidos ao instanciar a classe `MyORM` em [`ATRIBUTOS`](##Atributos)**

**Veja mais sobre WHERE (whe_()) e outras condições em [`CONDIÇÕES`](##Condições)**
