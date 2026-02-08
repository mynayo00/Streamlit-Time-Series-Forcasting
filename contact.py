import streamlit as st

def munculkan_kontak():
    st.title('Kontak')
    st.write('Hubungi saya melalui tautan berikut:')

    # Linkedin
    st.markdown(
        "[![Linkedin](https://img.shields.io/badge/Linkedin-Profile-blue)](https://www.linkedin.com/in/nadya-aswarani/)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue)](https://www.linkedin.com/in/nadya-aswarani/)"
    )

    #Email
    st.write('📧 Email : nadyaaswarani0@gmail.com')