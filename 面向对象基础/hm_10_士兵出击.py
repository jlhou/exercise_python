class Gun:
    def __init__(self, model, bullet_count):
        self.model = model
        self.bullet_count = bullet_count

    def add_bullet(self, add_numbers):
        self.bullet_count += add_numbers
        print("装填子弹%d颗" % add_numbers)
        print("弹夹还剩%d颗" % self.bullet_count)
        return self.bullet_count

    def shoot(self, shoot_numbers):
        self.bullet_count -= shoot_numbers
        print("发射后弹夹还剩%d" % self.bullet_count)
        return self.bullet_count


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun
        self.gun.bullet_count = gun.bullet_count

    def fire(self, numbers):
        if self.gun.bullet_count <= numbers:
            print("子弹不够啦，请装填子弹")
            return self.gun.bullet_count
        else:
            self.gun.bullet_count = self.gun.shoot(numbers)
            return self.gun.bullet_count

    def add_bullet(self, numbers):
        self.gun.bullet_count = self.gun.add_bullet(numbers)


ak47 = Gun("AK47", 20)
xusanduo = Soldier("xusanduo", ak47)
xusanduo.fire(10)
xusanduo.add_bullet(10)
xusanduo.add_bullet(20)
xusanduo.fire(50)
xusanduo.add_bullet(10)
