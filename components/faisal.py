import streamlit as st

# Function for Environmental Articles with Embedded Videos
def environmental_articles():
    st.markdown("""
    <style>
    /* Body Styling */
    body {
        
        font-family: 'Arial', sans-serif;
        background: linear-gradient(45deg, #a1c4fd, #c2e9fb);
        color: #333;
        margin: 0;
        padding: 0;
    }

    .header {
        text-align: center;
        font-size: 3.5em;
        color: #2e3a59;
        text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
        margin-top: 30px;
    }

    .subheader {
        font-size: 2.5em;
        color: #337ab7;
        margin-bottom: 20px;
        text-transform: uppercase;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
    }

    .content {
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        padding: 25px;
        margin: 30px;
        animation: fadeIn 1s ease-in-out;
    }

    .content:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .video-container {
        margin-top: 20px;
        text-align: center;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .video-container iframe {
        width: 100%;
        height: 350px;
        border: none;
        border-radius: 15px;
    }

    /* Animation */
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header">Environmental Impact Articles</div>', unsafe_allow_html=True)

    # Recycling Section
    st.markdown('<div class="subheader">Recycling</div>', unsafe_allow_html=True)
    st.write("""
    Recycling reduces waste in landfills and conserves natural resources. 
    It helps reduce pollution and saves energy by reusing materials.
    """)
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=6jQ7y_qQYUA")
    st.markdown('</div>', unsafe_allow_html=True)

    # Composting Section
    st.markdown('<div class="subheader">Composting</div>', unsafe_allow_html=True)
    st.write("""
    Composting converts organic waste into nutrient-rich fertilizer, 
    which can be used to enrich soil and grow healthy plants.
    """)
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=dRXNo7Ieky8")
    st.markdown('</div>', unsafe_allow_html=True)

# Function for News and Events with Improved Layout
def news_and_events():
    st.markdown("""
    <style>
    /* Body Styling */
    body {
        font-family: 'Arial', sans-serif;
        background: linear-gradient(45deg, #ff7e5f, #feb47b);
        color: #333;
        margin: 0;
        padding: 0;
    }

    .header {
        text-align: center;
        font-size: 3.5em;
        color: #2e3a59;
        text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
        margin-top: 30px;
    }

    .subheader {
        font-size: 2.5em;
        color: #f2f2f2;
        margin-bottom: 20px;
        text-transform: uppercase;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
    }

    .content {
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        padding: 25px;
        margin: 30px;
        animation: fadeIn 1s ease-in-out;
    }

    .content:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .video-container {
        margin-top: 20px;
        text-align: center;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .video-container iframe {
        width: 100%;
        height: 350px;
        border: none;
        border-radius: 15px;
    }

    /* Animation */
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header">News and Events</div>', unsafe_allow_html=True)

    st.write("🌍 *Upcoming Event:* Sustainability Fair")
    st.write("📅 *Date:* December 15th, 2024")
    st.write("""
    Join us for a day of learning about sustainable living practices, 
    green technology, and environmental conservation.
    """)
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=5bVDpmzMICE")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Recent News")
    st.write("""
    - *Global Recycling Rates Improve*: A new report highlights how recycling has increased by 20% globally.
    - *Innovative Composting Methods*: Researchers develop faster composting techniques to combat food waste.
    """)

# Sidebar for navigation with styling
st.markdown("""
    <style>
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(45deg, #a1c4fd, #c2e9fb);
        padding: 20px;
        border-radius: 15px;
    }

    .sidebar .sidebar-header {
        color: #ffffff;
        font-size: 2em;
        text-align: center;
    }

    .sidebar .sidebar-radio {s
        margin-top: 20px;
        color: #ffffff;
        font-size: 1.2em;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Explore")
page = st.sidebar.radio("Select a page", ["Environmental Articles", "News and Events"])

# Render the selected page
if page == "Environmental Articles":
    environmental_articles()
elif page == "News and Events":
    news_and_events()
