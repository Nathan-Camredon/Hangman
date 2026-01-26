from pathlib import Path

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