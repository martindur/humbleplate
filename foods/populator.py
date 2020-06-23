import json
from pathlib import Path
from .models import Food
cur_dir = Path(__file__).parent

def populate_foods():
    with open(cur_dir.parent / 'foods.json', 'r') as f:
        foods = json.load(f)

        for food in foods:
            new_food = Food.objects.create(
                fdc_id=food,
                name=foods[food]['name'],
                kcal=foods[food]['Energy'],
                protein=foods[food]['Protein'],
                fat=foods[food]['Total lipid (fat)'],
                carbohydrates=foods[food]['Carbohydrate, by difference'],
                #fiber=foods[food]['Fiber, total dietary'],
                water=foods[food]['Water'],
                calcium=foods[food]['Calcium, Ca'],
                magnesium=foods[food]['Magnesium, Mg'],
                potassium=foods[food]['Potassium, K'],
                #sodium=foods[food]['Sodium, Na'],
                #vitamin_c=foods[food]['Vitamin C, total ascorbic acid'],
                #riboflavin=foods[food]['Riboflavin']
            )
            print(foods[food]['name'])

