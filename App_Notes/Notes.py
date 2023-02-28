import datetime

class Notes:
    def __init__(self, id_notes: int, title: str, body_notes: str, date_last: datetime.datetime):   
        self.id_notes = id_notes
        self.title = title
        self.body_notes = body_notes
        self.date_last = date_last

    def __str__(self):
        return f'№{self.id_notes}. {self.title} - {self.body_notes}. {self.date_last.strftime("%Y-%m-%d-%H:%M:%S")}' 