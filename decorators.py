from datetime import datetime

def decorator(func):
  def wrapper():
    print("Esta es un ejemplo sencillo de un decorador")
    func()
  return wrapper


@decorator
def saludo():
  print("Hola!")


def upper(func):
  def wrapper(text):
    return func(text).upper()
  return wrapper


@upper
def mensaje(nombre):
  return f"{nombre}, este es un mensaje :)"

'''
*args(arguments): Todos los argurmentos posicionales, no importa cuantos sean (0 a N) la función los va a recibir.
**kwargs(keyword arguments): Todos los argumentos nombrados, no importa cuantos sean (0 a N) la función los va a recibir.
'''

def execution_time(func):
  def wrapper(*args, **kwargs): # Recibe los mismo parametros que la funcuón que se esta decorando
    initial_time = datetime.now()
    result = func(*args, **kwargs)
    final_time = datetime.now()
    time_elapsed = final_time - initial_time
    print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return result
  return wrapper


# Sin argumentos
@execution_time
def random_func():
  for _ in (1, 100000000000):
    pass


# Con argumentos posicionales
@execution_time
def sum(a: int, b: int) -> int:
  return a + b


# Con argumentos nombrados
@execution_time
def greatings(name = "nombre"):
  print(f"Hola {name}!")



if __name__ == "__main__":
  random_func()
  print(sum(5, 5))
  greatings("Paola")
