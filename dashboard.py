import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import streamlit as st
import seaborn as sns
sns.set(style='dark')



day_df = pd.read_csv("day.csv")

#mengubah keterangan pada nama musim
season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
day_df["season"] = day_df["season"].map(season_mapping)

#mengubah keterangan pada nama cuaca
weathersit_mapping = {1: "Clear/Few clouds/Partly cloudy", 2: "Mist + Cloudy\ Mist", 3: "Light Snow/Light Rain", 4: "Heavy Rain/ Snow"}
day_df["weathersit"] = day_df["weathersit"].map(weathersit_mapping)


# mengelompokkan data dan menghitung jumlah pengguna biasa (casual) dan terdaftar(registered)
season_data = day_df.groupby("season")[["casual", "registered"]].sum().reset_index()
weather_data = day_df.groupby("weathersit")[["casual", "registered"]].sum().reset_index()

#--------------------Melengkapi Dashboard dengan Berbagai Visualisasi Data---------------------------------------------------------#

st.header(":sparkles: BIKE SHARING DASHBOARD :sparkles:")


#Membuat barchart untuk menampilkan jumlah penyewa sepeda berdasarkan musim
st.subheader("Jumlah Penyewa Sepeda Berdasarkan Musim")


fig, ax = plt.subplots()
sns.barplot(x="season", y="casual", data=season_data, color="green", label="Casual", ax=ax)
sns.barplot(x="season", y="registered", data=season_data, color="blue", label="Registered", ax=ax, bottom=season_data["casual"])
ax.set_title("Jumlah Penyewa Sepeda Berdasarkan Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewa Sepeda")

ax.get_yaxis().set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}')) #Mengatur sumbu y untuk menampilkan format angka biasa, bukan notasi ilmiah
ax.legend()
st.pyplot(fig)

#Membuat barchart untuk menampilkan jumlah penyewa sepeda berdasarkan musim
st.subheader("Jumlah Penyewa Sepeda Berdasarkan Cuaca")


fig, ax = plt.subplots()
sns.barplot(x="weathersit", y="casual", data=weather_data, color="orange", label="Casual", ax=ax)
sns.barplot(x="weathersit", y="registered", data=weather_data, color="yellow", label="Registered", ax=ax, bottom=weather_data["casual"])
ax.set_title("Jumlah Penyewa Sepeda Berdasarkan Cuaca")
ax.set_xlabel("Cuaca")
plt.xticks(rotation=45)
ax.set_ylabel("Jumlah Penyewa Sepeda")
ax.get_yaxis().set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}')) #Mengatur sumbu y untuk menampilkan format angka biasa, bukan notasi ilmiah
ax.legend()
st.pyplot(fig)


