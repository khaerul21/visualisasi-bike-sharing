import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("main_data.csv") 

day_mapping = {0: "Minggu", 1: "Senin", 2: "Selasa", 3: "Rabu", 4: "Kamis", 5: "Jumat", 6: "Sabtu"}
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}

df["weekday"] = df["weekday"].map(day_mapping)
df["season"] = df["season"].map(season_mapping)

# Judul Dashboard
st.title("Dashboard Analisis Peminjaman Sepeda")

# Filter Tahun
mnth_terpilih = st.selectbox("Pilih Bulan:", sorted(df["mnth"].unique()))
df_filtered = df[df["mnth"] == mnth_terpilih]

# Analisis weekday dengan Peminjaman Terbanyak
st.subheader("Peminjaman Sepeda Berdasarkan weekday")
weekday_rental = df_filtered.groupby("weekday")["cnt"].sum().sort_values(ascending=False)
st.bar_chart(weekday_rental)

# Analisis Pengaruh season terhadap Peminjaman
st.subheader("Pengaruh season terhadap Peminjaman Sepeda")
fig, ax = plt.subplots()
sns.boxplot(x="season", y="cnt", data=df_filtered, palette="Set2", ax=ax)
st.pyplot(fig)

# Kesimpulan
st.write("Dari visualisasi di atas, kita dapat melihat weekday dengan peminjaman terbanyak dan bagaimana season mempengaruhi jumlah peminjaman sepeda.")
