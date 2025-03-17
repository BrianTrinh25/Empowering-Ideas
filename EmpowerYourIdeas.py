import os
import openai
import streamlit as st 
import time
# from IPython.display import Image, display
from openai import OpenAI
import pandas as pd
import toml

#my-api-key-here
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI() 

#st.set_page_config(layout="wide", initial_sidebar_state="expanded")
#st.sidebar.image("Logo.jpg", use_column_width=True)

col1, col2 = st.columns([1, 4])
with col1:
    st.image("Logo.jpg", width=125)
with col2:
    st.header("Empower Your Ideas", divider="blue")

# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": f"You are an expert AI researcher and developer.  First, summarize the {articles}.\
         Based on the summary, list the problems for all stakeholders.  Then, clearly explain how each stakeholder's needs can be met.\
        Suggest some creative project ideas to address the {problem} and incorporate the {technologies} along with {oth_technologies}.\
        For each of the {technologies} and {oth_technologies}, provide an example of how the project could be implemented in real life.\
        Finally, provide sample {datasets} related to the {problem} formatted in a table.  Organize the information using bolded \
        headings, add bullet points, and incorporate emojis.  Provide consistent output for the user every time." },
        {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content

def get_image(response):
    response = client.images.generate(
        model="dall-e-3",
        prompt=major,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    return response.data[0].url


# create our streamlit app
st.caption("Welcome to Empower Your Ideas, the ultimate platform for students to brainstorm and develop projects that contribute to a better world. \
           Here, we encourage you to harness your creativity and passion to create new AI-powered solutions. Together, we can build a sustainable future!")

with st.form(key = "chat"):
    # add questions here
    problem = st.text_input("Please enter the community problem you're trying to solve:")
    articles = st.text_area("Enter the website links associated with your chosen problem:")
    technologies = st.multiselect("**Select the technologies you're interested in:**", ["Text Generation", "Image Generation", "Speech to Text", "Text Summarization", "Key Point Extraction", "Action Item Extraction", "Sentiment Analysis", "Language Translation", "Text to Speech", "Computer Vision", "Chatbot"])
    delimiter = ', '    
    oth_technologies = st.text_input("If your preferred technologies aren't listed, enter them here:")
    datasets = st.text_input("List any datasets you might consider including:")
    submitted = st.form_submit_button("Submit")

    prompt = f"For a community member solving {problem} who is interested in experimenting with {technologies}, reading {articles}, and plans to use {datasets}"
    # response = 

    with st.spinner("Here we go!"):
        time.sleep(5)

    if submitted:
        st.success("Gathering project ideas...")
        st.write(get_completion(prompt))            
        # st.image(get_image(response), caption="")
        st.caption("We hope you found these project ideas inspiring! By aligning your projects with issues \
                   facing the City of San Jose, you can make a real impact on global issues and contribute to \
                   a more sustainable future. If you would like to explore more project ideas, feel free to \
                   rerun this application. Thank you for using Empower Your Ideas, and best of luck with your projects!")



