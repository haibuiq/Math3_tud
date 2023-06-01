import interpolation as inter
import numpy as np

#Creatings some sample variables
f = lambda x: np.sin(np.pi*x)

n = 4
lst_x_tscheb = inter.tscheb(4, 0, 2)
lst_x_norm = np.linspace(0, 2, n+1)

lst_dd_norm = inter.newton_interpolation_dd(n, f, lst_x_norm)
lst_dd_tscheb = inter.newton_interpolation_dd(n, f, lst_x_tscheb)

fct_norm = inter.newton_interpolation(n, f, lst_x_norm)
fct_tscheb = inter.newton_interpolation(n, f, lst_x_tscheb)

print("equidistante points :", lst_x_norm, "\n")
print("corresponding 'dividierte Differenzen' :", lst_dd_norm, "\n")
print("final interpolation :", fct_norm, "\n")

print("tschebyschev-abzissen :", lst_x_tscheb, "\n")
print("corresponding 'dividierte Differenzen' :", lst_dd_tscheb, "\n")
print("final interpolation :", fct_tscheb, "\n")
