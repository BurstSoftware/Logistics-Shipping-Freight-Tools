# app.py
import streamlit as st
import pandas as pd
from datetime import datetime

# ————————————————————————
# Page config & styling
# ————————————————————————
st.set_page_config(
    page_title="Transfer Logistics Tool",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .big-font {font-size: 2.5rem !important; font-weight: bold; color: #8B1A1A;}
    .section {margin: 2rem 0;}
    .check {color: #228B22; font-weight: bold;}
    .stButton>button {background-color: #8B1A1A; color: white;}
</style>
""", unsafe_allow_html=True)

# ————————————————————————
# Sidebar navigation
# ————————————————————————
st.sidebar.markdown("<h2 style='color:#8B1A1A;'>Dispatcher Skills</h2>", unsafe_allow_html=True)

pages = {
    "🏠 Home": "home",
    "📚 Freight Brokerage Knowledge": "knowledge",
    "💰 Negotiate Rates & Contracts": "negotiate",
    "💬 Communication Skills": "communication",
    "🔍 Prospect New Carriers": "prospect",
    "🚚 Coordinate Freight Movement": "coordinate",
    "🛠 Resolve Logistical Challenges": "resolve",
    "💸 Competitive Pay & Apply": "apply"
}

choice = st.sidebar.radio("Go to", list(pages.keys()))
page = pages[choice]

# ————————————————————————
# Page content
# ————————————————————————
if page == "home":
    st.image("https://via.placeholder.com/800x400?text=Smart+Move+Logistics", use_column_width=True)
    st.markdown("""
    ### Welcome to the **Logistics Dispatcher Mastery Hub**  
    Master every skill Transfer needs in 7 interactive modules.  
    Click any page on the left to dive in!
    """)

elif page == "knowledge":
    st.header("📚 Knowledge Base for Freight Brokerage")
    st.markdown("""
    **Goal:** Know every lane, tariff, and regulation like the back of your hand.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Quick Quiz")
        q = st.radio("What does LTL stand for?", 
                     ["Less-Than-Truckload", "Long-Term Lease", "Local Transit Line"])
        if q == "Less-Than-Truckload":
            st.success("Correct! 🎯")
    with col2:
        st.subheader("Hot Resources")
        st.markdown("- [FMCSA Regulations](https://www.fmcsa.dot.gov)")
        st.markdown("- [DAT RateView](https://www.dat.com)")

elif page == "negotiate":
    st.header("💰 Negotiate Rates & Contracts")
    st.markdown("Practice live negotiation scenarios.")
    carrier_rate = st.slider("Carrier’s asking rate ($/mile)", 1.5, 4.0, 2.5, 0.05)
    your_offer = st.number_input("Your counter-offer ($/mile)", 1.0, 3.0, 2.1, 0.05)
    if st.button("Simulate Deal"):
        savings = carrier_rate - your_offer
        st.metric("You saved", f"${round(savings*500, 2)} on a 500-mile load")
        if savings > 0.3:
            st.balloons()

elif page == "communication":
    st.header("💬 Communication & Interpersonal Skills")
    st.markdown("Draft perfect emails & calls.")
    template = st.selectbox("Choose template", 
                            ["Load Confirmation", "Rate Confirmation", "Check-Call Update"])
    body = {
        "Load Confirmation": "Hi [Carrier], Load #123 is confirmed for pickup 11/08 at 08:00...",
        "Rate Confirmation": "Thank you for accepting $2.15/mile on load 123...",
        "Check-Call Update": "Driver called in at 14:30, currently 200 miles out..."
    }
    msg = st.text_area("Edit & send", body.get(template, ""), height=200)
    if st.button("Send 🚀"):
        st.success("Message sent to carrier!")

elif page == "prospect":
    st.header("🔍 Prospect & Acquire New Carriers")
    st.markdown("Build your carrier pipeline.")
    uploaded = st.file_uploader("Upload carrier list (CSV)", type=["csv"])
    if uploaded:
        df = pd.read_csv上传(uploaded)
        st.dataframe(df.head())
        st.info(f"{len(df)} new carriers ready to onboard!")

elif page == "coordinate":
    st.header("🚚 Coordinate Movement of Freight")
    st.markdown("Real-time load board simulator.")
    loads = pd.DataFrame({
        "Load ID": ["123", "456", "789"],
        "Origin": ["Chicago, IL", "Dallas, TX", "Atlanta, GA"],
        "Dest": ["LA, CA", "NYC, NY", "Miami, FL"],
        "Pickup": [datetime(2025, 11, 8, 8), datetime(2025, 11, 9, 14), datetime(2025, 11, 10, 10)],
        "Status": ["Tendered", "In Transit", "Delivered"]
    })
    st.dataframe(loads, use_container_width=True)
    selected = st.selectbox("Track load", loads["Load ID"])
    st.map(pd.DataFrame({
        "lat": [41.8781, 34.0522], 
        "lon": [-87.6298, -118.2437]
    }))

elif page == "resolve":
    st.header("🛠 Identify & Resolve Logistical Challenges")
    st.markdown("Solve today’s headache in 3 clicks.")
    issue = st.selectbox("Issue", 
                         ["Late pickup", "Driver breakdown", "Accessorial charge dispute"])
    solutions = {
        "Late pickup": "Call backup carrier + expedite next load",
        "Driver breakdown": "Dispatch roadside assistance + reroute",
        "Accessorial charge dispute": "Pull BOL + escalate to accounting"
    }
    st.info(solutions[issue])
    if st.button("Create Resolution Ticket"):
        st.success("Ticket #RES-2025-11 opened!")

elif page == "apply":
    st.header("💸 Competitive Pay & Apply TODAY")
    st.markdown("""
    - Base + commission (top dispatchers earn **$80k+**)  
    - Full benefits & 401k  
    """)
    with st.form("apply_form"):
        name = st.text_input("Full Name")
        phone = st.text_input("Phone")
        resume = st.file_uploader("Resume (PDF)", type=["pdf"])
        submitted = st.form_submit_button("Submit Application")
        if submitted:
            st.success(f"Thank you, {name}! Ben will call you at {phone} within 24 hrs.")
            st.balloons()

# ————————————————————————
# Footer
# ————————————————————————
st.markdown("---")
st.markdown("""
<div style='text-align:center;'>
</div>
""", unsafe_allow_html=True)
