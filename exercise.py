import streamlit as st

class Animal:

    def __init__(self, legs):
        self.legs = legs

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def move():
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):

    def speak(): #Method overriding
        st.write("Woff")
    
    def move(self): #Method overriding
        print(f"Move with {self.legs} legs")


