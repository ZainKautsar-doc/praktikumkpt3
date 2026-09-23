"""
============================================================
  Tugas Praktikum MPI 1 — Scatter Sederhana
  Nama Lengkap : Zain Kautsar Ridha
  NPM          : 247006111153
  Kelas        : F
============================================================
  Cara run: mpirun -n 4 python mpi1_scatter.py
============================================================
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Pastikan jumlah proses = 4
if size != 4:
    if rank == 0:
        print("Harap jalankan dengan -n 4")
    raise SystemExit

# Hanya rank 0 yang punya data
data = [10, 20, 30, 40] if rank == 0 else None

# Scatter: tiap proses terima 1 elemen
recv = comm.scatter(data, root=0)

print(f"Rank {rank} menerima {recv}")
