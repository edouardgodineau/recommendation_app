import bigtree as bt
import streamlit as st
from chemistry_recommendations.data_prep import Recommendation
from streamlit_extras.switch_page_button import switch_page


file_path = "chemistry_recommendations/Recommendations.xlsx"
sheetname = "Amide_coupling_App_"

amide = Recommendation(file_path, sheetname)

# Build the tree for the reaction class
amide.build_nodes()
amide.build_recommendation()
amide.build_dict4tree()

# Build the tree for the reaction class
root_amide = bt.dict_to_tree(amide.leaves)



def show_page():

    # Define custom CSS styles
    with open('chemistry_recommendations/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        button1 = st.button('tips and tricks')
    with col2:
        button2 = st.button('Experimental Protocols')
    with col3:
        button3 = st.button('contact us')


    if button2:

        header = "Recommended methods to prepare amides"
        st.write(f'<h1 class="header_page">{header}</h1>', unsafe_allow_html=True)


        standard_conditions = root_amide.node_name

        subheader = f'For carboxylic acid which {standard_conditions} the following condition(s) are recommended:'
        st.write(f'<div class="normal_page_text">{subheader}</div>', unsafe_allow_html=True)

        results = bt.find(root_amide, lambda node: node.name == standard_conditions)

        # print best conditions (up to 3 conditions are returned)
        for i in range(1,4):
            i = str(i)
            item = results.get_attr(i)
            if item:
                with st.container():

                    with st.container():

                        # print the recommendation for the reaction class
                        st.markdown(f'<h1 class="container">{i} | {item.get("recommendation")}</h1>',
                                    unsafe_allow_html=True)

                        # print_additionnal_info(item) when it is available
                        if item['ELN'] != '':
                            st.markdown(f'<div class="additionnal_info">ELN reference: {item.get("ELN")}</div>',
                                        unsafe_allow_html=True)
                        else:
                            st.markdown(
                                f'<div class="additionnal_info">{"We unfortunately do not have any ELN reference to recommend. We are working on it!"}</div>',
                                unsafe_allow_html=True)
                        if item.get('comments') != '':
                            st.markdown(f'<div class="additionnal_info">Comment: {item.get("comments")}</div>',
                                        unsafe_allow_html=True)
                        if item.get('reference') != '':
                            st.markdown(
                                f'<div id="additionnal_info"><a href={item.get("link")} float:left target="_blank">Reference: {item.get("reference")}</a></div>',
                                unsafe_allow_html=True)


        alternatives = [i.name for i in root_amide.children]

        st.markdown("---")

        label_text = "The standard conditions did not work because the carboxylic acid:"

        st.markdown(f'<div class="normal_page_text">{label_text}</div>', unsafe_allow_html=True)

        problem = st.selectbox(' ', ['Please choose an option'] + alternatives)
        st.markdown('</div>', unsafe_allow_html=True)

        for alternative in alternatives:
            if alternative == problem:
                st.write(f"For a carboxylic acid which {alternative}, here are alternative conditions which are recommended:")
                results = bt.find(root_amide, lambda node: node.name == alternative)
                for i in range(1, 4):
                    i = str(i)
                    item = results.get_attr(i)
                    if item:
                        with st.container():

                            # print the recommendation for the reaction class
                            st.markdown(f'<h1 class="container">{i} | {item.get("recommendation")}</h1>',
                                        unsafe_allow_html=True)

                            # print_additionnal_info(item) when it is available
                            if item['ELN'] != '':
                                st.markdown(f'<div class="additionnal_info">ELN reference: {item.get("ELN")}</div>',
                                            unsafe_allow_html=True)
                            else:
                                st.markdown(
                                    f'<div class="additionnal_info">{"We unfortunately do not have any ELN reference to recommend. We are working on it!"}</div>',
                                    unsafe_allow_html=True)
                            if item.get('comments') != '':
                                st.markdown(f'<div class="additionnal_info">Comment: {item.get("comments")}</div>',
                                            unsafe_allow_html=True)
                            if item.get('reference') != '':
                                st.markdown(
                                    f'<div id="additionnal_info"><a href={item.get("link")} float:left target="_blank">Reference: {item.get("reference")}</a></div>',
                                    unsafe_allow_html=True)
                            st.markdown("---")

    if button1:
        with st.expander("Tips and tricks"):
            image1_1 = "chemistry_recommendations/images/image1_2.png"
            image2_1 = "chemistry_recommendations/images/image2_1.png"
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown('coupling agent')
                with col2:
                    st.markdown('Structure')
                with col3:
                    st.markdown('Expected side product(s)')
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown('T3P')
                with col2:
                    st.image(open(image1_1, "rb").read(), width=200, output_format="PNG")
                with col3:
                    st.image(open(image2_1, "rb").read(), width=200, output_format="PNG")

