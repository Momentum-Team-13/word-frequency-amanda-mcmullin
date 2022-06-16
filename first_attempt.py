import string


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with',
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file.  YOUR CODE GOES HERE"""
    # print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.read()
    print(read_file)

  #remove punctuation
    new_string = read_file.translate(str.maketrans('', '', string.punctuation))
    print(new_string)

  #normalize all words to lowercase
    new_string = new_string.lower()
    # print(new_string)  
    # print(type(new_string))
    
  #remove "stop words" -- words used so frequently they are ignored -- 
  #**new_string changed to list to filter words**
    new_string = new_string.split()
    # print(new_string)
    # print(type(new_string))

    for word in new_string:
      if word in STOP_WORDS:
        # print(word)
        new_string = list(filter((word).__ne__, new_string))
    print(new_string)
    print("Works up to here")

print_word_freq("simple-test-file.txt")

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()  

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


