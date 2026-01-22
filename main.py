from modules.games import games
from modules.games import games_difficulty
from modules.graphic_ui import menu, screen
from modules.delete_word_page import DeleteWordPage
from modules.add_word_page import AddWordPage
from modules.words_list import WordsListPage

state = "words_list"
current_page = WordsListPage(
    screen,
    on_back=lambda: set_state("menu"),
    on_add=lambda: set_state("add_word"),
    on_delete=lambda word: set_delete_word(word)
)
def main():
    while True: 
        difficulty = 0
        menu()
if __name__ == "__main__":
    main()

def set_delete_word(word):
    global current_page, state
    state = "delete_word"
    current_page = DeleteWordPage(screen, word, on_back=lambda: set_state("words_list"))

def set_state(new_state):
    global state, current_page
    state = new_state

    if new_state == "words_list":
        current_page = WordsListPage(screen, on_back=lambda: set_state("menu"),
                                     on_add=lambda: set_state("add_word"),
                                     on_delete=lambda word: set_delete_word(word))

    elif new_state == "add_word":
        current_page = AddWordPage(screen, on_back=lambda: set_state("words_list"))
