import uuid
import datetime
class Note:
    def _init_(self,id = str(uuid.uuid1()[0:3]), title = " ", body = " ", date = str(datetime.now())):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date