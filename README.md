

# Urban Air Pollution Dynamics Dashboard

Live App: [https://urban-air-pollution-dynamics-souptik-hazra.streamlit.app/](https://urban-air-pollution-dynamics-souptik-hazra.streamlit.app/)

A Streamlit dashboard for visualizing, analyzing, and exploring urban air pollution and weather data using Plotly.

## Features
- Fetches pollution and weather data from APIs for any city
- Saves raw API data to CSV for each city (data/<city>_pollution.csv)
- Appends new data to CSV on each run, avoiding duplicates
- Displays raw pollution and weather API data for inspection
- Preprocesses and merges data for analysis
- Interactive visualizations:
	- Time Series (PM2.5)
	- Correlation Heatmap
	- Pollution Clusters (3D)
	- Regression Model
	- Hourly, Daily, Monthly, Seasonal, Yearly Trends
	- Pollution Map (with manual refresh)
	- Custom scatter plot for any two pollution components
- Pollution map
- Custom plot selection via dropdowns

## Usage
1. Run the app: `streamlit run app.py`
2. Enter a city name to fetch and visualize data
3. Inspect raw API data in browser tabs
4. Explore interactive plots and custom scatter plots
