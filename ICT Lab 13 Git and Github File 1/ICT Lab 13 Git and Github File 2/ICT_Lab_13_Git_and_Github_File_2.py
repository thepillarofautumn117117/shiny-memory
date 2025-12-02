def greet_user(name):
  """
  This function takes a name as input and prints a personalized greeting.
  """
  print(f"Hello, {name}! Welcome.")

# Example usage of the function:
greet_user("Alice")
greet_user("Bob")

# You can also get input from the user:
user_name = input("Enter your name: ")
greet_user(user_name)
