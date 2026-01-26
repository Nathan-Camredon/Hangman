# Fichier word_list.py

import os
import random
from colored import Fore, Back, Style

def load_words():
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(base_dir, '..', 'data', 'words.txt')        
    words = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words.append(line.strip().lower())
    return words

def filter_words_by_length(words, length):
    difficulty_list = []
    #difficulty hard = words longer than 6 letters
    if length > 6:
        for word in words:
            if len(word) > 6:
                difficulty_list.append(word)
        return difficulty_list
    #difficulty easy = words shorter than or equal to 6 letters
    elif length < 6:
        for word in words:
            if len(word) <= length:
                difficulty_list.append(word)
    else:
        difficulty_list = words
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

def words_selector(difficulty):
    """
    Selects a random word from the dictionary based on the specified difficulty level.

    Args:
        difficulty (int): The difficulty level (0-3).
                          0: 5-letter words
                          1: 6-letter words
                          2: 7-letter words
                          3: 8-letter words

    Returns:
        str: A random word matching the difficulty length.
             Returns a random word from the full list if no match is found (fallback).
             Returns None if the word list is empty.
    """
    words= load_words()
    
    # Mapping difficulty index to word length
    # 0 -> 5, 1 -> 6, 2 -> 7, 3 -> 8
    target_length = 5 + difficulty
    
    filtered_words = filter_words_by_length(words, target_length)
    if filtered_words:
        return random.choice(filtered_words)
    
    # Fallback: if no words match the criteria, return a random word from the full list
    if words:
        return random.choice(words)
        
    return None



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