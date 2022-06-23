-- TRANSACTIONS

BEGIN;
SELECT true;
COMMIT;


-- example
BEGIN;

INSERT INTO public.tren(
	modelo, capacidad)
	VALUES ( 'modelo prueba 2', 322);
	
INSERT INTO public.estaciones(
	id, nombre, direccion)  -- this id already exists
	VALUES (108,'Estacion prueba 2', 'direccion 2');
	