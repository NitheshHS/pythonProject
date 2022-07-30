class Enemy:

    def __init__(self, name="enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points > 0:
            self.hit_points = remaining_points
            print(f"I took damage {damage} and remaining hit points {self.hit_points}")
        else:
            self.lives -= 1

    def __str__(self):
        return f"name: {self.name} hit_points: {self.hit_points} lives: {self.lives}"


class Troll(Enemy):

    def __init__(self, name):
        #Enemy.__init__(self, name=name, hit_points=10, lives=1)
        super(Troll, self).__init__(name=name, hit_points=1, lives=1)
