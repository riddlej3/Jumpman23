root_path = "/Users/ginariddle/Desktop/g.school/my_projects/Jumpman23"
source = "src"
data = "data"

import string
import googlemaps
from uszipcode import SearchEngine
import numpy as np
import pandas as pd
from lists import (
    loc_keys,
    zipcodes,
    city,
    median_income,
    median_home_value,
    pop,
    pop_density,
    land_area_in_sqmi,
    state,
    d,
    mode_dict,
    df_final_cols,
)
import os

search = SearchEngine(simple_zipcode=True)
os.chdir(root_path)
with open("data/api_key.txt") as f:
    api_key = f.readline()

googlem = googlemaps.Client(key=api_key)
punctuation = string.punctuation


def new_dict(old_dict):
    new_dict = {key: old_dict[key] for key in loc_keys}
    return new_dict


def get_loc_data(series_lat, series_lon):
    """
    Overview: Used to create df_zip which gets concated to original df in df_preprocess func
    """
    counter = 0

    for a, b in zip(series_lat.values, series_lon.values):
        result = search.by_coordinates(a, b, returns=1, radius=2)[0]
        # appending results to lists
        zipcodes.append(result.zipcode)
        city.append(result.city)
        median_income.append(result.median_household_income)
        median_home_value.append(result.median_home_value)
        pop.append(result.population)
        pop_density.append(result.population_density)
        land_area_in_sqmi.append(result.land_area_in_sqmi)
        state.append(result.state)
        counter += 1

    return pd.DataFrame(d)


def expected_duration(df):
    """
    OVerview: Only to be run once due to google credit cost: Calculates expected time duration to go from
    pickup to dropoff using selected mode of transport at provided time.
    """
    durations = []
    counter = 0
    date_diff = pd.to_timedelta("365 days") * 5 + pd.to_timedelta("2 days")
    for i in range(len(df)):
        print(counter)
        counter += 1
        duration = pd.to_timedelta(
            googlem.directions(
                (df["pickup_lat"].values[i], df["pickup_lon"].values[i]),
                (df["dropoff_lat"].values[i], df["dropoff_lon"].values[i]),
                departure_time=df["when_the_delivery_started"].values[i] + date_diff,
                mode=mode_dict[df["vehicle_type"].values[i]],
            )[0]["legs"][0]["duration"]["text"].replace("mins", "minutes")
        )
        durations.append(duration)
    return durations


def expected_distance(df):
    """
    OVerview: Only to be run once due to google credit cost: Calculates expected distance to go from
    pickup to dropoff using selected mode of transport at provided time.
    """
    distances = []
    counter = 0
    date_diff = pd.to_timedelta("365 days") * 5 + pd.to_timedelta("2 days")
    for i in range(len(df)):
        print(counter)
        counter += 1
        distance = float(
            googlem.directions(
                (df["pickup_lat"].values[i], df["pickup_lon"].values[i]),
                (df["dropoff_lat"].values[i], df["dropoff_lon"].values[i]),
                departure_time=df["when_the_delivery_started"].values[i] + date_diff,
                mode=mode_dict[df["vehicle_type"].values[i]],
            )[0]["legs"][0]["distance"]["text"]
            .replace("mi", "")
            .replace("ft", "")
            .strip()
        )
        distances.append(distance)
    return distances


def change_to_timedelta(string):
    """
    Overview: Used to change timestamp datatype series to pd.timedelta
    Requires: to_timedelta can first be applied once original timestamp series is converted to strings
    """
    return pd.to_timedelta(string)


def df_clean(df):
    """
    Overview: Used after df_process func to prep df for df_final file
    """

    df["total_time_to_deliver"] = df["time_to_deliver"].astype("timedelta64[m]")
    df = df.drop("time_to_deliver", axis=1)
    df["how_long_it_took_to_order"] = pd.to_timedelta(
        df["how_long_it_took_to_order"].apply(str)
    ).astype("timedelta64[m]")
    df["time_start_to_pickup"] = (
        df["when_the_Jumpman_arrived_at_pickup"].sub(df["when_the_delivery_started"])
    ).astype("timedelta64[m]")
    df["time_pickup_depart_to_dropoff"] = (
        df["when_the_Jumpman_arrived_at_dropoff"].sub(
            df["when_the_Jumpman_left_pickup"]
        )
    ).astype("timedelta64[m]")
    df["time_pickup_arrival_to_depart"] = (
        df["when_the_Jumpman_left_pickup"].sub(df["when_the_Jumpman_arrived_at_pickup"])
    ).astype("timedelta64[m]")
    df["item_quantity"] = df["item_quantity"].replace(np.nan, 1)
    df["day"] = df["when_the_Jumpman_arrived_at_dropoff"].dt.day
    df["weekday"] = df["when_the_Jumpman_arrived_at_dropoff"].dt.day_name()
    df = df[df_final_cols]
    return df


def df_preprocess(df):
    """
    Overview: Used to initially clean original file import by changing datatypes and adding cols
    """
    # datatype updates
    for col in df.columns[df.columns.str.contains("when")]:
        df[col] = pd.to_datetime(df[col])
    df["how_long_it_took_to_order"] = pd.to_datetime(
        df["how_long_it_took_to_order"]
    ).dt.time
    df["time_to_deliver"] = df["when_the_Jumpman_arrived_at_dropoff"].sub(
        df["when_the_delivery_started"]
    )

    # temp fillers so as not to keep calling to googlemaps api
    df["exp_duration"] = 1
    df["distance_traveled"] = 1
    # df['exp_duration'] = exp_duration
    # df['exp_distance'] = exp_distance

    # location df
    df_zip = get_loc_data(df["pickup_lat"], df["pickup_lon"])

    # create new df with df_zip
    df = pd.concat([df, df_zip], axis=1)
    del df_zip
    return df
