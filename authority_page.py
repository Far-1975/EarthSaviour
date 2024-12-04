import streamlit as st
import pandas as pd
from utils import load_issue_tickets, save_issue_ticket, send_email_to_citizen

def add_custom_styles():
    st.markdown(
        """
        <style>
        /* Body and Background Styling */
        body {
            background-image: url('https://th.bing.com/th/id/OIP.wFeEKmSErNWbK85eWetBNwHaE8?w=241&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7');
            font-family: 'Arial', sans-serif;
            background-attachment: fixed;
            color: #fff;
            padding: 20px;
            margin: 0;
            overflow: hidden;
        }

        /* Title Styling */
        .stTitle, .stHeader > header {
            font-size: 4em;
            color: #fff;
            text-align: center;
            margin: 0;
            font-weight: bold;
            text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5), 0 0 25px rgba(255, 255, 255, 0.5);
            animation: glow 1.5s ease-in-out infinite alternate;
        }

        /* Animation for glowing effect */
        @keyframes glow {
            0% {
                text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5), 0 0 25px rgba(255, 255, 255, 0.5);
            }
            50% {
                text-shadow: 3px 3px 15px rgba(0, 255, 255, 0.8), 0 0 30px rgba(255, 255, 255, 0.9);
            }
            100% {
                text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5), 0 0 25px rgba(255, 255, 255, 0.5);
            }
        }

        /* Header Container Styling */
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
        }

        @keyframes gradient-move {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Manage Issue Tickets Section Header Styling */
        .section-header {
            font-size: 3.2em;
            color: #fff;
            text-align: center;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 0px 4px 8px rgba(0, 0, 0, 0.7), 0 0 25px rgba(255, 255, 255, 0.5);
            background: linear-gradient(90deg, rgba(255, 255, 255, 0.1), rgba(0, 255, 255, 0.6));
            padding: 10px 25px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.4);
            animation: pulse 1.5s infinite alternate;
        }

        /* Pulse animation effect */
        @keyframes pulse {
            0% {
                transform: scale(1);
                box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.4);
            }
            100% {
                transform: scale(1.05);
                box-shadow: 0px 10px 25px rgba(0, 255, 255, 0.5);
            }
        }

        /* Button Styling */
        .button {
            background-color: #4caf50;
            color: white;
            padding: 10px 20px;
            font-size: 1.2em;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        .button:hover {
            transform: scale(1.05);
        }

        /* Table Styling */
        .stDataFrame {
            margin-top: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
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

        </style>
        """,
        unsafe_allow_html=True,
    )

def authority_interface():
    add_custom_styles()  # Apply custom styles

    st.markdown(
        """
        <div class="header-container">
            <h1 class="stTitle">BBMP Authority</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div class="section-header">
            Manage Issue Tickets
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Load tickets
    issue_tickets = load_issue_tickets()

    if issue_tickets:
        df_tickets = pd.DataFrame(issue_tickets)

        # Display open tickets
        open_tickets = [ticket for ticket in issue_tickets if ticket["status"] == "Open"]
        st.subheader("Open Tickets")

        if open_tickets:
            st.dataframe(pd.DataFrame(open_tickets), use_container_width=True)

            # Manage a selected ticket
            ticket_index = st.selectbox("Select a Ticket to Manage", range(len(open_tickets)))

            if ticket_index is not None:
                selected_ticket = open_tickets[ticket_index]

                st.subheader("Ticket Details")
                st.json(selected_ticket)

                # Resolve or take action
                if st.button("Mark as Resolved", key="mark-resolved", help="Click to resolve this ticket"):
                    # Mark ticket as resolved
                    selected_ticket["status"] = "Resolved"
                    save_issue_ticket(issue_tickets)  # Save updated ticket list to CSV

                    # Notify the citizen
                    st.success("Ticket marked as resolved!")

                    # Compose the email content
                    citizen_name = selected_ticket["name"]
                    citizen_email = selected_ticket["email"]
                    subject = f"Your reported issue '{selected_ticket['description']}' has been resolved"
                    body = f"Dear {citizen_name},\n\nYour reported issue '{selected_ticket['description']}' has been resolved. Thank you for bringing it to our attention.\n\nBest regards,\nBBMP Authority"
                    
                    # Send the email
                    send_email_to_citizen(citizen_email, subject, body)

                    # Simulate notifying the citizen in the app
                    st.write(f"Message sent to citizen: {citizen_name}")

                    # Refresh the page after resolving
                    st.rerun()  # Use st.rerun() to refresh the page and display the updated ticket status.
        else:
            st.info("No open tickets available.")
    else:
        st.info("No tickets to display.")

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