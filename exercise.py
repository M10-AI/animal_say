import streamlit as st
class Animal:

    def __init__(self, legs): # Constructor
        self.__legs = legs # Encapsulation: legs attribute cannot be accessed publicly

    @property #getter
    def legs(self):
        return self.__legs

    @legs.setter #setter
    def legs(self, legs):

        if isinstance(legs, int) and legs >= 0:
            self.__legs = legs
        else:
            raise ValueError("Fuck you")        

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal): # Inheritance

    def speak(self): # Abstraction & Method overriding 
        st.write("Woff")
    
    def move(self): # Abstraction &  Method overriding
        st.write(f"Move with {self.legs} legs") # Polymoprhism

# Leo: T-rex

# Joseph: Lion-King
class Lion(Animal):

    def speak(self):
        st.write("You gonna hear my roar!")

    def move(self):
        st.write(f"Move with {self.legs} legs")

# Sharik: High Koala

# Johan: Gorilla

# Frank: Elephant




