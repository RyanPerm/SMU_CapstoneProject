import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, distance, visibility, side, condition, temperature, wind_speed, humidity, pressure, road_type):  

        # Booleans
        Amenity = 0
        Bump = 0
        Crossing = 0
        Give_Way = 0
        Junction = 0
        No_Exit = 0
        Railway = 0
        Roundabout = 0
        Station = 0
        Stop = 0
        Traffic_Calming = 0
        Traffic_Signal = 0

        # Dummies
        Sunrise_Sunset_Day = 0
        Sunrise_Sunset_Night = 0
        Civil_Twilight_Day = 0
        Civil_Twilight_Night = 0
        Nautical_Twilight_Day = 0
        Nautical_Twilight_Night = 0
        Astronomical_Twilight_Day = 0
        Astronomical_Twilight_Night = 0

        precipitation = 0

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

        input_pred = [[distance, temperature, humidity, pressure, visibility, wind_speed, precipitation, Amenity, Bump, Crossing,
        Give_Way, Junction, No_Exit, Railway, Roundabout, Station, Stop, Traffic_Calming, Traffic_Signal, Side_L, Side_R, Weather_Condition1_Clear,
        Weather_Condition1_Cloudy, Weather_Condition1_Fog_Haze, Weather_Condition1_Rain, Weather_Condition1_Thunder_Storm, Weather_Condition1_Wintery_Mix,
        Sunrise_Sunset_Day, Sunrise_Sunset_Night, Civil_Twilight_Day, Civil_Twilight_Night, Nautical_Twilight_Day, Nautical_Twilight_Night, Astronomical_Twilight_Day, 
        Astronomical_Twilight_Night, Road_Type_Highway, Road_Type_Street]]


        filename = 'static/models/initial_model.sav'
        ada_load = pickle.load(open(filename, 'rb'))

        X = np.array(input_pred)
        preds = ada_load.predict_proba(X)
        preds_singular = ada_load.predict(X)

        # Model 2
        filename_mild = 'static/models/mild_model.sav'
        ada_load_mild = pickle.load(open(filename_mild, 'rb'))
        preds_mild = ada_load_mild.predict_proba(X)

        preds_mild_final = preds[0][0]*preds_mild[0]

                # Model 2
        filename_severe = 'static/models/severe_model.sav'
        ada_load_severe = pickle.load(open(filename_severe, 'rb'))
        preds_severe = ada_load_severe.predict_proba(X)

        preds_severe_final = preds[0][1]*preds_severe[0]


        all_preds = np.concatenate([preds_mild_final , preds_severe_final])
        returnval = np.argmax(all_preds) + 1



        return {"point": str(returnval), "proba": all_preds.tolist()}




        
