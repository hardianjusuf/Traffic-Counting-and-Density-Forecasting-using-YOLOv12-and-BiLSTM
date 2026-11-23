# menggunakan hasil percobaan 4 (model terbaik terpilih)

import streamlit as st
import pandas as pd
from pathlib import Path


# konfigurasi halaman
st.set_page_config(page_title="Prediksi Kepadatan Lalu Lintas", layout="wide")


# judul
st.title("Prediksi Kepadatan Lalu Lintas")

st.write(
    "Prototype visualisasi hasil forecasting kepadatan lalu lintas "
    "berdasarkan data penelitian."
)


# lokasi file csv
CSV_PATH = Path(
    r"D:\1-Kuliah\SEKRIPSI\Skripsi_Traffic_Density_Estimation_and_Forecasting\06_Forecasting\percobaan-bi-lstm\output_bilstm_percobaan-4\hasil_akhir_prediksi_bilstm.csv"
)


# cek file csv yang di import
if not CSV_PATH.exists():
    st.error("File hasil prediksi tidak ditemukan.")
    st.write(CSV_PATH)
    st.stop()

# read data
df = pd.read_csv(CSV_PATH)

# rapihkan data
df["tanggal"] = df["tanggal"].astype(str)

kolom_numerik = [
    "horizon",
    "menit_ke_depan",
    "DS_Aktual_IN",
    "DS_Prediksi_IN",
    "DS_Aktual_OUT",
    "DS_Prediksi_OUT",
]

for kolom in kolom_numerik:
    df[kolom] = pd.to_numeric(df[kolom], errors="coerce")


# section pilih data prediksi
st.subheader("Pilih Data Prediksi")


# section pilih tanggal prediksi
daftar_tanggal = sorted(df["tanggal"].dropna().unique())

tanggal_pilih = st.selectbox("Tanggal", daftar_tanggal)


# filter berdasarkan tanggal
df_tanggal = df[df["tanggal"] == tanggal_pilih].copy()


# section memilih sesi
daftar_sesi = sorted(df_tanggal["sesi"].dropna().unique())

sesi_pilih = st.selectbox("Sesi", daftar_sesi)


# filter sesi

df_sesi = df_tanggal[df_tanggal["sesi"] == sesi_pilih].copy()

# pilih horizon
horizon_jam = st.selectbox(
    "Horizon Prediksi", [1, 2, 3], format_func=lambda x: f"{x} jam"
)


# menampilkan hasil
tampilkan_hasil = st.button(
    "Tampilkan Hasil Prediksi", use_container_width=True, type="primary"
)


