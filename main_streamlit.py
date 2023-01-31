"""A main script to run streamlit application.

"""

from datetime import datetime

import streamlit as st
from src.utility.loggers import logger
from src.utility.utils import get_transcript_text
from src.inference.predictor_factory import get_predictor

st.title("Text Summarization")


with st.form("my_form"):
    uploaded_file = st.file_uploader("Choose a file for summarization ")
    summarization_method = st.radio(
        "Choose a text summarization method",
        ("Custom Model", "Reused Model"),
    )
    submit = st.form_submit_button("Submit")

    if submit:
        try:
            predictor = get_predictor(summarization_method)

            if uploaded_file is not None:
                start = datetime.now()
                transcript_text = get_transcript_text(uploaded_file)
                summary_text = predictor.get_model_output(transcript_text)
                end = datetime.now()
                # find difference loop start and end time and display
                td = (end - start).total_seconds()
            st.write("model_selected:", summarization_method)
            st.write("Summarization Code Execution Time in seconds:", td)
            st.write("model_output:", summary_text)
        except Exception as error:
            message = "Error while creating output"
            logger.error(message, str(error))
