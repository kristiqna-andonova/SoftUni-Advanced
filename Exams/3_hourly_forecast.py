def forecast(*args):
    forecast_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}
    result = []
    [forecast_dict[value].append(key) for key, value in args]
    [result.append(f"{name} - {key_}") for key_, value_ in forecast_dict.items() for name in sorted(value_)]

    return "\n".join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

