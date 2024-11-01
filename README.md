# My ORM

Biblioteca simples que facilita o desenvolvimento simples de **CRUDs** usando Python.

___

## Sumário

**[`MyORM`](#MyORM): Documentação da biblioteca. <br>
....[`Sumário`](#Sumário): Sumário. <br>
....[`Estrutura`](#Estrutura): Estrutura em que o projeto está organizado. <br>
....[`Instalação`](#Instalação): Como instalar a biblioteca. <br>
....[`Primeiros passos`](#Primeiros-passos): Como configurar a classe MyORM. <br>
....[`Criar tabela`](#Criar-tabela): Como criar uma tabela usando métodos da biblioteca (CREATE). <br>
....[`Inserir dados`](#Inserir-dados): Como inserir registros em uma tabela usando métodos da biblioteca (INSERT). <br>
....[`Selecionar dados`](#Selecionar-dados): Como selecionar dados de uma tabela usando os métodos da biblioteca (SELECT). <br>
....[`Atualizar dados`](#Atualizar-dados): Como atualizar e modificar registros de uma tabela usando os métodos da biblioteca (UPDATE). <br>
....[`Deletar dados`](#Deletar-dados): Como deletar registros de uma tabela usando métodos da biblioteca (DELETE). <br>
....[`Alterar tabela`](#Alterar-tabela): Alterar propriedades das colunas de uma tabela usando os métodos da biblioteca (ALTER TABLE). <br>
....[`Condições`](#Condições): Condições para executar uma consulta SQL <br>
........[`WHERE`](#WHERE): Como utilizar a condição WHERE com as funções da biblioteca. <br>
........[`BETWEEN`](#BETWEEN): Como utilizar a condição BETWEEN com as funções da biblioteca. <br>
........[`AND`](#AND): Como usar a condição AND com as funções da biblioteca. <br>
........[`OR`](#OR): Como usar a condição OR com as funções da biblioteca. <br>
....[`Propriedades`](#Propriedades): Propriedades das colunas. <br>
........[`Tipos de dados`](#Tipos-de-dados): Tipos de dados que a coluna armazenará. <br>
............[`INTEGER`](#INTEGER): Definir uma coluna como INTEGER. <br>
............[`FLOAT`](#FLOAT): Definir uma coluna como FLOAT. <br>
............[`DECIMAL`](#DECIMAL): Definir uma coluna como DECIMAL. <br>
............[`DOUBLE`](#DOUBLE): Definir uma coluna como DOUBLE. <br>
............[`CHAR`](#CHAR): Definir uma coluna como CHAR. <br>
............[`VARCHAR`](#VARCHAR): Definir uma coluna como VARCHAR. <br>
............[`TEXT`](#TEXT): Definir uma coluna como TEXT. <br>
............[`BOOLEAN`](#BOOLEAN): Definir uma coluna como BOOLEAN. <br>
............[`DATE`](#DATE): Definir uma coluna como DATE. <br>
............[`DATETIME`](#DATETIME): Definir uma coluna como DATETIME. <br>
............[`TIMESTAMP`](#TIMESTAMP): Definir uma coluna como TIMESTAMP. <br>
........[`Restrições`](#Restrições): Restrições para colunas. <br>
............[`FOREIGN KEY`](#FOREIGN-KEY): Definir uma chave estrangeira. <br>
................[`ON UPDATE`](#ON-UPDATE): Definir evento atualizar a coluna. <br>
................[`ON DELETE`](#ON-DELETE): Definir evento deletar a coluna. <br>
............[`Outras restrições`](#Outras-restrições): Outras restrições. <br>
................[`DEFAULT`](#DEFAULT): Definir um valor padrão para a coluna. <br>
................[`NOT NULL`](#NOT-NULL): Não permitir registros com valores vazios. <br>
................[`AUTO_INCREMENT / SERIAL`](#AUTO_INCREMENT-ou-SERIAL)
: Definir uma coluna que define seu valor com base em uma sequência. <br>
................[`PRIMARY KEY`](#PRIMARY-KEY): Definir uma coluna cujo valor não pode ser repetido e nem vazio. <br>
................[`UNIQUE`](#UNIQUE): Definir uma coluna cujo valor não pode ser repetido mas pode ser vazio. <br>
................[`Restrições personalizadas`](#Restrições-personalizadas): Adicionar restrições que não são padrão da ORM. <br>
........[`Atributos`](#Atributos): Atributos que podem ser definos ao instanciar a classe `MyORM` que mudam o comportamento da ORM. <br>
....[`Exemplos de uso`](#Exemplos-de-uso): Exemplos mais completos de como usar a ORM. <br>
........[`SQLite`](#SQLite): Exemplos de uso com SQLite. <br>
........[`MySQL`](#MySQL): Exemplos de uso com MySQL. <br>
........[`Postgres`](#Postgres): Exemplos de uso com Postgres. <br>
....[`Licença, termos e direitos`](#Licença-de-Uso-Livre): Licença e termos de uso deste Projeto. <br>**

## Estrutura

```
my-orm/
|
|—— src/
|    |
|    |—— SQL/
|    |    |—— __init__.py
|    |    |—— manager.py
|    |    |—— sql_commands_alter_table.py
|    |    |—— sql_commands_cond.py
|    |    |—— sql_commands_create.py
|    |    |—— sql_commands_prop.py
|    |
|    |—— utils/
|    |    |—— __init__.py
|    |    |—— convert.py
|    |    |—— validate.py
|    |    |—— verify_tags.py
|    |
|    |—— __init__.py
|    |—— my_orm.py
|
|—— tests/
|    |—— __init__.py
|    |—— test_my_orm.py
|    |—— test_my_orm_exceptions.py
|    |—— test_sql_commands_alter_table.py
|    |—— test_sql_commands_cond.py
|    |—— test_sql_commands_create.py
|    |—— test_sql_commands_prop.py
|
|—— README.md
|—— requirements.txt
|—— setup.py
```

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
* postgres - Usa o `pg8000` como suporte.

____

## Primeiros passos

Importe todas as funcionalidades da biblioteca:

```python
from my_orm import *
```

Dependendo do SGDB escolhido, a configuração muda:

* SQLite:

    ```python
    orm = MyORM(
        dbs="sqlite", # nome do SGDB
        path="./database/dbs.db" # caminho para o arquivo
    )
    ```

* MySQL:

    ```python
    orm = MyORM(
        dbs="mysql", # nome do SGDB
        user="root", # nome de usuário
        password="", # senha de conexão
        host="localhost", # endereço para o servidor
        database="database_name", # nome do banco de dados
        port=3306 # porta de conexão (não é obrigatória)
    )
    ```

    Por padrão, para o MySQL **`port=3306`**.

* Postgres:

    ```python
    orm = MyORM(
        dbs="postgres", # nome do SGDB
        user="root", # nome de usuário
        password="", # senha de conexão
        host="localhost", # endereço para o servidor
        database="database_name", # nome do banco de dados
        port=5432 # porta de conexão (não é obrigatória)
    )
    ```

    Por padrão, para o Postgres **`port=5432`**.

    **Obs: É importante notar que ao utilizar o SGDB do `Postgres`, nomes de tabelas que possuam letras maiúsculas devem ser passados entre aspas duplas ("Table"). Exemplo:**
  
     ```python
     orm.make('"Users"'...)
     orm.get('"Users"'...)
     orm.edit('"Users"'...)
     orm.remove('"Users"'...)
     orm.edit_table('"Users"'...)
     orm.exe('DROP TABLE "Users";', require_tags=False)
     ```

**OBS: Após a definição do banco de dados, todos os métodos e funções são universais, independente do SGDB escolhido!**

**Veja mais atributos que podem ser definidos ao instanciar a classe `MyORM` em [`ATRIBUTOS`](#Atributos)**

____

## Criar tabela

Para criar tabelas utiliza-se o método **`MyORM.make()`:**

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

**Veja mais sobre `foreign key` e outras propriedades em [`PROPRIEDADES`](#Propriedades)**

___

## Inserir dados

Para inserir dados em uma tabela, usa-se o método **`MyORM.add()`:**

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
INSERT INTO Users (name, email) VALUES (?, ?);
```

**OBS: Inserir mais de um registro por vez não alteraria o código `SQL` em si, apenas na hora de executá-lo!**

**Nota-se que para inserir vários registros de uma vez, define-se uma chave (columns) como uma lista de colunas e uma chave (values) como uma lista com outras listas dentro. Caso a quantidade de valores seja diferente da quantidade de colunas, um erro será exibido!**

____

## Selecionar dados

Para selecionar dados é utilizado o método **`MyORM.get()`:**

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
    whe_("name = 'example'") # condição/condições opcional(is)
)
```

Este comando é o mesmo que:

```sql
SELECT * FROM Users;
```

ou

```sql
SELECT id FROM Users WHERE name = "example";
```

**O retorno deste método por padrão é em formato de dicionário. Esta funcionalidade pode ser desativada definindo o argumento `in_dict` como `False`:**

```python
orm.get(in_dict=False)
```

Desta forma, o retorno será no formado padrão do SGDB, geralmente em listas!

**OBS: Sempre deve-se informar as colunas (ou "all"), caso contrário resultará em erro!**

**Veja mais sobre WHERE (whe_()) e outras condições em [`CONDIÇÕES`](#Condições)**

____

## Atualizar dados

Para atualizar dados, é o utilizado o método **`MyORM.edit()`:**

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.edit(
    "Users", # nome da tabela
    whe_("name = 'User1'"), # condição/condições
    name = "User2" # alteração/alterações
)
```

Este comando equivale a:

```sql
UPDATE Users SET name = "User2" WHERE name = "User1";
```

**Por padrão, alterar registros exige uma condição para evitar alterar todos os registros por acidente. Esta funcionalidade pode ser desativada ao instanciar a classe MyORM:**

```python
# True permite / False não permite (padrão)
orm = MyORM(alter_all=True)
```

Desta forma, não será obrigatório uma condição!

**Esta funcionalidade também existe em [`DELETAR`](#Deletar-dados)**

**Veja mais atributos que podem ser definidos ao instanciar a classe `MyORM` em [`ATRIBUTOS`](#Atributos)**

**Veja mais sobre WHERE (whe_()) e outras condições em [`CONDIÇÕES`](#Condições)**

____

## Deletar dados

Para deletar dados, usa-se o método **`MyORM.remove()`:**

```pythom
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.remove(
    "Users", # nome da tabela
    whe_("id=1001") # condição/condições
)
```

Este comando é o mesmo que:

```sql
DELETE FROM Users WHERE id = 1001;
```

**Assim como em [`ATUALIZAR`](#Atualizar-dados), uma condição é obrigatória por padrão para evitar exclusão acidental! É possível desativar esta fucionalidade:**

```python
# True permite / False não permite (padrão)
orm = MyORM(alter_all=True)
```

Assim não será necessário executar com uma condição!

**Veja mais atributos que podem ser definidos ao instanciar a classe `MyORM` em [`ATRIBUTOS`](#Atributos)**

**Veja mais sobre WHERE (whe_()) e outras condições em [`CONDIÇÕES`](#Condições)**

____

## Alterar tabela

Para alterar uma tabela (colunas, propriedades...), utiliza-se o método **`MyORM.edit_table`:**

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

# adicionar uma coluna
orm.edit_table(
    "Users", # nome da tabela
    add("email", (varchar(30), prop("n_null", "uni")) # alteração
)
```

Este método equivale ao comando SQL:

```sql
ALTER TABLE Users ADD email VARCHAR(30) NOT NULL UNIQUE;
```

Outras alterações na tabela são:

* drop():

    Remover uma coluna
  
    ```python
    orm.edit_table(
        "Users",
        drop("email")
    )
    ```

* edit():

    Alterar propriedades de uma coluna

    ```python
    orm.edit_table(
        "Users",
        edit("email", (varchar(20), prop("n_null")))
    )
    ```

* ren_column():

    Renomear uma coluna

    ```python
    orm.edit_table(
        "Users",
        ren_column("old_name", "new_name")
    )
    ```

* rename():
 
    Renomear uma tabela

  ```python
  orm.edit_table(
      "Users",
      rename("users")
  )
  ```

**Veja mais sobre `foreign key` e outras propriedades em [`PROPRIEDADES`](#Propiedades)**

____

## Condições

As condições desta **ORM** são, no geral, simplificadas para facilitar a organização do script final.

Caso o [`atributo`](#Atributos) `alter_all` esteja `True`, uma condição se torna **OBRIGATÓRIA**!

____

### WHERE

A condição `WHERE` pode ser declarada utilizando a função `whe_()`:

```python
whe_("id = 0")
whe_("name = 'User1'")
```

Note que para passar strings, usa-se aspas, simples ou duplas (neste caso simples) e para passar inteiros não utiliza-se nada!

O retorno desta função seria:

```sql
WHERE id = 0;
```

ou

```sql
WHERE name = "User1";
```

**Caso você queira verificar se um valor está em uma lista de outros valores, como no caso da condição [`IN`](#IN), basta usar a função assim:**

```python
whe_("classification", "'tag1', 'tag2'")
```

Esquivale à:

```sql
WHERE classification IN ('tag1', 'tag2');
```

**Estrutura:**

```python
whe_(condition: str, cond_in: Optional[str]=None)

# condition = condição
# cond_in = quando a condição está dentro de um IN
```

____

### BETWEEN

Para usar a condição `BETWEEN`, utiliza-se a função `betw_()` dentro das condição [`WHERE`](#WHERE), [`AND`](#AND) e/ou [`OR`](#OR):

```python
whe_(betw_("age", 10, 15))
```

O resultado deste comando seria:

```sql
WHERE age BETWEEN 10 AND 15;
```

**Estrutura:**

```python
betw_(column: str, par1, par2)

# column = nome da coluna verificada
# par1 e par2 = parâmetros que a coluna verificada deve estar
```

### AND

Para utilizar a condição `AND`, a função `and_()` é utilizada:

```python
and_("id = 0")
and_("name = 'User1'")
```

Note que para passar strings, usa-se aspas, simples ou duplas (neste caso simples) e para passar inteiros não utiliza-se nada!

O retorno desta função seria:

```sql
AND id = 0;
```

ou

```sql
AND name = "User1";
```

**Caso você queira verificar se um valor está em uma lista de outros valores, como no caso da condição [`IN`](#IN), basta usar a função assim:**

```python
and_("classification", "'tag1', 'tag2'")
```

Esquivale à:

```sql
AND classification IN ('tag1', 'tag2');
```

**Estrutura:**

```python
and_(condition: str, cond_in: Optional[str]=None)

# condition = condição
# cond_in = quando a condição está dentro de um IN
```

____

### OR

Para utilizar a condição `OR`, a função `or_()` é utilizada:

```python
or_("id = 0")
or_("name = 'User1'")
```

Note que para passar strings, usa-se aspas, simples ou duplas (neste caso simples) e para passar inteiros não utiliza-se nada!

O retorno desta função seria:

```sql
OR id = 0;
```

ou

```sql
OR name = "User1";
```

**Caso você queira verificar se um valor está em uma lista de outros valores, como no caso da condição [`IN`](#IN), basta usar a função assim:**

```python
or_("classification", "'tag1', 'tag2'")
```

Esquivale à:

```sql
OR classification IN ('tag1', 'tag2');
```

**Estrutura:**

```python
or_(condition: str, cond_in: Optional[str]=None)

# condition = condição
# cond_in = quando a condição está dentro de um IN
```

____

## Propriedades

Propriedades que podem ser atribuídas à colunas ([`tipos de dados`](#Tipos-de-dados) / [`Restrições`](#Restrições)).

**Obs: com exceção de [`PRIMARY KEY`](#PRIMARY-KEY), todas propriedades devem estar dentro de uma tupla!**

____

### Tipos de dados

Indica qual será o tipo de dado que uma coluna receberá.

#### INTEGER

Definir uma coluna como INTEGER ao criar ou editar uma tabela usa-se `integer()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    id = (integer())
)
```

____

#### FLOAT

Definir uma coluna como FLOAT ao criar ou editar uma tabela usa-se `t_float()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    height = (t_float())
)
```

____

#### DECIMAL

Definir uma coluna como DECIMAL ao criar ou editar uma tabela usa-se `decimal()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    balance = (decimal(10, 2))
)
```

Nota-se que decimal() recebe dois parâmetros: 
```python
decimal(precision: int, scale: int)

# precision: indica quantos dígitos terão no número armazenado
# scale: indica quantos dígitos terão após o ponto decimal
```

____

#### DOUBLE

Definir uma coluna como DOUBLE ao criar ou editar uma tabela usa-se `double()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    weight = (double())
)
```

____

#### CHAR

Definir uma coluna como CHAR ao criar ou editar uma tabela usa-se `char()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    cpf = (char(11))
)
```

char() recebe um parâmetro:
```python
char(length: int)

# length: quantidade fixa de caractéres que terão no dado armazenado
```

____

#### VARCHAR

Definir uma coluna como VARCHAR ao criar ou editar uma tabela usa-se `varchar()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    name = (varchar(100))
)
```

varchar() recebe um parâmetro:
```python
varchar(max_length: int)

# max_length: quantidade máxima de caractéres que terão no dado armazenado
```

____

#### TEXT

Definir uma coluna como TEXT ao criar ou editar uma tabela usa-se `text()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    address = (text())
)
```

____

#### BOOLEAN

Definir uma coluna como BOOLEAN ao criar ou editar uma tabela usa-se `boolean()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    status = (boolean())
)
```

____

#### DATE

Definir uma coluna como DATE ao criar ou editar uma tabela usa-se `date()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    creation = (date())
)
```

____

#### DATETIME

Definir uma coluna como DATETIME ao criar ou editar uma tabela usa-se `datetime()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    creation = (datetime())
)
```

____

#### TIMESTAMP

Definir uma coluna como TIMESTAMP ao criar ou editar uma tabela usa-se `timestamp()`:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    creation = (timestamp())
)
```

____

### Restrições

Restrições para inserir um novo registro:

#### FOREIGN KEY

Para adicionar uma chave estrangeira usa-se o parâmetro f_key:

```python
orm = MyORM(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Orders",
    user_id = (integer(), prop("n_null")),
    id = (integer(), prop("pri_key")),
    f_key("user_id", "Users(id)")
)
```

`f_key` recebe uma tupla onde: <br>
* O primeiro item é o referenciador.
* O segundo item é o referenciado, ele é definido por uma string no formato "table(column)".

`f_key` ainda pode receber mais dois itens:

##### ON UPDATE

Podendo ser o terceiro ou quarto item de [`f_key`](#FOREIGN-KEY), ON UPDATE pode ser definido por `on_up()`:

```python
f_key = ("user_id", "Users(id)", on_up("cascade"))
```

____

##### ON DELETE

Também podendo ser o terceiro ou quarto item de [`f_key`](#FOREIGN-KEY), ON DELETE pode ser definido por `on_del()`:

```python
f_key = ("user_id", "Users(id)", on_del("cascade"))
```

Ambos podem ser usados juntos!

O resultado destas funções seria:

```sql
FOREIGN KEY user_id REFERENCES Users(id) ON UPDATE CASCADE ON DELETE CASCADE;
```

____

### Outras restrições

As outras restrições são utilizadas usando a função `prop()`:

```python
orm = my_orm(dbs="sqlite", url="./database/dbs.db")

orm.make(
    "Users",
    id = (prop("pri_key"))
)
```

**Todos as restrições passadas por `prop()` são abreviadas. Veja:**

____

#### DEFAULT

Default é o único que é passado como parâmetro:

```python
prop(default="undefined")
```

____

#### NOT NULL

NOT NULL é passado por `"n_null"`:

```python
prop("n_null")
```

____

#### AUTO_INCREMENT ou SERIAL

AUTO_INCREMENT é passado por `"auto"`:

```python
prop("auto")
```

**Obs: `SQLite` não possui o comando `AUTO_INCREMENT` e caso seja usado com `Postgres` será alterado para `SERIAL` automaticamente.**

____

#### PRIMARY KEY

PRIMARY KEY é passado por `"pri_key"`:

```python
prop("pri_key")
```

____

#### CURRENT_TIMESTAMP

CURRENT_TIMESTAMP é passado por `"current"`:

```python
prop("current")
```

____

#### UNIQUE

UNIQUE é passado por `"uni"`:

```python
prop("uni")
```

____

#### Restrições personalizadas

É possível passar qualquer outras restrição usando `prop()`.

```python
prop("bigserial")

# BIGSERIAL não é um comando padrão da ORM
```

O retorno seria:

```sql
BIGSERIAL
```

Note que já fica com as letras maiúsculas automaticamente!

____

É possível passar várias restrições de uma só vez:

```python
prop("uni", "n_null", default=0)
```

____

## Atributos

Ao instanciar a classe `MyORM()`, é possível definir alguns atributos dependendo das necessidades do usuário:

* sql_return:

    Quando `True` retorna o comando SQL que será gerado pela classe.

    ```python
    orm = MyORM(sql_return=True/False)

    # por padrão, sql_return=False
    ```

* execute:

    Quando `False` não executa os comandos gerados.

    ```python
    orm = MyORM(execute=True/False)

    # por padrão, execute=True
    ```

* return_dict:

    Quando `True` permite que o método [`SELECT`](#Selecionar-dados) retorne a consulta em formato de dicionário.

    ```python
    orm = MyORM(return_dict=True/False)

    # por padrão, return_dict=True
    ```

* require_tags:

    Quando `True` exige que os comandos possuam tags de segurança, o que pode dificultar `injeções de SQL`.

    ```python
    orm = MyORM(require_tags=True/False)

    # por padrão, require_tags=True
    ```

* alter_all:

    Quando `False` impede que haja alterações nos registros sem [`Condições`](#Condições).

    ```python
    orm = MyORM(alter_all=True/False)

    # por padrão, alter_all=False
    ```

___

## Exemplos de uso

Exemplos mais completos de como usar a ORM:

### SQLite

```python
from my_orm import * # importa todas a funcionalidades da ORM
from env import * # importa os dados de configuração do servidor / banco de dados
from random import randint # importa uma função para aleatorizar registros e evitar conflitos


# gera dois valores "aleatórios" e soma-os
random_value = randint(1000, 9999) + randint(1000, 9999)


# configuração da ORM
orm = MyORM(
    dbs = "sqlite",
    path = SQLITE_PATH
)


# criar uma tabela
orm.make(
    "Clients", # nome da tabela
    
    # colunas = (tipo de dado + restrições)
    id = (integer(), prop("pri_key")),
    name = (varchar(100), prop("n_null")),
    email = (varchar(100), prop("uni", "n_null")),
    phone = (integer(), prop("uni", "n_null")),
    password = (varchar(150), prop("n_null")),
    adress = (text(), prop("n_null")),
    register_date = (timestamp(), prop(default="current"))
)


# adicionar um registro na tabela
orm.add(
    "Clients", # nome da tabela
    
    # coluna = valor
    name = f"Client{random_value}",
    email = f"client{random_value}@example.com",
    phone = 100001 + random_value,
    password = f"client{random_value}",
    adress = f"st. {random_value}"
)


# adicionar mais de um registro na tabela
orm.add(
    "Clients", # nome da tabela
    
    # column = lista[colunas]
    columns = ["name", "email", "phone", "password", "adress"],
    
    #values = lista[lista[valores]]
    values = [
        [
            f"{random_value}_Client", 
            f"{random_value}client@ex.com", 
            random_value + 100002, 
            f"{random_value}client", 
            f"St. {random_value}"
        ],
        [
            f"{random_value + 1}_Client", 
            f"{random_value + 1}client@ex.com", 
            random_value + 100003, 
            f"{random_value + 1}client", 
            f"St. {random_value + 1}"
        ],
        [
            f"{random_value + 2}_Client", 
            f"{random_value + 2}client@ex.com", 
            random_value + 100004, 
            f"{random_value + 2}client", 
            f"St. {random_value + 2}"
        ]
    ]
)


# retornar todos os registros de uma tabela
resp = orm.get(
    "Clients" # nome da tabela
)

print(resp)


# retornar registro específico de uma tabela
resp = orm.get(
    "Clients", # nome da tabela
    
    "all", # colunas retornadas
    
    # condições
    whe_("id > 1"), and_("id < 10")
)

print(resp)


# retornar coluna específica de uma tabela
resp = orm.get(
    "Clients", # nome da tabela
    
    # columns = lista[colunas]
    columns = ["id", "name", "email"]
)
print(resp)


# atualizar dados de uma tabela
orm.edit(
    "Clients", # nome da tabela
    
    # condições (por padrão obrigatória / pode ser alterada)
    whe_("id = 1"), or_("name = 'paulindavzl'"),
    
    # coluna = novo valor
    name = "ClientVIP"
)


# deletar dados de uma tabela
orm.remove(
    "Clients", # nome da tabela
    
    # condições (por padrão obrigatória / pode ser alterada)
    whe_("id > 0")
)


# alterar dados de uma tabela
orm.edit_table(
    "Clients", # nome da tabela
    
    # alteração
    rename("Users")
)


# apagar uma tabela do banco de dados (função específica no futuro)
orm.exe("DROP TABLE Users", require_tags=False)
```

____

### MySQL

```python
from my_orm import * # importa todas a funcionalidades da ORM
from env import * # importa os dados de configuração do servidor / banco de dados
from random import randint # importa uma função para aleatorizar registros e evitar conflitos


# gera dois valores "aleatórios" e soma-os
random_value = randint(1000, 9999) + randint(1000, 9999)


# configuração da ORM
orm = MyORM(
    dbs = "mysql",
    user = MYSQL_USER,
    password = MYSQL_PASS,
    host = MYSQL_HOST,
    database = MYSQL_DB
)


# criar uma tabela
orm.make(
    "Clients", # nome da tabela
    
    # colunas = (tipo de dado + restrições)
    id = (integer(), prop("auto", "pri_key")),
    name = (varchar(100), prop("n_null")),
    email = (varchar(100), prop("uni", "n_null")),
    phone = (integer(), prop("uni", "n_null")),
    password = (varchar(150), prop("n_null")),
    adress = (text(), prop("n_null")),
    register_date = (timestamp(), prop(default="current"))
)


# adicionar um registro na tabela
orm.add(
    "Clients", # nome da tabela
    
    # coluna = valor
    name = f"Client{random_value}",
    email = f"client{random_value}@example.com",
    phone = 100001 + random_value,
    password = f"client{random_value}",
    adress = f"st. {random_value}"
)


# adicionar mais de um registro na tabela
orm.add(
    "Clients", # nome da tabela
    
    # column = lista[colunas]
    columns = ["name", "email", "phone", "password", "adress"],
    
    #values = lista[lista[valores]]
    values = [
        [
            f"{random_value}_Client", 
            f"{random_value}client@ex.com", 
            random_value + 100002, 
            f"{random_value}client", 
            f"St. {random_value}"
        ],
        [
            f"{random_value + 1}_Client", 
            f"{random_value + 1}client@ex.com", 
            random_value + 100003, 
            f"{random_value + 1}client", 
            f"St. {random_value + 1}"
        ],
        [
            f"{random_value + 2}_Client", 
            f"{random_value + 2}client@ex.com", 
            random_value + 100004, 
            f"{random_value + 2}client", 
            f"St. {random_value + 2}"
        ]
    ]
)


# retornar todos os registros de uma tabela
resp = orm.get(
    "Clients" # nome da tabela
)

print(resp)


# retornar registro específico de uma tabela
resp = orm.get(
    "Clients", # nome da tabela
    
    "all", # colunas retornadas
    
    # condições
    whe_("id > 1"), and_("id < 10")
)

print(resp)


# retornar coluna específica de uma tabela
resp = orm.get(
    "Clients", # nome da tabela
    
    # columns = lista[colunas]
    columns = ["id", "name", "email"]
)
print(resp)


# atualizar dados de uma tabela
orm.edit(
    "Clients", # nome da tabela
    
    # condições (por padrão obrigatória / pode ser alterada)
    whe_("id = 1"), or_("name = 'paulindavzl'"),
    
    # coluna = novo valor
    name = "ClientVIP"
)


# deletar dados de uma tabela
orm.remove(
    "Clients", # nome da tabela
    
    # condições (por padrão obrigatória / pode ser alterada)
    whe_("id > 0")
)


# alterar dados de uma tabela
orm.edit_table(
    "Clients", # nome da tabela
    
    # alteração
    rename("Users")
)


# apagar uma tabela do banco de dados (função específica no futuro)
orm.exe("DROP TABLE Users", require_tags=False)
```

____

### Postgres

```python
from my_orm import * # importa todas a funcionalidades da ORM
from env import * # importa os dados de configuração do servidor / banco de dados
from random import randint # importa uma função para aleatorizar registros e evitar conflitos


# gera dois valores "aleatórios" e soma-os
random_value = randint(1000, 9999) + randint(1000, 9999)


# configuração da ORM
orm = MyORM(
    dbs = "postgres",
    user = POSTGRES_USER,
    password = POSTGRES_PASS,
    host = POSTGRES_HOST,
    database = POSTGRES_DB
)


# criar uma tabela
orm.make(
    '"Clients"', # nome da tabela
    
    # colunas = (tipo de dado + restrições)
    id = (prop("auto", "pri_key")),
    name = (varchar(100), prop("n_null")),
    email = (varchar(100), prop("uni", "n_null")),
    phone = (integer(), prop("uni", "n_null")),
    password = (varchar(150), prop("n_null")),
    adress = (text(), prop("n_null")),
    register_date = (timestamp(), prop(default="current"))
)


# adicionar um registro na tabela
orm.add(
    '"Clients"', # nome da tabela
    
    # coluna = valor
    name = f"Client{random_value}",
    email = f"client{random_value}@example.com",
    phone = 100001 + random_value,
    password = f"client{random_value}",
    adress = f"st. {random_value}"
)


# adicionar mais de um registro na tabela
orm.add(
    '"Clients"', # nome da tabela
    
    # column = lista[colunas]
    columns = ["name", "email", "phone", "password", "adress"],
    
    #values = lista[lista[valores]]
    values = [
        [
            f"{random_value}_Client", 
            f"{random_value}client@ex.com", 
            random_value + 100002, 
            f"{random_value}client", 
            f"St. {random_value}"
        ],
        [
            f"{random_value + 1}_Client", 
            f"{random_value + 1}client@ex.com", 
            random_value + 100003, 
            f"{random_value + 1}client", 
            f"St. {random_value + 1}"
        ],
        [
            f"{random_value + 2}_Client", 
            f"{random_value + 2}client@ex.com", 
            random_value + 100004, 
            f"{random_value + 2}client", 
            f"St. {random_value + 2}"
        ]
    ]
)


# retornar todos os registros de uma tabela
resp = orm.get(
    '"Clients"' # nome da tabela
)

print(resp)


# retornar registro específico de uma tabela
resp = orm.get(
    '"Clients"', # nome da tabela
    
    "all", # colunas retornadas
    
    # condições
    whe_("id > 1"), and_("id < 10")
)

print(resp)


# retornar coluna específica de uma tabela
resp = orm.get(
    '"Clients"', # nome da tabela
    
    # columns = lista[colunas]
    columns = ["id", "name", "email"]
)
print(resp)


# atualizar dados de uma tabela
orm.edit(
    '"Clients"', # nome da tabela
    
    # condições (por padrão obrigatória / pode ser alterada)
    whe_("id = 1"), or_("name = 'paulindavzl'"),
    
    # coluna = novo valor
    name = "ClientVIP"
)


# deletar dados de uma tabela
orm.remove(
    '"Clients"', # nome da tabela
    
    # condições (por padrão obrigatória / pode ser alterada)
    whe_("id > 0")
)


# alterar dados de uma tabela
orm.edit_table(
    '"Clients"', # nome da tabela
    
    # alteração
    rename('"Users"')
)


# apagar uma tabela do banco de dados (função específica no futuro)
orm.exe('DROP TABLE "Users"', require_tags=False)
```

___

**Todos estes exemplos de usos foram testados e até a versão `1.0.0` estão funcionando corretamente!**

____

## Licença de Uso Livre

Este projeto é 100% livre e pode ser usado, modificado e distribuído por qualquer pessoa para qualquer propósito, sem restrições.

### Termos

1. **Uso e Distribuição**  
   Você é livre para usar, modificar, distribuir e realizar qualquer outra ação com este projeto, seja para fins comerciais ou pessoais.

2. **Sem Garantias**  
   Este projeto é fornecido "como está", sem garantias de qualquer tipo, explícitas ou implícitas. Os autores não serão responsáveis por quaisquer danos ou perdas decorrentes do uso deste software.

3. **Atribuição Opcional**  
   Embora não seja obrigatório, a atribuição ao autor original deste projeto é sempre bem-vinda e apreciada.

### Direitos do Usuário

Todos os direitos são concedidos aos usuários deste projeto, sem qualquer limitação.

---

**Nota**: Esta licença foi criada para ser o mais aberta e permissiva possível. Sinta-se à vontade para usar e modificar conforme necessário.
