def load_words():
    #Load a list of words from a file and return them as a list.
    with open('words.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    return words

def filter_words_by_length(words, length):
    #Filter the list of words to include only those of a specific length for different difficulty.
    difficulty_list = []
    if length > 6:
        for word in words:
            if len(word) > 6:
                difficulty_list.append(word)
        return difficulty_list
    else:
        for word in words:
            if len(word) <= length:
                difficulty_list.append(word)
    return difficulty_list

def add_word(words, new_word):
    #Add a new word to the list if it is not already present.
    if new_word not in words:
        with open('words.txt', 'a', encoding='utf-8') as file:
            file.write(f"{new_word}\n")
        words.append(new_word)
    print(words)
    return words

def delete_word(words, word_to_delete):
    #Delete a word from the list if it exists.
    if word_to_delete in words:
        words.remove(word_to_delete)
        with open('words.txt', 'w', encoding='utf-8') as file:
                for word in words:
                    file.write(f"{word}\n")
    return words

#test
if __name__ == "__main__" :
    filter_words_by_length(load_words(), 5)
    add_word(load_words(), "example")
    delete_word(load_words(), "example")