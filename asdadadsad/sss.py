import random

def generate_equation(difficulty):
  """Generates a math equation based on the given difficulty."""

  if difficulty == "easy":
    # Generate a random number between 1 and 10.
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    # Choose a random operation from addition, subtraction, multiplication, and division.
    operation = random.choice(["+", "-", "*", "/"])

    # Generate the equation.
    equation = f"{a} {operation} {b}"

    return equation

  elif difficulty == "moderate":
    # Generate two random numbers between 11 and 100.
    a = random.randint(11, 100)
    b = random.randint(11, 100)

    # Choose a random operation from addition, subtraction, multiplication, and division.
    operation = random.choice(["+", "-", "*", "/"])

    # Generate the equation.
    equation = f"{a} {operation} {b}"

    return equation

  elif difficulty == "difficult":
    # Generate two random numbers between 101 and 1000.
    a = random.randint(101, 1000)
    b = random.randint(101, 1000)

    # Choose a random operation from addition, subtraction, multiplication, and division.
    operation = random.choice(["+", "-", "*", "/"])

    # Generate the equation.
    equation = f"{a} {operation} {b}"

    return equation

def check_answer(equation, answer):
  """Checks if the given answer is correct for the given equation."""

  # Split the equation into the operands and the operator.
  operands = equation.split(" ")
  operator = operands[1]

  # Convert the operands to integers.
  a = int(operands[0])
  b = int(operands[2])

  # Perform the operation on the operands and compare the result to the given answer.
  if operator == "+":
    result = a + b
    if result == answer:
      return True
    else:
      return False
  elif operator == "-":
    result = a - b
    if result == answer:
      return True
    else:
      return False
  elif operator == "*":
    result = a * b
    if result == answer:
      return True
    else:
      return False
  elif operator == "/":
    result = a // b
    if result == answer:
      return True
    else:
      return False

def play_game():
  """Plays the math mastermind game."""

  # Choose the difficulty of the game.
  difficulty = input("Choose difficulty (easy, moderate, or difficult): ")

  # Generate an equation based on the chosen difficulty.
  equation = generate_equation(difficulty)

  # Print the equation to the user.
  print(f"Equation: {equation}")

  # Get the user's answer.
  answer = input("Answer: ")

  # Check if the user's answer is correct.
  correct = check_answer(equation, answer)

  # If the user's answer is correct, print a congratulations message.
  if correct:
    print("Congratulations! Your answer is correct!")
  # Otherwise, print a message stating that the user's answer is incorrect.
  else:
    print("Incorrect answer. The correct answer is", eval(equation))

if __name__ == "__main__":
  play_game()
