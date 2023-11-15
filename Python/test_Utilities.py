from math import sqrt

from raytracer.Utilities.Vector3D import Vector3D
from raytracer.Utilities.Point3D import Point3D
from raytracer.Utilities.Normal import Normal

## Variables
i = 2.5

u = Vector3D(1, 2, 3)
v = Vector3D(4, 5, 6)

a = Point3D(2, 3, 4)
b = Point3D(5, 6, 7)

n = Normal(3, 4, 5)
m = Normal(6, 7, 8)

##=================================== Vector Tests
assert (u + v) == Vector3D(5, 7, 9)
assert (v - u) == Vector3D(3, 3, 3)
assert (i * u) == Vector3D(i*1, i*2, i*3)
assert (u * i) == Vector3D(i*1, i*2, i*3)
assert (u / i) == Vector3D(1/i, 2/i, 3/i)
assert (u * v) == 1*4 + 2*5 + 3*6
assert (u.cross(v)) == Vector3D(-3, 6, -3)
assert (u.norm())       == sqrt(1+4+9)
assert (u.norm_sq())    == 1+4+9
assert (-u) == Vector3D(-1, -2, -3)

##=================================== Point Tests
assert (a + u) == Point3D(3, 5, 7)
assert (a - u) == Point3D(1, 1, 1)
assert (a - b) == Vector3D(-3, -3, -3)
assert ((a-b).norm())       == sqrt(3*9)
assert ((a-b).norm_sq())    == 3*9
assert (i * a) == Point3D(i*2, i*3, i*4)
assert (a * i) == Point3D(i*2, i*3, i*4)

##=================================== Normal Tests
assert (n/n.norm() == n.normalize())
t = sqrt(3*3+4*4+5*5)
assert (n.normalize()) == Normal(3/t, 4/t, 5/t)
assert (-n) == Normal(-3, -4, -5)
assert (n + m) == Normal(9, 11, 13)
assert (n * u) == 3 + 8 + 15
assert (u * n) == 3 + 8 + 15
assert (i * n) == Normal(i*3, i*4, i*5)
assert (n * i) == Normal(i*3, i*4, i*5)
assert (n + u) == Vector3D(4, 6, 8)
assert (u + n) == Vector3D(4, 6, 8)