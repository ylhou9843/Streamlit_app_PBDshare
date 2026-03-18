import streamlit as st

st.set_page_config(page_title="RAM",layout="wide")
st.title("RAM Dashboard")



# Embed using an iframe
powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=2b7e49ce-e535-40a3-9851-662ff9852a21&autoAuth=true&ctid=ebb34bb0-e0c2-4ab2-b515-215ad41ea2e6"
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
            margin-top: 20px;  /* space below title */
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