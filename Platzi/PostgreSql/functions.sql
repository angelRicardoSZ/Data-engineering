DROP FUNCTION function2PL();
CREATE OR REPLACE FUNCTION function2PL()
 RETURNS integer
 AS $$
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
$$
LANGUAGE PLPGSQL;

SELECT function2PL();