"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
from pathlib import Path
import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyA2-usPnvsTsLC4T8BdC_5JhSzaP3p5C9I")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
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

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


st.image("pages/tony.png",width=100)
st.title("MeDTech-Your medical assistant")
st.subheader("An application- Medicine Analyser ")
exp=st.expander("Want to know about me?")
exp.write('''I'm a medicine analyzer chatbot designed to provide comprehensive details on medications. 
          From dosage information to potential side effects, 
          I offer accurate and reliable insights to empower users in making informed decisions about their health.''')
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

def send_message(convo, user_input):
    # Send user input to the conversation
    convo.send_message(user_input)
    # Return the last response
    return convo.last.text



# Sidebar for user input
user_input = st.text_area("Enter your message here:")


# Button to send message
if st.button("Send"):
    if user_input:
        # Get response from the chatbot
        convo = convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": ["Hey Gemini, please analyze the prescription details:\nDoctor's Name: [Doctor's Name]\nHospital Name: [Hospital Name]\nMedicine Name: [Medicine Name]\nDisease names: [based on medicine given by doctor]\nDosage Level: [High/Medium/Low]\nTiming Instructions: [Morning/Evening/Night] [Before/After] [Breakfast/Lunch/Dinner]\nHome remedies: [home remedies]\nayurveda alternative medicine: [give indian ayurveda medicine ]\n\nAdditionally, could you provide information on the possible side effects associated with [Medicine Name]?"]
        },
        {
            "role": "model",
            "parts": ["**Prescription Analysis**\n\n**Doctor's Name:** [Doctor's Name]\n**Hospital Name:** [Hospital Name]\n**Medicine Name:** [Medicine Name]\n**Disease Names:** [Disease name(s) based on the medicine prescribed]\n**Dosage Level:** [High/Medium/Low]\n**Timing Instructions:**\n    * Morning/Evening/Night\n    * Before/After [Breakfast/Lunch/Dinner]\n**Home Remedies:** [List of home remedies suggested]\n**Ayurveda Alternative Medicine:** [Indian Ayurveda medicine suggestion]\n\n**Possible Side Effects of [Medicine Name]**\n\n[Provide a list of potential side effects associated with the prescribed medicine.]\n\n**Note:** This analysis is for informational purposes only and should not be considered as a substitute for professional medical advice. It is recommended to consult with a healthcare professional for any specific medical concerns or questions."]
        }
    ])
        response = send_message(convo, user_input)
        st.write(response)
    else:
        st.write("Please enter a message.")


  
