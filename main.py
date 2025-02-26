import streamlit as st
from exercise import Dog, Koala


animal1, animal2, animal3, animal4, animal5, = st.tabs(["Dog", "Cat", "Parrot", "Koala", "Snake"])


with animal1:

    koala = Dog(3)
    
    st.image("https://static.streamlit.io/examples/dog.jpg", width=300)

    if st.button("Speak", key="dog_speak"):
        koala.speak()

    if st.button("Move", key="dog_move"):
        koala.move()


# with animal2:
#     st.image("https://www.rover.com/blog/wp-content/uploads/iStock-1014250732-1200x675.jpg", width=500)

#     if st.button("Speak", key="cat"):
#         pass
#         Cat.speak()
 

# with animal3:
#     st.image("https://i.pinimg.com/736x/c7/23/7e/c7237edf3dbef9e0aefb00cfa3fe9f29.jpg", width=500)
    
#     if st.button("Speak", key="parrot"):
#         pass        
#         Parrot.speak()

with animal4:
    koala = Koala(4)
    
    st.image("https://cdn.britannica.com/26/162626-050-3534626F/Koala.jpg?w=300", width=300)

    if st.button("Speak", key="koala_speak"):
        koala.speak()

    if st.button("Move", key="koala_move"):
        koala.move()

# with animal5:
#     st.image("https://thumbs.dreamstime.com/b/taipan-19351372.jpg", width=450)
#     if st.button("Speak", key="snake"):
#         pass
#         Snake.speak()
