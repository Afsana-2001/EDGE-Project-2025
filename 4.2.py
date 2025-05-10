import pandas as pd


data = {
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Population': [8419600, 3980400, 2716000],
    'Area': [789, 1302, 606]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


filtered_df = df[df['Area'] > 700]
print("\nFiltered DataFrame (Area > 700):")
print(filtered_df)

