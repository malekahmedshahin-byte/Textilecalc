<div align="center">

<img src="https://img.shields.io/badge/TextileCalc-v2.0.0-1B3A6B?style=for-the-badge&logo=python&logoColor=white" alt="TextileCalc v2.0.0"/>

# 🧵 TextileCalc

### *The Complete Python Library for Textile Engineering*

**AI-Powered Yarn Recommendation · Shade Recipe Prediction · Carbon Footprint Lifecycle Analysis**

[![PyPI Python Version](https://img.shields.io/badge/python-3.7%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen?style=flat-square)](setup.py)
[![Version](https://img.shields.io/badge/version-2.0.0-blueviolet?style=flat-square)](https://github.com/malekahmedshahin-byte/TextileCalc)
[![Author](https://img.shields.io/badge/author-Abdul%20Malek-orange?style=flat-square)](https://github.com/malekahmedshahin-byte)
[![Stars](https://img.shields.io/github/stars/malekahmedshahin-byte/TextileCalc?style=flat-square)](https://github.com/malekahmedshahin-byte/TextileCalc/stargazers)

<br/>

> **TextileCalc** is a production-grade, zero-dependency Python library engineered for textile professionals, researchers, and students. It covers every computational need in the textile pipeline — from raw fibre to finished fabric, from yarn counting to carbon footprint, from colour matching to cost analysis.

<br/>

---

</div>

## 📋 Table of Contents

- [✨ What's New in v2.0](#-whats-new-in-v20)
- [🗂️ Project Structure](#️-project-structure)
- [⚙️ Installation](#️-installation)
  - [Clone from GitHub](#clone-from-github)
  - [Install as Package](#install-as-package)
- [🚀 Quick Start](#-quick-start)
- [📦 Module Reference](#-module-reference)
  - [Module 1 — AI Yarn Count Recommender](#module-1--ai-yarn-count-recommender-new-in-v20)
  - [Module 2 — Shade Recipe Predictor](#module-2--shade-recipe-predictor-new-in-v20)
  - [Module 3 — Carbon Footprint Calculator](#module-3--carbon-footprint-calculator-new-in-v20)
  - [Module 4 — Yarn Calculations](#module-4--yarn-calculations)
  - [Module 5 — Fabric Calculations](#module-5--fabric-calculations)
  - [Module 6 — Dyeing & Auxiliaries](#module-6--dyeing--auxiliaries)
  - [Module 7 — Costing & Profitability](#module-7--costing--profitability)
  - [Module 8 — Production & Efficiency](#module-8--production--efficiency)
  - [Module 9 — Spinning](#module-9--spinning)
  - [Module 10 — Weaving](#module-10--weaving)
  - [Module 11 — QC & Testing](#module-11--qc--testing)
  - [Module 12 — Wastage & Material Planning](#module-12--wastage--material-planning)
  - [Module 13 — Unit Conversion](#module-13--unit-conversion)
- [🧪 Running the Demo](#-running-the-demo)
- [📊 API Reference Summary](#-api-reference-summary)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ What's New in v2.0

TextileCalc v2.0 introduces three groundbreaking engineering modules while maintaining **100% backward compatibility** with v1.x.

| Feature | v1.x | v2.0 |
|---|---|---|
| Yarn count conversion | ✅ | ✅ |
| Fabric & dyeing calculations | ✅ | ✅ |
| Costing, QC, production tools | ✅ | ✅ |
| **AI Yarn Count Recommender** | ❌ | 🆕 ✅ |
| **Shade Recipe Predictor** | ❌ | 🆕 ✅ |
| **Carbon Footprint Calculator** | ❌ | 🆕 ✅ |
| Zero external dependencies | ✅ | ✅ |

---

## 🗂️ Project Structure

```
TextileCalc/
│
├── textilecalc/                  # Core library package
│   ├── __init__.py               # Public API — all exports live here
│   │
│   ├── yarn_recommender.py       # ✦ AI Yarn Count Recommender (NEW v2.0)
│   ├── shade_recipe.py           # ✦ Shade Recipe Predictor (NEW v2.0)
│   ├── carbon_footprint.py       # ✦ Carbon Footprint Calculator (NEW v2.0)
│   │
│   ├── yarn.py                   # Yarn count conversions & CSP
│   ├── fabric.py                 # GSM, cover factor, shrinkage
│   ├── dyeing.py                 # Dye, liquor, salt, soda ash calculations
│   ├── dyeing_advanced.py        # Advanced dyeing formulations
│   ├── costing.py                # Yarn cost, profit price, break-even
│   ├── costing_advanced.py       # Advanced cost modelling
│   ├── production.py             # Efficiency, rate, machine utilisation
│   ├── wastage.py                # Wastage % and material planning
│   ├── spinning.py               # TPI, TPM, IPI, draft ratio
│   ├── weaving.py                # Loom efficiency, break rate, production
│   ├── qc.py                     # Moisture, shrinkage, absorbency, pilling
│   ├── testing.py                # Tensile strength, colour fastness
│   └── unit_conv.py              # Weight, length, temperature conversions
│
├── utils/
│   ├── __init__.py
│   └── validator.py              # Input validation helpers
│
├── main.py                       # Full demo & test script
├── setup.py                      # Package metadata
└── LICENSE                       # MIT License
```

---

## ⚙️ Installation

### Clone from GitHub

The recommended way to get started is by cloning the repository directly:

```bash
# 1. Clone the repository
git clone https://github.com/malekahmedshahin-byte/TextileCalc.git

# 2. Navigate into the project directory
cd TextileCalc

# 3. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 4. No dependencies to install — TextileCalc is pure Python!
#    You can start using it immediately:
python main.py
```

> ✅ **Zero dependencies.** TextileCalc runs on **pure Python 3.7+** — no pip install required for core functionality.

### Install as Package

If you prefer to install TextileCalc as a package directly into your Python environment:

```bash
# Clone first
git clone https://github.com/malekahmedshahin-byte/TextileCalc.git
cd TextileCalc

# Install in editable/development mode
pip install -e .

# Or install normally
pip install .
```

After installation, import from anywhere:

```python
import textilecalc
from textilecalc import recommend_yarn_count, calculate_carbon_footprint
```

---

## 🚀 Quick Start

After cloning, you can immediately start computing with a few lines:

```python
import sys, os
sys.path.insert(0, "path/to/TextileCalc")   # skip if installed via pip

from textilecalc import (
    # v2.0 AI modules
    recommend_yarn_count,
    predict_shade_recipe,
    calculate_carbon_footprint,
    # v1.x core
    ne_to_tex, gsm, dye_required, yarn_cost,
)

# ── Get a yarn recommendation ──────────────────────────────────────────────
rec = recommend_yarn_count(
    target_gsm=200,
    end_use="trouser",
    fiber_type="polyester",
    loom_type="rapier",
    width_inch=63
)
print(f"Recommended Ne  : {rec['recommended_ne']}")
print(f"EPI × PPI       : {rec['recommended_epi']} × {rec['recommended_ppi']}")
print(f"Confidence      : {rec['confidence_score']}%")

# ── Predict a dye recipe ────────────────────────────────────────────────────
recipe = predict_shade_recipe(
    color_input="#1B3A6B",          # navy blue (hex)
    fabric_weight_g=2000,
    fiber_type="cotton",
    mlr=10
)
print(f"\nShade           : {recipe['shade_description']}")
print(f"Dye class       : {recipe['dye_class']}")
print(f"Recipe (% owf)  : {recipe['recipe_percent']}")

# ── Calculate carbon footprint ─────────────────────────────────────────────
cf = calculate_carbon_footprint(
    fiber_type="cotton",
    fabric_weight_kg=500,
    spinning_method="ring",
    fabric_formation="weaving_rapier",
    dyeing_process="reactive_exhaust",
    finishing="softener_only",
    country="bangladesh",
    transport_mode="sea_freight",
    transport_distance_km=12000,
)
print(f"\nTotal CO₂e      : {cf['total_co2e_kg_per_kg']} kg per kg fabric")
print(f"Rating          : {cf['sustainability_rating']}")

# ── Classic core calculations ──────────────────────────────────────────────
print(f"\nNe 30 → Tex     : {ne_to_tex(30):.3f}")
print(f"GSM (50g,0.5²)  : {gsm(50, 0.5, 0.5)} g/m²")
print(f"Dye for 1kg@2%  : {dye_required(1000, 2)} g")
print(f"Yarn cost       : ${yarn_cost(100, 3.5)}")
```

**Expected output:**
```
Recommended Ne  : 32
EPI × PPI       : 72 × 60
Confidence      : 87%

Shade           : Deep Navy Blue
Dye class       : Reactive
Recipe (% owf)  : {'Navy Blue HE-R': 3.2, 'Turquoise HE-B': 0.4}

Total CO₂e      : 18.6 kg per kg fabric
Rating          : C

Ne 30 → Tex     : 19.683
GSM (50g,0.5²)  : 200.0 g/m²
Dye for 1kg@2%  : 20.0 g
Yarn cost       : $350.0
```

---

## 📦 Module Reference

---

### Module 1 — AI Yarn Count Recommender *(New in v2.0)*

> **File:** `textilecalc/yarn_recommender.py`

The Yarn Count Recommender is the flagship feature of v2.0. Given a target GSM, end-use, fibre type, loom, and width, it intelligently recommends the optimal yarn count (Ne), weave structure, thread density, and estimated cover factor — complete with confidence scoring and engineering warnings.

#### Functions

| Function | Description |
|---|---|
| `recommend_yarn_count(target_gsm, end_use, fiber_type, loom_type, width_inch)` | Full yarn specification recommendation |
| `compare_yarn_options(target_gsm, end_use, fiber_list, loom_type, width_inch)` | Side-by-side comparison across multiple fibres |
| `list_end_uses()` | Discover all supported end-use profiles with GSM/Ne ranges |
| `list_fiber_types()` | List all supported fibre types |

#### Usage

```python
from textilecalc import recommend_yarn_count, compare_yarn_options, list_end_uses

# ── Single recommendation ──────────────────────────────────────────────────
rec = recommend_yarn_count(
    target_gsm=340,
    end_use="denim",
    fiber_type="cotton",
    loom_type="shuttle",
    width_inch=58
)
print(f"Ne              : {rec['recommended_ne']}")
print(f"EPI × PPI       : {rec['recommended_epi']} × {rec['recommended_ppi']}")
print(f"Weave           : {rec['weave_structure']}")
print(f"Est. GSM        : {rec['estimated_gsm']} g/m²")
print(f"Cover Factor    : {rec['cover_factor']}")
print(f"Total Ends      : {rec['total_ends']:,}")
print(f"Confidence      : {rec['confidence_score']}%")

# ── Fibre comparison for bedsheet fabric (140 GSM, 90" wide) ───────────────
comps = compare_yarn_options(
    target_gsm=140,
    end_use="bedsheet",
    fiber_list=["cotton", "modal", "tencel"],
    loom_type="rapier",
    width_inch=90
)
for c in comps:
    print(f"{c['fiber']:12} Ne:{c['recommended_ne']:>4}  "
          f"EPI:{c['recommended_epi']:>4}  GSM:{c['estimated_gsm']:>6}  "
          f"Confidence:{c['confidence_score']:>3}%")
```

**Sample Output:**
```
Ne              : 10
EPI × PPI       : 64 × 44
Weave           : 3/1 Twill
Est. GSM        : 338 g/m²
Cover Factor    : 16.84
Total Ends      : 3,712
Confidence      : 91%

cotton       Ne:  40  EPI: 108  GSM: 141.2  Confidence: 94%
modal        Ne:  45  EPI: 112  GSM: 139.8  Confidence: 89%
tencel       Ne:  45  EPI: 110  GSM: 140.5  Confidence: 91%
```

#### Supported End-Uses

| End-Use | GSM Range | Ne Range | Description |
|---|---|---|---|
| `shirting` | 90–140 g/m² | Ne 60–100 | Dress & casual shirts |
| `trouser` | 160–240 g/m² | Ne 20–40 | Trousers & slacks |
| `denim` | 300–400 g/m² | Ne 7–14 | Denim jeans & jackets |
| `bedsheet` | 120–160 g/m² | Ne 40–60 | Home textiles |
| `voile` | 40–70 g/m² | Ne 80–120 | Lightweight sheers |
| `canvas` | 350–600 g/m² | Ne 4–10 | Industrial & upholstery |
| `towel` | 300–600 g/m² | Ne 10–20 | Terry & bath towels |

---

### Module 2 — Shade Recipe Predictor *(New in v2.0)*

> **File:** `textilecalc/shade_recipe.py`

Given a target colour (as hex `#RRGGBB` or CIE L\*a\*b\* values), the Shade Recipe Predictor selects the correct dye class, formulates a complete dye recipe (% owf and grams), recommends auxiliaries, and estimates ΔE\* colour accuracy. A built-in QC comparison tool validates produced shades against targets.

#### Functions

| Function | Description |
|---|---|
| `predict_shade_recipe(color_input, fabric_weight_g, fiber_type, mlr, input_format)` | Generate a complete dye recipe |
| `compare_shade_accuracy(produced_hex, target_hex)` | Colour QC: ΔE\*, ΔL\*, Δa\*, Δb\* analysis |
| `hex_to_rgb(hex_str)` | Convert `#RRGGBB` → `(R, G, B)` |
| `rgb_to_hex(r, g, b)` | Convert `(R, G, B)` → `#RRGGBB` |
| `rgb_to_lab(r, g, b)` | Convert RGB → CIE L\*a\*b\* |
| `lab_to_rgb(L, a, b)` | Convert CIE L\*a\*b\* → RGB |
| `delta_e(lab1, lab2)` | Calculate CIE ΔE\* between two colours |
| `list_dye_classes()` | Discover all supported dye classes |

#### Usage

```python
from textilecalc import predict_shade_recipe, compare_shade_accuracy

# ── Navy blue on cotton (2 kg fabric, MLR 1:10) ────────────────────────────
recipe = predict_shade_recipe(
    color_input="#1B3A6B",
    fabric_weight_g=2000,
    fiber_type="cotton",
    mlr=10
)
print(f"Shade           : {recipe['shade_description']}")
print(f"Dye Class       : {recipe['dye_class']}")
print(f"ΔE* Accuracy    : {recipe['delta_e_estimate']}")
print(f"Fixation Rate   : {recipe['fixation_rate_%']}%")
print(f"Liquor Volume   : {recipe['liquor_volume_L']} L")
print(f"\nRecipe (% owf):")
for dye, pct in recipe['recipe_percent'].items():
    print(f"  {dye:<25}: {pct}%")
print(f"\nAuxiliaries (grams):")
for chem, grams in recipe['auxiliaries_g'].items():
    print(f"  {chem:<30}: {grams} g")

# ── Shade QC — produced vs. target ────────────────────────────────────────
qc = compare_shade_accuracy(produced_hex="#1C3B6C", target_hex="#1B3A6B")
print(f"\nΔE*             : {qc['delta_e']}")
print(f"Verdict         : {qc['verdict']}")
print(f"Recommendation  : {qc['recommendation']}")

# ── Input via L*a*b* values ────────────────────────────────────────────────
recipe_lab = predict_shade_recipe(
    color_input=(30.0, 15.0, -40.0),
    fabric_weight_g=3000,
    fiber_type="cotton",
    input_format="lab",
    mlr=12
)
print(f"\nHex equivalent  : {recipe_lab['color_hex']}")
```

**Sample Output:**
```
Shade           : Deep Navy Blue
Dye Class       : Reactive (Vinyl Sulphone)
ΔE* Accuracy    : 1.8
Fixation Rate   : 75%
Liquor Volume   : 20.0 L

Recipe (% owf):
  Navy Blue HE-R          : 3.2%
  Turquoise HE-B          : 0.4%
  Black B                 : 0.6%

Auxiliaries (grams):
  Common Salt (NaCl)        : 2400 g
  Soda Ash (Na₂CO₃)         : 400 g
  Wetting Agent             : 4 g

ΔE*             : 1.2
Verdict         : Pass — Acceptable shade match
Recommendation  : Minor adjustment — reduce depth slightly

Hex equivalent  : #1A3575
```

#### Supported Fibre–Dye Class Mapping

| Fibre | Dye Class | Typical Fixation |
|---|---|---|
| Cotton, Viscose, Modal | Reactive | 70–80% |
| Wool, Nylon | Acid | 85–95% |
| Polyester | Disperse | 90–98% |
| Silk | Reactive / Acid | 75–90% |
| Acrylic | Basic (Cationic) | 95–99% |

---

### Module 3 — Carbon Footprint Calculator *(New in v2.0)*

> **File:** `textilecalc/carbon_footprint.py`

A full lifecycle assessment (LCA) tool that calculates the cradle-to-gate carbon footprint of fabric production. It accounts for fibre cultivation, spinning, fabric formation, dyeing, finishing, and transport — returning CO₂e per kg, water footprint, sustainability rating, and actionable reduction tips.

#### Functions

| Function | Description |
|---|---|
| `calculate_carbon_footprint(fiber_type, fabric_weight_kg, spinning_method, fabric_formation, dyeing_process, finishing, country, transport_mode, transport_distance_km)` | Full lifecycle CO₂e calculation |
| `compare_fiber_footprints(weight_kg)` | Compare CO₂e across all supported fibres |
| `carbon_offset_cost(co2e_kg, price_per_tonne_usd)` | Calculate carbon credit offset cost |
| `list_fiber_types_carbon()` | List all fibres with emission factors |
| `list_dyeing_processes_carbon()` | List all dyeing processes with emission data |
| `list_fabric_formations()` | List supported fabric formation methods |
| `list_finishing_processes()` | List finishing processes |
| `list_countries_carbon()` | List country-specific grid emission factors |

#### Usage

```python
from textilecalc import (
    calculate_carbon_footprint,
    compare_fiber_footprints,
    carbon_offset_cost,
)

# ── Conventional cotton reactive-dyed fabric ────────────────────────────────
cf = calculate_carbon_footprint(
    fiber_type="cotton",
    fabric_weight_kg=500,
    spinning_method="ring",
    fabric_formation="weaving_rapier",
    dyeing_process="reactive_exhaust",
    finishing="softener_only",
    country="bangladesh",
    transport_mode="sea_freight",
    transport_distance_km=12000,
)
print(f"Total CO₂e      : {cf['total_co2e_kg_per_kg']} kg/kg fabric")
print(f"Total batch     : {cf['total_co2e_kg']} kg CO₂e")
print(f"Water footprint : {cf['water_footprint_L']:,} L")
print(f"Rating          : {cf['sustainability_rating']} — {cf['rating_description']}")
print(f"\nStage breakdown (kg CO₂e per kg fabric):")
for stage, val in cf['breakdown_kg_per_kg'].items():
    bar = "█" * int(val * 4)
    print(f"  {stage:<45}: {val:>6}  {bar}")
print(f"\nReduction tips:")
for tip in cf['reduction_tips']:
    print(f"  → {tip}")

# ── Sustainable alternative: TENCEL pigment-dyed knit ─────────────────────
cf_green = calculate_carbon_footprint(
    fiber_type="tencel",
    fabric_weight_kg=500,
    spinning_method="open_end",
    fabric_formation="knitting_circular",
    dyeing_process="pigment_padding",
    finishing="none",
    country="eu_average",
    transport_mode="rail",
    transport_distance_km=2000,
)
print(f"\nGreen CO₂e      : {cf_green['total_co2e_kg_per_kg']} kg/kg")
print(f"Rating          : {cf_green['sustainability_rating']} — {cf_green['rating_description']}")

# ── Fibre comparison table ─────────────────────────────────────────────────
fibres = compare_fiber_footprints(1000)
print(f"\n{'Fibre':<22} {'CO₂e/kg':>9} {'Water L/kg':>12} {'Rating':>8}")
print("-" * 55)
for f in fibres:
    print(f"{f['fiber']:<22} {f['co2e_kg_per_kg']:>9.2f} "
          f"{f['water_L_per_kg']:>12,} {f['fiber_stage_rating']:>8}")

# ── Carbon offset cost ─────────────────────────────────────────────────────
offset = carbon_offset_cost(cf['total_co2e_kg'], price_per_tonne_usd=20)
print(f"\nOffset cost     : ${offset['offset_cost_usd']} USD")
```

**Sample Output:**
```
Total CO₂e      : 18.6 kg/kg fabric
Total batch     : 9,300 kg CO₂e
Water footprint : 7,500,000 L
Rating          : C — Moderate — above industry average

Stage breakdown (kg CO₂e per kg fabric):
  Fibre cultivation & processing           :   5.90  ████████████████████████
  Spinning                                 :   2.10  ████████
  Fabric formation                         :   1.80  ███████
  Dyeing & wet processing                  :   5.40  █████████████████████
  Finishing                                :   0.80  ███
  Transport                                :   2.60  ██████████

Reduction tips:
  → Switch to organic cotton to reduce fibre CO₂e by ~30%
  → Use cold-pad dyeing to cut wet processing energy by ~40%
  → Shift to sea freight or rail for transport leg

Fibre            CO₂e/kg   Water L/kg   Rating
-------------------------------------------------------
Recycled PET         1.20          50        A+
Tencel/Lyocell       2.10         200        A+
Hemp                 2.30         300        A+
Linen/Flax           2.70         500        A
Organic Cotton       4.50       5,000        B
Cotton               5.90      10,000        C
Wool                 7.20       8,000        C
Polyester            3.80          50        B
Nylon                7.60          70        D
```

---

### Module 4 — Yarn Calculations

> **File:** `textilecalc/yarn.py`

| Function | Args | Returns | Description |
|---|---|---|---|
| `ne_to_tex(ne)` | `ne: float` | `float` | Ne → Tex |
| `tex_to_ne(tex)` | `tex: float` | `float` | Tex → Ne |
| `tex_to_denier(tex)` | `tex: float` | `float` | Tex → Denier |
| `denier_to_tex(denier)` | `denier: float` | `float` | Denier → Tex |
| `ne_to_denier(ne)` | `ne: float` | `float` | Ne → Denier directly |
| `cv_percentage(sd, mean)` | `sd, mean: float` | `float` | Yarn unevenness CV% |
| `csp(count, strength)` | `count, strength: float` | `float` | Count Strength Product |

```python
from textilecalc import ne_to_tex, tex_to_ne, ne_to_denier, cv_percentage, csp

print(ne_to_tex(30))       # → 19.683
print(tex_to_ne(20))       # → 29.525
print(ne_to_denier(30))    # → 177.15
print(cv_percentage(1.5, 30))  # → 5.0  (CV% — evenness)
print(csp(30, 80))         # → 2400  (quality index)
```

---

### Module 5 — Fabric Calculations

> **File:** `textilecalc/fabric.py`

| Function | Args | Returns | Description |
|---|---|---|---|
| `gsm(weight_g, length_m, width_m)` | floats | `float` | Calculate fabric GSM |
| `fabric_weight(gsm_val, width_m, length_m)` | floats | `float` | Total weight from GSM |
| `warp_cover_factor(epi, count_ne)` | floats | `float` | Warp cover factor |
| `weft_cover_factor(ppi, count_ne)` | floats | `float` | Weft cover factor |
| `cover_factor(epi, ppi, count_ne)` | floats | `float` | Total cover factor (Peirce) |
| `shrinkage_percent(original, final)` | floats | `float` | Dimensional shrinkage |

```python
from textilecalc import gsm, cover_factor, shrinkage_percent

print(gsm(50, 0.5, 0.5))           # → 200.0 g/m²
print(cover_factor(60, 50, 40))    # → 14.152 (Peirce's formula)
print(shrinkage_percent(100, 96))  # → 4.0%
```

---

### Module 6 — Dyeing & Auxiliaries

> **Files:** `textilecalc/dyeing.py` · `textilecalc/dyeing_advanced.py`

| Function | Args | Returns | Description |
|---|---|---|---|
| `dye_required(fabric_weight, shade_percent)` | floats | `float` | Dye in grams |
| `liquor_required(material_weight, mlr)` | floats | `float` | Liquor volume in litres |
| `chemical_required(material_weight, percent)` | floats | `float` | Chemical in grams (owf) |
| `salt_required(fabric_weight, shade_percent)` | floats | `float` | Salt (g/L) for reactive dyeing |
| `soda_ash_required(material_weight, percent=20)` | floats | `float` | Soda ash in grams |

```python
from textilecalc import dye_required, liquor_required, salt_required

print(dye_required(1000, 2))     # → 20.0 g  (1kg fabric at 2% shade)
print(liquor_required(5, 10))    # → 50.0 L  (5kg material, MLR 1:10)
print(salt_required(10, 2))      # → 60 g/L  (medium shade)
```

---

### Module 7 — Costing & Profitability

> **Files:** `textilecalc/costing.py` · `textilecalc/costing_advanced.py`

| Function | Args | Returns | Description |
|---|---|---|---|
| `yarn_cost(weight, rate)` | floats | `float` | Total yarn cost |
| `process_cost(material_cost, labor_cost, overhead)` | floats | `float` | Full process cost |
| `profit_price(total_cost, profit_percent)` | floats | `float` | Selling price incl. profit |
| `break_even_units(fixed_cost, selling_price_per_unit, variable_cost_per_unit)` | floats | `float` | Break-even units |

```python
from textilecalc import yarn_cost, profit_price, break_even_units

print(yarn_cost(100, 3.5))               # → $350.0
print(profit_price(1000, 20))            # → $1200.0
print(break_even_units(10000, 50, 30))   # → 500 units
```

---

### Module 8 — Production & Efficiency

> **File:** `textilecalc/production.py`

| Function | Args | Returns | Description |
|---|---|---|---|
| `efficiency(actual, target)` | floats | `float` | Production efficiency % |
| `production_rate(output, hours)` | floats | `float` | Output per hour |
| `machine_utilization(run_time, available_time)` | floats | `float` | Machine utilisation % |
| `daily_production_target(shift_hours, efficiency_percent, machine_speed, count_ne)` | floats | `float` | Daily yield estimate |

```python
from textilecalc import efficiency, production_rate, machine_utilization

print(efficiency(900, 1000))           # → 90.0%
print(production_rate(500, 8))         # → 62.5 kg/hr
print(machine_utilization(7, 8))       # → 87.5%
```

---

### Module 9 — Spinning

> **File:** `textilecalc/spinning.py`

| Function | Args | Returns | Description |
|---|---|---|---|
| `yarn_twist_tpi(twist, length_inches)` | floats | `float` | Twist Per Inch (TPI) |
| `yarn_tpm(tpi)` | `float` | `float` | TPI → Twist Per Meter |
| `yarn_imperfection(u_percent, thin, thick, neps)` | floats | `float` | Imperfection Index (IPI) |
| `spinning_efficiency(actual_output, theoretical_output)` | floats | `float` | Spinning efficiency % |
| `draft(feed_count, delivery_count)` | floats | `float` | Draft ratio |

```python
from textilecalc import yarn_twist_tpi, yarn_tpm, spinning_efficiency

print(yarn_twist_tpi(200, 10))         # → 20.0 TPI
print(yarn_tpm(20))                    # → 787.4 TPM
print(spinning_efficiency(80, 100))    # → 80.0%
```

---

### Module 10 — Weaving

> **File:** `textilecalc/weaving.py`

| Function | Args | Returns | Description |
|---|---|---|---|
| `loom_efficiency(actual, ideal)` | floats | `float` | Loom efficiency % |
| `warp_break_rate(breaks, total_ends)` | floats | `float` | Warp break rate % |
| `weft_break_rate(breaks, picks)` | floats | `float` | Weft break rate % |
| `fabric_defect_rate(defects, total_length)` | floats | `float` | Defects per metre |
| `production_per_loom(rpm, efficiency_percent, epi, width_inch)` | floats | `float` | Metres/hour per loom |

```python
from textilecalc import loom_efficiency, production_per_loom

print(loom_efficiency(850, 1000))                # → 85.0%
print(production_per_loom(600, 85, 60, 60))     # → ~51 m/hr
```

---

### Module 11 — QC & Testing

> **Files:** `textilecalc/qc.py` · `textilecalc/testing.py`

| Function | Args | Returns | Description |
|---|---|---|---|
| `moisture_regain(original_weight, dry_weight)` | floats | `float` | Moisture regain % |
| `moisture_content(original_weight, dry_weight)` | floats | `float` | Moisture content % |
| `absorbency_rate(water_absorbed, dry_weight)` | floats | `float` | Absorbency % |
| `pilling_resistance_grade(pilling_score)` | `1–5` | `str` | ISO pilling grade |
| `tensile_strength(force, area)` | floats | `float` | N/mm² tensile strength |
| `color_fastness_grade(score)` | `1–5` | `str` | Colour fastness grade |

```python
from textilecalc import moisture_regain, pilling_resistance_grade, color_fastness_grade

print(moisture_regain(110, 100))           # → 10.0%
print(pilling_resistance_grade(4))         # → 'Good — Slight pilling'
print(color_fastness_grade(4))             # → 'Good'
```

---

### Module 12 — Wastage & Material Planning

> **File:** `textilecalc/wastage.py`

| Function | Args | Returns | Description |
|---|---|---|---|
| `wastage_percentage(input_weight, output_weight)` | floats | `float` | Wastage % |
| `material_required_with_wastage(required_output, wastage_percent)` | floats | `float` | Raw input needed |

```python
from textilecalc import wastage_percentage, material_required_with_wastage

print(wastage_percentage(100, 92))                      # → 8.0%
print(material_required_with_wastage(950, 5))           # → 1000.0 kg
```

---

### Module 13 — Unit Conversion

> **File:** `textilecalc/unit_conv.py`

| Function | Conversion |
|---|---|
| `kg_to_lbs(kg)` / `lbs_to_kg(lbs)` | Weight |
| `inch_to_meter(inch)` / `meter_to_inch(meter)` | Length |
| `cm_to_inch(cm)` / `inch_to_cm(inch)` | Length |
| `gsm_to_oz_yd2(gsm)` / `oz_yd2_to_gsm(oz)` | Fabric weight |
| `ne_to_nm(ne)` / `nm_to_ne(nm)` | Yarn count |
| `celsius_to_fahrenheit(c)` / `fahrenheit_to_celsius(f)` | Temperature |

```python
from textilecalc import kg_to_lbs, gsm_to_oz_yd2, ne_to_nm, celsius_to_fahrenheit

print(kg_to_lbs(50))               # → 110.231 lbs
print(gsm_to_oz_yd2(200))          # → 5.898 oz/yd²
print(ne_to_nm(30))                # → 50.79 Nm
print(celsius_to_fahrenheit(160))  # → 320.0 °F (typical dyeing temperature)
```

---

## 🧪 Running the Demo

The `main.py` file is a comprehensive end-to-end demonstration of every module in TextileCalc — all three v2.0 AI modules and all v1.x core modules.

```bash
# From the project root:
python main.py
```

The demo will run through:

1. **AI Yarn Count Recommender** — polyester trouser, cotton denim, silk voile, multi-fibre bedsheet comparison
2. **Shade Recipe Predictor** — navy blue reactive, burgundy acid, mint disperse, Lab\* input, QC comparison
3. **Carbon Footprint Calculator** — conventional cotton, sustainable TENCEL alternative, wool luxury suiting, fibre comparison table
4. **Core v1.x Modules** — yarn conversions, fabric, dyeing, costing, production, testing, weaving, spinning

Expected runtime: **< 1 second** (no network calls, zero dependencies).

---

## 📊 API Reference Summary

```
textilecalc v2.0 — Function Index
═══════════════════════════════════════════════════════════════════
Module                          Key Functions
───────────────────────────────────────────────────────────────────
yarn_recommender (v2.0)         recommend_yarn_count
                                compare_yarn_options
                                list_end_uses / list_fiber_types

shade_recipe (v2.0)             predict_shade_recipe
                                compare_shade_accuracy
                                hex_to_rgb, rgb_to_lab, delta_e
                                list_dye_classes

carbon_footprint (v2.0)         calculate_carbon_footprint
                                compare_fiber_footprints
                                carbon_offset_cost
                                list_* discovery helpers

yarn                            ne_to_tex, tex_to_ne
                                ne_to_denier, tex_to_denier
                                cv_percentage, csp

fabric                          gsm, fabric_weight
                                cover_factor, warp/weft_cover_factor
                                shrinkage_percent

dyeing                          dye_required, liquor_required
                                chemical_required, salt_required
                                soda_ash_required

costing                         yarn_cost, process_cost
                                profit_price, break_even_units

production                      efficiency, production_rate
                                machine_utilization
                                daily_production_target

spinning                        yarn_twist_tpi, yarn_tpm
                                yarn_imperfection, draft
                                spinning_efficiency

weaving                         loom_efficiency, warp_break_rate
                                weft_break_rate, fabric_defect_rate
                                production_per_loom

qc / testing                    moisture_regain, moisture_content
                                absorbency_rate, shrinkage_percent
                                pilling_resistance_grade
                                tensile_strength, color_fastness_grade

wastage                         wastage_percentage
                                material_required_with_wastage

unit_conv                       kg_to_lbs, lbs_to_kg
                                inch_to_meter, gsm_to_oz_yd2
                                ne_to_nm, celsius_to_fahrenheit
═══════════════════════════════════════════════════════════════════
Zero external dependencies — Pure Python 3.7+
```

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are warmly welcome!

```bash
# 1. Fork the repository on GitHub
#    https://github.com/malekahmedshahin-byte/TextileCalc

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/TextileCalc.git
cd TextileCalc

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Make your changes and commit
git add .
git commit -m "feat: add your feature description"

# 5. Push to your fork
git push origin feature/your-feature-name

# 6. Open a Pull Request on GitHub
```

### Contribution Guidelines

- Follow the existing docstring style (Args / Returns / Example)
- Add input validation via `utils/validator.py` for all numeric inputs
- Keep the zero-dependency constraint — pure Python only
- Add your function to `textilecalc/__init__.py` exports
- Test your function in `main.py` before submitting

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full terms.

```
MIT License
Copyright (c) 2026 malekahmedshahin-byte
```

---

<div align="center">

Made with ❤️ for the global textile engineering community

**[⭐ Star this repo](https://github.com/malekahmedshahin-byte/TextileCalc)** · **[🐛 Report a Bug](https://github.com/malekahmedshahin-byte/TextileCalc/issues)** · **[💡 Request a Feature](https://github.com/malekahmedshahin-byte/TextileCalc/issues)**

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-malekahmedshahin--byte-181717?style=for-the-badge&logo=github)](https://github.com/malekahmedshahin-byte)

</div>
