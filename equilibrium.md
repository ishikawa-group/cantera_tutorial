# 化学平衡
* 系が化学平衡にある場合の物理量・化学量を求める

## 例
* 以下では、酸素とメタンがモル分率1:1で混合した気体の例を考える

```python
import cantera as ct
gas = ct.Solution("gri30.yaml")

A = ct.Quantity(gas, constant="HP")
A.TPX = 300, ct.one_atm, "O2:0.5, CH4:0.5"

print("--- Before equilibration ---")
print(A.report())

print("--- After equilibration ---")
A.equilibrate("TP")
print(A.report())
```

* 化学反応メカニズムにあたる`Solution`クラスから、ある化学量をもつ状態を発生するために`Quantity`クラスを呼び出す
* 上記の例では、エンタルピー`H`と圧力`P`が一定となる条件`A`を作成する
* `A`の初期条件(温度、圧力、モル分率)をクラス属性`TPX`に割り当てる
* 条件設定後、`.equilibrate`で平衡化する。この場合、温度と圧力を一定で平衡化している
* 平衡化の前後で質量分率などが変化している

## 混合気体
* 2種の気体系を混合する場合

```python
import cantera as ct
gas = ct.Solution("gri30.yaml")

A = ct.Quantity(gas, constant="HP")
A.TPX = 300, ct.one_atm, "O2:0.2, N2:0.8"

B = ct.Quantity(gas, constant="HP")
B.TPX = 300, ct.one_atm, "CH4:1"

A.moles = 1

nO2 = A.X[A.species_index("O2")]
B.moles = nO2 * 0.5

M = A + B
print("--- Before equilibration ---")
print(M.report())

print("--- After equilibration ---")
M.equilibrate("TP")
print(M.report())
```

## 熱力学量
* 平衡化後の熱力学量を算出する場合

```python
import cantera as ct

# Create a gas mixture
gas = ct.Solution("gri30.yaml")

# Set the state
gas.TPX = 1200, 101325, "CH4:1, O2:2"

# Calculate properties
q1 = ct.Quantity(gas)
enthalpy = q1.enthalpy
entropy = q1.entropy
cp = gas.cp

# Output results
print(f"Enthalpy: {enthalpy:5.3f} J/kg")
print(f"Entropy: {entropy:5.3f} J/kg·K")
print(f"Specific Heat (Cp): {cp:5.3f} J/kg·K")
```