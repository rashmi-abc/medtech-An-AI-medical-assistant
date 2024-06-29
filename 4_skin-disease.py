import streamlit as st
from pathlib import Path
import google.generativeai as genai

genai.configure(api_key="AIzaSyA2-usPnvsTsLC4T8BdC_5JhSzaP3p5C9I")

genai.configure(api_key="AIzaSyA2-usPnvsTsLC4T8BdC_5JhSzaP3p5C9I")

system_prompts=''' 
As a highly skilled medical practioner specializing in image analysis in a renowed hospital,
Identify the disease name and describe the treatment options,symptomps and recommandations for the disease by analysing the uploaded image. Provide 3 examples, each within 150 words.
'''

# Set up the model
generation_config = {
  "temperature": 0.55,
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


st.image("pages/tony.png",width=100)
st.title("MeDTech-Your medical assistant")
st.subheader("An application- Skin disease Analyser using image ")
exp=st.expander("Want to know about me?")
exp.write('''I analyze symptoms, medical history, and images to identify and provide information about various skin diseases, offering guidance and recommendations for seeking professional medical assistance when needed. 
          My goal is to assist users in understanding their skin conditions and directing them towards appropriate care.''')
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
   } ''',
    unsafe_allow_html=True
)
uploaded_file=st.file_uploader("Upload an image",type=['png','jpg','jpeg'])
submit_button=st.button("Generate the results")

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
