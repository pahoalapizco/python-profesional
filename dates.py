import datetime as dt

def working_with_dates():
  my_date = dt.datetime.now() # Hora local configurada en la computadora
  print(f"now: {my_date}")
  my_utcdate = dt.datetime.utcnow() # Hora universal
  print(f"utc: {my_utcdate}")

  my_day = dt.date.today() # Solo el día actual
  print(f"Complate day: {my_day}")
  # Desestructurar la fecha por partes.
  print(f"Year: {my_day.year}")
  print(f"Month:{my_day.month}")
  print(f"Day: {my_day.day}")


# Formateo de fechas
def formating_dates():
  my_date = dt.datetime.now()

  # US Format
  str_date = my_date.strftime("%m/%d/%Y")
  print(f"US Format: {str_date}")

  # LATAM Formar
  str_date = my_date.strftime("%d/%m/%Y")
  print(f"US Format: {str_date}")
  

if __name__ == "__main__":
  working_with_dates()
  print("")
  formating_dates()