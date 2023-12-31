import numpy as np

"""
Module to menage persons object
"""


class Person:
    """
    Class which represent Persons

    """

    def __init__(self, name, age):
        """
        Creating Person object and attributes to it name and age
        :param name: Name of person
        :type name: str
        :param age:
        :type age: int
        """
        self.name = name
        self.age = age

    def personHello(self):
        """
        Function to say HELLO by person which introduce yourself
        :rtype: NoneType
        """
        print("Hello my name is " + self.name)

    def __str__(self):
        """
        Function override string representation of object
        :return: Name and age of person
        :rtype: str
        """
        return f"{self.name} ({self.age} yo)"


def show_all(persons):
    """
    Function to print all Persons from parameter
    :param persons: collection of Person objects
    :type persons: numpy.ndarray
    :rtype: NoneType
    """
    print("\nAll persons in collection")
    for p in persons:
        print(p)


if __name__ == '__main__':
    """
    Some test of working program
    """
    p1 = Person("John", 36)
    p2 = Person("Ann", 46)
    p3 = Person("Emma", 31)
    p4 = Person("Lucas", 22)
    collection = np.array([p1, p2, p3, p4])
    a = p1.personHello()
    print(p1)
    show_all(collection)
