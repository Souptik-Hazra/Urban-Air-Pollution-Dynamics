## Urban Air Pollution Dynamics Research Project

This project investigates how meteorological variables influence air pollution levels and identifies temporal patterns and pollution clusters in urban environments.

### Features
- Fetches pollution and weather data from APIs
- Hourly, daily, monthly, seasonal, and yearly analysis
- Feature engineering for ratios and calendar variables
- Clustering and regression modeling
- Interactive Streamlit dashboard

### Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run dashboard: `streamlit run app.py`
3. Enter a city and explore results

### Structure
- `data/` - Data storage
- `src/` - Source code modules
- `app.py` - Dashboard entry point
- `requirements.txt` - Dependencies

### Suggestions
- Add more calendar features (holidays, events)
- Try different clustering/modeling algorithms
- Improve error handling and logging
- Add more visualizations (heatmaps, filters)