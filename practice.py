"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """Prints 'Hello World'"""

    print "Hello World"

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    """Prints "Hi" followed by the someone's name"""

    print "Hi", name

# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.

def print_product(x, y):
    """Prints the result of two integers x & y multiplied together"""

    print x * y


# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times

def repeat_string(string, x):
    """Prints the string repeated x times"""

    print string * x

# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".

def print_sign(x):
    """Prints 'Higher than 0' if x is higher than zero.  Prints 'Lower than 0' 
    if x is lower than xero.  Prints 'Zero' if x is zero."""

    if x > 0:
        print "Higher than 0"
    
    elif x < 0:
        print "Lower than 0"

    elif x == 0:
        print "Zero"

# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.

def is_divisible_by_three(x):
    """Returns True or False if x is evenly divisible by 3"""

    return x % 3 == 0

# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.

def num_spaces(string):
    """Returns the number of spaces in a string"""

    count = 0 

    # Iterates over each character in string and adds one to the counter for each
    # space.

    for character in string:
        if character == " ":
            count += 1

    return count

# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.

def total_meal_price(price, tip=0.15):
    """Returns total amount of meal including tip.  Tip is optional, and is
    defaulted to 15%"""

    return price + price * tip


# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.

def sign_and_parity(x):
    """Takes an integer and returns 'Positive' or 'Negative' and 'Even' or 'Odd'
    in a list."""

    sign_and_parity_list = []

    if x > 0:
        sign_and_parity_list.append('Positive')
    elif x < 0:
        sign_and_parity_list.append('Negative')

    if x % 2 == 0:
        sign_and_parity_list.append('Even')
    else:
        sign_and_parity_list.append('Odd')

    return sign_and_parity_list

# Calls the function sign_and_parity() and unpacks 4 into two variables, sign and parity.
sign, parity = sign_and_parity(4)

print sign
print parity

###############################################################################

# PART TWO

# 1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string.

def full_title(recipient_name, job_title='Engineer'):
    """Takes the a name and job title and returns full title in one string.  If
    job title is not passed, the title defaults to 'Engineer'"""

    return "{} {}".format(job_title, recipient_name)

# 2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(recipient_name, job_title, sender_name):
    """Takes 3 arguments to print the following letter: 'Dear JOB_TITLE 
    RECIPIENT_NAME, I think you are amazing! Sincerely, SENDER_NAME.'"""

    print "Dear {}, I think you are amazing! Sincerely, {}".format(full_title(recipient_name, job_title), sender_name)

###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
