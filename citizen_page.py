import streamlit as st
import datetime
from PIL import Image
from utils import save_issue_ticket, classify_waste, classify_issue
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium
import os
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from sklearn.preprocessing import StandardScaler

def add_custom_styles():
    st.markdown(
        """
        <style>
        /* Your custom CSS styles */
        body {
            background-image: url('https://th.bing.com/th/id/OIP.wFeEKmSErNWbK85eWetBNwHaE8?w=241&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7');
            font-family: 'Arial', sans-serif;
            background-attachment: fixed;
            color: #fff;
            padding: 20px;
            margin: 0;
            overflow: hidden;
        }



        body::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5); /* Adjust transparency */
            z-index: -1;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(45deg, #ff6ec4, #7873f5, #4facfe);
            animation: gradient-move 6s infinite;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
            margin-bottom: 30px;
            transition: transform 0.3s ease;
        }

        .header-container:hover {
            transform: scale(1.05);
        }

        @keyframes gradient-move {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        
        

        .header-title {
            font-size: 3em;
            color: white;
            text-align: center;
            margin: 0;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
        }

        .section-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: rgba(255, 255, 255, 0.1); /* Transparent background */
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            padding: 30px;
            max-width: 600px;
            margin: 30px auto;
            backdrop-filter: blur(10px); /* Glass effect */
        }

        .section-header {
            font-size: 1.8em;
            margin-bottom: 20px;
            color: #4CAF50;
            text-align: center;
            text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.3);
        }

        .stTextInput > div, .stTextArea > div, .stSelectbox > div {
            margin-bottom: 15px;
            border-radius: 8px;
            border: 1px solid #ddd;
            box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent inputs */
        }

        .stTextInput:hover > div, .stTextArea:hover > div, .stSelectbox:hover > div {
            border-color: #4CAF50;
            box-shadow: 0px 4px 10px rgba(76, 175, 80, 0.4);
        }

        .stButton > button {
            background: linear-gradient(45deg, #ff6ec4, #4facfe); /* Pink and Sky Blue Gradient */
            color: white; /* Text color */
            font-size: 1.2em; /* Slightly larger font */
            font-weight: bold; /* Bold text */
            padding: 15px 30px; /* Button size */
            border: none; /* No border */
            border-radius: 50px; /* Rounded button */
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Subtle shadow */
            cursor: pointer; /* Pointer cursor on hover */
            transition: all 0.4s ease; /* Smooth animation */
            outline: none; /* Remove outline */
            text-transform: uppercase; /* Make text uppercase */
            position: relative; /* Position for effects */
            z-index: 0; /* Set for layering */
            overflow: hidden; /* Hide overflow for pseudo-elements */
        }

                .stButton > button:hover {
            transform: translateY(-3px) scale(1.05); /* Lift effect */
            box-shadow: 0px 8px 20px rgba(255, 110, 196, 0.6); /* Glow effect */
        }

                .stButton > button::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0);
            width: 300%;
            height: 300%;
            background: rgba(255, 255, 255, 0.2); /* Light ripple effect */
            border-radius: 50%;
            z-index: -1; /* Send ripple behind text */
            transition: all 0.6s ease-out;
        }
                .stButton >button:hover::before {
            transform: translate(-50%, -50%) scale(1); /* Ripple expands */
            opacity: 0; /* Fade out effect */
        }



        .stButton >button:focus {
            outline: none; /* No focus outline */
            box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.5); /* Focus ring */
        }

        .half-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 40px;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            backdrop-filter: blur(8px);
            border: 2px solid #ffffff; /* Stylish border */
            box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2); /* Soft shadow */
            transition: all 0.3s ease-in-out; /* Animation for smooth transition */
        }

        /* Hover effect for the half-container */
        .half-container:hover {
            transform: scale(1.05); /* Slight scaling on hover */
            box-shadow: 0px 15px 30px rgba(0, 0, 0, 0.3); /* Darker shadow */
        }

        /* Text Section */
        .half-container .text-section {
            flex: 1;
            padding-right: 20px;
            font-size: 1.1em;
            line-height: 1.6;
            color: #fff;
            transition: color 0.3s ease;
        }

        /* Image Section */
        .half-container .image-section {
            flex: 1;
            padding-left: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: transform 0.3s ease;
        }

        /* Smaller Image Size */
        .half-container .image-section img {
            width: 80%;  /* Adjust this value as needed */
            max-width: 400px; /* Adjust maximum width */
            height: auto;
            border-radius: 15px;
            transition: all 0.3s ease;
        }

        /* Image on hover */
        .half-container:hover .image-section img {
            transform: scale(1.1); /* Slight zoom on hover */
        }

        /* Styling the text content */
        .half-container .text-section h3 {
            font-size: 1.8em;
            margin-bottom: 15px;
            color: #4CAF50; /* Green heading */
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2); /* Subtle shadow */
        }

        .half-container .text-section p {
            font-size: 1.2em;
            color: #ddd; /* Lighter text color */
        }

        .social-icons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
    }

    .social-icons a {
        display: inline-block;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: #fff;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .social-icons a:hover {
        transform: scale(1.2); /* Zoom effect on hover */
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3); /* Shadow effect */
    }

    .social-icons img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }


     .login-link {
            margin:40px;
            position: fixed;
            top: 20px;
            right: 40px;
            font-size: 1.2em;
            font-weight: bold;
            color: white;
            text-decoration: none;
            background-color: rgba(0, 0, 0, 0.7);
            padding: 12px 20px;
            border-radius: 30px;
            box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.4);
            transition: all 0.4s ease;
        }

        .login-link:hover {
            background-color: #4CAF50;
            transform: translateY(-5px);
            box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.5);
        }

        .login-link:active {
            transform: translateY(0);
        }

        .login-link::after {
            content: ' →';
            transition: all 0.3s ease;
        }

        .login-link:hover::after {
            content: ' ←';
        }
        /* Your other styles here */
        </style>
        """,
        unsafe_allow_html=True,
    )

