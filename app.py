import pandas as pd
import streamlit as st
import plotly.express as px

vehi_us = pd.read_csv('./vehicles_us.csv')

st.header('Used Car listings in the USA (2018-19)')
st.markdown("An analysis of a dataframe containing 51525 used car listings for the period 2018-05-01 to 2019-04-19.")
st.write(vehi_us)

# Feature Engineering: Add 'car_maker' column
# List of car makers
car_makers = ['bmw', 'ford', 'hyundai', 'chrysler', 'toyota', 'honda', 'kia', 'chevrolet',
              'ram', 'gmc', 'jeep', 'nissan', 'subaru', 'dodge', 'mercedes-benz', 'acura',
              'cadillac', 'volkswagen', 'buick']
# Function to extract car maker and create a new column
def extract_car_maker(vehi_us, car_makers):
    # Initialize a new column with None
    vehi_us['car_maker'] = None
    # Iterate through the car makers and set the Car_Maker column
    for maker in car_makers:
        vehi_us['car_maker'] = vehi_us.apply(lambda row: maker if maker in row['model'] else row['car_maker'], axis=1)
    return vehi_us

# Call the function to add the Car_Maker column
vehi_us = extract_car_maker(vehi_us, car_makers)

# Create dataframe with car maker counts
brands = vehi_us['car_maker'].value_counts().reset_index()
# Rename the columns for clarity
brands.columns = ['maker', 'count']
# Car maker bar chart in plotly express
fig = px.bar(brands, x='maker', y='count', title='Car maker brands by popularity')
fig.update_traces(marker_color='green', marker_line_color='black', marker_line_width=2)
fig.update_xaxes(title_text='Car Maker Brands', tickangle=45, tickfont=dict(size=14))
fig.update_yaxes(title_text='Count', title_font=dict(size=16))
fig.update_layout(
    title_font=dict(size=24),
    title_x=0.5,
    barmode='group',
    bargap=0.2)
st.write(fig, brands)

#add checkbox to display car brands count info:
#check = st.checkbox("Click here to see car brands by popularity")
#if check:
    #st.write(fig, brands)

st.markdown("The most important factor in determining the value of a used car is odometer readings:")
fig = px.histogram(vehi_us, x='odometer', title='Histogram of odometer readings',
                   nbins=100,
                   color_discrete_sequence=['blue'],
                   opacity=0.7,
                   range_x=(0, 600000)
                   )

odo_mean = vehi_us['odometer'].mean()
price_mean = vehi_us['price'].mean()
st.write(fig)
st.write("The average odometer reading is:", f"{odo_mean:.2f}", "miles")
st.write("The average price is:", f"{price_mean:.2f}", "US dollars")

fig = px.scatter(vehi_us, x='price', y='odometer')
fig.update_traces(marker=dict(size=3, opacity=0.3, line=dict(width=1, color='blue')))
fig.update_layout(title='Scatterplot Price/Odometer (zoom)', xaxis_title='Price', yaxis_title='Odometer')
fig.update_xaxes(range=[0, 75000])  # Set the x-axis range from 2 to 4
fig.update_yaxes(range=[0, 400000])  # Set the y-axis range from 1 to 5
st.write(fig)
st.write("Most cars are under $50,000 and have under 400,000 miles.")
st.write("The tendency is a clear inverse correlation between price and odometer readings.")
st.write("The few outliers can be attributed to all other variables such as color, transmission, type, etc.")