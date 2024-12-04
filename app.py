import streamlit as st
from citizen_page import citizen_interface
from components.community import community_challenges, report_illegal_dumping, share_waste_tips
from components.partnerships import waste_collection_status, feedback_to_authorities
from components.faisal import environmental_articles, news_and_events


st.set_page_config(page_title="Waste Management App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a section",
    [
        "Citizen Page",
        "Authority Page",
        "Community Engagement",
        "Partnerships",
        "Education"
    ]
)

if page == "Citizen Page":
    citizen_interface()
elif page == "Authority Page":
    from authority_page import authority_interface
    authority_interface()
elif page == "Community Engagement":
    st.sidebar.subheader("Engage with the Community")
    activity = st.sidebar.radio("Activities", ["Challenges", "Report Illegal Dumping", "Share Waste Tips"])
    if activity == "Challenges":
        community_challenges()
    elif activity == "Report Illegal Dumping":
        report_illegal_dumping()
    elif activity == "Share Waste Tips":
        share_waste_tips()
elif page == "Partnerships":
    st.sidebar.subheader("Collaborate with Authorities")
    activity = st.sidebar.radio("Activities", ["Waste Collection Status", "Feedback to Authorities"])
    if activity == "Waste Collection Status":
        waste_collection_status()
    elif activity == "Feedback to Authorities":
        feedback_to_authorities()
elif page == "Education":
    st.sidebar.subheader("Learn and Explore")
    activity = st.sidebar.radio("Activities", ["Environmental Articles", "News and Events"])
    if activity == "Environmental Articles":
        environmental_articles()
    elif activity == "News and Events":
        news_and_events()