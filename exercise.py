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

# Sharik: High Koala
class Koala(Animal):
    def __init__(self, legs):
        super().__init__(legs)
        self.move_responses = ["Nah, I think I'll stay", "In your dreams", "Maybe another day", "no", "Can you stop", "I'm not going to move", "...."]
        self.move_responses_i = 0

    def speak(self):
        st.write("Hi~")
    
    def move(self):
        st.write(self.move_responses[self.i])
        self.i += 1

# Johan: Gorilla

# Frank: Elephant




