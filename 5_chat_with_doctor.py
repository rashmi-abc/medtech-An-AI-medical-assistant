import streamlit as st


st.markdown(
        """
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #000000;
        }
        .sidebar .sidebar-content {
            background-color: #000000;
            color: white; /* Set text color to white */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Define doctor names and medical specialties
doctor_specialties = {
        "Dr. Samantha Patel": "Dermatology",
        "Dr. Marcus Nguyen": "Cardiology",
        "Dr. Emily Chang": "Emergency Medicine",
        "Dr. Javier Rodriguez": "Family Medicine",
        "Dr. Priya Sharma": "Gastroenterology",
        "Dr. Alexander Mitchell": "Hematology",
        "Dr. Natalie Wilson": "Immunology",
        "Dr. Omar Khan": "Internal Medicine",
        "Dr. Gabriella Russo": "Nephrology",
        "Dr. Benjamin Lee": "Neurology",
        "Dr. Sophia Martinez": "Obstetrics and Gynecology (OB/GYN)",
        "Dr. Liam O'Connor": "Oncology",
        "Dr. Isabella Flores": "Ophthalmology",
        "Dr. Jacob Thompson": "Orthopedics",
        "Dr. Maya Gupta": "Pediatrics"
    }

    # Add header section with logo
st.image("pages/tony.png", width=100)
st.title("Chat with Doctor")

    # Add doctor's name dropdown
selected_doctor = st.selectbox("Doctor Name:", list(doctor_specialties.keys()))

    # Add dropdown box for medical specialties
selected_specialty = st.selectbox("Medical Specialty:", list(set(doctor_specialties.values())))

    # Display initial doctor message
st.write(f"Doctor: Hi there! How can {selected_doctor} assist you today?")

    # Display chat log
chat_log = st.text_area("Chat log:", "", height=200, max_chars=None, key=None)

    # Add send button
if st.button("Send"):
    st.write("User: <User's input>")

