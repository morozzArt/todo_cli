import os
import json
from Note import Note


class Shower:
    @classmethod
    def get_list_note(cls):
        note_list = []
        with open("/home/" + os.getlogin() + "/.todo/" + 'store.txt', 'r') as f:
            for line in f:
                word = line.split(",")
                if word[1] == "True":
                    status = True
                else:
                    status = False
                note = Note(word[3].strip(), word[0], status, word[2])
                note_list.append(note)

        return note_list
