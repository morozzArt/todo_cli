from Note import Note
from common_func import get_last_id, set_last_id
import os


class Adder:
    @classmethod
    def add_note(cls, text):
        last_id = get_last_id("/home/" + os.getlogin() + "/.todo/")
        note = Note(text, last_id)
        with open("/home/" + os.getlogin() + "/.todo/" + 'store.txt', 'a') as f:
            note.to_file(f)

        set_last_id(last_id + 1, "/home/" + os.getlogin() + "/.todo/")

    @classmethod
    def reset(cls):
        username = os.getlogin()
        filepath = "/home/" + username + "/.todo/"
        set_last_id(1, filepath)
        f = open(filepath + "store.txt", 'w')
        f.close()
