# Dataset Deteksi Kendaraan YOLO

Dataset YOLO yang digunakan dalam penelitian ini disimpan secara terpisah melalui Google Drive karena ukuran dataset yang besar.

Dataset berisi citra lalu lintas yang diperoleh dari rekaman CCTV pada ruas Jalan A.P. Pettarani–Andi Djemma, tepatnya di depan Kampus Universitas Negeri Makassar (UNM). Dataset digunakan untuk proses pelatihan dan validasi model YOLO dalam mendeteksi kendaraan.

## Informasi Dataset

| Informasi          | Keterangan                                                                                     |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| Nama Dataset       | New_YOLO_Datasets                                                                              |
| Sumber Data        | Rekaman CCTV lalu lintas Dinas Komunikasi dan Informatika Kota Makassar (Diskominfo Makassar) |
| Lokasi             | Ruas Jalan A.P. Pettarani–Andi Djemma, Makassar                                               |
| Jumlah Citra       | 2.400 citra (setelah augmentasi)                                                              |
| Kelas Kendaraan    | motor, mobil, bus, truk                                                                        |
| Format Anotasi     | YOLO                                                                                           |
| Ukuran Citra       | 640 × 640 piksel                                                                              |
| Pengolahan Dataset | Roboflow                                                                                       |

## Struktur Dataset

```text
New_YOLO_Datasets/
├── train/
├── valid/
└── data.yaml
```

Folder `train` berisi citra dan anotasi untuk pelatihan model, sedangkan folder `valid` digunakan untuk validasi. File `data.yaml` berisi konfigurasi dataset, termasuk lokasi data dan daftar kelas kendaraan.

## Akses Dataset

Dataset dapat diakses melalui tautan Google Drive berikut:

**Google Drive:** [Unduh Dataset YOLO](https://drive.google.com/drive/folders/1mhhdXoxFfeFT6_5sxPmgicFzDigqq48t?usp=drive_link)

## Penggunaan Dataset

Unduh dan ekstrak dataset dari Google Drive. Selanjutnya, sesuaikan konfigurasi direktori pada file `data.yaml` sebelum menjalankan proses pelatihan model YOLO.

Dataset ini digunakan untuk keperluan penelitian akademis mengenai deteksi kendaraan, estimasi kepadatan lalu lintas, dan prediksi kepadatan menggunakan YOLO dan Bi-LSTM.

Penggunaan dan pendistribusian ulang dataset harus memperhatikan izin penggunaan rekaman CCTV yang menjadi sumber data.
