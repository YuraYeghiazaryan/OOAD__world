import time
import nature as nt


class World:
    def __init__(self):
        self.light = True
        self.tree = nt.Tree()
        self.frog = nt.Frog()
        self.sun = nt.Sun()
        self.grass = nt.Grass()

    def change_day(self):
        if second >= half_day:
            self.light = False
            print("Մութը ընկավ")
            print()


    def make_day(self):
        print(self.sun.is_shine(self.light))
        print(self.tree.photosynthesis(self.light))
        #self.frog.awake()
        self.frog.is_awake(self.light)
        print(self.frog.walk())
        print(self.frog.breathe())
        print(self.frog.eat())
        print()


while True:
    second = 0
    minute = 0
    hour = 0
    day_times = int(input("Enter the length of the day: in seconds \n"))

    half_day = day_times / 2

    world = World()
    print("Լույսը բացվեց")
    print()
    for i in range(day_times):
        time.sleep(1)
        world.change_day()
        world.make_day()
        second += 1
        if second % 60 == 0:
            minute += 1
        if minute % 60 == 0:
            hour += 1



