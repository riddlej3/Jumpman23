avg_time_start_to_pickup = df_final[df_final["time_start_to_pickup"] > 0][
    "time_start_to_pickup"
].mean()
avg_time_pickup_arrival_to_depart = df_final[
    df_final["time_pickup_arrival_to_depart"] > 0
]["time_pickup_arrival_to_depart"].mean()
avg_time_pickup_dropoff = df_final[df_final["time_pickup_depart_to_dropoff"] > 0][
    "time_pickup_depart_to_dropoff"
].mean()
avg_exp_time_pickup_dropoff = df_final[df_final["exp_duration"] > 0][
    "exp_duration"
].mean()
print(
    "Avg distance from pickup to drop: \t\t",
    round(df_final["distance_traveled"].mean(), 3),
)
print("Avg time start to pickup: \t\t\t", round(avg_time_start_to_pickup, 2))
print(
    "Avg time pickup arrival to depart: \t\t",
    round(avg_time_pickup_arrival_to_depart, 2),
)
print("Avg time from pickup depart to drop: \t\t", round(avg_time_pickup_dropoff, 2))
print(
    "Avg expected time from pickup depart to drop: \t",
    round(avg_exp_time_pickup_dropoff, 2),
)
print(
    "Avg time diff from pickup depart to drop: \t",
    round(avg_time_pickup_dropoff - avg_exp_time_pickup_dropoff, 2),
)
print(
    "Avg delivery time: \t\t\t\t",
    round(
        avg_time_start_to_pickup
        + avg_time_pickup_arrival_to_depart
        + avg_time_pickup_dropoff,
        2,
    ),
)

