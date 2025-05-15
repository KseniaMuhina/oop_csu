class LogImporter:
    def __init__(self, reader):
        self._reader = reader

    def import_logs(self, source: str):
        file = self._reader.read_log_file(source)
        print(f"Imported: {file}")
