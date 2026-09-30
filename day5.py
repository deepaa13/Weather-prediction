total_days = 20
rain_days = 8
not_rain_days = 12

cloudy_given_rain_days = 7       
cloudy_given_not_rain_days = 3   

observation = "Cloudy"

p_rain = rain_days / total_days
p_not_rain = not_rain_days / total_days

p_cloudy_given_rain = cloudy_given_rain_days / rain_days
p_cloudy_given_not_rain = cloudy_given_not_rain_days / not_rain_days

p_cloudy = (p_cloudy_given_rain * p_rain) + (p_cloudy_given_not_rain * p_not_rain)

p_rain_given_cloudy = (p_cloudy_given_rain * p_rain) / p_cloudy
p_not_rain_given_cloudy = (p_cloudy_given_not_rain * p_not_rain) / p_cloudy

prediction = "Rain" if p_rain_given_cloudy > p_not_rain_given_cloudy else "Not Rain"

print(f"Observation: Sky = {observation}\n")
print(f"P(Rain)               = {p_rain:.3f}")
print(f"P(Not Rain)           = {p_not_rain:.3f}")
print(f"P(Cloudy | Rain)      = {p_cloudy_given_rain:.3f}")
print(f"P(Cloudy | Not Rain)  = {p_cloudy_given_not_rain:.3f}")
print(f"P(Cloudy)             = {p_cloudy:.3f}")
print(f"P(Rain | Cloudy)      = {p_rain_given_cloudy:.3f}")
print(f"P(Not Rain | Cloudy)  = {p_not_rain_given_cloudy:.3f}")
print(f"\nPredicted Weather = {prediction}")