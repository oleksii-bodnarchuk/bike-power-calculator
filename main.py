import pandas as pd

# Передні зірки для порівняння
front_teeth_options = [11, 12, 13, 14]
rear_teeth = 50
top_speed_13 = 82  # базова максимальна швидкість на 13 зубах

# Розрахунок передатного числа і максимальної швидкості
gear_ratios = [rear_teeth / ft for ft in front_teeth_options]
top_speeds = [top_speed_13 * (gear_ratios[2] / gr) for gr in gear_ratios]  # gear_ratios[2] відповідає 13 зубам

# Ціль — максимальна швидкість 60 км/год
target_speed = 65

# Всі можливі передні зірки: 11–15 зубів
front_teeth_range = range(11, 12)
# Можливі задні зірки: 50–62 зубів
rear_teeth_range = range(50, 62)

# Розрахунок комбінацій
data = []

for ft in front_teeth_range:
    for rt in rear_teeth_range:
        gear_ratio = rt / ft
        speed = top_speed_13 * (gear_ratios[2] / gear_ratio)
        accel = gear_ratio / gear_ratios[2] * 100
        if speed <= target_speed + 1:  # трішки з запасом
            data.append({
                "Передня зірка": ft,
                "Задня зірка": rt,
                "Передатне число": round(gear_ratio, 2),
                "Макс. швидкість (км/год)": round(speed, 1),
                "Прискорення (%)": round(accel, 1)
            })

if data:
    df = pd.DataFrame(data)
    df = df.sort_values(by="Прискорення (%)", ascending=False)
else:
    df = pd.DataFrame(columns=[
        "Передня зірка", "Задня зірка", "Передатне число",
        "Макс. швидкість (км/год)", "Прискорення (%)"
    ])

import ace_tools_open as tools; tools.display_dataframe_to_user(name="Комбінації зірок для 60 км/год", dataframe=df)