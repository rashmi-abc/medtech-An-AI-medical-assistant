import streamlit as st

def appointment_request():
    st.header("Appointment Request")
    st.image(r"b.jpg", width=100)
    selected_doctor = st.selectbox("Select Doctor", ["Dr.Barathvasan", "Dr.jaswanth Raj", "Dr.Rashmi"])
    date = st.date_input("Date")
    time = st.time_input("Time")
    reason = st.text_input("Reason for Appointment", "")
    submit_button = st.button("Submit Appointment Request")
    if submit_button:
        st.success("Appointment request submitted successfully!")

def telecom_request():
    st.header("Telecom Request")
    st.image(r"c.jpg", width=100)
    selected_doctor = st.selectbox("Select Doctor", ["Dr.Barathvasan", "Dr.jaswanth Raj", "Dr.Rashmi"])
    doctor_phone_numbers = {
        "Dr.Barathvasan": "8249431753",
        "Dr.jaswanth Raj": "7836472643",
        "Dr.Rashmi": "8793746285"
    }
    if selected_doctor in doctor_phone_numbers:
        phone_number = doctor_phone_numbers[selected_doctor]
        st.write(f"Phone Number: {phone_number}")
    else:
        st.write("Phone Number not available")
    request_details = st.text_area("Request Details", "")
    submit_button = st.button("Submit Telecom Request")
    if submit_button:
        st.success("Telecom request submitted successfully!")

st.title("Request System")

selected_option = st.sidebar.radio("Navigation", ("Appointment", "Telecom"))

if selected_option == "Appointment":
    appointment_request()
elif selected_option == "Telecom":
    telecom_request()