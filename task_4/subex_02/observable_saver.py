from external_libs.interfaces import IDatabaseSaver

class ObservableSaver(IDatabaseSaver):
    def __init__(self, saver):
        self._saver = saver
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def save_data(self, data):
        self._saver.save_data(data)
        for obs in self._observers:
            obs.on_save(data)
