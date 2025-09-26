# 🚗 US Road Accidents Analysis (2016-2023)

## 📊 Project Overview

A comprehensive analysis of US road accidents using a dataset containing approximately 7.7 million accidents recorded between 2016-2023. The project explores various aspects of accidents through multiple analytical lenses to understand patterns, causes, and potential prevention strategies.

## 🎯 Objectives

- Analyze accident patterns and severity across different conditions
- Identify high-risk locations and time periods
- Understand the impact of weather and road conditions on accidents
- Generate actionable insights for road safety improvements

## 📂 Repository Structure

This repository contains four main analytical notebooks:

### 1. 📈 Univariate Analysis (`Univariate_Analysis.ipynb`)

- Basic data exploration and cleaning
- Distribution analysis of individual variables
- Time-based patterns (yearly, monthly, hourly)
- Missing value analysis

### 2. 🔄 Bivariate Analysis (`Bivarient_Analysis.ipynb`)

- Relationship between accident severity and weather conditions
- Impact of visibility on accident severity
- Correlation analysis between numerical variables
- Traffic features vs accident severity

### 3. 🗺️ Geospatial Analysis (`Geospaal_and_Location_Based_Analysis.ipynb`)

- Nationwide accident hotspot visualization
- State-level accident density analysis
- City-level accident patterns
- Interactive heatmaps using Folium

### 4. 📊 EDA Overview (`RoadSafe_Analytics_EDA.ipynb`)

- Initial data loading and preprocessing
- Dataset characteristics
- Preliminary insights
- Data quality assessment

## 🔑 Key Findings

### Weather Impact

- Poor visibility (<2 miles) significantly increases accident severity
- Rain and fog conditions lead to higher severity accidents
- Clear weather has the most accidents but lower average severity

### Infrastructure Effects

- Traffic signals help reduce accident severity
- Crossings show higher proportion of severe accidents
- Location-based patterns reveal urban area hotspots

### Temporal Patterns

- Clear daily and seasonal patterns in accident occurrence
- Peak hours correlate with commute times
- Seasonal variations affect accident frequency

## 🛠️ Technologies Used

- Python 3.x
- Pandas for data manipulation
- Matplotlib & Seaborn for visualization
- Folium for interactive maps
- GeoPandas for geospatial analysis

## 📊 Dataset

**Source**: [US Accidents (2016-2023)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)

- 7.7+ million accident records
- 47 variables including location, time, weather, and road conditions
- Coverage of 49 states in the United States

## 🔍 Getting Started

### Prerequisites

```python
pip install pandas numpy matplotlib seaborn folium geopandas
```

### Running the Analysis

1. Clone this repository
2. Download the dataset from Kaggle
3. Update file paths in notebooks if necessary
4. Run notebooks in the following order:
   - RoadSafe_Analytics_EDA.ipynb
   - Univariate_Analysis.ipynb
   - Bivarient_Analysis.ipynb
   - Geospaal_and_Location_Based_Analysis.ipynb

## 💡 Recommendations

1. Improve street lighting and signalization in accident-prone areas
2. Implement real-time weather alert systems
3. Focus on intersection safety improvements
4. Enhanced monitoring of high-risk locations
5. Driver education programs for adverse weather conditions

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss proposed changes.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Authors

- P.Sai Sriram
- Prerna Chhabra
- Sindhu Musturu
- NIKHIL KRISHNA
- V.Kishan

## 🙏 Acknowledgements

- Sobhan Moosavi for creating and maintaining the US Accidents dataset
- Kaggle for hosting the dataset
- Contributors to the Python data science ecosystem
