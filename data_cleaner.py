import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()

    def remove_duplicates(self):
        """Removes duplicate rows"""
        self.df.drop_duplicates(inplace=True)

    def handle_missing_values(self, strategy="mean"):
        """Fills missing values using mean, median, or mode"""
        # Handle numeric columns
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            num_imputer = SimpleImputer(strategy=strategy)
            self.df.loc[:, numeric_cols] = num_imputer.fit_transform(self.df[numeric_cols])

        # Handle categorical columns (fill with mode)
        cat_cols = self.df.select_dtypes(include=["object"]).columns
        if len(cat_cols) > 0:
            cat_imputer = SimpleImputer(strategy="most_frequent")
            self.df.loc[:, cat_cols] = cat_imputer.fit_transform(self.df[cat_cols])

    def fix_data_types(self):
        """Converts columns to appropriate data types"""
        for col in self.df.columns:
            if self.df[col].dtype == "object":  # If column is text-based
                try:
                    # Explicitly set date format to avoid warnings
                    self.df[col] = pd.to_datetime(self.df[col], format="%Y-%m-%d", errors="coerce")
                except Exception:
                    try:
                        self.df[col] = pd.to_numeric(self.df[col])  # Convert numeric-like strings to numbers
                    except ValueError:
                        pass  # If both fail, keep it as a string
        # Convert binary categorical columns to boolean
        for col in self.df.select_dtypes(include=["object"]).columns:
            if self.df[col].nunique() == 2:
                self.df[col] = self.df[col].astype("boolean")

    def standardize_text(self):
        """Standardizing text formatting (lowercase, strip spaces)"""
        for col in self.df.select_dtypes(include=["object"]).columns:
            self.df.loc[:, col] = self.df[col].str.lower().str.strip()

    def remove_outliers(self, z_threshold=3):
        """Remove outliers using the Z-score method"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        mask = np.ones(len(self.df), dtype=bool)  # Keep track of rows to keep
        for col in numeric_cols:
            z_scores = (self.df[col] - self.df[col].mean()) / self.df[col].std()
            mask &= z_scores.abs() < z_threshold  # Combine conditions across all numeric columns
        self.df = self.df.loc[mask]

    def clean_data(self):
        """Runs all cleaning functions"""
        self.remove_duplicates()
        self.handle_missing_values()
        self.fix_data_types()
        self.standardize_text()
        self.remove_outliers()
        return self.df

if __name__ == "__main__":
    # Load sample data
    df = pd.read_excel(r"D:\Book1.xlsx")  # Replace with your dataset
    print("Original Data:\n", df.head())

    cleaner = DataCleaner(df)
    cleaned_df = cleaner.clean_data()

    # Save cleaned data
    cleaned_df.to_csv("cleaned_dataset.csv", index=False)
    print("Data cleaning completed and saved!")

