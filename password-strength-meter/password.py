import re
import streamlit as st

# Styling page
st.set_page_config(page_title="Password Strength Checker by Rimsha Aslam", page_icon="🔒", layout="centered", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
            <style>
            /* Centering and styling main content */
            .main {text-align: center;}

            /* Styling input field */
            .stTextInput {width: 70% !important; margin: auto; padding: 10px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc;}

            /* Styling buttons */
            .stButton button {width: 60%; background-color: skyblue; color: white; font-size: 20px; padding: 10px; border-radius: 5px; border: none;}
            .stButton button:hover {background-color: blue;}

            /* Styling the title */
            .stTitle {font-size: 36px; font-weight: bold; color: #4CAF50; text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);}

            /* Styling the sidebar */
            .sidebar .sidebar-content {background-color: #f4f4f9;}
            .sidebar .sidebar-content .stTextInput {background-color: #f9f9f9;}

            /* Input box styling */
            .stTextInput input {padding: 10px; border-radius: 5px; border: 1px solid #ddd; font-size: 16px; width: 80%;}

            /* Expandable feedback section */
            .stExpander {background-color: #f1f1f1; border: 1px solid #ddd; padding: 10px; border-radius: 5px;}

            /* Success message styling */
            .stSuccess {background-color: #4CAF50; color: white;}

            /* Warning message styling */
            .stWarning {background-color: #ffcc00; color: black;}

            /* Error message styling */
            .stError {background-color: #f44336; color: white;}
            </style>
            """, unsafe_allow_html=True)

# Title with Emoji on the same line
st.markdown("<h1 style='text-align: center; font-size: 36px; font-weight: bold;'>🔑 Password Strength Meter 🔒</h1>", unsafe_allow_html=True)
st.write("Enter your password below to check its security level. 🛡️")

# Function to check password strength
def password_strength(password):
    score = 0
    feedback = []

    # Check if password length is at least 8 characters
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least **8 characters long**. 📝")

    # Check for both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password must contain **uppercase (A-Z) and lowercase (a-z) letters**. 🔠")

    # Check for at least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password must contain **at least one number (0-9)**. 🔢")

    # Check for at least one special character
    if re.search(r"\W", password):  # Non-alphanumeric characters
        score += 1
    else:
        feedback.append("Password must contain **at least one special character (!@#$%^&*)**. 💎")

    # Display password strength message
    if score == 4:
        st.success("**Strong password** - Your password is secured. 🔒")
    elif score == 3:
        st.warning("**Medium password** - Your password is not secure enough. ⚠️")
    else:
        st.error("**Weak password** - Your password is very weak. 🚨")
    
    # Show progress bar based on score
    st.progress(score * 25)  # Progress bar from 0 to 100 based on score
    
    # Provide feedback for improvements
    if feedback:
        with st.expander("**Improve your password** ✍️"):
            for item in feedback:
                st.markdown(f"- {item}")

# Input field for password with placeholder
if 'password' not in st.session_state:
    st.session_state.password = ""  # Set default value if not already set

password = st.text_input("🔑 Enter your password", type="password", placeholder="e.g., MySecureP@ssw0rd", help="Password must be at least 8 characters long.", value=st.session_state.password)

# Button to trigger strength check
if st.button("Check Strength 🔍"):
    if password:
        st.session_state.password = password  # Store the password in session state
        password_strength(password)
    else:
        st.warning("Please enter a password first. ❗")

# Add a clear button (optional)
if st.button("Clear"):
    st.session_state.password = ""  # Clear the session state password
    # No need to call st.experimental_rerun(), the app will automatically re-render
