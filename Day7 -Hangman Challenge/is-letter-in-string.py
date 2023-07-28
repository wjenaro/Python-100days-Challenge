def is_letter_in_string(letter, string):
  """Checks whether the letter is in the string.

  Args:
    letter: The letter to check.
    string: The string to check the letter in.

  Returns:
    True if the letter is in the string, False otherwise.
  """

  for i in range(len(string)):
    if string[i] == letter:
      return True
  return False


if __name__ == "__main__":
  letter = "d"
  string = "hello world"
  print(is_letter_in_string(letter, string))
