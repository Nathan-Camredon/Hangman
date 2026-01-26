from pathlib import Path
import random

WORDS_FILE = Path(__file__).parent.parent / "data" / "words.txt"

def load_words():
    words = []
    if not WORDS_FILE.exists():
        return print("Erreur : fichier words.txt introuvable"), []
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().lower())
    return words

def save_words(words):
    words[-1] = words[-1].lower()
    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(words))

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