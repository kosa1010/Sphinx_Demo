import numpy as np

"""
Module to menage dogs object
"""


class Dog:
    """
    Class which represent Dogs
    """

    def __init__(self, name, age):
        """
        Creating Dog object and attributes to it name and age
        :param name: Name of dog
        :type name: str
        :param age: Age of dog
        :type age: int
        """
        self.name = name
        self.age = age

    def dogWoof(self):
        """
        Function to say WOOF by dog which introduce yourself
        :rtype: NoneType
        """
        print("Woof my name is " + self.name)

    def __str__(self):
        """
        Function override string representation of object
        :return: Name and age of dog
        :rtype: str
        """
        return f"{self.name} ({self.age} yo)"


def show_all(dogs):
    """
    Function to print all Dogs from parameter
    :param dogs: collection of Dog objects
    :type dogs: numpy.ndarray
    :rtype: NoneType
    """
    print("\nAll dogs in collection")
    for p in dogs:
        print(p)


if __name__ == '__main__':
    """
    Some test of working program
    """
    p1 = Dog("John", 6)
    p2 = Dog("Ann", 4)
    p3 = Dog("Emma", 1)
    collection = np.array([p1, p2, p3])
    a = p1.dogWoof()
    print(p1)
    show_all(collection)
