from datetime import datetime
import pytz

def run():
  mexico_timezone = pytz.timezone("America/Mexico_City")
  mexico_date = datetime.now(mexico_timezone)
  str_time = mexico_date.strftime("%d/%m/%Y %H:%M:%S")
  print(f"Ciudad de México: {str_time}")

  culiacan_timezone = pytz.timezone("America/Mazatlan")
  culiacan_date = datetime.now(culiacan_timezone)
  str_time = culiacan_date.strftime("%d/%m/%Y %H:%M:%S")
  print(f"Culiacán: {str_time}")


  LA_ca_timezone = pytz.timezone("America/Los_Angeles")
  LA_ca_date = datetime.now(LA_ca_timezone)
  str_time = LA_ca_date.strftime("%m/%d/%Y %H:%M:%S")
  print(f"Los Angeles, CA. : {str_time}")

if __name__ == "__mian__":
  run()