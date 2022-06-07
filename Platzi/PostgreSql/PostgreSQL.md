

# PostgreSQL

## Foregin key

```sql
ALTER TABLE IF EXISTS public.trayectos
    ADD CONSTRAINT trayecto_extacion_fk FOREIGN KEY (id_estacion)
    REFERENCES public.estaciones (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE
    NOT VALID;
```

Add

INSERT INTO public.name_table(
	item1, item2, item3)
	VALUES ('value1', 'value2', 'value3');

## Procedural Language

​	PL/pgSQL is a loadable procedural language for the PostgreSQL database system

```postgresql
[ <<label>> ]
[DECLARE 
	declarations]
BEGIN
	statments
END [label]
```

```postgresql
DO $$
BEGIN 
	RAISE NOTICE 'ALGO ESTA PASANDO';
END
$$

```

Example #2: For loop

```postgresql
DO $$
DECLARE   /* declarate variables*/ 
	rec record := NULL; 
BEGIN  
	FOR rec IN SELECT * FROM pasajero LOOP  /* for loop*/
		RAISE NOTICE 'Un pasajero se llama %', rec.nombre;
	END LOOP;		
END
$$
```

Example #3 Declare functions

```postgresql
-- FUNCTION: public.function3()

-- DROP FUNCTION IF EXISTS public.function3();

CREATE OR REPLACE FUNCTION public.function3(
	)
    RETURNS integer
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE
	rec record := NULL;
	contador integer := 0;
BEGIN 
	FOR rec IN SELECT * FROM pasajero LOOP
		RAISE NOTICE 'Un pasajero se llama %', rec.nombre;
		contador := contador + 1;
	END LOOP;	
	RAISE NOTICE 'Conteo es %', contador;
	RETURN contador;
END
$BODY$;

ALTER FUNCTION public.function3()
    OWNER TO postgres;
```

Trigger

PL/pgSQL can be used to define trigger functions on data changes or database events. A trigger function is created with the `CREATE FUNCTION` command, declaring it as a function with no arguments and a return type of `trigger` (for data change triggers) or `event_trigger` (for database event triggers).

Example

function-trigger

```postgresql
-- FUNCTION: public.functionExample()
-- DROP FUNCTION IF EXISTS public.functionExample();
CREATE OR REPLACE FUNCTION public.functionExample(
	)
    RETURNS TRIGGER
    LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
	rec record := NULL;
	contador integer := 0;
BEGIN 
	FOR rec IN SELECT * FROM pasajero LOOP
		contador := contador + 1;
	END LOOP;	
	INSERT INTO cont_pasajeros (total, tiempo)  /* insert into another table*/
	VALUES (contador, now());
	RETURN NEW
END
$BODY$;
```

create trigger

```postgresql
CREATE TRIGGER nameTrigger
AFTER INSERT 
on pasajero
FOR EACH ROW
EXECUTE PROCEDURE functionExample();
```

