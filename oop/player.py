class Player:

    def __init__(self, name):
        self.name = name;
        self._level = 5

    def get_level(self):
        return self._level

    def set_level(self, level):
        self._level = level

    level = property(get_level, set_level)
