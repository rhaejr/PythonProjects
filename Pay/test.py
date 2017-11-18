import pandas as pd
import pickle
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os, pickle

pay = pickle.load( open( "pay.p", "rb" ) )

pay.xs('Lee County',level='County')