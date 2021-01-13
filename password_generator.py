import random


def password_generator(password_length):
    random_string = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    generated_password = ""
    for x in range(password_length):
        generated_password += random_string[random.randint(0, len(random_string) - 1)]
    print(generated_password)


password_generator(5)
password_generator(9)
password_generator(13)