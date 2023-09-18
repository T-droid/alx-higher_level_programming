#!/usr/bin/python3

"""base class"""

import turtle as t
import json
import csv
class Base:
    """base class"""
    __nb_object = 0

    def __init__(self, id=None):
        """initialisation method
        Args:
            id(int): identity no
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON representation of list dictionaries
        Args:
            list_dictionaries: dictionary to be converted to JSON
        Return: a JSON representation
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a JSON string representation of list_objs
        Args:
            list_objs: a list of instances who inherits from base
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as f:
            f.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary: a double pointer to a dictionary
        Returns: an instance of all attributes set
        """
        r1 = cls(10, 10, 10, 10)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        """loads from a json file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                content = f.read()

        except FileNotFoundError:
            return []

        dict_list = cls.from_json_string(content)
        instances = [cls.create(**dictionary) for dictionary in dict_list]

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves instances to a CSV file
        Args:
            list_objs: List of instances that inherit from base
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            csvwriter = csv.writer(f)

            if list_objs:
                # Use the first object to determine the attributes dynamically
                attributes = list_objs[0].to_dictionary().keys()

                # Write the header row based on class attributes
                csvwriter.writerow(["id"] + list(attributes))

                # Write the data rows
                for obj in list_objs:
                    csvwriter.writerow([getattr(obj, attr) for attr in ["id"] + list(attributes)])

    @classmethod
    def load_from_file_csv(cls):
        """method to load from csv file"""
        data_list = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r') as f:
            csvreader = csv.reader(f)

            for row in csvreader:
                data_list.append(row)
        return data_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """method to draw a shape
        Args:
            list_rectangle: all instance of rectangles
            list_square: all instance of squares
        """
        window = t.Screen()
        pen = t.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
