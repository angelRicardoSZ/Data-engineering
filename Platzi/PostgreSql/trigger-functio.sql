-- FUNCTION: public.function3()

-- DROP FUNCTION IF EXISTS public.function3();

CREATE OR REPLACE FUNCTION public.exampleFunction()
    RETURNS trigger  /*Function type trigger*/
    LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
	rec record := NULL;
	contador integer := 0;
BEGIN 
	FOR rec IN SELECT * FROM pasajero LOOP
		contador := contador + 1;
	END LOOP;	
	INSERT INTO cont_pasajeros (total, tiempo)  /**/
	VALUES (contador, now());
	
	RETURN NEW;
END
$BODY$;

ALTER FUNCTION public.exampleFunction()
    OWNER TO postgres;
