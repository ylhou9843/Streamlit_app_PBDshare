import streamlit as st

st.set_page_config(page_title="Circle K",layout="wide")
# st.set_page_config(layout="wide")  # Use full-width layout


# Embed using an iframe
powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=ba8e2e97-d57f-4780-a3e9-7197cbd9f081&autoAuth=true&ctid=ebb34bb0-e0c2-4ab2-b515-215ad41ea2e6"
# st.markdown(
#     f'<iframe width="1500" height="800" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>',
#     unsafe_allow_html=True
# )

# Full-page iframe
st.markdown(
    f"""
    <style>
        .full-screen-iframe {{
            position: relative;
            width: 100%;
            height: 90vh;  /* adjust height as needed */
            padding: 0;
            margin: 0;
            border: none;
        }}
        .report-container {{
            padding: 0;
            margin: 0;
        }}
    </style>

    <div class="report-container">
        <iframe 
            class="full-screen-iframe"
            src="{powerbi_url}" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)