import pandas as pd
import streamlit as st
import joblib as jb




model=jb.load(r'C:\Users\samir\Documents\proj\flight_prediction_rff.pkl')
expected_cols=jb.load(r'C:\Users\samir\Documents\proj\columns.pkl')



st.title("Flight price prediction via samir")
st.markdown("please fill the following info")


#journey
Dep_date_time=st.date_input("Departure Date")
Dep_time=st.time_input("departure time")
Dep_min=Dep_time.minute
Dep_hour=Dep_time.hour
journey_day=Dep_date_time.day
journey_month=Dep_date_time.month


#arrival

arrival_date_time=st.date_input("arrival date")
arrival_time=st.time_input("arrival time")
arrival_hour=arrival_time.hour
arrival_min=arrival_time.minute



# durations

duration_hours=abs(arrival_hour-Dep_hour)
duration_min=abs(arrival_min-Dep_min)

#stops

Total_stops=st.number_input("Total stops",min_value=0,max_value=4,step=1)

#airline
Airline=st.selectbox("Airline",['Jet Airways','IndiGo','Air India','Multiple carriers','SpiceJet','Vistara','Air Asia','GoAir','Multiple carriers premium economy','Jet Airways business','Vistara Premium economy','Trujet'])


Source=st.selectbox("Source",['Delhi','Kolkata','Banglore','Mumbai','Chennai'])
Destination=st.selectbox("Destination",['Cochin','Delhi','Hyderabad','Kolkata','New Delhi'])



input_data={
    "Total_stops":[Total_stops],
    "journey_day":[journey_day],
    "journey_month":[journey_month],
    "dep_hour":[Dep_hour],
    "dep_min":[Dep_min],
    "arrival_hour":[arrival_hour],
    "arrival_min":[arrival_min],
    "duration_hour":[duration_hours],
    "duration_min":[duration_min],
    "Airline":[Airline],
    "Source":[Source],
    "Destination":[Destination],
}


#dataframe ma conversion
input_df=pd.DataFrame(input_data)


# one hot encoding
input_df=pd.get_dummies(input_df)


for col in expected_cols:
    if col not in input_df.columns:
        input_df[col]=0


input_df=input_df[expected_cols]


if st.button("Predict Flight Price"):
    prediction = model.predict(input_df)
    st.success(f"💰 Predicted Flight Price: Rs. {round(prediction[0], 2)}")

 



