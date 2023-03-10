# Hey there! :astronaut:
In this repository you'll find projects that I created following [Curso Profesional de Python](https://platzi.com/clases/old/python-profesional/), a Python	:snake: mid level course from Platzi.

## Virtual env & dependencies
Before run this poject, you have to create a virtual env.
```sh
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## `Palindrome`
If a word or sentence can be read in the same way forward and backward then we can say that is a palindrome.

> "Ana" :white_check_mark:  Is palindrome <br>
"Paola" :x: Is not a palindrome <br>
"Anita laba la tina" :white_check_mark: Is a palindrome <br>
"Hola mundo" :x: Is not a palindrome <br>

### Run this project
```sh
# Using linux or mac
python3 palindrome.py
```

```sh
# Using windows
py palindrome.py
```
Checking static typing
```sh
mypy palindrome.py --check-untyped-defs
```


## `Odd`
A number is odd when it can't be divisible by 2.

### Run this project
```sh
# Using linux or mac
python3 odd.py
```

```sh
# Using windows
py odd.py
```
Checking static typing
```sh
mypy odd.py --check-untyped-defs
```


## `Closures`
With this project I've ben practiced the closure concept. You'll find two functions.
1. Text repeater
2. Multiplier
### Run this project
```sh
# Using linux or mac
python3 closures.py
```

```sh
# Using windows
py closures.py
```

## `Decorators`
This is just a simple practice to understand decorator concept.
### Run this example
```sh
# Using linux or mac
python3 decorators.py
```

```sh
# Using windows
py decorators.py
```


## `Iterators`
This is just a simple practice to understand how iterators work.
In file `iterators.py` you'll find two classes
1. `EvenNumbers`: Generate an iterator of all even numbers, unless you put a max number to stop the program.
2. `Fibonacci`: Generate an iterator of all fibonacci succesion, unless you put a specific number to get its fibonacci.

### Run this example
```sh
# Using linux or mac
python3 iterators.py
```

```sh
# Using windows
py iterators.py
```


## `Playground`
Little project that wrap all functional exercises created in this repo.
I hope you enjoy it :smile:

### Run this example
```sh
# Using linux or mac
python3 main.py
```

```sh
# Using windows
py main.py
```