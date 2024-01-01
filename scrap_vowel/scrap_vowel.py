def main():
  # Get the input from the user
    input_string = input("Input: ")
    print (shorten(input_string))


  # Remove the vowels from the input string
def shorten(input_string):
    output_string = ""
    for char in input_string:
        if char not in 'aeiouAEIOU':
            output_string += char

  # Print the output string
    return f"{output_string}"

if __name__ == "__main__":
    main()
