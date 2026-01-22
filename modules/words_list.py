import os
from colored import Fore, Back, Style

def load_words():
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(base_dir, '..', 'data', 'words.txt')        
    words = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words.append(line.strip().lower())
    return words, file_path

def filter_words_by_length(words, length):
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

def add_word(words, new_word, file_path):
    if new_word not in words:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f"{new_word.lower()}\n") 
        words.append(new_word.lower())
    return words

def delete_word(words, word_to_delete, file_path):
    word_to_delete = word_to_delete.lower().strip()
    if word_to_delete in words:
        words.remove(word_to_delete)
        with open(file_path, 'w', encoding='utf-8') as file:
                for word in words:
                    file.write(f"{word}\n")
    return words

#test
if __name__ == "__main__":

    Fore.rgb('100%', '50%', '30%')
    words, file_path = load_words()

    print(f"{Fore.white}{Back.green}Filtrage :{Style.reset}", filter_words_by_length(words, 5))
    print(f"{Fore.white}{Back.green}Filtrage hard:{Style.reset}", filter_words_by_length(words, 7))

    words = add_word(words, "example", file_path)
    print(f"{Fore.white}{Back.green}Après ajout :{Style.reset}", words)

    words = delete_word(words, "example", file_path)
    print(f"{Fore.white}{Back.green}Après suppression :{Style.reset}", words)