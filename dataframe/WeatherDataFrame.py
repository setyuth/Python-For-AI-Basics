import numpy as np
import pandas as pd

data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu'],
    'Temp': [22, 25, 19, 28],
    'Rain': [0.1, 0.0, 0.3, np.nan]
}
df_weather = pd.DataFrame(data)

# 1. Add a column for “Feels Like” (Temp - 2 if Rain > 0, else Temp).
df_weather['Feels Like'] = df_weather.apply(
    lambda row: row['Temp'] - 2 if row['Rain'] > 0 else row['Temp'], axis=1
)

# 2. Fill the missing Rain value with the mean.
mean_rain = df_weather['Rain'].mean()
df_weather['Rain'] = df_weather['Rain'].fillna(mean_rain)

# 3. Filter for days when Temp > 20.
hot_days = df_weather[df_weather['Temp'] > 20]
print(hot_days)


