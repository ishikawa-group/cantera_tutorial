# メカニズムファイルの書き方
* ここでは、メカニズムファイルの書き方を解説する
* 以下に実際のファイル(表面反応)を示す

```yaml
units: {length: cm, quantity: mol, activation-energy: J/mol}

phases:
- name: gas
  thermo: ideal-gas
  elements: [O, H, C, N, Ar]
  species:
  - gri30.yaml/species: [H2, H, O, O2, OH, H2O, HO2, 
      H2O2, C, CH, CH2, CH2(S), CH3, CH4, CO, CO2, C2H2, C2H3, C2H4, C2H5, C2H6, AR, N2]
  skip-undeclared-elements: true
  kinetics: gas
  reactions:
  - gri30.yaml/reactions: declared-species

- name: Pt_surf
  thermo: ideal-surface
  adjacent-phases: [gas]
  elements: [Pt, H, O, C]
  species: [PT(S), H(S), H2O(S), OH(S), CO(S), CO2(S), CH3(S), CH2(S), CH(S), C(S), O(S)]
  kinetics: surface
  reactions: all
  state:
    T: 900.0
    coverages: {O(S): 0.0, PT(S): 0.5, H(S): 0.5}
  site-density: 2.7063e-09

species:
- name: PT(S)
  composition: {Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: H(S)
  composition: {H: 1, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: H2O(S)
  composition: {O: 1, H: 2, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: OH(S)
  composition: {O: 1, H: 1, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: CO(S)
  composition: {C: 1, O: 1, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: CO2(S)
  composition: {C: 1, O: 2, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: CH3(S)
  composition: {C: 1, H: 3, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: CH2(S)
  composition: {C: 1, H: 2, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: CH(S)
  composition: {C: 1, H: 1, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: C(S)
  composition: {C: 1, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
- name: O(S)
  composition: {O: 1, Pt: 1}
  thermo:
    model: NASA7
    temperature-ranges: [300.0, 1000.0, 3000.0]
    data:
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    - [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

reactions:
- equation: H2 + 2 PT(S) => 2 H(S)
  rate-constant: {A: 4.4579e+10, b: 0, Ea: 0}
  orders: {PT(S): 2}
- equation: 2 H(S) => H2 + 2 PT(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 67400}
- equation: O2 + 2 PT(S) => 2 O(S)
  rate-constant: {A: 1.8e+21, b: 0, Ea: 0}
  orders: {PT(S): 2}
- equation: 2 O(S) => O2 + 2 PT(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 213200}
- equation: H2O + PT(S) => H2O(S)
  sticking-coefficient: {A: 0.75, b: 0, Ea: 0}
- equation: H2O(S) => H2O + PT(S)
  rate-constant: {A: 1.0e+13, b: 0, Ea: 40300}
- equation: H(S) + O(S) <=> OH(S) + PT(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 11500}
- equation: H(S) + OH(S) <=> H2O(S) + PT(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 17400}
- equation: OH(S) + OH(S) <=> H2O(S) + O(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 48200}
- equation: CO + PT(S) => CO(S)
  rate-constant: {A: 1.618e+20, b: 0, Ea: 0}
- equation: CO(S) => CO + PT(S)
  rate-constant: {A: 1.0e+13, b: 0, Ea: 125500}
- equation: CO2(S) => CO2 + PT(S)
  rate-constant: {A: 1.0e+13, b: 0, Ea: 20500}
- equation: CO(S) + O(S) => CO2(S) + PT(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 105000}
- equation: CH4 + 2 PT(S) => CH3(S) + H(S)
  rate-constant: {A: 4.6334e+20, b: 0, Ea: 0}
  orders: {PT(S): 2}
- equation: CH3(S) + PT(S) => CH2(S) + H(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 20000}
- equation: CH2(S) + PT(S) => CH(S) + H(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 20000}
- equation: CH(S) + PT(S) => C(S) + H(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 20000}
- equation: C(S) + O(S) => CO(S) + PT(S)
  rate-constant: {A: 3.7e+21, b: 0, Ea: 62800}
- equation: CO(S) + PT(S) => C(S) + O(S)
  rate-constant: {A: 1.0e+18, b: 0, Ea: 184000}
```

## ポイント
### phases
* 表面反応の場合、気相と表面の両方を定義する必要がある。ここではそれぞれ`gas`と`Pt_surf`にしている
* 気相反応の部分は`gri30.yaml`を読み込んでいる

### species
* 反応に現れる化学種をここで定義する必要がある
* 気体分子は`species: - gri30.yaml/species`で定義してあるので、表面のみがここでは必要
* 熱力学データがある場合(Gibbsエネルギー、エンタルピー、エントロピーの温度依存性)はここで指定することができる

### reactions
* 素反応式(`equation`)、反応速度定数(`rate-constant`)を与える
* 反応速度定数は拡張Arrhenius型( $ k = AT^b\exp(-Ea/RT) $)
* 反応次数(`orders`)を与えることもできる。デフォルトは一次反応になっているものと思われる