import os
import django

# Set the correct path to the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hu_v1q2_plazz.local_settings")
django.setup()

# imports, except djangos, must be set after Django setup
import json
from plazz.models import Neighbourhood, City, NeighbourhoodCity


def run():
    with open('assets/data/input_neighbourhood.json') as neighbourhood_input:
        neighbourhood_data = json.load(neighbourhood_input)

        """
        Neighbourhood table
        """
        # First, clear the table
        Neighbourhood.objects.all().delete()

        # Iterate over the supplies JSON file and create one new instance per row
        for item in neighbourhood_data['value']:
            neighbourhood = Neighbourhood()
            neighbourhood.name = item['Title']
            neighbourhood.key = item['Key']
            neighbourhood.save()

    with open('assets/data/input_city.json') as city_input:
        city_data = json.load(city_input)

        """
        City table
        """
        # First, clear the table
        City.objects.all().delete()

        # Iterate over the supplies JSON file and create one new instance per row
        for item in city_data['value']:
            city = City()
            city.name = "Utrecht"
            city.Sec_edu = item['VoortgezetOnderwijs_108']
            city.Sec_vocational_edu = item['MiddelbaarBeroepsonderwijs_109']
            city.Higher_prof_edu_bachelor = item['HogerBeroepsonderwijsBachelor_110']
            city.Wo_master_doctoraal = item['WoMasterDoctoraal_111']
            city.save()

    with open('assets/data/input_neighbourhoodcity_restaurant.json') as neighbourhood_city_input:
        neighbourhood_city_data = json.load(neighbourhood_city_input)

        """
        Neighbourhood_City table
        """
        # First, clear the table
        NeighbourhoodCity.objects.all().delete()

        # Iterate over the supplies JSON file and create one new instance per row
        for item in neighbourhood_city_data['value']:
            # Create relations between tables
            neighbourhood = Neighbourhood.objects.get(key=item["WijkenEnBuurten"])
            city = City.objects.get(name="Utrecht")

            nc = NeighbourhoodCity()
            nc.Avg_restaurant_dist = None if item["AfstandTotRestaurant_44"].strip() == "." else \
                item["AfstandTotRestaurant_44"]
            nc.Avg_restaurant_amt_1_km = None if item["Binnen1Km_45"].strip() == "." else item["Binnen1Km_45"]
            nc.Avg_restaurant_amt_3_km = None if item["Binnen3Km_46"].strip() == "." else item["Binnen3Km_46"]
            nc.Avg_restaurant_amt_5_km = None if item["Binnen5Km_47"].strip() == "." else item["Binnen5Km_47"]

            with open('assets/data/input_neighbourhoodcity.json') as f:
                data_b = json.load(f)

                for item_b in data_b['value']:
                    if item_b["WijkenEnBuurten"] == item["WijkenEnBuurten"]:
                        nc.Age_0_to_15 = item_b["k_0Tot15Jaar_8"]
                        nc.Age_15_to_25 = item_b["k_15Tot25Jaar_9"]
                        nc.Age_25_to_45 = item_b["k_25Tot45Jaar_10"]
                        nc.Age_45_to_65 = item_b["k_45Tot65Jaar_11"]
                        nc.Age_65_or_older = item_b["k_65JaarOfOuder_12"]
                        nc.Avg_income = None if item_b["GemiddeldInkomenPerInkomensontvanger_65"].strip() == "." else \
                            item_b["GemiddeldInkomenPerInkomensontvanger_65"]
                        nc.Population = item_b["AantalInwoners_5"]

            nc.neighbourhood = neighbourhood
            nc.city = city
            nc.save()


# Run this file in a Django environment to connect to the database
if __name__ == '__main__':
    run()
