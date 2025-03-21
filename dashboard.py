from datetime import date
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("cleaned_data.csv") 


# Judul Dashboard
st.title("Dashboard Analisis Peminjaman Sepeda")

# Filter Bulan dengan opsi "Semua Bulan"
bulan_list = ["Semua Bulan"] + list(df['mnth'].unique()) 
mnth_terpilih = st.selectbox("Pilih Bulan:", bulan_list)

# Filter data berdasarkan bulan yang dipilih
if mnth_terpilih == "Semua Bulan":
    df_filtered = df 
else:
    df_filtered = df[df["mnth"] == mnth_terpilih]

# Analisis weekday dengan Peminjaman Terbanyak
st.subheader("Peminjaman Sepeda Berdasarkan Weekday")
weekday_rental = df_filtered.groupby("weekday")["cnt"].sum().sort_values(ascending=False)
st.bar_chart(weekday_rental)

# Agregasi total penyewaan berdasarkan musim dan tahun
season_trend = df_filtered.groupby(['yr', 'season'])['cnt'].sum().reset_index()

# Urutan musim agar sesuai dengan siklus tahunan
season_order = ["Spring", "Summer", "Autumn", "Winter"]

# Subjudul
st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim (2011-2012)")

# Visualisasi dengan Matplotlib & Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', hue='yr', data=season_trend, order=season_order, ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Tren Penyewaan Sepeda Berdasarkan Musim (2011-2012)")
ax.legend(title="Tahun")

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Kesimpulan
st.write("Dari visualisasi di atas, kita dapat melihat jumlah penyewaan sepeda berdasarkan hari dan musim. Dashboard ini interaktif dengan fitur pemilihan bulan untuk memfilter data sesuai kebutuhan.")
