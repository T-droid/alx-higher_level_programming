#!/usr/bin/python3

"""module to define a class"""


class Student:
    """class to define a student"""
    def __init__(self, first_name, last_name, age):
        """initialisation method
        Args:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary reprentaion of student"""
        return vars(self)

