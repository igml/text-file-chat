import user
import client


def get_login_type():
  loop = True
  while loop:
    user_choice = input("Register (R) or Login (L)? ").upper()

    if user_choice in ['L', 'LOGIN', 'R', 'REGISTER']:
      return user_choice

    print("\nPlease try again.\n")
  

def login_user():
  user_list = get_user_info()
  
  loop = True
  while loop:
    username = input("\nUsername: ")
    password = input("Password: ")

    user_found = False
    for chatter in user_list:
      if username == chatter.name and password != chatter.password:
        user_found = True
        print("\nYour password was incorrect.")
      
      if username == chatter.name and password == chatter.password:
        user_found = True
        print("\nYour login was successful!\n")
        return chatter

    if user_found != True:
      print("\nUser was not found.")
        
    print("\nPlease try again.")
        

def get_user_info():
  file = open("user_info.txt", "r")

  user_list = []
  
  id = 0
  
  for info in file:
    username = ""
    password = ""
    on_password = False
    for char in info:
      if on_password and char != '\n':
        password += char

      if not on_password and char != ':':
        username += char
        
      elif char == ':':
        on_password = True

    user_list.append(user.User(username, password, id))
    id += 1

  return user_list


def create_user():
  user_list = get_user_info()

  loop = True
  while loop:
    
    username = input("\nUsername: ")

    msg = "\n"

    if username.isalnum() and len(username) >= 1:
      if len(user_list) == 0:
        loop = False
        continue

      loop = False
      for chatter in user_list:
        if username == chatter.name:
          msg += "Username already in use."
          loop = True

        if loop == True:
          break
        
    else:
      msg += "Only letters, and characters are allowed."

    if loop == False:
        continue

    print(msg + " Please try again.")

  loop = True
  while loop:
    password = input("Password: ")

    if len(password) >= 5 and len(password) <= 1000:
      break

    print("\nPasswords can only be 5-1000 characters in length.\n")

  file = open("user_info.txt", "r")

  lines = ""
  for line in file:
    lines += line
  
  if len(lines) < 8:
    file = open("user_info.txt", "w")
    file.write("")

  file = open("user_info.txt", "a")
  
  file.write(username + ":" + password + "\n")
  file.close()

  print("\nYour account has been successfully created. Please run the program again to login.\n")

# Program starts here

def main():
  
  user_choice = get_login_type()

  if user_choice in ['L', 'LOGIN']:
    token = login_user()
    print(f"Logged in as '{token}'.\n")
    client.main(token)

  else:
    create_user()


main()
