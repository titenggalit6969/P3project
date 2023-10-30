import random

# Define the different equations
EQUATIONS = {
    "addition": "+",
    "subtraction": "-",
    "multiplication": "*",
    "division": "/"
}

# Define the different difficulty levels
DIFFICULTY_LEVELS = {
    "easy": {
        "range": (1, 11),
        "chances": 3
    },
    "moderate": {
        "range": (11, 101),
        "chances": 3
    },
    "difficult": {
        "range": (101, 1001),
        "chances": 3,
        "time_limit": 10
    }
}

# Define a function to generate a random equation
def generate_random_equation(equation_type, difficulty_level):
    """Generates a random equation based on the given equation type and difficulty level.

    Args:
        equation_type: The type of equation to generate, e.g. "addition", "subtraction", "multiplication", or "division".
        difficulty_level: The difficulty level of the equation to generate, e.g. "easy", "moderate", or "difficult".

    Returns:
        A random equation tuple, where the first element is the equation string and the second element is the correct answer.
    """

    # Get the range of numbers to use in the equation
    number_range = DIFFICULTY_LEVELS[difficulty_level]["range"]

    # Generate two random numbers within the given range
    num1 = random.randint(number_range[0], number_range[1])
    num2 = random.randint(number_range[0], number_range[1])

    # Generate the equation string
    equation_string = str(num1) + EQUATIONS[equation_type] + str(num2)

    # Calculate the correct answer
    correct_answer = eval(equation_string)

    return equation_string, correct_answer

# Define a function to play the game
def play_game():
    """Plays the math game."""

    # Get the user's desired equation type and difficulty level
    equation_type = input("Choose an equation type (addition, subtraction, multiplication, or division): ")
    difficulty_level = input("Choose a difficulty level (easy, moderate, or difficult): ")

    # Generate a random equation
    equation_string, correct_answer = generate_random_equation(equation_type, difficulty_level)

    # Display the equation to the user
    print(equation_string)

    # Get the user's answer
    user_answer = input("Enter your answer: ")

    # Check if the user's answer is correct
    correct = False
    if user_answer == str(correct_answer):
        correct = True

    # Display the results to the user
    if correct:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", correct_answer)

# Start the game
play_game()