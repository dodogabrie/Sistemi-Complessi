import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from scipy.stats import kde
from numba import njit, objmode

@njit
def get_param():
    n = 20000 # step di ogni camminatore
    dt = 0.08
    eps = 0.005
    mu = 0
    sigma = 1 
    return n, dt, eps, mu, sigma

@njit
def f(x):
    '''Forza applicata sui camminatori'''
    return x-x**3
@njit
def step(x, dw, dt, eps):
    '''Incremento sulla posizione'''
    return f(x)*dt + np.sqrt(eps)*dw
@njit
def motion(x):
    '''Gestione del movimento del camminatore'''
    n, dt, eps, mu, sigma = get_param()
    dw = np.random.normal(mu, sigma, n)
    for i in range(n-1):
        x[i+1] = x[i] + step(x[i], dw[i], dt, eps)
    return x, dw

@njit
def find_paths(x_init, n_camminatori):
    n, dt, eps, _, _ = get_param()
    m = n_camminatori
    X = np.empty((n,m))
    dW = np.copy(X)
    idx_array = np.zeros(m).astype(np.int32)
    success_path = 0
    while success_path < m:
        x, dw = motion(x_init)
        j = np.argmax(x>=1)
        if j > 0:
            idx_array[success_path] = j
            X[:, success_path] = x
            dW[:, success_path] = dw
            success_path += 1
            print(f"Finded {success_path}")
    return X, dW, idx_array

def run():
    np.random.seed(10) # Risultati riproducibili
    m = 300
    n, dt, eps, _, _ = get_param() # prendo i parametri del problema
    
    # Inizializzo matrice delle posizioni e dei numeri casuali
    x_init = np.empty(n)
    x_init[0] = -1 # posizione iniziale dei camminatori
    
    # trovo le traiettorie
    X, dW, jj = find_paths(x_init, m)
    return X.T, dW.T


if __name__ == "__main__":
    n, dt, eps,_,_ = get_param()
    print(f'rapporto eps/dt = {eps/dt}')
    p, w = run()
    t = np.arange(0,n*dt,dt)
    jm = n
    paths = []
    # Cerco il camminatore che ci ha messo meno ad arrivare ad 1 (sarà questo a decretare la lunghezza degli x_n)
    for path in p:
        j = np.argmax(path>=1)
        if jm > j:
            jm = j 
    
    #time = np.arange(-t[jm],0,dt)
    # Riformatto tutti gli array per avere la stessa lunghezza
    times = []
    for path in p:
        j = np.argmax(path>=1)
        if j > jm: # Escludo il più veloce (si potrebbe includere con una riga in più...)
            paths.append(path[:j]) # vado dal primo elemento fino al punto in cui x=1
            times.append(t[:j]-t[j]) # Creo un nuovo array di tempi sincronizzato con questo x_n
    
    # Plotto i risultati in HD
    n, m = p.shape
    num_plot = m # numero di plot da visualizzare
    for path in p[:num_plot]:
        j = np.argmax(path>=1)
        plt.plot(t - t[j], path, alpha=0.5, linewidth=0.5)
    plt.xlim(-3*t[jm],0)
    #plt.savefig("../../figures/lez_12_walker_t_path.png", dpi = 300) 
    plt.xlabel('t')
    plt.ylabel('x')
    plt.show()
