import streamlit as st

# Function for Waste Collection Status
def waste_collection_status():
    st.header("Submit Waste Details")
    st.info("Provide your waste details to send them to appropriate buyers.")

    # User input fields
    name = st.text_input("Your Name")
    address = st.text_area("Your Address")
    phone = st.text_input("Your Phone Number")
    waste_type = st.selectbox(
        "Type of Waste",
        ["Recyclable", "Biodegradable", "E-Waste"]
    )
    weight = st.number_input("Weight of Waste (in kg)", min_value=0.1, step=0.1)

    # Submit button
    if st.button("Submit Waste Details"):
        if name and address and phone and weight > 0:
            # Example: Save waste details (replace with actual implementation)
            waste_data = {
                "name": name,
                "address": address,
                "phone": phone,
                "waste_type": waste_type,
                "weight": weight
            }
            st.success("Waste details submitted successfully!")
            st.write("Your submitted information:")
            st.json(waste_data)
        else:
            st.error("Please fill in all required fields.")

# Function for Feedback to Authorities
def feedback_to_authorities():
    st.header("Buyers and Payments")

    # Simulated list of buyers
    buyers = [
        {"name": "Recycle Co.", "contact": "123-456-7890", "accepted_waste": ["Recyclable"]},
        {"name": "Green Bio Ltd.", "contact": "987-654-3210", "accepted_waste": ["Biodegradable"]},
        {"name": "E-Waste Solutions", "contact": "555-666-7777", "accepted_waste": ["E-Waste"]},
    ]

    # Display buyers
    st.subheader("Available Buyers")
    for buyer in buyers:
        st.write(f"Name: {buyer['name']}")
        st.write(f"Contact: {buyer['contact']}")
        st.write(f"Accepted Waste Types: {', '.join(buyer['accepted_waste'])}")
        st.markdown("---")

    # Payment section
    st.subheader("Payment Details")
    buyer_name = st.selectbox("Select Buyer", [buyer["name"] for buyer in buyers])
    
    # Simulate payment amount based on waste type and weight
    # (In real-world, calculate based on actual rates)
    payment_amount = st.number_input(
        "Enter Estimated Payment Amount (in $)", 
        min_value=0.1, 
        step=0.1, 
        help="Estimated amount buyer pays for the waste."
    )

    # Confirm payment
    if st.button("Confirm Payment Receipt"):
        if buyer_name and payment_amount > 0:
            st.success(f"You will receive ${payment_amount} from {buyer_name}.")
        else:
            st.error("Please fill in all required fields.")

# Sidebar for navigation
st.sidebar.title("Activities")
activity = st.sidebar.radio("Select an activity", ["Submit Waste Details", "Buyers and Payments"])

# Render the selected activity
if activity == "Submit Waste Details":
    waste_collection_status()
elif activity == "Buyers and Payments":
    feedback_to_authorities()