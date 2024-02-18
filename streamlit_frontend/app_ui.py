import streamlit as st


# st. set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .appview-container .main .block-container {
        padding-top: 2rem;
        margin: 0;
    }
    .css-usj992 {
    background-color: transparent;
    }
    .subtitle {
        margin-bottom: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<h1 style='text-align: center; padding: 10px;'>SimpliMedi-Assist</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h5 class='subtitle' style='text-align: center; padding: 2px;'>Your Health in Plain English</h5>",
    unsafe_allow_html=True
)


# Create a Streamlit file uploader widget
uploaded_file = st.file_uploader(
    "Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])


# Check if a file has been uploaded
if uploaded_file is not None:
    # Load the document
    st.write("Loading document...")