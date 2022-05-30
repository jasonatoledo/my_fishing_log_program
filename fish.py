# -*- coding: utf-8 -*-
"""
Jason Toledo
Class: CS 521 - Fall 1
Date: 10/18/2021
Homework Problem # Final Project user-defined Class
"""

class Fish(object):
    """this is a class that establishes Fish instances and has methods to
    update the values of the instance's habitat and taste based on the
    available constants."""
    TASTES = ["okay","bad","good","yummy","delicious","weird","unknown"]
    HABITATS = ["bay","lake","ocean"]
    
    def __init__(self, species = "new_fish", habitat = "new_place",\
                 taste= "okay"):
        """this initializes an instance of Fish and takes 3 string parameters.
        the parameters are: species, habitat, and taste"""
        self.species = species
        self.__habitat = habitat
        self.taste = taste

        
    def __str__(self):
        """built in method used to describe an instance of fish"""
        return "{} is part of the {} habitat and tastes {}".format\
            (self.species, self.__habitat, self.taste)
    
    def __repr__(self):
        """built in Python method to allow the instance to call itself with
        only the instance name"""
        return self.__str__()
    
    def __set_habitat(self, new_habitat):
        """this method will accepts a new habitat in the HABITATS list as its 
        parameter and will update the current habitat of the fish instance"""
        if new_habitat in Fish.HABITATS:
            self.__habitat = new_habitat
        else:
            print("please enter a valid habitat value in the HABITAT list.")
        return "the new habitat for {} is {}".\
            format(self.species, self.__habitat)
            
    def update_taste(self, taste):
        """this is a private method that will modify the instance of the
        fish's taste attribute with a string value in the TASTES list."""
        if taste in Fish.TASTES:
            self.taste = taste
        else:
            print("please enter a valid taste value in the TASTES list.")
        return "the updated taste value for {} is {}".\
            format(self.species, self.taste)
    
    def __eq__(self, second_fish):
        """this is an equality magic method that will identify whether a
        fish is the same species or not for a user"""
        return (self.species == second_fish.species)
    
# run unit tests with assert statements
if __name__ == '__main__':
    fish1 = Fish()
    assert fish1.update_taste("weird")
    assert fish1._Fish__set_habitat("lake")
    fish2 = Fish()
    assert fish1 == fish2
    
    
    
    
    
    