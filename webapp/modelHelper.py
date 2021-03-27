import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, distance, temperature, humidity, wind_speed, pressure, road_type, visibility, side, condition):  

        # Distance(mi) = distance
        # Temperature(F) = temperature
        # Humidity(%) = humidity
        # Wind_Speed(mph) = wind_speed
        # Pressure(in) = pressure
        # Visibility(mi) = visibility

        Weather_Condition1_Clear = 0
        Weather_Condition1_Cloudy = 0
        Weather_Condition1_Fog_Haze = 0
        Weather_Condition1_Rain = 0
        Weather_Condition1_Thunder_Storm = 0
        Weather_Condition1_Wintery_Mix = 0

        Road_Type_Highway = 0
        Road_Type_Street = 0

        Side_R = 0
        Side_L = 0

        # parse Weather Condition
        if (condition == "Clear"):
            Weather_Condition1_Clear = 1
        elif (condition == "Cloudy"):
            Weather_Condition1_Cloudy = 1
        elif (condition == "Fog/Haze"):
            Weather_Condition1_Fog_Haze = 1
        elif (condition == "Rain"):
            Weather_Condition1_Rain = 1
        elif (condition == "Thunderstorm"):
            Weather_Condition1_Thunder_Storm = 1
        elif (condition == "Wintery Mix"):
            Weather_Condition1_Wintery_Mix = 1
        else:
            pass

        # parse Road Type
        if (road_type == "Street"):
            Road_Type_Street = 1
        elif (road_type == "Highway"):
            Road_Type_Highway = 1
        else:
            pass

         # parse Road Side
        if (side == "Right"):
            Side_R = 1
        elif (side == "Left"):
            Side_L = 1
        else:
            pass

        input_pred = [[distance, temperature, humidity, wind_speed, pressure, Road_Type_Street, Road_Type_Highway, visibility, Side_L, Side_R, 
        Weather_Condition1_Clear, Weather_Condition1_Cloudy, Weather_Condition1_Fog_Haze, Weather_Condition1_Rain, Weather_Condition1_Thunder_Storm, Weather_Condition1_Wintery_Mix]]


        filename = 'initial_model.sav'
        ada_load = pickle.load(open(filename, 'rb'))

        X = np.array(input_pred)
        preds = ada_load.predict_proba(X)
        preds_singular = ada_load.predict(X)

        return preds_singular[0]



        
        # # Booleans
        # Amenity = 0
        # Bump = 0
        # Crossing = 0
        # Give_Way = 0
        # Junction = 0
        # No_Exit = 0
        # Railway = 0
        # Roundabout = 0
        # Station = 0
        # Stop = 0
        # Traffic_Calming = 0
        # Traffic_Signal = 0
        # Turning_Loop = 0

        # # Dummies
        # Civil_Twilight_Day = 
        # Civil_Twilight_Night = 
        # Nautical_Twilight_Day = 
        # Nautical_Twilight_Night = 
        # Astronomical_Twilight_Day = 
        # Astronomical_Twilight_Night = 