import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\eturi\OneDrive\Pictures\Desktop\Ecommerce-Analytics\Data\SampleSuperstore.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Create new useful metrics
df['Revenue_per_item'] = df['Sales'] / df['Quantity']

# Profit percentage
df['Profit_Percentage'] = (df['Profit'] / df['Sales']) * 100

print("\nFirst 5 rows:")
print(df.head())

# Save cleaned file
df.to_csv(
    r"C:\Users\eturi\OneDrive\Pictures\Desktop\Ecommerce-Analytics\Data\cleaned_superstore.csv",
    index=False
)

print("\nData cleaned successfully")