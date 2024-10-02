import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import streamlit as st
import seaborn as sns
sns.set(style='dark')



day_df = pd.read_csv("day.csv")

# Mapping the seasons
season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
day_df["season"] = day_df["season"].map(season_mapping)

# Mapping the weathers
weathersit_mapping = {1: "Clear/Few clouds/Partly cloudy", 2: "Mist + Cloudy\ Mist", 3: "Light Snow/Light Rain", 4: "Heavy Rain/ Snow"}
day_df["weathersit"] = day_df["weathersit"].map(weathersit_mapping)


# Grouping the data and summing the casual and registered users
season_data = day_df.groupby("season")[["casual", "registered"]].sum().reset_index()
weather_data = day_df.groupby("weathersit")[["casual", "registered"]].sum().reset_index()

#--------------------Completing Dashboards with Various Data Visualizations---------------------------------------------------------#

st.header(":sparkles: BIKE SHARING DASHBOARD :sparkles:")


# Plotting using seabon to show the number of bike renters by season
st.subheader("Number of Bike Renters by Season")


fig, ax = plt.subplots()
sns.barplot(x="season", y="casual", data=season_data, color="green", label="Casual", ax=ax)
sns.barplot(x="season", y="registered", data=season_data, color="blue", label="Registered", ax=ax, bottom=season_data["casual"])
ax.set_title("Number of Bike Renters by Season")
ax.set_xlabel("Season")
ax.set_ylabel("JNumber of Bike Renters")

ax.get_yaxis().set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}')) # Set the y-axis to display regular number format instead of scientific notation
ax.legend()
st.pyplot(fig)

# Plotting using seabon to show the number of bike renters by weather
st.subheader("Number of Bike Renters by Weather")


fig, ax = plt.subplots()
sns.barplot(x="weathersit", y="casual", data=weather_data, color="orange", label="Casual", ax=ax)
sns.barplot(x="weathersit", y="registered", data=weather_data, color="yellow", label="Registered", ax=ax, bottom=weather_data["casual"])
ax.set_title("Number of Bike Renters by Weather")
ax.set_xlabel("Weather")
plt.xticks(rotation=45)
ax.set_ylabel("Number of Bike Renters")
ax.get_yaxis().set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}')) # Set the y-axis to display regular number format instead of scientific notation
ax.legend()
st.pyplot(fig)


