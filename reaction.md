# 化学反応
* Canteraで化学反応のシミュレーションを行う方法をここで解説する

## 理論的背景
* ここでは、反応器として **plug flow reactor (PFR)** を仮定する
* PFRは管型反応器のモデルとしてよく用いられる
* 計算上は、管をいくつかの部位に分割して各部位はバッチ反応器に近いcontinuoues stirred tank reactor (CSTR)として計算するケースもよく用いられる。ここではこの方法を採用することにする
* 管をいくつに分割するかの分割数(下のコードにおける`n_reactor`)を定義する必要がある

<div align="center">
<img src="./figures/cstr.png" width=50%>
</div>

## コードの基本的な流れ
1. メカニズムをファイルから読み込んでオブジェクトを作成する
```python
gas = ct.Solution("gri30.yaml")
```

2. 系の初期条件を設定する
* 温度、圧力、モル分率を設定する
```python
gas.TPX = 500, ct.one_atm, "CH4:1, O2:1, AR:0.5"
```

3. 反応器を設定する
* 反応器を設定する。反応器の種類は様々であるが、最も簡単な`IdealGasReactor`を用いる
* 反応器だけでなく、以下のような設定を通常置く
    + `ct.Reservoir`: 反応器の前後
    + `ct.MassFlowController`: 反応器の前
        + upstreamとdownstreamを引数で指定
    + `ct.PressureController`: 反応器の後
        + upstreamとdonwstreamを引数で指定
        + 質量流量速度を求めるデバイスをprimaryで指定(`MassFlowController`でよい)
        + Kという定数に1.0e-5を入れるとよい？ -> 調査中
* 反応器の設定が終わったら、**反応器のみ**を`ReactorNet`に設定する

4. 化学反応をシミュレーションする
* `ReactorNet`のメソッドを使って時間ステップを進めることができる。以下のようなメソッドがある
    + `.advance(tout)`: `tout`まで進める
    + `.advance_to_steady_state()`: 定常状態まで進める

## スクリプトの例
* 上記をまとめたスクリプトの例

```python
import cantera as ct
import csv

p = ct.one_atm  # pressure: 1 atm =  1013 [Pa]
Tin = 1500  # temperature [K]
comp = "CH4:1, O2:1, AR:0.5"
vin = 0.005  # inlet gas velocity [m/s]
length = 5.0e-6  # length of reactor [m]
area = 1.0e-4 # cross section area of reactor [m^2]
n_reactor = 200  # numerical parameter to divide reactor

gas = ct.Solution("gri30.yaml")
gas.TPX = Tin, p, comp
mdot = vin * area * gas.density  # mass flow rate
dx = length / n_reactor  # length of one simulation cell

r = ct.IdealGasReactor(gas)
r.volume = area * dx

upstream = ct.Reservoir(gas, name="upstream")
downstream = ct.Reservoir(gas, name="downstream")
m = ct.MassFlowController(upstream=upstream, downstream=r, mdot=mdot)
v = ct.PressureController(upstream=r, downstream=downstream, primary=m, K=1.0e-5)
net = ct.ReactorNet([r])

# solve
outfile = open("pfr.csv", "w", newline="")
writer = csv.writer(outfile)
writer.writerow(["Distance [m]", "u [m/s]", "time [s]", "T [K]", "P [Pa]"] + gas.species_names)

t_res = 0.0
for n in range(n_reactor):
    gas.TDY = r.thermo.TDY
    upstream.syncState()
    net.reinitialize()
    net.advance_to_steady_state()
    dist = n * dx
    u = mdot / area / r.thermo.density  # velocity
    t_res += r.mass / mdot  # residence time
    writer.writerow([dist, u, t_res, r.T, r.thermo.P] + list(r.thermo.X))

outfile.close()
```

## 反応経路解析
* 反応経路を描くことができる

```python
import cantera as ct
import os

gas = ct.Solution("gri30.yaml")
gas.TPX = 1500, ct.one_atm, "CH4:0.25, O2:1.0, N2:3.76"

r = ct.IdealGasReactor(gas)
net = ct.ReactorNet([r])

T = r.T
while T < 1900:
    net.step()
    T = r.T

element = "N"
diagram = ct.ReactionPathDiagram(gas, element)
diagram.title = "asdf"
diagram.label_threshold = 0.01

dot_file = "asdf.dot"
img_file = "asdf.png"

diagram.write_dot(dot_file)
os.system(f"dot {dot_file} -Tpng -o{img_file}")
```
