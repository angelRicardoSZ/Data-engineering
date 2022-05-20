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