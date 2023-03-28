import bigtree as bt
import streamlit as st
from chemistry_recommendations.data_prep import Recommendation


file_path = "chemistry_recommendations/Recommendations.xlsx"
sheetname = "Suzuki_App_"

# # Load data for the reaction class and build the recommendations
suzuki = Recommendation(file_path, sheetname)
suzuki.build_nodes()
suzuki.build_recommendation()
suzuki_dict = suzuki.build_dict4tree()

# # Build the tree for the reaction class

root_suzuki = bt.dict_to_tree(suzuki_dict)

def show_page():

    # Define custom CSS styles
    with open('chemistry_recommendations/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    header = "Recommended methods to perform Suzuki Cross couplings"
    st.write(f'<h1 class="header_page">{header}</h1>', unsafe_allow_html=True)


    standard_conditions = root_suzuki.node_name

    results = bt.find(root_suzuki, lambda node: node.name == standard_conditions)

    subheader = f'The {standard_conditions} reaction conditions for cyanations are the following condition(s):'
    st.write(f'<div class="normal_page_text">{subheader}</div>', unsafe_allow_html=True)

    st.write(f'')

    # print best conditions (up to 3 conditions are returned)
    for i in range(1, 4):
        i = str(i)
        item = results.get_attr(i)
        if item:
            with st.container():

                # print the recommendation for the reaction class
                st.markdown(f'<h1 class="container">{i} | {item.get("recommendation")}</h1>', unsafe_allow_html=True)
                # print(f'{i} | {item.get("recommendation")}')

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

    # print('Standard conditions did not work because the carboxylic acid (choose from the list below):')
    alternatives = [i.name for i in root_suzuki.children]

    st.markdown("---")

    label_text = "The standard conditions above did not work because the:"
    st.markdown(f'<div class="normal_page_text">{label_text}</div>', unsafe_allow_html=True)

    problem = st.selectbox(' ', ['Please choose an option'] + alternatives)
    st.markdown('</div>', unsafe_allow_html=True)

    for alternative in alternatives:
        if alternative == problem:
            st.write(
                f"If the {alternative}, here are alternative conditions which are recommended:")
            results = bt.find(root_suzuki, lambda node: node.name == alternative)
            for i in range(1, 4):
                i = str(i)
                item = results.get_attr(i)
                if item:
                    with st.container():

                        # print the recommendation for the reaction class
                        st.markdown(f'<h1 class="container">{i} | {item.get("recommendation")}</h1>',
                                    unsafe_allow_html=True)
                        # print(f'{i} | {item.get("recommendation")}')

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


