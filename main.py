import streamlit as st
from exercise import Dog, Cat, Parrot, Owl, Snake


animal1, animal2, animal3, animal4, animal5, = st.tabs(["Dog", "Cat", "Parrot", "Owl", "Snake"])


with animal1:
    st.image("https://static.streamlit.io/examples/dog.jpg", width=300)

    if st.button("Speak", key="dog"):
        Dog.speak()

with animal2:
    st.image("https://www.rover.com/blog/wp-content/uploads/iStock-1014250732-1200x675.jpg", width=500)

    if st.button("Speak", key="cat"):
        pass
        Cat.speak()
 

with animal3:
    st.image("https://i.pinimg.com/736x/c7/23/7e/c7237edf3dbef9e0aefb00cfa3fe9f29.jpg", width=500)
    
    if st.button("Speak", key="parrot"):
        pass        
        Parrot.speak()

with animal4:
    st.image("https://i.redd.it/rfsd49kkc6w91.png", width=300)
    if st.button("Speak", key="owl"):
        pass
        Owl.speak()

with animal5:
    st.image("https://thumbs.dreamstime.com/b/taipan-19351372.jpg", width=450)
    if st.button("Speak", key="snake"):
        pass
        Snake.speak()
