from google.cloud import firestore
import streamlit as st

db = firestore.Client.from_service_account_json("careworld/images/firestore-key.json")

doc_ref = db.collection("patient_details").document("0000")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
