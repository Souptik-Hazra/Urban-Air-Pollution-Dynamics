
# Urban Air Pollution Dynamics Dashboard

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
- Manual refresh button for pollution map
- Custom plot selection via dropdowns

## Usage
1. Run the app: `streamlit run app.py`
2. Enter a city name to fetch and visualize data
3. Inspect raw API data in browser tabs
4. Explore interactive plots and custom scatter plots

## Images
(Add your screenshots below each section)

### Dataset & Raw API Data
_Example: Screenshot of dataset and raw API tabs_

### Time Series
_Example: Screenshot of PM2.5 time series plot_

### Correlation Heatmap
_Example: Screenshot of correlation heatmap_

### Pollution Clusters (3D)
_Example: Screenshot of 3D cluster plot_

### Regression Model
_Example: Screenshot of regression plot_

### Trends (Hourly, Daily, etc.)
_Example: Screenshot of trend plots_

### Pollution Map
_Example: Screenshot of pollution map with refresh button_

### Custom Component Scatter Plot
_Example: Screenshot of custom scatter plot selection_

---

## Interviewer Notes
- All code is modular and organized for easy review
- Data is always saved before processing
- All visualizations are interactive and customizable
- Easy to extend for more cities, data sources, or plot types