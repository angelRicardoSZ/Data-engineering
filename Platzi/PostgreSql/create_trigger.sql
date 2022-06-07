
CREATE TRIGGER nameOfTrigger
    AFTER INSERT
    ON public.pasajero
    FOR EACH ROW
    EXECUTE FUNCTION public.nameOfTrigger();