import streamlit as st
import pickle

# Model aur Vectorizer load karein
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("📩 SMS Spam Classification App")
st.write("Apna message text box mein likhein aur check karein ke yeh Spam hai ya Legit!")

user_input = st.text_area("Message Input:", "")

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Pehle koi message type karein!")
    else:
        data = [user_input]
        vectorized_data = vectorizer.transform(data)
        prediction = model.predict(vectorized_data)
        
        if prediction[0] == 1:
            st.error("🚨 Yeh message **SPAM** hai!")
        else:
            st.success("✅ Yeh message **Legit (HAM)** hai!")