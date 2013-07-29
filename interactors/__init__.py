__author__ = 'Stas'


class CommonInteractor(object):
    pass


class Auth(object):
    interactors = {'jira': None, 'wiki': None, 'code': None, 'sonar': None}

    def __init__(self, settings=set()):
        pass

    def add_interactor(self, interactor):
        pass

    @property
    def jira(self):
        return self.interactors.get('jira', None)
