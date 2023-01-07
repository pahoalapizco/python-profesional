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
