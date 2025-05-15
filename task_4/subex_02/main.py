from external_libs.database_saver import DatabaseSaver
from subex_02.observable_saver import ObservableSaver
from subex_02.observer import MailObserver, CacheObserver

def do_something(saver):
    saver.save_data(data=None)

def main():
    base = DatabaseSaver()
    observable = ObservableSaver(base)
    observable.add_observer(MailObserver("user@example.com"))
    observable.add_observer(CacheObserver())

    do_something(observable)

if __name__ == "__main__":
    main()
