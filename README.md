# Sprint4Project
This project shows the analysis of a dataframe containg 51525 used car listings in the USA for the period 2018-2019.
The conclusion is that the most important factor in determining the value of a used car is the odometer reading.<br><br>
Using plotly.express, we created a histogram of odometer readings, showing that most used cars have between 100k-150k miles, the average being 115,553.46 miles. The average price of a used car is $12,132.46.<br>
Using plotly.express, we created a scatterplot showing the relation between price/odometer reading. The tendency is a clear inverse correlation between price and odometer readings.<br>
Using Feature Engineering we created a function to extract the car maker brand from the 'model' column and created a bar chart showing the counts by car maker, using Altair. This chart shows brand popularity in the USA and it has been included as an optional feature in the app which can be accesed by clicking a Streamlit checkbox.<br><br>

This project has been implemented on Streamlit and is available as a web application on Render.com<br>
The source code can be found at https://github.com/JoseGarayBoszeta/Sprint4Project.git<br>
To run on a local machine, download the repository and run app.py on Streamlit at the terminal<br>
-> Open terminal, go to the directory and type streamlit run app.py<br><br>