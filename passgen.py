import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
  """
  Generates a random password based on user-defined criteria.

  Args:
    length: The desired length of the password.
    use_letters: Whether to include letters in the password.
    use_numbers: Whether to include numbers in the password.
    use_symbols: Whether to include symbols in the password.

  Returns:
    The generated password as a string.
  """

  characters = ''
  if use_letters:
    characters += string.ascii_letters
  if use_numbers:
    characters += string.digits
  if use_symbols:
    characters += string.punctuation

  if not characters:
    return "Error: No character types selected."

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

if __name__ == "__main__":
  try:
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print("Generated Password:", password)

  except ValueError:
    print("Invalid input. Please enter a valid integer for password length.")