from controller import Authentication

phonenumber = '0709911007'
password = 'Morrisochleon12!'
email = 'leonfortgens@hotmail.se'
full_name = 'Leon Fortgens'

print(Authentication.password_is_valid(password))
print(Authentication.phonenumber_is_valid(phonenumber))
print(Authentication.email_is_valid(email))
print(Authentication.full_name_is_valid(full_name))