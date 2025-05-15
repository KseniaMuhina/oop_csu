class SaveObserver:
    def on_save(self, data):
        raise NotImplementedError

class MailObserver(SaveObserver):
    def __init__(self, email):
        self.email = email

    def on_save(self, data):
        from external_libs.mail_sender import MailSender
        MailSender().send(self.email)

class CacheObserver(SaveObserver):
    def on_save(self, data):
        from external_libs.cache_updater import CacheUpdater
        CacheUpdater().update_cache()
