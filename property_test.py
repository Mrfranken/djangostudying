class SessionHandler(object):
    HELLO = None

    def __init__(self):
        self.num = 2

    def create_session(self):
        print('hello world')

class MegazoneClient(object):
    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self._session_handler = None

    @property
    def session_handler(self):
        print('second time to call this')
        if not self._session_handler:
            raise RuntimeError("you need to create session first.")
        return self._session_handler

    @session_handler.setter
    def session_handler(self, session):
        print('first time to call this')
        self._session_handler = session
        print(type(self._session_handler))

    def create_session(self):
        self.session_handler = SessionHandler()
        self.session_handler.create_session()

if __name__ == '__main__':
    mc = MegazoneClient()
    mc.create_session()
