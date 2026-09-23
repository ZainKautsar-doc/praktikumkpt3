"""
============================================================
  Tugas Praktikum MPI 5 — Reduce vs Allreduce (MAX & Rata-Rata Global)
  Nama Lengkap : Zain Kautsar Ridha
  NPM          : 247006111153
  Kelas        : F
============================================================
  Cara run: mpirun -n 4 python mpi5_reduce_allreduce.py
============================================================
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"{'='*50}")
print(f"[Rank {rank}] Mulai eksekusi (size={size})")

# ─── Bagian A: MAX dengan Reduce ──────────────────────────
my_val = rank * 7 + 3   # Rank 0→3, Rank 1→10, Rank 2→17, Rank 3→24

max_val = comm.reduce(my_val, op=MPI.MAX, root=0)

if rank == 0:
    print(f"\n{'─'*50}")
    print(f"[BAGIAN A] Reduce dengan MPI.MAX")
    print(f"  Nilai tiap rank: rank*7+3  →  0→3, 1→10, 2→17, 3→24")
    print(f"  [REDUCE-MAX] max = {max_val}")
    print(f"  Proses dengan nilai terbesar: rank {size-1} (fungsi naik vs rank)")

# ─── Bagian B: Rata-rata global via Allreduce ─────────────
val_for_avg = rank + 1   # Rank 0→1, 1→2, 2→3, 3→4

global_sum = comm.allreduce(val_for_avg, op=MPI.SUM)
global_avg = global_sum / size

print(f"[ALLREDUCE-AVG] Rank {rank}: sum={global_sum}, avg={global_avg:.6f}")

if rank == 0:
    print(f"\n{'─'*50}")
    print(f"[BAGIAN B] Allreduce rata-rata global")
    print(f"  Nilai tiap rank: rank+1  →  0→1, 1→2, 2→3, 3→4")
    print(f"  Global SUM = {global_sum}, AVG = {global_avg:.6f}")

# ─── Bagian C: Total 1000 bilangan acak per proses ────────
rng   = np.random.default_rng(seed=12345 + rank)
nums  = rng.random(1000)
local_sum  = float(np.sum(nums))
total_sum  = comm.allreduce(local_sum, op=MPI.SUM)

if rank == 0:
    print(f"\n{'─'*50}")
    print(f"[BAGIAN C] Allreduce total 1000 bilangan acak per proses")
    print(f"  Total {size}x1000 = {size*1000} bilangan acak")
    print(f"  [ALLREDUCE-SUM] Total 1000*size bilangan acak = {total_sum:.6f}")

# ─── Tabel ringkasan (rank 0) ─────────────────────────────
if rank == 0:
    print(f"\n{'='*50}")
    print(f"  TABEL HASIL RINGKASAN")
    print(f"{'─'*50}")
    print(f"  {'Bagian':<8} {'Metrik':<22} {'Nilai':>12}")
    print(f"{'─'*50}")
    print(f"  {'A':<8} {'MAX (Reduce)':<22} {max_val:>12}")
    print(f"  {'B':<8} {'SUM (Allreduce)':<22} {global_sum:>12}")
    print(f"  {'B':<8} {'AVG (SUM/Size)':<22} {global_avg:>12.6f}")
    print(f"  {'C':<8} {'TOTAL (Allreduce)':<22} {total_sum:>12.6f}")
    print(f"{'='*50}")
