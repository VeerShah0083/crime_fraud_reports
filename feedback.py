import streamlit as st

# Read CSS code from external file
with open("feedback.css", "r") as file:
    css_code = file.read()

# Custom CSS to style the feedback form
st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)

# Feedback form
st.title("Report Anamoly")

with st.container() as feedback_container:
    st.markdown('<p class="feedback-title">Tell Us Your Feedback</p>', unsafe_allow_html=True)

    feedback_type = st.selectbox("Type of Issue", ["Cyber Security Incident", "Translation Accuracy Issue", "Other(Describe)"])

    description = st.text_area("Description of the Issue", height=100)

    severity = st.select_slider("Severity of the Issue", options=["Very low","Low", "Medium", "High","Very high"])

    comments = st.text_area("Additional Comments", height=100)

    submit_button = st.button("Submit Feedback")

if submit_button:
    # Handle feedback submission
    with st.spinner("Submitting Feedback..."):
        # Placeholder for handling feedback submission (e.g., store in database, send notifications)
        st.success("Feedback submitted successfully!")
