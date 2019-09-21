import json
from datetime import datetime


class Note:
    def __init__(self, text, id, status=False, date=datetime.now()):
        self.id = id
        self.status = status
        self.date = date.__str__()
        self.text = text

    def set_status(self, new_status):
        self.status = new_status

    @property
    def get_symbol_status(self):
        if self.status:
            return "+"
        else:
            return "-"

    def set_date(self, date):
        self.date = date

    @property
    def get_date(self):
        return self.date

    def set_text(self, text):
        self.text = text

    @property
    def get_text(self):
        return self.text

    def set_id(self, id):
        self.id = id

    @property
    def get_id(self):
        return self.id

    def to_file(self, file):
        file.write(str(self.id) + "," + str(self.status) + "," + self.date + "," + self.text + "\n")