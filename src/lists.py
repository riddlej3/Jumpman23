mode_dict = {
    "bicycle": "bicycling",
    "car": "driving",
    "scooter": "driving",
    "truck": "driving",
    "motorcycle": "driving",
    "walker": "walking",
    "van": "driving",
}


loc_keys = [
    "zipcode",
    "major_city",
    "population",
    "population_density",
    "land_area_in_sqmi",
    "housing_units",
    "median_home_value",
    "median_household_income",
]

zipcodes = []
city = []
median_income = []
median_home_value = []
pop = []
pop_density = []
land_area_in_sqmi = []
state = []

d = {
    "zipcodes": zipcodes,
    "city": city,
    "median_income": median_income,
    "median_home_value": median_home_value,
    "pop": pop,
    "pop_density": pop_density,
    "land_area_in_sqmi": land_area_in_sqmi,
    "state": state,
}


df_final_cols = [
    "delivery_id",
    "customer_id",
    "jumpman_id",
    "merchant_id",
    "vehicle_type",
    "pickup_place",
    "place_category",
    "item_name",
    "item_quantity",
    "item_category_name",
    "zipcodes",
    "zipcodes_dropoff",
    "pop_dropoff",
    "median_home_value_dropoff",
    "city",
    "pickup_lat",
    "pickup_lon",
    "dropoff_lat",
    "dropoff_lon",
    "median_income",
    "median_home_value",
    "day",
    "weekday",
    "pop",
    "pop_density",
    "land_area_in_sqmi",
    "state",
    "how_long_it_took_to_order",
    "total_time_to_deliver",
    "time_start_to_pickup",
    "time_pickup_arrival_to_depart",
    "time_pickup_depart_to_dropoff",
    "exp_duration",
    "distance_traveled",
    "when_the_delivery_started",
    "when_the_Jumpman_arrived_at_pickup",
    "when_the_Jumpman_left_pickup",
    "when_the_Jumpman_arrived_at_dropoff",
]

df_delivery_cols = [
    "delivery_id",
    "customer_id",
    "jumpman_id",
    "merchant_id",
    "vehicle_type",
    "pickup_place",
    "place_category",
    "zipcodes",
    "zipcodes_dropoff",
    "pop_dropoff",
    "median_home_value_dropoff",
    "city",
    "pickup_lat",
    "pickup_lon",
    "dropoff_lat",
    "dropoff_lon",
    "median_income",
    "median_home_value",
    "day",
    "weekday",
    "pop",
    "pop_density",
    "land_area_in_sqmi",
    "state",
    "how_long_it_took_to_order",
    "total_time_to_deliver",
    "time_start_to_pickup",
    "time_pickup_arrival_to_depart",
    "time_pickup_depart_to_dropoff",
    "exp_duration",
    "distance_traveled",
    "when_the_delivery_started",
    "when_the_Jumpman_arrived_at_pickup",
    "when_the_Jumpman_left_pickup",
    "when_the_Jumpman_arrived_at_dropoff",
]

