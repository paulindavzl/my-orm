# My ORM

Biblioteca simples que facilita o desenvolvimento simples de **CRUDs** usando Python.

___

## Sumário

**[`MyORM`](#MyORM): Documentação da biblioteca. <br>
..........[`Sumário`](#Sumário): Sumário. <br>
..........[`Estrutura`](#Estrutura): Estrutura em que o projeto está organizado. <br>
..........[`Instalação`](#Instalação): Como instalar a biblioteca. <br>
..........[`Primeiros passos`](#Primeiros-passos): Como configurar a classe MyORM. <br>
..........[`Criar tabela`](#Criar-tabela): Como criar uma tabela usando métodos da biblioteca (CREATE). <br>
..........[`Inserir dados`](#Inserir-dados): Como inserir registros em uma tabela usando métodos da biblioteca (INSERT). <br>
..........[`Selecionar dados`](#Selecionar-dados): Como selecionar dados de uma tabela usando os métodos da biblioteca (SELECT). <br>
..........[`Atualizar dados`](#Atualizar-dados): Como atualizar e modificar registros de uma tabela usando os métodos da biblioteca (UPDATE). <br>
..........[`Deletar dados`](#Deletar-dados): Como deletar registros de uma tabela usando métodos da biblioteca (DELETE). <br>
..........[`Alterar tabela`](#Alterar-tabela): Alterar propriedades das colunas de uma tabela usando os métodos da biblioteca (ALTER TABLE). <br>
..........[`Condições`](#Condições): Condições para executar uma consulta SQL <br>
....................[`WHERE`](#WHERE): Como utilizar a condição WHERE com as funções da biblioteca. <br>
....................[`BETWEEN`](#BETWEEN): Como utilizar a condição BETWEEN com as funções da biblioteca. <br>
....................[`AND`](#AND): Como usar a condição AND com as funções da biblioteca. <br>
....................[`OR`](#OR): Como usar a condição OR com as funções da biblioteca. <br>
..........[`Propriedades`](#Propriedades): Propriedades das colunas. <br>
....................[`Tipos de dados`](#Tipos-de-dados): Tipos de dados que a coluna armazenará. <br>
..............................[`INTEGER`](#INTEGER): Definir uma coluna como INTEGER. <br>**

____

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

**Veja mais sobre `foreign key` e outras propriedades em [`PROPRIEDADES`](#Propiedades)**

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

As condições desta **ORM** são, no geral, simplificadas para facilitar a organização do script final:

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

____

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
    address = (boolean())
)
```

____

