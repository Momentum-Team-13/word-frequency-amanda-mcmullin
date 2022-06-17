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
    # print(read_file)

  #remove punctuation
    new_string = read_file.translate(str.maketrans('', '', string.punctuation))
    # print(new_string)

  #normalize all words to lowercase
    new_string = new_string.lower()
    # print(new_string)  
    # print(type(new_string))
    
  #remove "stop words" -- words used so frequently they are ignored -- 
  #**new_string changed to list to filter words**
    new_string = new_string.split()
    # print(new_string)
    # print(type(new_string))

  #capture unique words
    filtered_words = [word for word in new_string if word not in STOP_WORDS]

  #build object to store unique words and their frequency count 
    word_frequency_object = {}
    for word in filtered_words:
      if word in word_frequency_object:
        word_frequency_object[word] = word_frequency_object[word] + 1
      else:
        word_frequency_object.update({word: 1})

  #sort list - descending order
    word_frequency_object = ({k: v for k, v in sorted(word_frequency_object.items(), key=lambda item: item[1], reverse=True)})

  #print it - but make it look pretty
    def build_final_tally():
      for key, value in word_frequency_object.items():
        print(f'{key} | {value}')
    build_final_tally()
    

print_word_freq("simple-test-file.txt")
print_word_freq("one-today.txt")
print_word_freq("praise_song_for_the_day.txt")
print_word_freq("the-hill-we-climb.txt")


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
