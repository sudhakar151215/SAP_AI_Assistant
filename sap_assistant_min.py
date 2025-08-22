import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# .env file load करो
load_dotenv()

# Secret use करो
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="SAP Business One AI Assistant")

st.markdown("<h1 style='color:green;'>🟢 SAP Business One AI Assistant</h1>", unsafe_allow_html=True)
st.write("Ask me anything about SAP B1:")

# Input box
question = st.text_input("Your question", "")

if st.button("Ask"):
    if not question.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        try:
            # ✅ Call Groq API
            response = client.chat.completions.create(
                model="llama3-8b-8192",   # Groq free model
                messages=[
                    {"role": "system", "content": "You are an expert in SAP Business One. Answer queries clearly."},
                    {"role": "user", "content": question}
                ],
                temperature=0.2,
                max_tokens=500
            )

            # ✅ Show answer
            answer = response.choices[0].message.content
            st.success(answer)

        except Exception as e:
            st.error(f"Error: {str(e)}")
