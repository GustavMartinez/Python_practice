from google_solar_api_data import solar_data

print(solar_data["name"])
print()
for k,v in solar_data["center"].items():
    print(k,v)
print()

longitud = solar_data["center"]["longitude"]
print(f"La longitud del lugar es: {longitud}")

print()

sunshine_quant = solar_data["solarPotential"]["wholeRoofStats"]["sunshineQuantiles"]
print(f"The sunshine Quantiles are: \n{sunshine_quant}")