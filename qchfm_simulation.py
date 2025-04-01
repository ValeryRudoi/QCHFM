
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Grid setup
nx, ny = 100, 50
lx, ly = 10.0, 5.0
dx, dy = lx / nx, ly / ny
x = np.linspace(0, lx, nx)
y = np.linspace(0, ly, ny)
X, Y = np.meshgrid(x, y)

# Time setup
dt = 0.01
timesteps = 200

# Initialize fields
u = np.zeros((ny, nx))  # velocity x
v = np.zeros((ny, nx))  # velocity y
p = np.zeros((ny, nx))  # pressure
sigma = np.zeros((ny, nx))  # uncertainty amplitude

# Initial wind/thermal setup
u[:, :] = 1.0  # base wind
sigma += 0.1 * np.random.rand(ny, nx)  # uncertainty field

# Quantum-inspired stochastic noise (Wiener process)
def add_quantum_drift(u, sigma, dt):
    noise = sigma * np.random.randn(*u.shape) * np.sqrt(dt)
    return u + noise

# Confidence index
def compute_confidence(sigma, alpha=0.05):
    return np.exp(-sigma**2 / alpha)

# Run simulation
u_snapshots = []
conf_snapshots = []

for t in range(timesteps):
    # Update u with stochastic drift
    u = add_quantum_drift(u, sigma, dt)
    confidence = compute_confidence(sigma)
    
    # Store snapshots
    if t % 10 == 0:
        u_snapshots.append(u.copy())
        conf_snapshots.append(confidence.copy())

# Plot animation
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

def animate(i):
    ax[0].cla()
    ax[1].cla()
    ax[0].imshow(u_snapshots[i], cmap='coolwarm', origin='lower', extent=[0, lx, 0, ly])
    ax[0].set_title("Velocity Field (u)")
    ax[1].imshow(conf_snapshots[i], cmap='viridis', origin='lower', extent=[0, lx, 0, ly])
    ax[1].set_title("Confidence Map")

ani = animation.FuncAnimation(fig, animate, frames=len(u_snapshots), interval=100)
plt.tight_layout()
plt.show()
