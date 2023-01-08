# This closure returns a nested funtion that multiplies n times an string
# Hello 3 -> HelloHelloHello
# Bye 5 -> ByeByeByeByeBye
def make_repeater_of(n):
  
  def repeater_of(text: str):
    return text * n

  return repeater_of

# This clouser returns a nested function tha multiplies the x value to n value
# x = 3 & n = 8 -> 24
def make_multiplier(x):

  def multiplier(n):
    return x * n

  return multiplier


def option_repeater():
  while True:
    n = input("Please enter the number of times you want to repeat of: ")
    if n.isdigit():
      break

  n = int(n)
  text = input(f"Now, please enter some text do you want to repeat {n} times: ")

  repeate = make_repeater_of(n)
  print(repeate(text))


def option_multiplier():
  while True:
    x = input("Please enter the first multiplier: ")
    if x.isdigit():
      break

  while True:
    n = input("Please enter the second multiplier: ")
    if n.isdigit():
      break

  times = make_multiplier(int(x))
  print(times(int(n)))


def run():
  menu = '''
    [0] -> Repite a text N times.
    [1] -> Mekes multiplier
  '''
  options = ("0", "1")

  while True:
    option = input(menu)
    
    if not option.isdigit() or not option in options:
      print(f"Sorry {option} is not a valid option, please try again...")
    else:
      break;

  if int(option) == 0:
    option_repeater()
  elif int(option) == 1:
    option_multiplier()
  else:
    print("Sorry :(, I'm working on this opction.")

if __name__ == "__main__":
  run()
  