import base64
import os
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

parent_dir = os.path.abspath(os.path.join(os.getcwd(), ""))
st.set_page_config(page_title="Chemistry Recommendations",
                   page_icon=':book:',
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={'Get Help': 'https://www.extremelycoolapp.com/help',
                               'Report a bug': "https://www.extremelycoolapp.c",
                               'About': "This app was developped by Edouard Godineau for Fabien Barreteau",
                               }
                   )

with open('chemistry_recommendations/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

raav_url = "https://spotfire.rt.intra/spotfire/wp/analysis?file=/Apps/RAAV/RAAV/RAAV&waid=CJCil4DJxUakljae-Pri8-14000249f4zA96&wavid=0"
borse_url = "https://spotfire.rt.intra/spotfire/wp/analysis?file=/Apps/RAAV/RAAV/RAAV&waid=CJCil4DJxUakljae-Pri8-14000249f4zA96&wavid=0"
swift_url = "http://pipelinepilot.rt.intra:9944/webapps/shared/HTML/Swift2.html"
digital_poster = "https://syngenta.sharepoint.com/sites/sustchem/Public/Forms/AllItems.aspx?id=%2Fsites%2Fsustchem%2FPublic%2FGreen%20Chemistry%20Poster%2Epdf&parent=%2Fsites%2Fsustchem%2FPublic"
acs_reagent_guide = "https://reagents.acsgcipr.org/reagent-guides"
solvent_guide = "https://syngenta.sharepoint.com/:x:/r/sites/sustchem/_layouts/15/Doc.aspx?sourcedoc=%7B691390FA-470A-44A8-BA03-F04887CF7D6E%7D&file=Solvent%20Sustainability%20Guide.xlsx&_DSL=1&action=default&mobileredirect=true"
chemsupport = "https://chemsupport.syngentaaws.org/dashboard/entries/(status:opened)"


st.markdown(f"""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #5F7800;">
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href={raav_url} target="_blank">RAAV</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href={borse_url} target="_blank">Borse</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href={borse_url} target="_blank">ChemBörse Portal</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href={swift_url} target="_blank">Swift</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href={digital_poster} target="_blank">Digital Poster</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href={solvent_guide} target="_blank">Solvent Guide</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href={chemsupport} target="_blank">ChemSupport</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href={acs_reagent_guide} target="_blank">ACS Reagent Guide</a>
                </li>
            </ul>
        </div>
    </nav>      
""", unsafe_allow_html=True)



with st.container():
    st.markdown(f'<div class="header">{"This application is an information hub for helping chemists to quickly find useful information for performing their daily work"}</div>', unsafe_allow_html = True)

    st.markdown(f'<div class="paragraph">{"On this site can be found in particurlar:"}</div>', unsafe_allow_html = True)
    st.markdown(f'<div class="bullet_points">{"Tips and tricks for performing efficiently chemistry"}</div>', unsafe_allow_html = True)
    st.markdown(f'<div class="bullet_points">{"Alternative protocols which can be tried when classical conditions did not work"}</div>', unsafe_allow_html = True)
    st.markdown(f'<div class="bullet_points">{"Tips and tricks, protocols and alternative protocol to make chemistry greener"}</div>', unsafe_allow_html = True)

with st.container():
    st.write("---")
    col1, col3 = st.columns([1,1])
    with col1:
        st.markdown(f'<div style="color:#5F7800;font-size:20px; text-align: center">{"Sustainability in Chemistry Sharepoint"}</div>', unsafe_allow_html=True)
        with st.columns([2, 1, 1, 1, 1, 2])[1]:
            url = "https://syngenta.sharepoint.com/sites/sustchem"
            file_path = "chemistry_recommendations/images/shutterstock_1345050239.jpg"
            link = f'<a href={url} target="_blank"><img src="data:image/jpeg;base64,{base64.b64encode(open(file_path, "rb").read()).decode()}" alt="Clickable image" width="200" text-align="center"></a>'
            st.markdown(link, unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="color:#5F7800;font-size:20px; text-align: center">{"Stein Research Chemistry"}</div>', unsafe_allow_html=True)
        with st.columns([1,2,1,1,4,1])[2]:
            url = "https://syngenta.sharepoint.com/sites/sustchem"
            file_path = "chemistry_recommendations/images/Stein_research_chemistry.PNG"
            link = f'<a href={url} float:left target="_blank"><img src="data:image/png;base64,{base64.b64encode(open(file_path, "rb").read()).decode()}" alt="Clickable image" width="200"></a>'
            st.markdown(f'<h1 float:left">{link}</h1>', unsafe_allow_html=True)

