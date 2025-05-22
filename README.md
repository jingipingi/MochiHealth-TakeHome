# Mood Queue Logger
This app is hosted live on [Streamlit Cloud](https://juliananoronha-mochihealth-takehome.streamlit.app/)!

## Scenario
The Ops Team at Mochi would like a way to track support ticket moods! 

## Process Flow
1. Ops team members recieve tickets and can log the moods they're observing for specific tickets or groups of tickets seen within a day
2. Clicking submit sends the submission time, mood and note to a Google sheet (linked in the Stack section below)
3. Moods submitted on the current day are visualized in a bar chart in the app!

## Stack
* **Backend "Database"**: [This Google Sheet](https://docs.google.com/spreadsheets/d/1qFWRxwRvVc8SXp4RiMj3w26aHI3XHNFEbHJktNOyKes/edit?usp=sharing)
* **Frontend**: Streamlit (and deployed to Streamlit cloud!)
* **APIs used**: Google Cloud Console -> Google Drive API Service provisioned for the application

## Next Steps (other potential features)
* Adding a line chart that shows trends over time (each line would be a different mood, y-axis would be daily mood counts and x-axis would be submission date)

## Alternative options
The Ops team at Mochi of course has much better things to do than manually log ticket moods!
I can imagine the following infrastructure:
* Tickets are recorded in a backend relational database (e.g. postgres)
* An NLP pipeline is running at some frequency (or perhaps is triggered by new records) that automatically writes ticket sentiments back to the DB.
    * I personally have experience with the IBM Watson NLU API, but the specific NLP service used would depend on the cloud services we're using and the pricing.
    * Pipeline triggering would also depend on what we're willing to spend :)
* We could then make a ticket health dashboard (using LookerStudio or whatever SQL dashboarding tool we have available) that is automatically plotting all kinds of data related to ticket health, sentiment, etc. 
