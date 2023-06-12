<?php

/**
 * La interfaz Builder declara un conjunto de métodos para ensamblar una consulta SQL.
 * 
 * En este caso todos los pasos de construcción devuelven el objeto de constructor actual para permitir el encadenamiento: $ builder-> select (...) -> where (...)
 */
interface SQLQueryBuilder //* BUILDER
{
    public function select(string $table, array $fields): SQLQueryBuilder;

    public function where(string $field, string $value, string $operator = '='): SQLQueryBuilder;

    public function limit(int $start, int $offset): SQLQueryBuilder;

    // Otras 100 métodos de sintaxis SQL ...

    public function getSQL(): string;
}

/**
 * Cada Constructor Concreto corresponde a un dialecto SQL específico y puede implementar
 * los pasos del constructor un poco diferente de los demás.
 * 
 * Este Constructor Concreto puede construir consultas SQL compatibles con MySQL.
 */
class MysqlQueryBuilder implements SQLQueryBuilder //* CONCRETE BUILDER
{
    protected $query;

    protected function reset(): void
    {
        $this->query = new \stdClass(); // stdClass es una clase estándar de PHP que tiene algunas propiedades y métodos internos para almacenar datos.
    }

    /**
     * Construye una consulta SELECT base.
     */
    public function select(string $table, array $fields): SQLQueryBuilder
    {
        $this->reset();
        $this->query->base = "SELECT " . implode(", ", $fields) . " FROM " . $table;
        $this->query->type = 'select';

        return $this;
    }

    /**
     * Agrega una condición WHERE.
     */
    public function where(string $field, string $value, string $operator = '='): SQLQueryBuilder
    {
        // Si el tipo de consulta no es SELECT, UPDATE o DELETE, no podemos usar la cláusula WHERE en la consulta.
        if (!in_array($this->query->type, ['select', 'update', 'delete'])) {
            throw new \Exception("WHERE can only be added to SELECT, UPDATE OR DELETE");
        }
        $this->query->where[] = "$field $operator '$value'";

        return $this;
    }

    /**
     * Agrega una restricción LIMIT.
     */
    public function limit(int $start, int $offset): SQLQueryBuilder
    {
        // Si el tipo de consulta no es SELECT, no podemos usar la cláusula LIMIT en la consulta.
        if (!in_array($this->query->type, ['select'])) {
            throw new \Exception("LIMIT can only be added to SELECT");
        }
        $this->query->limit = " LIMIT " . $start . ", " . $offset;

        return $this;
    }

    /**
     * Devuelve la cadena de consulta final.
     */
    public function getSQL(): string
    {
        $query = $this->query;
        $sql = $query->base;
        if (!empty($query->where)) {
            $sql .= " WHERE " . implode(' AND ', $query->where);
        }
        if (isset($query->limit)) {
            $sql .= $query->limit;
        }
        $sql .= ";";
        return $sql;
    }
}

/**
 * Este Constructor Concreto es compatible con PostgreSQL. Si bien Postgres es muy
 * similar a Mysql, todavía tiene varias diferencias. Para reutilizar el código común,
 * lo extendemos desde el constructor MySQL, mientras anulamos algunos de los pasos de construcción.
 */
class PostgresQueryBuilder implements SQLQueryBuilder //* CONCRETE BUILDER
{
    protected $query;

    protected function reset(): void
    {
        $this->query = new \stdClass(); // stdClass es una clase estándar de PHP que tiene algunas propiedades y métodos internos para almacenar datos.
    }

/**
     * Construye una consulta SELECT base.
     */
    public function select(string $table, array $fields): SQLQueryBuilder
    {
        $this->reset();
        $this->query->base = "SELECT " . implode(", ", $fields) . " FROM " . $table;
        $this->query->type = 'select';

        return $this;
    }

    /**
     * Agrega una condición WHERE.
     */
    public function where(string $field, string $value, string $operator = '='): SQLQueryBuilder
    {
        // Si el tipo de consulta no es SELECT, UPDATE o DELETE, no podemos usar la cláusula WHERE en la consulta.
        if (!in_array($this->query->type, ['select', 'update', 'delete'])) {
            throw new \Exception("WHERE can only be added to SELECT, UPDATE OR DELETE");
        }
        $this->query->where[] = "$field $operator '$value'";

        return $this;
    }

    /**
     * Entre otras cosas, PostgreSQL tiene una sintaxis LIMIT ligeramente diferente.
     */
    public function limit(int $start, int $offset): SQLQueryBuilder
    {
        // Si el tipo de consulta no es SELECT, no podemos usar la cláusula LIMIT en la consulta.
        if (!in_array($this->query->type, ['select'])) {
            throw new \Exception("LIMIT can only be added to SELECT");
        }

        $this->query->limit = " LIMIT " . $start . " OFFSET " . $offset;

        return $this;
    }

    /**
     * Devuelve la cadena de consulta final.
     */
    public function getSQL(): string
    {
        $query = $this->query;
        $sql = $query->base;
        if (!empty($query->where)) {
            $sql .= " WHERE " . implode(' AND ', $query->where);
        }
        if (isset($query->limit)) {
            $sql .= $query->limit;
        }
        $sql .= ";";
        return $sql;
    }

    // + toneladas de otras anulaciones ...
}


/**
 * Note que el código del cliente usa el objeto constructor directamente. 
 * Una clase de Director designada no es necesaria en este caso, porque el código del cliente necesita consultas diferentes casi todo el tiempo, por lo que la secuencia de los pasos de construcción no se puede reutilizar fácilmente.
 * 
 * Dado que todos nuestros constructores de consultas crean productos del mismo tipo (que es una cadena), podemos interactuar con todos los constructores usando su interfaz común. Más tarde, si implementamos una nueva clase Builder, podremos pasar su instancia al código de cliente existente sin romperlo gracias a la interfaz SQLQueryBuilder.
 */
function clientCode(SQLQueryBuilder $queryBuilder) // dentro del patrón builder, este es el director
{
    // ...

    $query = $queryBuilder
        ->select("users", ["name", "email", "password"])
        ->where("age", 18, ">")
        ->where("age", 30, "<")
        ->limit(10, 20)
        ->getSQL();

    echo $query;

    // ...
}

//* La aplicación debería en la vida real seleccionar el tipo de constructor de consulta adecuado según una configuración actual o la configuración del entorno, por ejemplo:
// if ($_ENV['database_type'] == 'postgres') {
//     $builder = new PostgresQueryBuilder(); } else {
//     $builder = new MysqlQueryBuilder(); }
// clientCode($builder);


//* Pero para mantener este ejemplo simple, se crean los constructores de consultas manualmente para comprobar el funcionamiento del patrón Builder.
echo "Probando el constructor de consultas MySQL:\n";
$constructorMysql = new MysqlQueryBuilder();
clientCode($constructorMysql);

echo "\n\n";

echo "Probando el constructor de consultas PostgresSQL:\n";
$constructorPostgres = new PostgresQueryBuilder();
clientCode($constructorPostgres);
