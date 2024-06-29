"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import streamlit as st
from streamlit_option_menu import option_menu

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

# Add CSS gradient backgroundstr
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
st.image("tony.png",width=100)
st.title("MeDTech-Your medical assistant")
st.subheader("An application-Symptoms identifier from the user's inputs in form of short keywords ")
exp=st.expander("Want to know about me?")
exp.write('''I analyze user-reported symptoms and medical history to provide potential diagnoses and recommend seeking professional medical advice for accurate diagnosis and treatment.
           Safety and privacy are my priorities in handling sensitive health information.''')
exp.image("AI-Chatbot.jpg",width=100)


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
        model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
        convo = model.start_chat(history=[
        {
    "role": "user",
    "parts": ["fever (100° F),headache,more intense pain and fatigue, andmore severe, often dry cough."]
        },
       {
    "role": "model",
    "parts": ["The symptoms you describe could be indicative of several different medical conditions, including:\n\n**1. Influenza (Flu):**\n* **Type of disease:** Viral infection\n* **Possible causes:** Influenza virus strains A, B, and C\n* **Symptoms:** Fever, chills, headache, body aches, fatigue, cough, sore throat, runny or stuffy nose\n* **Treatment:** Antiviral medications, rest, fluids\n* **Prevention:** Flu vaccine, hand hygiene, avoiding contact with sick people\n\n**2. Common Cold:**\n* **Type of disease:** Viral infection\n* **Possible causes:** Rhinoviruses, coronaviruses, and other viruses\n* **Symptoms:** Runny or stuffy nose, sore throat, cough, sneezing, headache, fatigue\n* **Treatment:** Over-the-counter medications, rest, fluids\n* **Prevention:** Hand hygiene, avoiding contact with sick people\n\n**3. COVID-19:**\n* **Type of disease:** Viral infection\n* **Possible causes:** SARS-CoV-2 virus\n* **Symptoms:** Fever, cough, fatigue, shortness of breath, loss of taste or smell\n* **Treatment:** Varies depending on severity, may include antiviral medications, oxygen therapy, or hospitalization\n* **Prevention:** Vaccination, wearing masks, social distancing, hand hygiene\n\n**4. Pneumonia:**\n* **Type of disease:** Lung infection\n* **Possible causes:** Bacteria, viruses, fungi\n* **Symptoms:** Fever, chills, cough, chest pain, shortness of breath\n* **Treatment:** Antibiotics (for bacterial pneumonia), antiviral medications (for viral pneumonia), antifungal medications (for fungal pneumonia)\n* **Prevention:** Vaccination, hand hygiene, avoiding contact with sick people\n\n**5. Bronchitis:**\n* **Type of disease:** Inflammation of the bronchial tubes\n* **Possible causes:** Viruses, bacteria, irritants (e.g., smoke, pollution)\n* **Symptoms:** Cough, wheezing, chest tightness, shortness of breath\n* **Treatment:** Bronchodilators, inhaled corticosteroids, antibiotics (for bacterial bronchitis)\n* **Prevention:** Avoiding smoking and secondhand smoke, hand hygiene\n\nIt is important to note that these are just a few possibilities, and a proper diagnosis can only be made by a healthcare professional. If you are experiencing these symptoms, it is recommended that you consult a doctor for evaluation and treatment."]
       },
       ])
            
        response = send_message(convo, user_input)
        st.write(response)
    else:
        st.write("Please enter a message.")
