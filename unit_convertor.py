import streamlit as st

st.title("Unit Convertor App")
st.markdown("#### Convert Length, Weight and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to meters":
            return value * 1000 
        elif unit == "meters to kilometers":
            return value / 1000  

    elif category == "Weight":
        if unit == "kilograms to grams":
            return value * 1000  
        elif unit == "grams to kilograms":
            return value / 1000  
    
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24

if category == "Length":
    unit = st.selectbox("Select conversion", ["kilometers to meters", "meters to kilometers"])            
elif category == "Weight":
    unit = st.selectbox("Select conversion", ["kilograms to grams", "grams to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select conversion", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])

value = st.number_input("Enter the value to convert")    
    
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")

st.write("**Created by Muhammad Asad**")                          

