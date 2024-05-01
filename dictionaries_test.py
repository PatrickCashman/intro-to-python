numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
}

phone = input("Phone: ")
phone_list = list(phone)

for text in phone_list:
    print(numbers.get(text, "Not a digit")) #providing a default value
