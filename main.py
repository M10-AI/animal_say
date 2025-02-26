import streamlit as st
from exercise import Dog, T_Rex


animal1, animal2, animal3, animal4, animal5, animal6 = st.tabs(["Dog", "T-rex", "Gorilla", "Lion", "Elephant", "Koala"])


with animal1:

    dog = Dog(3)
    
    st.image("https://static.streamlit.io/examples/dog.jpg", width=300)

    if st.button("Speak", key="dog_speak"):
        dog.speak()

    if st.button("Move", key="dog_move"):
        dog.move()


with animal2:
    st.image("https://a.silvergames.com/j/b/t-rex.jpg", width=500)

    if st.button("Speak", key="t_rex"):
        pass
        T_Rex.speak()
 

with animal3:
    st.image("https://i.pinimg.com/736x/c7/23/7e/c7237edf3dbef9e0aefb00cfa3fe9f29.jpg", width=500)
    
    if st.button("Speak", key="gorilla"):
        pass        
#        gorilla.speak()

with animal4:
    st.image("https://static.standard.co.uk/s3fs-public/thumbnails/image/2015/02/02/08/katyperry0202d.jpg?width=1200", width=1200)
    if st.button("Speak", key="lion"):
        pass
 #       Owl.speak()

with animal5:
    st.image("https://thumbs.dreamstime.com/b/taipan-19351372.jpg", width=450)
    if st.button("Speak", key="elephant"):
        pass
  #      Snake.speak()

with animal6:
    st.image("https://thumbs.dreamstime.com/b/taipan-19351372.jpg", width=450)
    if st.button("Speak", key="koala"):
        pass
   #     koala.speak()
