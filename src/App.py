import requests
from geopandas import GeoDataFrame
import pycollection.collection as Collection


class MainApp:
    country = 'indonesia'
    endpoint = f'http://api.globalplasticwatch.org/countries/{country}/sites'
    params = {'apikey': 'xylem', 'limit': 10000}
    data = {}

    def run(self):
        response = requests.get(self.endpoint, params=self.params)
        self.data = response.json()
        return

    def print_data(self):
        print(self.data)
        return

    def render_geo(self):
        render = GeoDataFrame.from_features(self.data['features'])
        return render

    def generate_collection(self):
        collection = Collection.Collection()
        data = self.render_geo()

        for i in data.values:
            in_data = {
                'geometry': i[0],
                'waterway_distance': i[1],
                'drainage_direction': i[2],
                'elevation': i[3],
                'fine_earth_density': i[4],
                'height_above_drainage': i[5],
                'landform_type': i[6],
                'nearest_watertype': i[7],
                'population_1km': i[8],
                'population_10km': i[9],
                'population_5km': i[10],
                'slope_degrees': i[11],
                'soil_clay_fraction': i[12],
                'soil_clay_group': i[13],
                'soil_sand_fraction': i[14],
                'upstream_drainage_area': i[15],
                'area': i[16],
                'area_km^2': i[17],
                'country': i[18],
                'id': i[19],
                'place_name': i[20],
                'risk': i[21],
            }
            collection.set(i[20], in_data)

        return collection
