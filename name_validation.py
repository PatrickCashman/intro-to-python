#name validation
print("enter username: ")
username = input()

if len(username) < 3:
    print("name must be at least 3 characters")

elif len(username) > 50:
    print("name can be a maximum of 50 characters")

else:
    print("name looks good!")