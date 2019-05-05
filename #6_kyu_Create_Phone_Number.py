Description:

"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example:
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
createPhoneNumber(Array[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
create_phone_number(Array[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
createPhoneNumber(Array[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
createPhoneNumber [1,2,3,4,5,6,7,8,9,0] -- => returns "(123) 456-7890"
Kata.CreatePhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
Kata.createPhoneNumber(Seq(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)) # => returns "(123) 456-7890"
createPhoneNumber([1,2,3,4,5,6,7,8,9,0]); -- => returns "(123) 456-7890"
createPhoneNumber [1; 2; 3; 4; 5; 6; 7; 8; 9; 0] // => returns "(123) 456-7890"create-phone-number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
CreatePhoneNumber([10]uint{1,2,3,4,5,6,7,8,9,0})
create_phone_number(phnum, (const unsigned char[]){1,2,3,4,5,6,7,8,9,0});
    /* phnum <- "(123) 456-7890" */
phnum:  resb 15
nums:   db  1,2,3,4,5,6,7,8,9,0

mov rdi, phnum
mov rsi, nums
call create_phone_number  ; RAX <- phnum <- "(123) 456-7890" The returned format must be correct in order to complete this challenge. 
Don't forget the space after the closing parentheses!

"""

My codes:

def create_phone_number(n):
    return '({}) {}-{}'.format(''.join(map(str,n[:3])),''.join(map(str,n[3:6])),''.join(map(str,n[6:10])))

Others codes:

def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number(n):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)
