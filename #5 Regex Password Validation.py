"""
Description:
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.
"""

#My codes:

regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$"

#Others codes:

from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)

regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"

regex="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[^a-zA-Z0-9]).{6,}$"

regex='(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])^[^\W_]{6,}$'

regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[a-z])[a-zA-Z0-9]{6,}$'
