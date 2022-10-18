#  using pygal country codes
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    # return Pygal 2-digit country code for country
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

print(get_country_code("Malaysia"))
print(get_country_code("Andorra"))
print(get_country_code("Singapore"))
