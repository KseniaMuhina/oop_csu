from external_libs.interfaces import IDatabaseSaver
from external_libs.mail_sender import MailSender
from external_libs.cache_updater import CacheUpdater

class ExtendedDatabaseSaver(IDatabaseSaver):
    def __init__(self, saver, email: str):
        self._saver = saver
        self._email = email
        self._mail_sender = MailSender()
        self._cache_updater = CacheUpdater()

    def save_data(self, data):
        self._saver.save_data(data)
        self._mail_sender.send(self._email)
        self._cache_updater.update_cache()
