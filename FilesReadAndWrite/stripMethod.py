text_file = "country_info.txt"
country_info = {}
with open(text_file) as countryList:
    countryList.readline()
    for country in countryList:
        country_name, capital, cc, cc3, iac, timezone, currency = country.strip("\n").split("|")
        country_dict = {
            'name': country_name,
            'capital': capital,
            'country_code': cc,
            'cc3': cc3,
            'iac': iac,
            'timezone': timezone,
            'currency': currency
        }
        country_info[country_name] = country_dict

print(country_info)

get_country_info = input("Please enter the country name: ")
if get_country_info in country_info:
    print(country_info[get_country_info])
else:
    print(f"country data not found for: {get_country_info}")
