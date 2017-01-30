import pickle, vincent
import pandas as pd

with open('db.p', 'rb') as f:
    df = pickle.load(f)

world_topo = r'world-countries.topo.json'
geo_data = [{'name': 'countries',
             'url': world_topo,
             'feature': 'world-countries'}]

vis = vincent.Map(geo_data=geo_data, scale=200)