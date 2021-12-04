class Proxy():
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            return self._real_subject.request()

    def check_access(self):
        print("Revisando acceso a la api de sensores")
        return True
