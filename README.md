# My ORM
**Um script para facilitar interação com bancos de dados, simplificando a implementação de CRUDs e consultas SQL**

### OBS
**Este projeto ainda está em desenvolvimento e pode ser instável!**

____

## Instalação

```bash
$ git clone git@github.com:paulindavzl/my-orm.git
$ pip install -r requirements.txt
```

Ou

```bash
$ pip install -e .
```

`pip install -e .` é mais recomendado, já que importa este projeto como uma biblioteca Python

____

## Primeiros passos:

**Importe todos as funcionalidades contidas na biblioteca e instancie a classe MyORM, passando como parâmetro o tipo de banco de dados (_tipo: str_) e os dados (_tipo: dict_) necessários para realizar a conexão com o mesmo:**

```python
from my_orm import *

# dados necessários para conectar-se ao banco de dados
data = {
    "url": "./database/database.db"
}

orm = MyORM("sqlite", data)
```

**É possível ativar o retorno dos comandos SQL**

```python
MyORM(sql_return=True)
```

**Também é possível desativar a execução dos comandos**

```python
MyORM(execute=False)
```

____

## Criar uma tabela no banco de dados

**Você pode criar uma tabela usando método _create()_, passando como primeiro parâmentro o nome da tabela (_tipo: str_) seguida pelas colunas (_tipo: str_):**

```python
orm.create(
    "users",
    integer("id", prop("n_null", "pri_key", "uni")),
    varchar("name", 30, prop("n_null")),
    datetime("creation", prop("n_null"))
```

Este comando equivale ao comando:

```sql
CREATE TABLE IF NOT EXISTS users(
    "id" INTEGER NOT NULL PRIMARY KEY UNIQUE,
    "name" VARCHAR(30) NOT NULL,
    "creation" DATETIME NOT NULL
)
```

**Você também pode usar comandos SQL diretamente usando o método:**

```python
# passe o comando SQL como primeiro parâmetro e possíveis valores como segundo parâmetro
orm.execute()
```

____

## Tipos de dados

### Para usar com MyORM.create():

* **integer** <br>
Para criar colunas do tipo INTEIRO

    * col_name (str): nome da coluna
    
    * *args(str): propriedades da coluna

```python
integer(col_name: str, *args: str)
```

* **t_float** <br>
Para criar colunas tipo FLOAT
    
    * col_name (str): nome da coluna

    * *args(str): propriedades da coluna

```python
t_float(col_name: str, *args: str)
```

* **decimal** <br>
Para criar colunas tipo DECIMAL

    * col_name (str): nome da coluna

    * precision (int): número total de dígitos

    * scale (int): número de dígitos depois da vírgula

    * *args (str): propriedades da coluna

```python
decimal(col_name: str, precision: int, scale: int, *args: str)
```

* **double** <br>
Para criar colunas tipo DOUBLE
    * col_name (str): nome da coluna

    * *args (str): propriedades da coluna

```python
double(col_name: str, *args: str)
```

* **char** <br>
Para criar colunas tipo CHAR
    * col_name (str): nome da coluna
    * length (int): tamanho que o dado que a coluna receberá
    * *args (str): propriedades da coluna

```python
char(col_name: str, length: int, *args: str)
```

* **varchar** <br>
Para criar colunas tipo VARCHAR
    * col_name (str): nome da coluna
    * max_length (int): tamanho máximo do dado que a coluna recebera
    * *args (str): propriedades da coluna

```python
varchar(col_name: str, max_length: int, *args: str)
```

* **text** <br>
Para criar colunas tipo TEXT
    * col_name (str): nome da coluna
    * *args (str): propriedades da coluna

```python
text(col_name: str, *args: str)
```

* **boolean** <br>
Para criar colunas tipo BOOLEAN
    * col_name (str): nome da coluna
    * *args (str): propriedades da coluna

```python
boolean(col_name: str, *args: str)
```

* **date** <br>
Para criar tabelas tipo DATE
    * col_name (str): nome da coluna
    * *args (str): propriedades da coluna

```python
date(col_name: str, *args: str)
```

`formato: YYYY/MM/DD`

* **datetime** <br>
Para criar tabelas tipo DATETIME
    * col_name (str): nome da coluna
    * *args (str): propriedades da coluna

```python
datetime(col_name: str, *args: str)
```

`formato: YYYY/MM/DD HH:MM:SS`

* **timestamp** <br>
Para criar tabelas tipo TIMESTAMP
    * col_name (str): nome da coluna
    * *args (str): propriedades da coluna

```python
timestamp(col_name: str, *args: str)
```

`formato: YYYY/MM/DD HH:MM:SS`

____

## Propriedades

* **foreign_key** <br>
Para adicionar a propriedade FOREIGN KEY
    * referrer (str): chave estrangeira, referenciadora
    * referenced (str): chave primária, referenciada
    * *args (str): propriedades extras para FOREIGN KEY

```python
foreign_key(referrer: str, referenced: str, *args: str)
```

OBS: _referenced_ precisa estar no formato: **table(column)**

* **on_up** <br>
Para adicionar a propriedade ON UPDATE
    * command (str): ação executada quando atualizado

```python
on_up(command: str)
```

OBS: _on_up_ é uma propriedade de **foreign_key**

* **on_del** <br>
Para adicionar a propriedade ON DELETE
    * command (str): ação executada quando deletado

```python
on_del(command: str)
```

OBS: _on_del_ é uma propriedade de **foreign_key**

* **prop** <br>
Para adicionar propriedades extras de forma abreviada
    * *args (str): propriedades abreviadas
    * default: valor para DEFAULT

```python
prop(*args: str, default=None)
```

**Como usar cada propriedade:**

```python
# AUTO_INCREMENT
prop("auto")

# DEFAULT
prop(default="example")

# DEFAULT CURRENT_TIMESTAMP
prop(default="current")

# PRIMARY KEY
prop("pri_key")

# NOT NULL
prop("n_null")

# UNIQUE
prop("uni")
```

OBS: É possível usar varias propriedades em um único _**prop()**_:

```python
prop("uni", "n_null", "pri_key", "auto", default="current")
```

O resultado dessa função seria o equivalente ao comando:

```sql
DEFAULT CURRENT_DATETIME UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT
```