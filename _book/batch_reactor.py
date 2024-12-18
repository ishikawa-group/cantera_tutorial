import cantera as ct
import matplotlib.pyplot as plt

# Create a gas mixture
gas = ct.Solution("gri30.yaml")

# Set initial state
gas.TPX = 1000, 101325, "CH4:1, O2:2, N2:7.52"

# Analyze the first reaction
reaction = gas.reaction(0)
print(f"Reaction: {reaction.equation}")

# Create a constant volume reactor
reactor = ct.IdealGasReactor(gas)
network = ct.ReactorNet([reactor])

# Simulate the reaction
time = 0.0
end_time = 2.0  # seconds

x = []
h2o = []
ch4 = []
while time < end_time:
    time = network.step()
    x.append(time)
    h2o.append(reactor.thermo.concentrations[5])
    ch4.append(reactor.thermo.concentrations[13])

plt.plot(x, h2o, label="H2O")
plt.plot(x, ch4, label="CH4")
plt.xlabel("Time (s)")
plt.ylabel("Molar fraction (-)")

plt.tight_layout()
plt.legend()
plt.show()
