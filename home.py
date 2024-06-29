import streamlit as st
st.set_page_config(page_title="Medical Bot", page_icon="🩺")
st.markdown(
        """
        <style>
        body {
            font-family: 'Vaporwave', cursive;
            background-color: beige;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: beige;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Add header section with logo
st.image("pages/tony.png", width=100)
st.title("MedTech- Multi featured-Medical Bot")
st.markdown("*****Welcome to Medical Bot! Here are the features available*****")
st.markdown(
    '''
    <style>
    .appview-container.st-emotion-cache-1wrcr25.ea3mdgi9{
    background-color:#000000;
    color: white; /* Set text color to white */
    }
    </style>
    ''',
    unsafe_allow_html=True
)
st.image('pages/main.jpg', use_column_width=True)

# Add description
def user_login():
    st.write("User Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    if login_button:
        # Implement your authentication logic here
        st.write("User logged in successfully!")

def doctor_login():
    st.write("Doctor Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    if login_button:
        # Implement your authentication logic here
        st.write("Doctor logged in successfully!")

option = st.radio("Select login type:", ("User", "Doctor"))

if option == "User":
    user_login()
elif option == "Doctor":
    doctor_login()
