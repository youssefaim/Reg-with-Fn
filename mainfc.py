# Import functions from the 'fc' module (presumed to be your custom module)
from Fonctions import check_word, check_digit, remove_space, phone_number, email

# Test the check_word function to see if the word 'saad' is present in the given text
checkword = check_word('youssef', 'I am youssef ait mellouk.')
print(checkword)

# Test the check_digit function to check if the string contains at least one digit
checkdigtal = check_digit('my number is 065434')
print(checkdigtal)

# Test the remove_space function to replace spaces with hyphens in the given string
removespace = remove_space('I am youssef ait mellouk my number is 065434')
print(removespace)

# Test the phone_number function to validate the phone number format
phonenumber = phone_number('06-213-435-435')
print(phonenumber)

# Test the email function to validate the email address format
emailcheck = email('maknazapsagufum.com')
print(emailcheck)