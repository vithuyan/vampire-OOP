class Vampire:

    coven = []

    def __init__(self, name, age, in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today


    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        new_vampire = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(new_vampire)
        return new_vampire

        def drink_blood(self):
         self.drank_blood_today = True
         return self.drank_blood_today


    @classmethod
    def sunrise(cls):
        for num in range(0, len(cls.coven)):
            current_vampire = cls.coven[num]
            if not current_vampire.in_coffin or not current_vampire.drank_blood_today:
                Vampire.coven.remove(current_vampire)
        return Vampire.coven


    @classmethod
    def sunset(cls):
        for num in range(0, len(cls.coven)):
            current_vampire = cls.coven[num]
            current_vampire.drank_blood_today = False
            current_vampire.in_coffin = False


    def go_home(self):
        self.in_coffin = True
