class Bird:

    def __init__(self, name="bird", canfly=True):
        self.name = name
        self.canfly = canfly

    def __str__(self):
        return f"name: {self.name} canfly={self.canfly}"