# proses hanya jika button di-click
if tampilkan_hasil:

    # filter sesi
    df_sesi = df_tanggal[df_tanggal["sesi"] == sesi_pilih].copy()

    # filter horizon

    batas_menit = horizon_jam * 60

    df_hasil = df_sesi[df_sesi["menit_ke_depan"] <= batas_menit].copy()

    # Urutkan berdasarkan horizon
    df_hasil = df_hasil.sort_values(by="menit_ke_depan")

    # cek data

    if df_hasil.empty:
        st.warning("Tidak ada data prediksi untuk pilihan tersebut.")
        st.stop()

    # informasi prediksi
    st.divider()

    st.subheader("Informasi Prediksi")

    tipe_hari = df_hasil["tipe_hari"].iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Tanggal", tanggal_pilih)

    with col2:
        st.metric("Tipe Hari", tipe_hari)

    with col3:
        st.metric("Sesi", sesi_pilih)

    with col4:
        st.metric("Horizon Prediksi", f"{horizon_jam} jam")

    # prediksi kepadatan
    st.divider()

    st.subheader("Prediksi Kepadatan")

    # arah IN
    st.markdown("### Arah IN")

    tabel_in = df_hasil[
        [
            "waktu_yang_diprediksi",
            "menit_ke_depan",
            "DS_Prediksi_IN",
            "LOS_Prediksi_IN",
            "Status_Prediksi_IN",
        ]
    ].copy()

    tabel_in["DS_Prediksi_IN"] = tabel_in["DS_Prediksi_IN"].round(3)

    tabel_in = tabel_in.rename(
        columns={
            "waktu_yang_diprediksi": "Waktu Prediksi",
            "menit_ke_depan": "Menit ke Depan",
            "DS_Prediksi_IN": "Prediksi DS",
            "LOS_Prediksi_IN": "Prediksi LOS",
            "Status_Prediksi_IN": "Status",
        }
    )

    st.dataframe(tabel_in, hide_index=True, use_container_width=True)

    # Arah OUT
    st.markdown("### Arah OUT")

    tabel_out = df_hasil[
        [
            "waktu_yang_diprediksi",
            "menit_ke_depan",
            "DS_Prediksi_OUT",
            "LOS_Prediksi_OUT",
            "Status_Prediksi_OUT",
        ]
    ].copy()

    tabel_out["DS_Prediksi_OUT"] = tabel_out["DS_Prediksi_OUT"].round(3)

    tabel_out = tabel_out.rename(
        columns={
            "waktu_yang_diprediksi": "Waktu Prediksi",
            "menit_ke_depan": "Menit ke Depan",
            "DS_Prediksi_OUT": "Prediksi DS",
            "LOS_Prediksi_OUT": "Prediksi LOS",
            "Status_Prediksi_OUT": "Status",
        }
    )

    st.dataframe(tabel_out, hide_index=True, use_container_width=True)

    # Grafik prediksi DS
    st.divider()

    st.subheader("Grafik Prediksi Degree of Saturation (DS)")

    grafik_prediksi = df_hasil[
        ["waktu_yang_diprediksi", "DS_Prediksi_IN", "DS_Prediksi_OUT"]
    ].copy()

    grafik_prediksi = grafik_prediksi.set_index("waktu_yang_diprediksi")

    grafik_prediksi = grafik_prediksi.rename(
        columns={"DS_Prediksi_IN": "IN", "DS_Prediksi_OUT": "OUT"}
    )

    st.line_chart(grafik_prediksi, height=500, color=["#2196F3", "#FF9800"])

    # Detail hasil prediksi
    st.divider()

    st.subheader("Detail Hasil Prediksi")

    tabel_hasil = df_hasil[
        [
            "waktu_yang_diprediksi",
            "horizon",
            "menit_ke_depan",
            "DS_Aktual_IN",
            "DS_Prediksi_IN",
            "DS_Aktual_OUT",
            "DS_Prediksi_OUT",
            "LOS_Aktual_IN",
            "LOS_Prediksi_IN",
            "LOS_Aktual_OUT",
            "LOS_Prediksi_OUT",
            "Status_Aktual_IN",
            "Status_Prediksi_IN",
            "Status_Aktual_OUT",
            "Status_Prediksi_OUT",
        ]
    ].copy()

    kolom_ds = ["DS_Aktual_IN", "DS_Prediksi_IN", "DS_Aktual_OUT", "DS_Prediksi_OUT"]

    for kolom in kolom_ds:
        tabel_hasil[kolom] = tabel_hasil[kolom].round(3)

    tabel_hasil = tabel_hasil.rename(
        columns={
            "waktu_yang_diprediksi": "Waktu Prediksi",
            "horizon": "Horizon",
            "menit_ke_depan": "Menit ke Depan",
            "DS_Aktual_IN": "DS Aktual IN",
            "DS_Prediksi_IN": "DS Prediksi IN",
            "DS_Aktual_OUT": "DS Aktual OUT",
            "DS_Prediksi_OUT": "DS Prediksi OUT",
            "LOS_Aktual_IN": "LOS Aktual IN",
            "LOS_Prediksi_IN": "LOS Prediksi IN",
            "LOS_Aktual_OUT": "LOS Aktual OUT",
            "LOS_Prediksi_OUT": "LOS Prediksi OUT",
            "Status_Aktual_IN": "Status Aktual IN",
            "Status_Prediksi_IN": "Status Prediksi IN",
            "Status_Aktual_OUT": "Status Aktual OUT",
            "Status_Prediksi_OUT": "Status Prediksi OUT",
        }
    )

    st.dataframe(tabel_hasil, hide_index=True, use_container_width=True)
