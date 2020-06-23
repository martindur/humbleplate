import json
import pandas as pd
from pathlib import Path

base_dir = Path(Path(__file__).parent)


food_categories_id = [2, # Spices and Herbs
                      9, # Fruits and Fruit Juices
                      11, # Vegetables and Vegetable Products
                      12, # Nut and Seed Products
                      16, # Legumes and Legume Products
                      20  # Cereal Grains and Pasta
                     ]

nutrients_base = [
    1008, # Energy (Kcal)
    1003, # Protein
    1004, # Total lipid (fat)
    1005, # Carbohydrate, by difference
    1050, # Carbohydrate, by summation
    1051, # Water
    1079, # Fiber, total dietary
    1087, # Calcium
    1090, # Magnesium
    1092, # Potassium
    1093, # Sodium
    1114, # Vitamin D
    1162, # Vitamin C
    1166, # Riboflavin
]

food_df = pd.read_csv(base_dir / 'food_data' / 'food.csv')
nutrient_lookup_df = pd.read_csv(base_dir / 'food_data' / 'food_nutrient.csv')
nutrients = pd.read_csv(base_dir / 'food_data' / 'nutrient.csv')

base_nutrients = nutrients[nutrients['id'].isin(nutrients_base)]


food_df = food_df[food_df['data_type'] == 'foundation_food']
food_df = food_df[food_df['food_category_id'].isin(food_categories_id)]

foods_collected = {}

for i, food in food_df.iterrows():
    fdc_id = food.fdc_id

    food_nutrients = nutrient_lookup_df[nutrient_lookup_df['fdc_id'] == fdc_id]

    combined = food_nutrients[food_nutrients['nutrient_id'].isin(nutrients_base)]
    combined = combined.sort_values('nutrient_id')[['amount', 'nutrient_id']]

    food_result = base_nutrients.merge(combined, left_on='id', right_on='nutrient_id')
    food_result = food_result[['name', 'amount', 'unit_name']]

    foods_collected[fdc_id] = {}
    foods_collected[fdc_id]['name'] = food.description
    for j, n in food_result.iterrows():
        foods_collected[fdc_id][n['name']] = n.amount


with open('foods.json', 'w') as f:
    json.dump(foods_collected, f)