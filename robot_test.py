import os
import roboticstoolbox as rtb
from roboticstoolbox.backends.swift import Swift


#inicializa el modelo
panda = rtb.models.URDF.Panda()
backend = Swift()
backend.launch()
backend.add(panda)

qt = rtb.jtraj(panda.qz, panda.qr,40)

for qk in qt.q:
    panda.q = qk
    backend.step()

backend.hold()