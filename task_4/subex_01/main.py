from external_libs.database_saver import DatabaseSaver
from subex_01.extended_saver import ExtendedDatabaseSaver

def do_something(saver):
    saver.save_data(data=None)

def main():
    base_saver = DatabaseSaver()
    extended_saver = ExtendedDatabaseSaver(base_saver, email="user@example.com")
    do_something(extended_saver)

if __name__ == "__main__":
    main()
