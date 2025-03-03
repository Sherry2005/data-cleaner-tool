# Data Cleaner Tool

## Overview
This Python script is designed to clean datasets efficiently using Pandas and Scikit-Learn. It removes duplicates, handles missing values, fixes data types, standardizes text, and removes outliers to ensure high-quality data processing.

## Features
- **Remove Duplicates**: Eliminates duplicate rows.
- **Handle Missing Values**: Fills missing data using mean, median, or mode.
- **Fix Data Types**: Converts strings to numeric values or dates.
- **Standardize Text**: Formats text to lowercase and removes extra spaces.
- **Remove Outliers**: Uses the Z-score method to eliminate extreme values.

## Installation
To use this script, install the necessary dependencies:
```sh
pip install pandas numpy scikit-learn
```

## Usage
1. Replace the dataset path in `df = pd.read_excel(r"D:\Book1.xlsx")` with your dataset.
2. Run the script:
```sh
python data_cleaner.py
```
3. The cleaned dataset will be saved as `cleaned_dataset.csv`.

## Example Code
```python
cleaner = DataCleaner(df)
cleaned_df = cleaner.clean_data()
cleaned_df.to_csv("cleaned_dataset.csv", index=False)
```

## Author
Sherry2005

## License
This project is open-source. Feel free to modify and distribute it.

