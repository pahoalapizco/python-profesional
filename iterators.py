class EvenNumbers:
  """
  Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo
  """

  # Constructor
  # self: Es el objeto futuro con el que se va estar trabajando con la clase EvenNumbers
  def __init__(self, max = None):
    self.max = max

  # Metodo para almacenar/tener los elementos necesarios para que le iterador funcione, en este caso es self
  # Inicializa los atributos necesarios y regresa el objeto self con los atributos que creamos
  def __iter__(self):
    self.num = 0 # Primer par
    return self

  # Método que permite extraer cada uno de los elementos del iterador.
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2 # Siguiente número par
      return result
    else:
      raise StopIteration


class Fibonacci:
  def __init__(self, fib_of = None):
    self.fib_of = fib_of

  def __iter__(self):
    self.prev_num = 0
    self.next_num = 1
    self.next_fib = 0
    return self

  def __next__(self):
    if not self.fib_of or self.next_fib <= self.fib_of:
      result = self.next_num
      self.next_num += self.prev_num
      self.prev_num = result
      self.next_fib += 1
      return result
    else:
      raise StopIteration


def run():
  menu = """
    [0] -> Even Numbers
    [1] -> Fibonacci

    WARNING: Be carefull, if you don't type a max number, both functions will run to infinite.
  """
  menu_option = ("0", "1")

  while True:
    option = input(menu)
    if option in menu_option:
      break

  while True: 
    number = input("Please enter a valid numer from 1 to N: ")
    if number.isdigit() or number == "":
      number = 0 if number == "" else int(number)
      break

  if int(option) == 0:
    print(f"All even numbers until {number}")
    iterator = EvenNumbers(number)
  else:
    print(f"All fibonacci until {number}")
    iterator =  Fibonacci(number)

  for iter in iterator:
    print(iter)
    


if __name__ == "__main__":
  # for par in EvenNumbers(10):
  #  print(par)
  # for fib in Fibonacci(2):
  #   print(fib)
  run()
