[train-yolov12m](https://github.com/hardianjusuf/Traffic-Counting-and-Density-Forecasting-using-YOLOv12-and-BiLSTM/tree/main/03_Vehicle_Detection/runs/train-yolov12m "train-yolov12m")percobaan-train-yolov12n.ipynb

# Estimasi dan Prediksi Kepadatan Lalu Lintas Menggunakan YOLOv12 dan Bi-LSTM

Repository ini berisi implementasi penelitian skripsi mengenai **estimasi dan prediksi kepadatan lalu lintas menggunakan YOLOv12 dan Bidirectional Long Short-Term Memory (Bi-LSTM)** berdasarkan rekaman CCTV.

**Studi Kasus:** Ruas Jalan A.P. Pettarani–Andi Djemma, depan Kampus Universitas Negeri Makassar (UNM), Kota Makassar, Sulawesi Selatan.

## 1. Deskripsi Penelitian

Penelitian ini bertujuan mengestimasi dan memprediksi kondisi kepadatan lalu lintas melalui pengolahan rekaman CCTV dengan mengintegrasikan deteksi objek, penghitungan kendaraan, analisis lalu lintas, dan prediksi deret waktu.

Pendekatan yang digunakan meliputi:

1. **YOLOv12** , untuk mendeteksi kendaraan berdasarkan rekaman CCTV.
2. **Object Tracking dan Vehicle Counting** , untuk melacak serta menghitung kendaraan berdasarkan arah pergerakannya.
3. **Manual Kapasitas Jalan Indonesia (MKJI)** , untuk menghitung volume lalu lintas, kapasitas jalan, dan derajat kejenuhan ( *Degree of Saturation/DS* ).
4. **Bi-LSTM** , untuk memprediksi derajat kejenuhan berdasarkan data historis lalu lintas.
5. **Streamlit** , untuk memvisualisasikan hasil estimasi dan prediksi kepadatan lalu lintas.

Penelitian dilakukan pada dua arah lalu lintas:

* **IN:** Menuju Jalan A.P. Pettarani.
* **OUT:** Menuju Jalan Andi Djemma.

## 2. Alur Penelitian

```text
Rekaman CCTV
      |
      v
Deteksi Kendaraan (YOLOv12)
      |
      v
Pelacakan dan Penghitungan Kendaraan
      |
      v
Perhitungan Volume Lalu Lintas
      |
      v
Estimasi Kepadatan Berdasarkan MKJI
      |
      v
Prediksi Kepadatan (Bi-LSTM)
      |
      v
Visualisasi Hasil (Streamlit)
```

## 3. Struktur Repository

```text
Traffic-Counting-and-Density-Forecasting-using-YOLOv12-and-BiLSTM/
│
├── 01_Datasets/
│   └── YOLO_DATASET.md
│
├── 02_Model_Comparison/
│   ├── notebook/
│   │   └── yolo_model_comparison.ipynb
│   └── hasil_train_yolo/
│       ├── train-yolov8/results.csv
│       ├── train-yolov9t/results.csv
│       ├── train-yolov10/results.csv
│       ├── train-yolov11/results.csv
│       ├── train-yolov12/results.csv
│       └── train-yolo26/results.csv
│
├── 03_Vehicle_Detection/
│   ├── notebook/
│   │   ├── perbandingan_mAP_YOLOv12.ipynb
│   │   ├── percobaan-train-yolov12m.ipynb
│   │   ├── percobaan-train-yolov12n.ipynb
│   │   └── percobaan-train-yolov12s.ipynb
│   └── runs/
│       ├── train-yolov12m/
│       │   └── weights/best.pt
│       ├── train-yolov12n/
│       │   └── weights/best.pt
│       └── train-yolov12s/
│           └── weights/best.pt
│
├── 04_Vehicle_Counting/
│   ├── notebook/
│   │   └── traffic_counting_2roi_2garis.ipynb
│   ├── evaluasi_traffic_counting/
│   │   └── pagi_2menit_interval_counting.csv
│   └── final-dataset-vehicle-counting/
│       └── Semua_6_sampai_20_April_interval_counting.csv
│
├── 05_Traffic_Analysis/
│   ├── notebook/
│   │   └── convert-counting-to-mkji.ipynb
│   └── output_mkji_convert_directory/
│       └── dataset_mkji.csv
│
├── 06_Forecasting/
│   ├── bilstm-model/
│   │   └── best_bilstm.keras
│   ├── notebook/
│   │   ├── evaluasi_perbandingan_bilstm.ipynb
│   │   ├── percobaan1_Bi-LSTM-Forecasting.ipynb
│   │   ├── percobaan2_Bi-LSTM-Forecasting.ipynb
│   │   ├── percobaan3_Bi-LSTM-Forecasting.ipynb
│   │   ├── percobaan4_Bi-LSTM-Forecasting.ipynb
│   │   └── percobaan5_Bi-LSTM-Forecasting.ipynb
│   └── percobaan-bi-lstm/
│       ├── output_bilstm_percobaan-1/hasil_akhir_prediksi_bilstm.csv
│       ├── output_bilstm_percobaan-2/hasil_akhir_prediksi_bilstm.csv
│       ├── output_bilstm_percobaan-3/hasil_akhir_prediksi_bilstm.csv
│       ├── output_bilstm_percobaan-4/hasil_akhir_prediksi_bilstm.csv
│       └── output_bilstm_percobaan-5/hasil_akhir_prediksi_bilstm.csv
│
├── 07_Streamlit_Prototype_App/
│   └── app.py
│
├── .gitignore
└── README.md
```

## 4. Metodologi Penelitian

### 4.1 Dataset

Dataset digunakan untuk melatih dan mengevaluasi model deteksi kendaraan pada rekaman CCTV.

Dokumentasi dataset YOLO tersedia pada:

`01_Datasets/YOLO_DATASET.md`

Dataset deteksi kendaraan menggunakan tiga kelas utama, yaitu:

| Kelas | Jenis Kendaraan                        |
| ----- | -------------------------------------- |
| MC    | Sepeda motor                           |
| LV    | Kendaraan ringan                       |
| HV    | Kendaraan berat, termasuk bus dan truk |

### 4.2 Perbandingan Model YOLO

Tahap awal penelitian dilakukan dengan membandingkan enam arsitektur YOLO, yaitu YOLOv8n, YOLOv9t, YOLOv10n, YOLOv11n, YOLOv12n, dan YOLO26n.

Perbandingan dilakukan menggunakan metrik Precision, Recall, mAP50, dan mAP50-95 untuk menentukan model deteksi kendaraan yang paling sesuai.

| Model    | Precision | Recall |  mAP50 | mAP50-95 |
| -------- | --------: | -----: | -----: | -------: |
| YOLOv8n  |    0.9248 | 0.8808 | 0.9392 |   0.7526 |
| YOLOv9t  |    0.9191 | 0.8773 | 0.9380 |   0.7509 |
| YOLOv10n |    0.9168 | 0.8398 | 0.9243 |   0.7386 |
| YOLOv11n |    0.9186 | 0.8907 | 0.9373 |   0.7500 |
| YOLOv12n |    0.9159 | 0.8755 | 0.9364 |   0.7577 |
| YOLO26n  |    0.9241 | 0.8467 | 0.9217 |   0.7311 |

Berdasarkan hasil perbandingan tersebut, **YOLOv12n memperoleh nilai mAP50-95 tertinggi sebesar 0.7577**, sehingga dipilih sebagai model dasar untuk tahap penelitian selanjutnya.

Analisis perbandingan tersedia pada: `02_Model_Comparison/notebook/yolo_model_comparison.ipynb`

### 4.3 Deteksi dan Penghitungan Kendaraan

Setelah pemilihan arsitektur YOLOv12, dilakukan eksperimen pelatihan dengan tiga varian model:

- YOLOv12n (nano)
- YOLOv12s (small)
- YOLOv12m (medium)

Eksperimen bertujuan mengevaluasi kinerja deteksi kendaraan dari masing-masing varian.

Notebook pelatihan dan perbandingan tersedia pada folder `03_Vehicle_Detection/notebook/`.

### 4.4 Vehicle Counting

Tahap penghitungan kendaraan dilakukan melalui penerapan ROI (*Region of Interest*), pelacakan objek, dan garis penghitungan ( *counting line* ) untuk masing-masing arah lalu lintas.

Implementasi utama tersedia pada:

`04_Vehicle_Counting/notebook/traffic_counting_2roi_2garis.ipynb`

Proses evaluasi dan pengumpulan data menghasilkan:

| File                                              | Keterangan                                                    |
| ------------------------------------------------- | ------------------------------------------------------------- |
| `pagi_2menit_interval_counting.csv`             | Hasil counting untuk evaluasi pada interval dua menit         |
| `Semua_6_sampai_20_April_interval_counting.csv` | Dataset hasil penghitungan kendaraan pada periode 6–20 April |

Model Bi-LSTM digunakan untuk memprediksi derajat kejenuhan berdasarkan pola historis lalu lintas.

### 4.5 Analisis Lalu Lintas Menggunakan MKJI

Data hasil penghitungan kendaraan dikonversi menjadi parameter lalu lintas menggunakan pendekatan Manual Kapasitas Jalan Indonesia (MKJI).

Nilai ekuivalensi mobil penumpang (EMP) yang digunakan adalah:

| Jenis Kendaraan | EMP  |
| --------------- | ---- |
| MC              | 0.25 |
| LV              | 1.00 |
| HV              | 1.20 |

Perhitungan derajat kejenuhan menggunakan persamaan:

DS = Q / C

Keterangan:

* **DS:** Derajat kejenuhan.
* **Q:** Volume lalu lintas (smp/jam).
* **C:** Kapasitas jalan (smp/jam).

Nilai derajat kejenuhan digunakan untuk mengidentifikasi kondisi lalu lintas berdasarkan tingkat pelayanan jalan ( *Level of Service/LOS* ).

Proses konversi dilakukan melalui notebook:

`05_Traffic_Analysis/notebook/convert-counting-to-mkji.ipynb`

Dataset hasil konversi tersedia pada:

`05_Traffic_Analysis/output_mkji_convert_directory/dataset_mkji.csv`

Dataset tersebut menjadi dasar penyusunan data untuk proses prediksi menggunakan Bi-LSTM.

Streamlit digunakan untuk mengembangkan prototipe visualisasi hasil estimasi dan prediksi kepadatan lalu lintas.

### 4.6 Prediksi Kepadatan Menggunakan Bi-LSTM

Model Bidirectional Long Short-Term Memory (Bi-LSTM) digunakan untuk memprediksi nilai derajat kejenuhan pada dua arah lalu lintas berdasarkan data historis.

**Eksperimen Pemodelan**

Penelitian melibatkan lima percobaan pemodelan Bi-LSTM yang didokumentasikan melalui notebook terpisah.

| Percobaan   | Notebook                                                  | Direktori output                               |
| ----------- | --------------------------------------------------------- | ---------------------------------------------- |
| 1           | `percobaan1_Bi-LSTM-Forecasting.ipynb`                  | `output_bilstm_percobaan-1`                  |
| 2           | `percobaan2_Bi-LSTM-Forecasting.ipynb`                  | `output_bilstm_percobaan-2`                  |
| 3           | `percobaan3_Bi-LSTM-Forecasting.ipynb`                  | `output_bilstm_percobaan-3`                  |
| **4** | `<strong>percobaan4_Bi-LSTM-Forecasting.ipynb</strong>` | `<strong>output_bilstm_percobaan-4</strong>` |
| 5           | `percobaan5_Bi-LSTM-Forecasting.ipynb`                  | `output_bilstm_percobaan-5`                  |

Kelima percobaan dianalisis untuk mengevaluasi hasil prediksi derajat kejenuhan pada arah IN dan OUT.

Notebook evaluasi perbandingan tersedia pada:

`06_Forecasting/notebook/evaluasi_perbandingan_bilstm.ipynb`

Pemilihan Hasil Akhir: 

**Percobaan ke-4 digunakan sebagai hasil akhir pemodelan Bi-LSTM dalam penelitian ini.**

Hasil keluaran percobaan tersebut disimpan pada direktori:

`06_Forecasting/percobaan-bi-lstm/output_bilstm_percobaan-4/`

Data hasil prediksi dari percobaan ke-4 kemudian digunakan sebagai sumber visualisasi pada prototipe aplikasi Streamlit.

Repository juga menyediakan file model Bi-LSTM:

`06_Forecasting/bilstm-model/best_bilstm.keras`

### 4.7 Visualisasi Menggunakan Streamlit

Tahap akhir penelitian berupa pengembangan prototipe aplikasi menggunakan Streamlit untuk menyajikan hasil estimasi dan prediksi kepadatan lalu lintas.

Implementasi aplikasi tersedia pada:

`07_Streamlit_Prototype_App/app.py`

Visualisasi prediksi menggunakan **hasil dari percobaan Bi-LSTM ke-4** sebagai keluaran pemodelan yang dipilih dalam penelitian.

Dengan demikian, aplikasi berfungsi sebagai sarana penyajian hasil penelitian, khususnya hasil prediksi derajat kejenuhan pada arah IN dan OUT.

## 5. Teknologi yang Digunakan

| Teknologi          | Penggunaan                         |
| ------------------ | ---------------------------------- |
| Python             | Bahasa pemrograman utama           |
| Ultralytics YOLO   | Deteksi kendaraan                  |
| PyTorch            | Framework deep learning untuk YOLO |
| OpenCV             | Pengolahan video dan citra         |
| TensorFlow / Keras | Pemodelan Bi-LSTM                  |
| Pandas dan NumPy   | Pengolahan dataset                 |
| Scikit-learn       | Evaluasi model                     |
| Matplotlib         | Visualisasi grafik                 |
| Jupyter Notebook   | Eksperimen dan analisis            |
| Streamlit          | Prototipe aplikasi                 |

## 6. Ketersediaan Dataset dan Model

Repository menyediakan kode program, notebook penelitian, hasil evaluasi, dan beberapa artefak pelatihan model.

Untuk menjaga ukuran repository, sejumlah file tidak disertakan, antara lain:

- Dataset YOLO berukuran besar.
- Rekaman CCTV dalam format `.mp4`.
- Model YOLO pretrained.
- Checkpoint `last.pt`.
- Folder `weights` dari eksperimen perbandingan model.
- File sementara dan cache lingkungan pengembangan.

File hasil eksperimen seperti `results.csv`, `results.png`, dan `args.yaml` tetap disertakan untuk mendukung dokumentasi dan analisis.

Checkpoint `best.pt` dari eksperimen deteksi kendaraan disediakan pada `03_Vehicle_Detection/runs/`, sedangkan model Bi-LSTM tersedia dalam format `.keras`.

## 7. Instalasi

Clone repository:

```bash
git clone https://github.com/hardianjusuf/Traffic-Counting-and-Density-Forecasting-using-YOLOv12-and-BiLSTM.git
```

Masuk ke direktori repository:

```bash
cd Traffic-Counting-and-Density-Forecasting-using-YOLOv12-and-BiLSTM
```

Buat virtual environment:

```bash
python -m venv .venv
```

Aktifkan virtual environment pada Windows:

```powershell
.venv\Scripts\activate
```

Instal dependensi sesuai kebutuhan notebook atau aplikasi yang akan dijalankan.

**Catatan:** Beberapa eksperimen memerlukan dataset, rekaman CCTV, atau bobot model yang tidak disertakan dalam repository. Sesuaikan direktori dan path file sebelum menjalankan program.

## 8. Informasi Penelitian

**Judul Skripsi:**

Estimasi dan Prediksi Kepadatan Kendaraan Lalu Lintas Menggunakan Model YOLO dan Bi-LSTM pada Citra CCTV (Studi Kasus: Ruas Jalan Pettarani–Andi Djemma Depan Kampus UNM)

**Peneliti:** M. Hardian Jusuf Herdiansyah

**Bidang:** Teknik Informatika — Computer Vision dan Deep Learning

**Lokasi Penelitian:** Makassar, Sulawesi Selatan, Indonesia.

## 9. Penulis

**M. Hardian Jusuf Herdiansyah**

GitHub: [hardianjusuf](https://github.com/hardianjusuf)

---

*Repository ini dikembangkan untuk keperluan penelitian akademik, eksperimen, dan dokumentasi implementasi sistem estimasi serta prediksi kepadatan lalu lintas.*
