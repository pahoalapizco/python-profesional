def is_odd(number: int) -> bool:
  return number % 2 != 0

def run():
  while True:
    input_number = input("Type a number to evaluate if it is odd or not => ")

    if input_number.isdigit():
      break
  if is_odd(int(input_number)):
    print(f"{input_number} is an odd number.")
  else:
    print(f"{input_number} is not an odd number")
  


if __name__ == "__main__":
  run()