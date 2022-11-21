def main():

  word = input("Enter a word here:")
  print("Is it a pallendrome?", word == word[::-1])
  pass


if __name__ == "__main__":
  main()