import streamlit as st
from exercise import Dog


animal1, animal2, animal3, animal4, animal5, = st.tabs(["Dog", "Cat", "Parrot", "Owl", "Snake"])


with animal1:

    dog = Dog(3)
    
    st.image("https://static.streamlit.io/examples/dog.jpg", width=300)

    if st.button("Speak", key="dog_speak"):
        dog.speak()

    if st.button("Move", key="dog_move"):
        dog.move()


# with animal2:
#     st.image("https://www.rover.com/blog/wp-content/uploads/iStock-1014250732-1200x675.jpg", width=500)

#     if st.button("Speak", key="cat"):
#         pass
#         Cat.speak()
 

with animal3:
    st.image("https://static.standard.co.uk/s3fs-public/thumbnails/image/2015/02/02/08/katyperry0202d.jpg?width=1200", width=1200)
    
    if st.button("Speak", key="Lion"):
        pass        
        Lion.speak()
        

# with animal4:
#     st.image("https://i.redd.it/rfsd49kkc6w91.png", width=300)
#     if st.button("Speak", key="owl"):
#         pass
#         Owl.speak()

# with animal5:
#     st.image("https://thumbs.dreamstime.com/b/taipan-19351372.jpg", width=450)
#     if st.button("Speak", key="snake"):
#         pass
#         Snake.speak()
