def fibonacci_fun(fib_of):
  prev_num = 0
  next_num = 1
  counter = 0
  max_fib = fib_of

  while True:
    if not max_fib or counter <= max_fib:
      result = next_num
      next_num += prev_num
      prev_num = result
      counter += 1
      yield result
    else:
      return

  


if __name__ == "__main__":
  for fib in fibonacci_fun(5):
    print(fib)