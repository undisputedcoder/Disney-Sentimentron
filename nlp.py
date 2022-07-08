import streamlit as st
import tensorflow as tf

st.markdown('## 🎡🏰🚝🎠🪧🎈✨🍬🎆🎇🎪')
st.title('Disneyland Reviews Classification')

model_1 = tf.keras.models.load_model('model_1')
sentiment = {0: 'negative', 1: 'positive'}

review = st.text_area('Enter a review of your experience at Disneyland', height=350)

if st.button('Submit'):
    pred_prob = tf.squeeze(model_1.predict([review]))
    pred = tf.round(pred_prob)
    st.markdown(f"The review is {tf.cast(pred_prob*100, tf.uint8)}% **{sentiment[int(pred)]}**")
    #print(f"pred {int(pred)}, prob {pred_prob}")