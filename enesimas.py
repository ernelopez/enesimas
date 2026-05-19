```python id="n5q8vz"
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Raíces enésimas de un número complejo")

st.write(
    "Ingresá un número complejo y un valor de n "
    "para calcular y graficar sus raíces enésimas."
)

# ---------------------------------
# Entrada de datos
# ---------------------------------

real = st.number_input(
    "Parte real",
    value=1.0
)

imag = st.number_input(
    "Parte imaginaria",
    value=0.0
)

n = st.number_input(
    "Valor de n",
    min_value=1,
    step=1,
    value=3
)

# ---------------------------------
# Número complejo
# ---------------------------------

z = complex(real, imag)

st.write(f"Número complejo: $z = {real} + {imag}i$")

# ---------------------------------
# Cálculo de raíces
# ---------------------------------

r = abs(z)
theta = np.angle(z)

raices = []

for k in range(n):
    modulo = r**(1/n)
    argumento = (theta + 2*np.pi*k)/n

    w = modulo * (
        np.cos(argumento)
        + 1j*np.sin(argumento)
    )

    raices.append(w)

# ---------------------------------
# Mostrar raíces
# ---------------------------------

st.subheader("Raíces enésimas")

for i, w in enumerate(raices):
    st.write(
        f"$w_{i} = "
        f"{w.real:.4f} "
        f"+ "
        f"{w.imag:.4f}i$"
    )

# ---------------------------------
# Gráfico
# ---------------------------------

fig, ax = plt.subplots(figsize=(6, 6))

# número original
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
ax.set_xlabel("Parte real")
ax.set_ylabel("Parte imaginaria")

ax.legend()

st.pyplot(fig)
```
