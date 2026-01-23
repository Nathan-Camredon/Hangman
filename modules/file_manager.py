from pathlib import Path

WORDS_FILE = Path(__file__).parent / "data" / "words.txt"

def load_words():
    if not WORDS_FILE.exists():
        return print("Erreur : fichier words.txt introuvable"), []
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        return [w.strip() for w in f.readlines()]

def save_words(words):
    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(words))