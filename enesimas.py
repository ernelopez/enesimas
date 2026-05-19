import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# Datos de entrada
# ---------------------------------

z = 3 + 4j      # número complejo
n = 5           # raíz enésima

# ---------------------------------
# Cálculo de raíces enésimas
# ---------------------------------

r = abs(z)
theta = np.angle(z)

raices = []

for k in range(n):
    modulo = r**(1/n)
    argumento = (theta + 2*np.pi*k)/n

    w = modulo * (
        np.cos(argumento) + 1j*np.sin(argumento)
    )

    raices.append(w)

# ---------------------------------
# Mostrar raíces
# ---------------------------------

print("Raíces enésimas:")

for i, w in enumerate(raices):
    print(f"w_{i} = {w}")

# ---------------------------------
# Gráfico
# ---------------------------------

fig, ax = plt.subplots(figsize=(6,6))

# raíz original
ax.plot(
    z.real,
    z.imag,
    'o',
    markersize=10,
    label='z'
)

# raíces
for i, w in enumerate(raices):
    ax.plot(
        w.real,
        w.imag,
        'o',
        markersize=8,
        label=f'raíz {i}'
    )

# ejes
ax.axhline(0)
ax.axvline(0)

# aspecto cuadrado
ax.set_aspect('equal')

# grilla
ax.grid(True)

# etiquetas
ax.set_xlabel('Parte real')
ax.set_ylabel('Parte imaginaria')

plt.legend()
plt.show()
