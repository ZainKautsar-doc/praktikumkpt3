"""
============================================================
  Tugas Praktikum MPI 3 — Scatter + Gather (Kombinasi)
  Nama Lengkap : Zain Kautsar Ridha
  NPM          : 247006111153
  Kelas        : F
============================================================
  Cara run: mpirun -n 4 python mpi3_scatter_gather.py
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

# Input 1: [1, 2, 3, 4]   — ubah ke [2, 4, 6, 8] untuk uji kedua
data = [1, 2, 3, 4] if rank == 0 else None   # Uji juga: [2, 4, 6, 8]

# Stage 1: Scatter — tiap proses terima 1 elemen
x = comm.scatter(data, root=0)

# Stage 2: Komputasi lokal — kuadrat
y = x * x

# Stage 3: Gather — kumpul hasil ke rank 0
hasil = comm.gather(y, root=0)

if rank == 0:
    print(f"Input  : {data}")
    print(f"Output : {hasil}")
    print()
    print(f"{'Rank':<6} {'Input':>8} {'Output (Kuadrat)':>18}")
    print("-" * 36)
    for r, (inp, out) in enumerate(zip(data, hasil)):
        print(f"{r:<6} {inp:>8} {out:>18}")
