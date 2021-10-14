# import dataclass in order to create dataclasses
from dataclasses import dataclass, field


# classes using the normal class creation:
class Person:
    name: str
    job: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age


@dataclass(order=True, frozen=False)  # the order argument provide ordering for the instances, forzen arg provided read_only instances
class Persona:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self):
        return f'{self.name}, {self.job}, {self.age} years old'


person1 = Person("Geralt", "Carpenter", 36)
person2 = Person("Maria", "Developer", 23)
person3 = Person("Romero", "Actress", 78)

persona1 = Persona("Geralt", "Carpenter", 36, 8)
persona2 = Persona("Maria", "Developer", 23)
persona3 = Persona("Romero", "Actress", 78)


if __name__ == '__main__':
    # printing old instances
    print(id(person2))
    print(id(person3))
    print(person1)

    # printing new dataclass instances
    print(persona1)
    print(id(persona2))
    print(id(persona3))
    print(persona3 == persona2)
    print(persona1 < persona2)
