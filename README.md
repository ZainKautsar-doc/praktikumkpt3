# Praktikum MPI — Message Passing Interface

**Nama Lengkap :** [NAMA LENGKAP KAMU]  
**NPM           :** [NPM KAMU]  
**Kelas         :** [KELAS KAMU]

---

## Struktur File

```
mpi/
├── mpi1_scatter.py              — Tugas 1: Scatter Sederhana
├── mpi2_gather.py               — Tugas 2: Gather Sederhana
├── mpi3_scatter_gather.py       — Tugas 3: Scatter + Gather (Kombinasi)
├── mpi4_sum.py                  — Tugas 4: Hitung Jumlah Scatter+Gather (Bonus)
├── mpi5_reduce_allreduce.py     — Tugas 5: Reduce vs Allreduce
└── README.md                    — Panduan ini
```

---

## Persyaratan

```bash
# Install MPI (Ubuntu/Debian)
sudo apt-get install mpich

# Install mpi4py
pip install mpi4py
```

---

## Cara Menjalankan

### Tugas 1 — Scatter Sederhana (wajib -n 4)

```bash
mpirun -n 4 python mpi1_scatter.py
```

Output yang diharapkan:
```
Rank 0 menerima 10
Rank 1 menerima 20
Rank 2 menerima 30
Rank 3 menerima 40
```
*(urutan baris bisa berbeda karena non-determinisme output paralel)*

---

### Tugas 2 — Gather Sederhana (-n 4 dan -n 6)

```bash
mpirun -n 4 python mpi2_gather.py
mpirun -n 6 python mpi2_gather.py
```

| Proses | Hasil List di Rank 0       |
|--------|---------------------------|
| 4      | [0, 5, 10, 15]            |
| 6      | [0, 5, 10, 15, 20, 25]   |

---

### Tugas 3 — Scatter + Gather Kombinasi (wajib -n 4)

```bash
mpirun -n 4 python mpi3_scatter_gather.py
```

Edit baris `data = [1, 2, 3, 4]` → `[2, 4, 6, 8]` untuk uji kedua.

| Input      | Output Kuadrat       |
|------------|----------------------|
| [1,2,3,4]  | [1, 4, 9, 16]        |
| [2,4,6,8]  | [4, 16, 36, 64]      |

---

### Tugas 4 — Hitung Jumlah Bonus (wajib -n 4)

```bash
mpirun -n 4 python mpi4_sum.py
```

Ekspektasi: `Total akhir = 100`

---

### Tugas 5 — Reduce vs Allreduce (contoh p = 1, 2, 4, 8)

```bash
mpirun -n 4 python mpi5_reduce_allreduce.py
mpirun -n 8 python mpi5_reduce_allreduce.py   # ubah juga seed jika perlu
```

| Bagian | Metrik            | Nilai (n=4)   |
|--------|-------------------|---------------|
| A      | MAX (Reduce)      | 24            |
| B      | SUM (Allreduce)   | 10            |
| B      | AVG (SUM/Size)    | 2.500000      |
| C      | TOTAL (Allreduce) | 1993.195672   |

---

## Catatan Penting

- Semua script **harus** dijalankan dengan `mpirun`/`mpiexec`, bukan `python` langsung.
- Urutan output antar-rank **tidak dijamin** (non-deterministik) karena setiap proses menulis ke stdout secara independen.
- Untuk `-n 6` pada Tugas 2, cukup jalankan `mpirun -n 6 python mpi2_gather.py` tanpa mengubah kode (kode otomatis menyesuaikan `size`).