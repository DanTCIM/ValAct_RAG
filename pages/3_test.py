import streamlit as st


def pdf_container():
    pdf_display = f"""
    <style>
        .pdf-container {{
            width: 100%;
            height: calc(100vh - 15rem);
            overflow: auto;
        }}
        .pdf-container iframe {{
            width: 100%;
            height: 100%;
        }}
    </style>
    <div class="pdf-container">
        <iframe src="https://drive.google.com/file/d/1b1OZwMaIM9_-_pSWeA0Fl1Y9i2ZsrMsj/preview" allow = "autoplay"></iframe>
    </div>
    """

    return pdf_display


pdf_content = pdf_container()
st.write(pdf_content, unsafe_allow_html=True)
