import odd
import palindrome
import closures
import iterators
import timezones
'''
Encapsular los ejercicios creados durante el curso en un solo entorno de ejecución
utilizando un menú con dichos ejercicios.
'''
def number_validate() -> int:
  while True:
    num = input("Please enter a number ")
    if num.isdigit():
      return int(num)

def play() -> bool:
  menu = '''
    Type the number of the corresponding exercise you want to test:

    [1] -> Odd numbers
    [2] -> Palintrome
    [3] -> Multiplier
    [4] -> Text repeater
    [5] -> Fibonacci
    [6] -> Even numbers
    [7] -> Time zones

    To quit the program type: q
  '''
  options = ("1", "2", "3", "4", "5", "6", "7")
  while True:
    usr_option = input(menu)

    if usr_option in options:
      break
    elif usr_option.lower() == "q":
      return False

  if usr_option == "1": # odd numbers
    print("===== Odd Numbers =====")
    num = number_validate()
    if odd.is_odd(num):
      print(f"{num} is an odd number.")
    else: 
      print(f"{num} isn't an odd number.")

  elif usr_option == "2":
    print("===== Palindrome =====")
    input_text = input("Tell me a word or sentence: ")
    if  palindrome.is_palindrome(input_text):
      print(f"Your input {input_text} is a palindrome")
    else:
      print(f"Your input {input_text} isn't a palindrome")

  elif usr_option == "3":
    print("===== Multiplier =====")
    closures.option_multiplier()

  elif usr_option == "4":
    print("===== Text repeater =====")
    closures.option_repeater()

  elif usr_option == "5":
    print("===== Fibonacci =====")
    num = number_validate()
    for fib in iterators.Fibonacci(num):
      print(fib)

  elif usr_option == "6":  
    print("===== Evem Numbers =====")
    num = number_validate()
    for even in iterators.EvenNumbers(num):
      print(even)

  elif usr_option == "7":  
    print("===== Timezones =====")
    timezones.run()
  
  return True

def run():
  is_play = play()
  while is_play:
    is_play = play()

if __name__ == "__main__":
  run()