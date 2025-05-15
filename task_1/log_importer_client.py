from log_importer import LogImporter
from log_reader import FileLogReader
from ftp_log_reader import FtpLogReader

def do_method():
    source = "ftp://log.txt"

    if source.startswith("ftp://"):
        reader = FtpLogReader("user123", "securepass")
    else:
        reader = FileLogReader()

    importer = LogImporter(reader)
    importer.import_logs(source)

if __name__ == "__main__":
    do_method()
