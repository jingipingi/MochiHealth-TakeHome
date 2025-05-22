import streamlit as st
import pandas as pd
import plotly.express as px
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# --- Google Sheets Setup ---
SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Upload your service account credentials JSON file in Streamlit
creds_json = st.secrets["gcp_service_account"]  # assumes use of Streamlit secrets for security
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, SCOPE)
client = gspread.authorize(credentials)
sheet = client.open("Mood Queue Log").sheet1  # assumes the sheet exists with headers: Timestamp, Mood, Note

# --- Log Mood UI ---
st.title("Mood of the Ticket Queue")
st.subheader("Log the moods you're seeing on tickets!")

mood = st.selectbox("Select a mood:", ["😊", "😠", "😕", "🎉", "Other"])
note = st.text_input("Optional note:")

if st.button("Submit Mood"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, mood, note])
    st.success("Mood logged!")

# --- Visualization ---
st.subheader("Today's Mood Summary")

# Load data from Google Sheet
raw_records = sheet.get_all_records()

if raw_records:
    data = pd.DataFrame(raw_records)

    # Defensive: ensure required columns exist
    if "Timestamp" in data.columns and "Mood" in data.columns:
        try:
            data["Timestamp"] = pd.to_datetime(data["Timestamp"], errors="coerce")
            data_today = data[data["Timestamp"].dt.date == datetime.today().date()]

            if not data_today.empty:
                mood_counts = data_today["Mood"].value_counts().reset_index()
                mood_counts.columns = ["Mood", "Count"]
                fig = px.bar(mood_counts, x="Mood", y="Count", title="Mood Count for Today", text="Count")
                st.plotly_chart(fig)
            else:
                st.info("No mood entries for today yet. Be the first to log one! 😊")

        except Exception as e:
            st.error(f"Error processing timestamps: {e}")

    else:
        st.warning("Data format issue: missing expected columns.")
else:
    st.info("No mood entries have been logged yet. Start the trend!")

# Signature :)
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        color: gray;
        font-size: 0.9em;
    }
    </style>
    <div class="footer">
        Made by Juliana Noronha
    </div>
    """,
    unsafe_allow_html=True
)

