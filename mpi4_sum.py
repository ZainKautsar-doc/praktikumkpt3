"""
============================================================
  Tugas Praktikum MPI 4 — Hitung Jumlah dengan Scatter + Gather (Bonus)
  Nama Lengkap : Zain Kautsar Ridha
  NPM          : 247006111153
  Kelas        : F
============================================================
  Cara run: mpirun -n 4 python mpi4_sum.py
  Ekspektasi total akhir = 100
============================================================
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size != 4:
    if rank == 0:
        print("Harap jalankan dengan -n 4")
    raise SystemExit

# Data awal di rank 0
data = [5, 10, 15, 20] if rank == 0 else None

# Scatter: tiap proses terima 1 elemen
x = comm.scatter(data, root=0)

# Komputasi lokal: 2 × data
local = 2 * x

# Gather: kumpul hasil ke rank 0
kumpul = comm.gather(local, root=0)

if rank == 0:
    total = sum(kumpul)
    print(f"Data awal      : {data}")
    print(f"×2 per-proses  : {kumpul}")
    print(f"Total akhir    : {total}")   # Ekspektasi: 100
    print()
    print(f"{'Rank':<6} {'Input':>8} {'Output (x2)':>14}")
    print("-" * 32)
    for r, (inp, out) in enumerate(zip(data, kumpul)):
        print(f"{r:<6} {inp:>8} {out:>14}")
    print(f"\nValidasi: (2×5)+(2×10)+(2×15)+(2×20) = 10+20+30+40 = {total}")
