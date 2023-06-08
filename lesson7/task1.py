def count_words(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
input_sentence = input("Enter the words: ")
result = count_words(input_sentence)
print(result)