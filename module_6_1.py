class Animal:  # Содержит подклассы Mammal и Predator


    alive = True  # Атрибуты класса Animal
    fed = False

    def __init__(self, name):  # Базовый класс иерархии. При вызове не принимает аргументов и возвращает
        # новый экземпляр, не имеющий атрибутов.
        self.name = name

    def eat(self, food):  # Метод класса Animal.
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:  # Содержит подклассы Flower и Fruit
    edible = False

    def __init__(self, name):  # Переопределяется в Fruit
        self.name = name
        self.edible = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)  # используется для вызова метода родительского класса Plant из дочернего Fruit.

        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)