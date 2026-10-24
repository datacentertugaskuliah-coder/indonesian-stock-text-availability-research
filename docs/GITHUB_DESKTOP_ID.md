# Panduan GitHub Desktop untuk repositori penelitian

**Gunakan file ZIP repositori dari paket ChatGPT, bukan ZIP 20 hasil eksperimen.**
Paket berisi folder `indonesian-stock-text-availability-research/`.

## Mac / Windows, tanpa terminal

1. Ekstrak ZIP repositori di folder Downloads atau Documents.
2. Buka **GitHub Desktop**, masuk akun GitHub pada Preferences/Options -> Accounts.
3. Pilih **File > New Repository**. Isi `Name` dengan `indonesian-stock-text-availability-research`,
   pilih `Local path` di Documents/GitHub atau lokasi pilihan. Jangan centang opsi membuat README
   karena paket sudah memuat README. Klik **Create Repository**.
4. Buka folder repo baru melalui **Repository > Show in Finder** (Mac) atau
   **Repository > Show in Explorer** (Windows).
5. Pada Mac, tekan `Command + Shift + .` di Finder untuk menampilkan `.github` dan `.gitignore`;
   kedua berkas/folder tersembunyi ini perlu ikut dicopy. Dari hasil ekstrak ZIP, **copy seluruh isi folder repo** (README.md, .gitignore,
   `.github`, audit, data, docs, notebooks, results, scripts, requirements.txt) ke folder repo
   baru yang dibuka pada langkah 4. Jangan copy folder pembungkusnya agar tidak bersarang.
6. Kembali ke GitHub Desktop. Tab **Changes** akan mencantumkan file baru.
7. Pastikan tidak ada `*.docx`, `*.ris`, raw tweet text, atau file kredensial.
8. Isi **Summary** dengan `Initial reproducible research archive` dan klik **Commit to main**.
9. Klik **Publish repository**. Disarankan **Keep this code private** tetap dicentang pada
   pemeriksaan pertama. Setelah yakin data/izin aman, Anda dapat menjadikannya publik.
10. Pilih **Repository > View on GitHub** untuk melihat folder `notebooks/`, `results/`,
    `docs/` dan status GitHub Actions pada website.

Panduan resmi: https://docs.github.com/en/desktop/overview/creating-your-first-repository-using-github-desktop

## Update penelitian berikutnya

Ubah/tambahkan file lokal, periksa **Changes**, tulis ringkasan commit yang jelas,
klik **Commit to main**, lalu **Push origin**. Gunakan branch/pull request untuk perubahan
metode signifikan. Jangan menimpa output lama tanpa versioning.

## Audit yang harus terlihat di GitHub

- `README.md` adalah halaman depan.
- `docs/DATA_PROVENANCE.md` berisi DOI dan SHA-256 asli.
- `notebooks/` menunjukkan bagaimana prediksi dihitung.
- `results/tables/` dan `results/figures/` berisi 40 keluaran.
- `audit/evidence_manifest.json` berisi ukuran dan SHA-256 semua hasil.
- **Actions > Static evidence audit** menunjukkan berhasil/gagalnya verifikasi berkas.

**Jangan upload ZIP yang berisi DOCX/RIS atau file data mentah ke repository publik.**
Kode analisis tetap memerlukan file sumber resmi saat dijalankan kembali.
