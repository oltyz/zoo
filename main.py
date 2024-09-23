# Базовый класс Animal (Животное)
class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах")

    def eat(self):
        return f"{self.name} ест."


# Подклассы для различных типов животных
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # Размах крыльев

    def make_sound(self):
        return f"{self.name} чирикает!"

    def fly(self):
        return f"{self.name} летит."


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # Цвет меха

    def make_sound(self):
        return f"{self.name} рычит!"

    def run(self):
        return f"{self.name} бежит."


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # Тип чешуи

    def make_sound(self):
        return f"{self.name} шипит!"

    def crawl(self):
        return f"{self.name} ползет."


# Функция, демонстрирующая полиморфизм
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Классы для сотрудников зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name  # Имя сотрудника

    def feed_animal(self, animal):
        return f"Смотритель {self.name} кормит {animal.name}."


class Veterinarian:
    def __init__(self, name):
        self.name = name  # Имя ветеринара

    def heal_animal(self, animal):
        return f"Ветеринар {self.name} лечит {animal.name}."


# Класс зоопарка с композицией
class Zoo:
    def __init__(self, name):
        self.name = name  # Название зоопарка
        self.animals = []  # Список животных
        self.staff = []    # Список сотрудников

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_to_file(self, filename):
        # Открываем файл с указанием кодировки utf-8
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Зоопарк: {self.name}\n")
            f.write("Животные:\n")
            for animal in self.animals:
                f.write(f"- {animal.name}, Возраст: {animal.age}\n")
            f.write("Сотрудники:\n")
            for staff_member in self.staff:
                f.write(f"- {staff_member.name}, Роль: {staff_member.__class__.__name__}\n")

    def load_from_file(self, filename):
        # Открываем файл с указанием кодировки utf-8
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.readlines()
        # В реальной программе нужно дополнить логику восстановления объектов из файла


# Пример использования программы
if __name__ == "__main__":
    # Создаем животных
    parrot = Bird("Попугай", 3, 0.5)
    lion = Mammal("Лев", 5, "золотистый")
    snake = Reptile("Змея", 2, "гладкая")

    # Демонстрируем полиморфизм
    animal_sound([parrot, lion, snake])

    # Создаем сотрудников
    keeper = ZooKeeper("Иван")
    vet = Veterinarian("Анна")

    # Создаем зоопарк и добавляем в него животных и сотрудников
    zoo = Zoo("Сафари Парк")
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Сохраняем информацию о зоопарке в файл с правильной кодировкой
    zoo.save_to_file("информация_о_зоопарке.txt")

    # Пример работы сотрудников
    print(keeper.feed_animal(lion))
    print(vet.heal_animal(snake))
