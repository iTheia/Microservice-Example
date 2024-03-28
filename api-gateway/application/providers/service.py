class ServiceManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.urls = {}
        return cls._instance

    def add_service(self, name, url):
        self.urls[name] = url

    def remove_service(self, name):
        if name in self.urls:
            del self.urls[name]

    def get_url(self, name):
        return self.urls.get(name, "")
