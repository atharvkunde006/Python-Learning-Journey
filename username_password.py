user=input("username:")
password=input("password:")
if user=="admin":
  if password=="1234":
        print("Login successful!")
  else:
        print("Incorrect password.")
else:
    print("Invalid username.") 