import streamlit as st
import requests

# adding text widget to sidebar
API_URL = st.sidebar.text_input("Enter API URL")

# Page title
st.write("# Machine Learning Project")
st.write("## Group Members : ")
st.write("### * Bilal Rahim")
st.write("### * Shouzab Khan")
st.write("### * Mubeen Ghauri")


st.write("\n\n # Translating From English to German using Transformaers (not the robots ;) )")

text = st.text_area("Enter Text to translate")

if st.button('Translate'):
	
	if API_URL == "":
		st.write("[ERROR] Please specify API URL in sidebar")
		pass
	else:
		# get translated text from api
		translated_text = requests.get(API_URL+"/translate?text="+text)

		st.write("\n\n# Response : ")
		if translated_text.status_code == 200:
			st.write("\n##", translated_text.text)
		elif transtaled_text.status_code == 404:
			st.write("\n### Link not found, please specify correct APL link")

