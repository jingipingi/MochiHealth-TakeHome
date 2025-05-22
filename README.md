# Mood Queue Logger
This app is hosted live on [Streamlit Cloud](https://juliananoronha-mochihealth-takehome.streamlit.app/)!

## Scenario
The Ops Team at Mochi would like a way to track support ticket moods! 

## Process Flow
1. Ops team members recieve tickets and can log the moods they're observing for specific tickets or groups of tickets seen within a day
2. Clicking submit sends the submission time, mood and note to a Google sheet (linked in the Stack section below)
3. Moods submitted on the current day are visualized in a bar chart in the app!

## Stack
**Backend "Database"**: [This Google Sheet](https://docs.google.com/spreadsheets/d/1qFWRxwRvVc8SXp4RiMj3w26aHI3XHNFEbHJktNOyKes/edit?usp=sharing)
**Frontend**: Streamlit (and deployed to Streamlit cloud!)
**APIs used**: Google Cloud Console -> Google Drive API Service provisioned for the application
