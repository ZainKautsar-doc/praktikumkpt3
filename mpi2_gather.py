"""
============================================================
  Tugas Praktikum MPI 2 — Gather Sederhana
  Nama Lengkap : Zain Kautsar Ridha
  NPM          : 247006111153
  Kelas        : F
============================================================
  Cara run: mpirun -n 4 python mpi2_gather.py
            mpirun -n 6 python mpi2_gather.py
============================================================
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Tiap proses mengirim rank * 5
send_val = rank * 5

# Gather: kumpulkan semua nilai ke rank 0
gathered = comm.gather(send_val, root=0)

if rank == 0:
    print(f"Jumlah proses : {size}")
    print(f"Hasil gather di rank 0: {gathered}")
