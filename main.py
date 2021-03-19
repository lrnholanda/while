#the while loop in action

current_number = 1
while current_number <= 5:
  print(current_number)
  current_number += 1

#letting the user choose when to quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
  message = input(prompt)
  print(message)