def citizen_interface():
    add_custom_styles()  # Add styles

    st.markdown(
        """
        <div class="header-container">
            <h1 class="header-title">Citizen</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="section-container">
            <h2 class="section-header">Raise an Issue Ticket</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Get user details
    user_name = st.text_input("Your Name")
    user_email = st.text_input("Your Email")  # Capture user's email
    issue_description = st.text_area("Describe the Issue")
    issue_category = st.selectbox(
        "Issue Category", ["Water Management", "Garbage Collection", "Road Management", "Other"]
    )

    # Optional image upload
    uploaded_image = st.file_uploader("Upload an Image (optional)", type=["jpg", "jpeg", "png"])
    processed_image = None
    if uploaded_image:
        try:
            processed_image = Image.open(uploaded_image)
        except Exception as e:
            st.error(f"Error loading image: {e}")

    # Manual Location Input (Street, City, Pincode)
    st.subheader("Location Details")
    street = st.text_input("Street")
    city = st.text_input("City")
    pincode = st.text_input("Pincode")

    # Geolocator initialization (make sure this is only initialized once)
    if "geolocator" not in st.session_state:
        st.session_state.geolocator = Nominatim(user_agent="streamlit_app")

    # Show location on map
    if st.button("Show on Map"):
        if street and city and pincode:
            full_address = f"{street}, {city}, {pincode}"
            geolocator = st.session_state.geolocator
            try:
                location = geolocator.geocode(full_address)
                if location:
                    latitude = location.latitude
                    longitude = location.longitude

                    # Check if the map exists in session state
                    if "map" not in st.session_state or st.session_state.location != full_address:
                        # Create a new map only if the location is different or map does not exist
                        st.session_state.map = folium.Map(location=[latitude, longitude], zoom_start=15)
                        folium.Marker([latitude, longitude], popup=full_address).add_to(st.session_state.map)
                        st.session_state.location = full_address  # Store the current location

                    # Display the map
                    st.subheader("Location on Map:")
                    st.write(f"Map showing {full_address}")
                    st_folium(st.session_state.map, width=700, height=500)
                else:
                    st.error("Location not found. Please check the address.")
            except Exception as e:
                st.error(f"Error geocoding address: {e}")
        else:
            st.warning("Please complete the address fields.")

    # Display the entered location
    if street and city and pincode:
        st.write(f"Street: {street}, City: {city}, Pincode: {pincode}")
    else:
        st.warning("Please enter complete address details.")

    # Submit issue
    if st.button("Submit Issue"):
        suggested_category = classify_issue(issue_description)
        waste_category = classify_waste(processed_image) if processed_image else "Not Specified"

        issue_data = {
            "name": user_name,
            "email": user_email,
            "description": issue_description,
            "category": issue_category,
            "suggested_category": suggested_category,
            "geo_location": {"street": street, "city": city, "pincode": pincode},
            "date": datetime.datetime.now().isoformat(),  # Save date in ISO format
            "status": "Open",  # Add status
        }

        save_issue_ticket(issue_data)
        st.success("Issue ticket submitted successfully!")

    st.markdown(
        """
        <div class="half-container">
            <div class="text-section">
                <h3>How the Citizen Interface Helps</h3>
                <p>This interface enables citizens to raise issues such as waste disposal or road repairs. By uploading relevant images, we streamline the process of reporting and resolving these issues efficiently.</p>
            </div>
            <div class="image-section">
                <img src="https://as1.ftcdn.net/v2/jpg/06/17/45/48/1000_F_617454811_8anSGAiEJskRM2QBEUxHCjbBbdJDh7ow.jpg" alt="Citizen Reporting">
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="social-icons">
        <a href="https://web.whatsapp.com/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp">
        </a>
        <a href="https://www.facebook.com/login.php/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook">
        </a>
        <a href="https://www.instagram.com/vijay_sonke_28/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
        </a>
        <!-- Add more social icons if needed -->
        </div>

        """,
        unsafe_allow_html=True,
    )
