import os
import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
# from dotenv import main
# main.load_dotenv()

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    -Properly format the email
    -Convert the input text to a specific tone
    -Convert the input to a specific dialect

    Here are some exampe differnt Tones:
    -Formal: We wnt to Barcelona for the weekend. We have a lot of things to tell you.
    -Informal: Went to Barcelona for the weekend. Lots to tell you.

    Here are some examples of words in different dialects:
    -American English: French Fries, cotton candy, apartment, garbage, cookie
    -British English: chips, candyfloss, flag, rubbish, biscuit

    Below is the email, tone and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}

    YOUR RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template
)

def load_LLM():
    """Logic for loading the chain you want to use should go here"""
    llm = OpenAI(temperature=.5)
    return llm

llm = load_LLM()


st.set_page_config(page_title="Globalize Email", page_icon=":ronot:")
st.header("Globalize Text")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Often professionals would like to improve their emails, but don't have the skills to do so. This tool will help you improve your email skills by converting your emails into a more professional format. This tool is powered by [LangChain](www.langchain.com) and [OpenAI](https://openai.com) and made by @GregKamradt.View Source Code on [Github](www.github.com)")

with col2:
    st.image(image='IMG_0017.JPG',width=500, caption='')

st.markdown('## Enter Your Email To Convert')

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox("Which tole would you like your email to have?",('Formal','Informal'))

with col2:
    option_dialect = st.selectbox("Which English dialect would you like?",('American English','British English'))

def get_text():
    input_text = st.text_area(label="", placeholder="Your Email...", key="email_input")
    return input_text

email_input = get_text()

st.markdown('## Your converted Email:')

if email_input:
    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)
    formatted_email = llm(prompt_with_email)
    st.write(formatted_email)
