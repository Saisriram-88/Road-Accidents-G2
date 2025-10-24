# 🚗 US Road Accidents Analysis (2016-2023)

## 📖 Table of Contents
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [Analysis Components](#-analysis-components) 
- [Key Findings](#-key-findings)
- [Data Processing](#-data-processing)
- [Contributing](#-contributing)
- [Known Limitations](#-known-limitations)
- [License](#-license)
- [Team](#-team)
- [Acknowledgements](#-acknowledgements)

## 📊 Project Overview

A comprehensive data science project analyzing US road accidents from 2016-2023, leveraging a massive dataset of 7.7 million accident records. The project employs advanced data analysis techniques to uncover patterns in road safety and accident occurrence, aiming to provide actionable insights for reducing accident risks.

### Purpose
- Identify accident patterns and high-risk factors
- Enable data-driven road safety improvements
- Provide insights for traffic management
- Support policy-making with empirical evidence

## ✨ Features

### Core Analysis Components
- Univariate distribution analysis
- Bivariate relationship exploration
- Geospatial hotspot mapping
- Temporal pattern detection
- Weather impact assessment
- Infrastructure analysis

### Visualization Capabilities
- Interactive heatmaps
- Geographic accident plotting
- Statistical distribution plots
- Correlation matrices
- Time series visualizations

## 🛠 Technology Stack

### Core Technologies
- Python 3.x
- Jupyter Notebooks

### Key Libraries
- **Data Processing**: 
  - Pandas (1.x+)
  - NumPy (1.x+)
- **Visualization**: 
  - Matplotlib
  - Seaborn
  - Folium
- **Geospatial Analysis**:
  - GeoPandas
  - Shapely
- **Data Loading**:
  - Kaggle API

## 📂 Project Structure

This repository contains six main analytical notebooks:

### 1. 📊 EDA Overview (`RoadSafe_Analytics_EDA.ipynb`)

- Initial data loading and preprocessing
- Dataset characteristics and quality assessment
- Preliminary insights extraction
- Missing value analysis and data cleaning

### 2. 📈 Univariate Analysis (`Univariate_Analysis.ipynb`)

- Distribution analysis of individual variables
- Time-based patterns (yearly, monthly, hourly)
- Categorical variable frequencies
- Numerical variable distributions

### 3. 🔄 Bivariate Analysis (`Bivarient_Analysis.ipynb`)

- Relationship between accident severity and weather conditions
- Impact of visibility on accident severity
- Correlation analysis between numerical variables
- Traffic features vs accident severity

### 4. 📊 Multivariate Analysis (`Multivarient_analysis.ipynb`)

- Complex relationships between multiple variables
- Principal Component Analysis (PCA)
- Feature importance analysis
- Interaction effects between variables

### 5. 🗺️ Geospatial Analysis (`Geospaal_and_Location_Based_Analysis.ipynb`)

- Nationwide accident hotspot visualization
- State-level accident density analysis
- City-level accident patterns
- Interactive heatmaps using Folium

### 6. 📌 Hypothesis Testing (`Hypothesis_Testing.ipynb`)

- Statistical significance testing
- Weather impact hypothesis validation
- Time-of-day effect analysis
- Infrastructure influence testing

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
   - Multivarient_analysis.ipynb
   - Geospaal_and_Location_Based_Analysis.ipynb
   - Hypothesis_Testing.ipynb

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

- [P.Sai Sriram](https://github.com/Saisriram-88)
- [Prerna Chhabra](https://github.com/Prerna1317)
- [Thirukovela Moulya](https://github.com/rishi300101)
- [NIKHIL KRISHNA](https://github.com/nikhil-krishna-2003)
- [V.Kishan](https://github.com/kishuverse)

## 🙏 Acknowledgements

- Sobhan Moosavi for creating and maintaining the US Accidents dataset
- Kaggle for hosting the dataset
- Contributors to the Python data science ecosystem
