# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as pl

#%% Q2 setup
def binomial(n, p, N):
    return np.math.factorial(N)/(np.math.factorial(n)*np.math.factorial(N-n))*(p**n)*((1-p)**(N-n))

def uniform(n, p, N):
    return 1/(N+1)

def KL(p, N, distp, distq):
    kl = 0
    for n in range(N):
        kl -= distp(n, p, N)*np.log2(distq(n, p, N)/distp(n, p, N))
    return kl

def align_yaxis(ax1, v1, ax2, v2):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _, y1 = ax1.transData.transform((0, v1))
    _, y2 = ax2.transData.transform((0, v2))
    inv = ax2.transData.inverted()
    _, dy = inv.transform((0, 0)) - inv.transform((0, y1-y2))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy)

#%% Q2(c)
KL_N10 = []
KL_N100 = []

for p in np.linspace(0, 1, 1000):
    KL_N10.append(KL(p, 10, uniform, binomial))
    KL_N100.append(KL(p, 100, uniform, binomial))

fig, ax = pl.subplots(1,1)
ax.plot(np.linspace(0, 1, 1000), KL_N10, 'b-', label="N=10")
ax2 = ax.twinx()
ax2.plot(np.linspace(0, 1, 1000), KL_N100, 'r-', label="N=100")
ax.set_xlabel("p")
ax.set_ylabel("KL divergence (N=10)")
ax2.set_ylabel("KL divergence (N=100)")
align_yaxis(ax, 0, ax2, 0)
ax.legend()
ax2.legend()

#%% Q2(d)
def poisson(n, p, N):
    lam = p*N
    return (lam**n)*(np.exp(-lam))/np.math.factorial(n)

KL_lam_N10 = []
KL_lam_N100 = []

for p in np.linspace(0, 1, 1000):
    KL_lam_N10.append(KL(p, 10, poisson, binomial))
    KL_lam_N100.append(KL(p, 100, poisson, binomial))
    
fig1, ax1 = pl.subplots(1,1)
ax1.plot(np.linspace(0, 1, 1000), KL_lam_N10, 'b-', label="N=10")
ax3 = ax1.twinx()
ax3.plot(np.linspace(0, 1, 1000), KL_lam_N100, 'r-', label="N=100")
ax1.set_xlabel("p")
ax1.set_ylabel("KL divergence (N=10)")
ax3.set_ylabel("KL divergence (N=10000)")
align_yaxis(ax1, 0, ax3, 0)
ax1.legend(loc=0)
ax3.legend(loc=6)

#%% Q5(a)
import math
def eff(N):
    return np.log2(N)/math.ceil(np.log2(N))

N_arr = []

for n in range(2,101):
    N_arr.append(eff(n))

fig2, ax4 = pl.subplots(1,1)
ax4.plot(np.arange(2, 101), N_arr, 'b-')
ax4.set_xlabel(r"$N$")
ax4.set_ylabel(r"Efficiency")

#%%
N_arr = np.array(N_arr)
print(np.arange(2,101)[np.argmin(N_arr)]) # N = 5 gives smallest efficiency
print(np.min(N_arr))
print(N_arr[-1])