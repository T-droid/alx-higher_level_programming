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

    def to_json(self, attrs=None):
        """retrieves dictionary representaion of student
        Args:
            attrs: attributes
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the student
        Args:
            json: dictionary to replace the student attributes
        """
        for key, value in self.__dict__.items():
            for key1, value1 in json.items():
                key = key1
                self.__dict__[key] = value1
