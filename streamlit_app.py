
import streamlit as st
import pandas as pd
from datetime import date
from database import engine, SessionLocal, Base
from models import Customer

Base.metadata.create_all(bind=engine)

st.set_page_config(page_title="FollowUp AI", page_icon="🤖", layout="wide")
st.title("AI-Powered Customer Follow-Up Assistant")
today = date.today()

# ---------- Adding Customer Form ----------
st.subheader("Add Customer")

with st.form("customer_form"):
    name = st.text_input("Customer Name")
    contact = st.text_input("Contact (email or phone)")
    company = st.text_input("Company")
    last_interaction = st.date_input("Last Interaction Date", value=today)
    next_followup = st.date_input("Next Follow-Up Date", value=today)
    status = st.selectbox("Status", ["New", "Interested", "Follow-up Needed", "Closed"])
    interest_level = st.selectbox("Interest Level", ["Low", "Medium", "High"])
    notes = st.text_area("Notes")

    submitted = st.form_submit_button("Save Customer")

    if submitted:
        if name and contact:
            db = SessionLocal()
            customer = Customer(
                name=name,
                contact=contact,
                company=company,
                last_interaction=last_interaction,
                next_followup=next_followup,
                status=status,
                interest_level=interest_level,
                notes=notes,
            )
            db.add(customer)
            db.commit()
            db.close()
            st.success("Customer saved successfully!")
        else:
            st.warning("Please fill in Customer Name and Contact.")

st.divider()

# ---------- Loading Customers ----------
db = SessionLocal()
customers = db.query(Customer).all()
db.close()

def followup_bucket(next_followup_date):
    if not next_followup_date:
        return "No Date"
    if next_followup_date < today:
        return "Overdue"
    elif next_followup_date == today:
        return "Due Today"
    else:
        return "Upcoming"

# ---------- Converteng to DataFrame ----------
data = []
for c in customers:
    bucket = followup_bucket(c.next_followup)
    data.append({
        "ID": c.id,
        "Name": c.name,
        "Contact": c.contact,
        "Company": c.company,
        "Last Interaction": c.last_interaction,
        "Next Follow-Up": c.next_followup,
        "Status": c.status,
        "Interest": c.interest_level,
        "Notes": c.notes,
        "Bucket": bucket,
    })

df = pd.DataFrame(data)

# ---------- Dashboard ----------
st.subheader("Follow-Up Dashboard")

if not df.empty:
    overdue_count = (df["Bucket"] == "Overdue").sum()
    today_count = (df["Bucket"] == "Due Today").sum()
    upcoming_count = (df["Bucket"] == "Upcoming").sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Overdue", overdue_count)
    col2.metric("Due Today", today_count)
    col3.metric("Upcoming", upcoming_count)

    tab1, tab2, tab3, tab4 = st.tabs(["All Customers", "Overdue", "Due Today", "Upcoming"])

    with tab1:
        st.dataframe(df, use_container_width=True)

    with tab2:
        st.dataframe(df[df["Bucket"] == "Overdue"], use_container_width=True)

    with tab3:
        st.dataframe(df[df["Bucket"] == "Due Today"], use_container_width=True)

    with tab4:
        st.dataframe(df[df["Bucket"] == "Upcoming"], use_container_width=True)
else:
    st.info("No customers added yet.")
    
# Integrating MIstral model to write personolised followup mwssages based on customer details 

from llm import generate_followup

st.divider()
st.subheader("Generate Follow-Up Message")

if not df.empty:
    customer_names = df["Name"].tolist()
    selected_name = st.selectbox("Select a customer", customer_names)

    tone = st.selectbox("Select tone", ["professional", "polite", "friendly", "persuasive"])

    selected_row = df[df["Name"] == selected_name].iloc[0]

    customer_data = {
        "name": selected_row["Name"],
        "contact": selected_row["Contact"],
        "company": selected_row["Company"],
        "last_interaction": str(selected_row["Last Interaction"]),
        "next_followup": str(selected_row["Next Follow-Up"]),
        "status": selected_row["Status"],
        "interest_level": selected_row["Interest"],
        "notes": selected_row["Notes"],
    }

    if st.button("Generate Follow-Up"):
        with st.spinner("Generating message..."):
            output = generate_followup(customer_data, tone=tone)
            st.text_area("Generated Follow-Up", output, height=220)
else:
    st.info("Add customers first to generate a message.")