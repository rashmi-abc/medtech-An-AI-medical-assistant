"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import google.generativeai as genai
import streamlit as st


genai.configure(api_key="AIzaSyBCMezv0Z4EHJn401DHiycKGvRP7Yr6t-4")

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


model = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
st.image("tony.png",width=100)
st.title("MeDTech-Your medical assistant")
st.subheader("An application- Prescription Analyser using images ")
exp=st.expander("Want to know about me?")
exp.write('''I would analyze prescriptions inputted by users, checking for accuracy, potential interactions, dosage appropriateness, and any other relevant factors. 
             I would provide feedback on the prescription, flagging any concerns or offering suggestions to ensure safe and effective medication use.
        ''')
exp.image("AI-Chatbot.jpg",width=100)

st.markdown(
   '''<style>
   .appview-container.st-emotion-cache-1wrcr25.ea3mdgi9{
       background-color:#000000;
    }
   .block-container.st-emotion-cache-gh2jqd.ea3mdgi5{
   border-radius: 16px;
   background-color:#000000;
   color: white; /* Set text color to white */
   } 
   ''',
    unsafe_allow_html=True
)
st.sidebar.success("Select a page above")
uploaded_file=st.file_uploader("Upload an image",type=['png','jpg','jpeg'])
submit_button=st.button("Generate the results")

system_prompts='''As a highly skilled image analyzer, from the given image
Identify the patient name, age and gender and medication prescribed with the dosage and time should be analysed from the uploaded image
Consider this as an example, "The patient's name is Ma. Flora Cua. She is 25 years old and female. The medication prescribed for her is Sorbifer Durules, and she is to take 1 tablet twice a day for 30 days
'''

if submit_button:
  image_data=uploaded_file.getvalue()
  image_parts = [
       {
    "mime_type": "image/jpeg",
    "data": image_data
       },
    ]
  prompt_parts = [
  image_parts[0],
  system_prompts,
]
  response = model.generate_content(prompt_parts)
  st.write(response.text)





