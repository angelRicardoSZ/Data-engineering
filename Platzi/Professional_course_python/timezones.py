from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
MX_timezone = pytz.timezone("America/Mexico_City")
bogota_date = datetime.now(bogota_timezone)
mexico_date = datetime.now(MX_timezone)

print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))
print("México: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))