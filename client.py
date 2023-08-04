import replit


def main(token):
  loop = True
  while loop:

    separator = ""
    for num in range(36):
      separator += "`"
  
    user_input = input(f"{separator}\n!quit can be used to exit the chat.\n\nPress 'ENTER' to see new messages.\n\nWould you like to connect now? (Y/N) ").upper()
  
    if user_input in ['Y', 'YES']:
      print(f"\nSuccessfully connected as '{token.name}'.\n")
      loop = False

    elif user_input in ['N', 'NO']:
      print("\nDisconnecting...\n")
      return

    else:
      print("\nPlease try again.\n")

  chat = open("chat.txt", "a")
  join_message = f"{token.name} has joined the chat!\n"
  chat.write('\n' + join_message + '\n')

  loop = True
  while loop:
    replit.clear()
    chat = open("chat.txt", "r")
    for line in chat:
      print(line)
      
    message = input(f"{token.name}:\n\n\t") 
    chat = open("chat.txt", "a")
  
    if message.lower() == "!quit":
      loop = False
      chat.write(f"\n{token.name} has left the session.\n")
      continue

    if message != "":
      chat.write(f"{token.name}:\n\t{message}\n")

  chat.close()
