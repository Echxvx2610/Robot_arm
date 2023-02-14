import os
import roboticstoolbox as rtb
from spatialmath import SE3
from roboticstoolbox.backends.swift import Swift

panda = rtb.models.URDF.Panda()
#robot = rtb.models.DH.Panda()
print(panda)

#print(robot.qz)
#print(robot.qr)
#T = robot.fkine(robot.qz)
#print(T)

T = SE3(0.7,0.2,0.1)*SE3.OA([0, 1, 0],[0, 0 ,-1])
print(T)

sol = panda.ikine_LM(T)
print(sol)

q_pickup = sol.q
print(panda.fkine(q_pickup))
qt = rtb.jtraj(panda.qz,q_pickup,70)
print(qt.q.shape)

#backend = Swift()
#backend.launch()
#backend.add(panda)

#for qk in qt.q:
#    panda.q = qk
#    backend.step()

#backend.hold()