from .interfaces import IDatabaseSaver

class DatabaseSaver(IDatabaseSaver):
    def save_data(self, data):
        print("Data saved to the database")
