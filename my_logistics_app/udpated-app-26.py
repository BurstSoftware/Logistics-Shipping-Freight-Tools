import streamlit as st

st.set_page_config(page_title="Logistics Concepts", layout="wide")

# -----------------------------
# PAGE 1 – Freight Broker
# -----------------------------
def page_freight_broker():
    st.title("🚛 What is a Freight Broker?")
    st.markdown("""
A **freight broker** acts as a middleman connecting shippers (companies needing goods shipped)
with carriers (trucking companies that haul freight).

### What Freight Brokers Do
- Match loads with carriers  
- Negotiate freight rates  
- Coordinate logistics and communication  
- Handle paperwork and compliance  
- Assist with issues during transit  

Freight brokers are the “connectors” of the supply chain.
    """)

# -----------------------------
# PAGE 2 – Logistics Sales
# -----------------------------
def page_logistics_sales():
    st.title("📦 What is Logistics Sales?")
    st.markdown("""
**Logistics sales** is the process of selling shipping and supply chain services such as trucking,
freight brokerage, warehousing, and global freight forwarding.

### Responsibilities
- Find and qualify shipping customers  
- Understand freight needs  
- Create quotes and pricing  
- Negotiate rates and contracts  
- Maintain long-term customer relationships  
- Coordinate with operations  

Logistics sales keeps freight moving and drives business growth.
    """)

# -----------------------------
# PAGE 3 – Active Book of Shipping Customers
# -----------------------------
def page_active_book():
    st.title("📘 What is an Active Book of Shipping Customers?")
    st.markdown("""
An **active book of shipping customers** is a freight broker or salesperson’s current,
revenue-producing list of shippers who regularly send them freight.

### What Makes a Book ‘Active’
- Consistent shipping volume  
- Strong existing relationships  
- Active quoting, booking, and communication  
- Loads currently being moved  
- Not just leads or inactive accounts  

A broker’s active book shows their earning power and industry value.
    """)

# -----------------------------
# PAGE 4 – TMS, Load Boards, Truckstop, Sylectus & Back Office Support
# -----------------------------
def page_tms_loadboards():
    st.title("🧰 TMS, Load Boards, Truckstop, Sylectus & Back Office Support")

    st.markdown("## 🚛 Transportation Management System (TMS)")
    st.markdown("""
A **TMS** is software used by freight brokers, carriers, and shippers 
to manage transportation operations from start to finish.

### What a TMS Does
- Build and manage loads  
- Track shipments  
- Store customer & carrier data  
- Generate documents  
- Integrate with load boards  
    """)

    st.markdown("---")

    st.markdown("## 📋 Load Boards")
    st.markdown("""
A **load board** is an online marketplace where brokers post loads 
and carriers find freight to haul.

### Common Uses
- Brokers post available freight  
- Carriers search for loads  
- Real-time communication  
- Market rate tools  
    """)

    st.markdown("---")

    st.markdown("## 🟧 Truckstop")
    st.markdown("""
**Truckstop** is one of the largest load board platforms in the industry.

### Features
- Freight postings  
- Carrier safety/insurance checks  
- Market rates & analytics  
- Book-It-Now tools  
    """)

    st.markdown("---")

    st.markdown("## 🔵 Sylectus")
    st.markdown("""
**Sylectus** is a specialized load board for expedited freight with a 
closed, vetted carrier network.

### Highlights
- Vetted carrier-only network  
- Load sharing  
- Expedited freight tools  
- Built-in tracking  
    """)

    st.markdown("---")

    st.markdown("## 🧾 Back Office Support")
    st.markdown("""
Back office support includes the administrative tasks that keep a freight brokerage running.

### Common Tasks
- Carrier onboarding  
- Customer credit checks  
- Invoicing & billing  
- POD document collection  
- Collections  
- Compliance  
- Data entry  
    """)

    st.success("This page explains the critical systems and tools used across freight brokerage operations.")


# -----------------------------
# NAVIGATION (MULTI-PAGE SYSTEM)
# -----------------------------
pg = st.navigation(
    {
        "Logistics Concepts": [
            st.Page(page_freight_broker, title="Freight Broker", icon="🚛"),
            st.Page(page_logistics_sales, title="Logistics Sales", icon="📦"),
            st.Page(page_active_book, title="Active Book of Customers", icon="📘"),
            st.Page(page_tms_loadboards, title="TMS / Load Boards / Back Office", icon="🧰"),
        ]
    }
)

pg.run()
