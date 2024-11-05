# 表面反応
```python{cmd}
import cantera as ct
import csv

p = ct.one_atm  # pressure: 1 atm =  1013 [Pa]
Tin = 1500  # temperature [K]
comp = "CH4:1, O2:1, AR:0.5"
vin = 0.005  # inlet gas velocity [m/s]
length = 5.0e-6  # length of reactor [m]
area = 1.0e-4 # cross section area of reactor [m^2]
area_cat_vol = 3149.0  # catalyst surface area [m^2/m^3]
porosity = 1.0  # catalyst porosity
n_reactor = 200  # numerical parameter to divide reactor

filename = "ptcombust.yaml"
gas = ct.Solution(filename, "gas")
gas.TPX = Tin, p, comp
mdot = vin * area * gas.density  # mass flow rate
dx = length / n_reactor  # length of one simulation cell

# define surface
surf = ct.Interface(filename, "Pt_surf", [gas])
surf.TP = Tin, p

r = ct.IdealGasReactor(gas)
vol = area * dx * porosity
r.volume = area * dx

upstream = ct.Reservoir(gas, name="upstream")
downstream = ct.Reservoir(gas, name="downstream")
m = ct.MassFlowController(upstream, r, mdot=mdot)
v = ct.PressureController(r, downstream, primary=m, K=1.0e-5)

area_cat = area_cat_vol * vol
rsurf = ct.ReactorSurface(surf, r, A=area_cat)

net = ct.ReactorNet([r])

# solve
outfile = open("catalytic_pfr.csv", "w", newline="")
writer = csv.writer(outfile)
writer.writerow(["Distance [m]", "u [m/s]", "time [s]", "T [K]", "P [Pa]"] + gas.species_names + surf.species_names)

t_res = 0.0
for n in range(n_reactor):
  gas.TDY = r.thermo.TDY
  upstream.syncState()
  net.reinitialize()
  net.advance_to_steady_state()
  dist = n * dx
  u = mdot / area / r.thermo.density  # velocity
  t_res += r.mass / mdot  # residence time
  writer.writerow([dist, u, t_res, r.T, r.thermo.P] + list(r.thermo.X) + list(rsurf.kinetics.coverages))

outfile.close()
```