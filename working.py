import string
stop_words = ["in", "the", "and"]
sentence = "You'r boat-in the Row, ro!w, row river? your boat boat boat boat and the o'cean."
sentence = sentence.lower().replace("-", " ")
new_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
array = new_sentence.split()
filtered_words = [word for word in array if word not in stop_words]
# list comprehension
# print(filtered_words)
word_frequency_object = {}
for word in filtered_words:
    if word in word_frequency_object:
        # print(f'{word} count before assignment: {word_frequency_object[word]}')
        word_frequency_object[word] = word_frequency_object[word] + 1
        # print(f'{word} count after assignment: {word_frequency_object[word]}')
    else:
        word_frequency_object.update({word: 1})
        # print(word_frequency_object)
word_frequency_object = ({k: v for k, v in sorted(word_frequency_object.items(),
      key=lambda item: item[1], reverse=True)})
def build_final_tally():
    for key, value in word_frequency_object.items():
        print(f'{key} | {value}')
build_final_tally()