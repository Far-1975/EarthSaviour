import streamlit as st

# Function for Community Challenges
def community_challenges():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(45deg, #ff7e5f, #feb47b);
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .header {
        text-align: center;
        font-size: 3.5em;
        color: #4CAF50;  /* Green for Challenges */
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        transition: color 0.3s ease;
    }
    .info {
        text-align: center;
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
    }
    .subheader {
        font-size: 2.5em;
        color: #337ab7;  /* Blue for Subheadings */
        margin-bottom: 15px;
        transition: color 0.3s ease;
    }
    .challenge-card {
        background-color: #fff;
        padding: 20px;
        margin: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .challenge-card:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    .button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .button:active {
        transform: scale(0.98);
    }
    .selectbox select, .file-uploader input {
        padding: 12px;
        font-size: 16px;
        border-radius: 8px;
        border: 2px solid #ddd;
        transition: border 0.3s ease, box-shadow 0.3s ease;
    }
    .selectbox select:focus, .file-uploader input:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
    }
    .stTextArea textarea {
        padding: 12px;
        font-size: 16px;
        border-radius: 8px;
        border: 2px solid #ddd;
        transition: border 0.3s ease, box-shadow 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
    }
    .stSuccess {
        color: #28a745;
        font-weight: bold;
        font-size: 18px;
        transition: color 0.3s ease;
    }
    .stError {
        color: #dc3545;
        font-weight: bold;
        font-size: 18px;
        transition: color 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header">Community Challenges</div>', unsafe_allow_html=True)
    st.markdown('<div class="info">Participate in impactful challenges to make a difference!</div>', unsafe_allow_html=True)

    st.subheader("Active Challenges")
    challenges = {
        "Zero Waste Week": "Track and reduce your waste for a week.",
        "Walk for Waste": "Collect litter while walking in your neighborhood.",
        "Eco Photography Contest": "Capture creative waste reduction efforts."
    }

    for challenge, desc in challenges.items():
        st.markdown(f'<div class="challenge-card">📌 *{challenge}*: {desc}</div>', unsafe_allow_html=True)

    selected_challenge = st.selectbox("Join a Challenge", list(challenges.keys()))
    if st.button("Join Challenge", key="join_challenge"):
        st.success(f"You've joined *{selected_challenge}*! Let’s make a change!")

    # Leaderboard
    st.subheader("Challenge Leaderboard")
    st.write("🏆 *Top Performers* (Simulated Data):")
    leaderboard = [
        {"Name": "Alice", "Points": 150},
        {"Name": "Bob", "Points": 140},
        {"Name": "Charlie", "Points": 130},
    ]
    for person in leaderboard:
        st.write(f"{person['Name']} - {person['Points']} Points")

# Function to Report Illegal Dumping with Image Upload
def report_illegal_dumping():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(45deg, #ff7e5f, #feb47b);
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .header {
        text-align: center;
        font-size: 3.5em;
        color: #ff6347;  /* Tomato for Reporting */
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        transition: color 0.3s ease;
    }
    .form-container {
        background-color: #fff;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        padding: 25px;
        margin: 30px;
        transition: box-shadow 0.3s ease;
    }
    .form-container:hover {
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    }
    .button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin-top: 15px;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .button:active {
        transform: scale(0.98);
    }
    .file-uploader input {
        padding: 12px;
        font-size: 16px;
        border-radius: 8px;
        border: 2px solid #ddd;
        transition: border 0.3s ease, box-shadow 0.3s ease;
    }
    .file-uploader input:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header">Report Illegal Dumping</div>', unsafe_allow_html=True)

    location = st.text_input("Enter the location", key="location")
    description = st.text_area("Describe the issue", key="description")
    image = st.file_uploader("Upload a photo of the issue", type=["jpg", "jpeg", "png"], key="image")

    if st.button("Submit Report"):
        if location and description and image:
            st.success("Your report has been submitted to local authorities!")
            st.image(image, caption="Uploaded Image", use_column_width=True)
        else:
            st.error("Please provide all details and upload an image.")

# Function for Sharing and Voting on Waste Tips
def share_waste_tips():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(45deg, #ff7e5f, #feb47b);
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .header {
        text-align: center;
        font-size: 3.5em;
        color: #20B2AA;  /* LightSeaGreen for Tips */
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        transition: color 0.3s ease;
    }
    .button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin-top: 15px;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .button:active {
        transform: scale(0.98);
    }
    .stTextArea textarea {
        padding: 12px;
        font-size: 16px;
        border-radius: 8px;
        border: 2px solid #ddd;
        transition: border 0.3s ease, box-shadow 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header">Share and Explore Waste Reduction Tips</div>', unsafe_allow_html=True)

    tip = st.text_area("Share your eco-friendly tips", key="tip")
    if st.button("Submit Tip"):
        st.success("Thank you for sharing your tip!")

    # Community Tips (Simulated Data)
    st.subheader("Community Tips")
    tips = [
        {"tip": "Use cloth bags instead of plastic.", "votes": 15},
        {"tip": "Compost your food scraps.", "votes": 12},
        {"tip": "Repair broken items before buying new ones.", "votes": 10}
    ]

    for t in tips:
        st.write(f"💡 {t['tip']} — 👍 {t['votes']} votes")
        if st.button(f"Vote for '{t['tip']}'", key=t['tip']):
            st.success(f"You voted for: {t['tip']}!")

# Sidebar for Navigation
st.sidebar.title("Community Engagement")
page = st.sidebar.radio("Select a section", 
                        ["Community Challenges", 
                         "Report Illegal Dumping", 
                         "Share Waste Tips", 
                         "Community Clubs", 
                         "Initiatives and Events"])

# Render the selected section
if page == "Community Challenges":
    community_challenges()
elif page == "Report Illegal Dumping":
    report_illegal_dumping()
elif page == "Share Waste Tips":
    share_waste_tips()
elif page == "Community Clubs":
    community_clubs()
elif page == "Initiatives and Events":
    initiatives_and_events()
