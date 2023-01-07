def is_palindrome(text: str) -> bool:
  text = text.replace(" ", "").lower()
  return text == text[::-1]


def run():
  # input_text = input("Tell me a word o sentence: ")
  palindrome = is_palindrome(10000)
  if palindrome:
    print(f"Your input {input_text} is a palindrome")
  else:
    print(f"Your input {input_text} isn't a palindrome")


if __name__ == "__main__":
  run()
