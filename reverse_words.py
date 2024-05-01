#Write a Python function called reverse_words that takes a string as input
#and returns the string with the order of the words reversed. 
#Words are separated by spaces. You should preserve the whitespace between words.

reverse_words = ("hello world")

words = reverse_words.split(" ")
reversed_string = " ".join(words[::-1]) #[:; -1], slicing syntax instead of reverse()

print(reversed_string)
