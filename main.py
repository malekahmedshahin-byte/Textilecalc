"""
textilecalc v2.0 — Full Demo & Test Script
Author: Abdul Malek
===========================================
Run:  python main.py
"""

# fmt: off
print(r"""
 ████████╗███████╗██╗  ██╗████████╗██╗██╗     ███████╗
    ██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝██║██║     ██╔════╝
    ██║   █████╗   ╚███╔╝    ██║   ██║██║     █████╗
    ██║   ██╔══╝   ██╔██╗    ██║   ██║██║     ██╔══╝
    ██║   ███████╗██╔╝ ██╗   ██║   ██║███████╗███████╗
    ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝

  ██████╗ █████╗ ██╗      ██████╗
 ██╔════╝██╔══██╗██║     ██╔════╝
 ██║     ███████║██║     ██║
 ██╚═══╝ ██╔══██║██║     ██║
  ██████╗ ██║  ██║███████╗╚██████╗
  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝

  v2.0  |  Author: Abdul Malek  |  Pure Python 3.7+
  16 Modules  |  60+ Functions  |  Zero Dependencies
""")
# fmt: on

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from textilecalc import (
    # ── v2.0 new modules ──────────────────────────────────────────
    recommend_yarn_count,
    compare_yarn_options,
    list_end_uses,
    list_fiber_types,
    predict_shade_recipe,
    compare_shade_accuracy,
    hex_to_rgb, rgb_to_hex, rgb_to_lab, lab_to_rgb, delta_e,
    list_dye_classes,
    calculate_carbon_footprint,
    compare_fiber_footprints,
    carbon_offset_cost,
    list_fiber_types_carbon,
    list_dyeing_processes_carbon,
    list_fabric_formations,
    list_finishing_processes,
    list_countries_carbon,
    # ── v1.1 yarn module ──────────────────────────────────────────
    ne_to_tex, tex_to_ne, tex_to_denier, denier_to_tex, ne_to_denier,
    cv_percentage, csp,
    # ── v1.1 fabric module ────────────────────────────────────────
    gsm, fabric_weight, warp_cover_factor, weft_cover_factor,
    cover_factor, shrinkage_percent,
    # ── v1.1 dyeing module ────────────────────────────────────────
    dye_required, liquor_required, chemical_required,
    salt_required, soda_ash_required,
    # ── v1.1 dyeing advanced module ───────────────────────────────
    dye_exhaustion, dye_fixation, liquor_ratio,
    chemical_utilization, wash_fastness_efficiency,
    # ── v1.1 costing module ───────────────────────────────────────
    yarn_cost, process_cost, profit_price, break_even_units,
    # ── v1.1 costing advanced module ─────────────────────────────
    cost_per_meter, energy_cost, depreciation,
    profit_margin, total_manufacturing_cost,
    # ── v1.1 production module ────────────────────────────────────
    efficiency, production_rate, machine_utilization,
    daily_production_target,
    # ── v1.1 wastage module ───────────────────────────────────────
    wastage_percentage, material_required_with_wastage,
    # ── v1.1 unit conversion module ───────────────────────────────
    kg_to_lbs, lbs_to_kg, inch_to_meter, meter_to_inch,
    cm_to_inch, inch_to_cm, gsm_to_oz_yd2, oz_yd2_to_gsm,
    ne_to_nm, nm_to_ne, celsius_to_fahrenheit, fahrenheit_to_celsius,
    # ── v1.1 quality control module ───────────────────────────────
    moisture_regain, moisture_content, absorbency_rate,
    pilling_resistance_grade,
    # ── v1.1 spinning module ──────────────────────────────────────
    yarn_twist_tpi, yarn_tpm, yarn_imperfection,
    spinning_efficiency, draft,
    # ── v1.1 weaving module ───────────────────────────────────────
    loom_efficiency, warp_break_rate, weft_break_rate,
    fabric_defect_rate, production_per_loom,
    # ── v1.1 testing module ───────────────────────────────────────
    tensile_strength, elongation_percent, bursting_strength,
    abrasion_index, stiffness_index, color_fastness_grade,
)


SEP  = "=" * 65
SEP2 = "-" * 65


def section(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)


def sub(title):
    print(f"\n{SEP2}")
    print(f"  {title}")
    print(SEP2)


# ═══════════════════════════════════════════════════════════════════
# 1. AI YARN COUNT RECOMMENDER
# ═══════════════════════════════════════════════════════════════════

section("MODULE 1 — AI YARN COUNT RECOMMENDER  (NEW in v2.0)")

sub("Example A: Men's trouser fabric (polyester, rapier loom, 63\" width)")
rec = recommend_yarn_count(
    target_gsm=200,
    end_use="trouser",
    fiber_type="polyester",
    loom_type="rapier",
    width_inch=63
)
print(f"  Recommended Ne       : {rec['recommended_ne']}")
print(f"  EPI × PPI            : {rec['recommended_epi']} × {rec['recommended_ppi']}")
print(f"  Weave structure      : {rec['weave_structure']}")
print(f"  Estimated GSM        : {rec['estimated_gsm']} g/m²")
print(f"  Cover factor         : {rec['cover_factor']}")
print(f"  Total warp ends      : {rec['total_ends']:,}")
print(f"  Confidence score     : {rec['confidence_score']}%")
print(f"  Weave strength/drape : {rec['weave_properties']['strength']} / {rec['weave_properties']['drape']}")
print(f"  Fiber note           : {rec['fiber_note']}")
print(f"  End-use profile      : {rec['end_use_profile']}")
if rec["warnings"]:
    for w in rec["warnings"]:
        print(f"  ⚠  {w}")

sub("Example B: Denim fabric (cotton, shuttle loom, 58\" width)")
rec2 = recommend_yarn_count(340, "denim", "cotton", "shuttle", 58)
print(f"  Recommended Ne       : {rec2['recommended_ne']}")
print(f"  EPI × PPI            : {rec2['recommended_epi']} × {rec2['recommended_ppi']}")
print(f"  Weave structure      : {rec2['weave_structure']}")
print(f"  Estimated GSM        : {rec2['estimated_gsm']} g/m²")
print(f"  Cover factor         : {rec2['cover_factor']}")
print(f"  Confidence score     : {rec2['confidence_score']}%")

sub("Example C: Silk voile (silk, air-jet loom, 54\" width)")
rec3 = recommend_yarn_count(55, "voile", "silk", "airjet", 54)
print(f"  Recommended Ne       : {rec3['recommended_ne']}")
print(f"  EPI × PPI            : {rec3['recommended_epi']} × {rec3['recommended_ppi']}")
print(f"  Estimated GSM        : {rec3['estimated_gsm']} g/m²")
print(f"  Cover factor         : {rec3['cover_factor']}")
print(f"  Confidence score     : {rec3['confidence_score']}%")

sub("Example D: Side-by-side fiber comparison for bedsheet (140 GSM)")
comps = compare_yarn_options(140, "bedsheet", ["cotton", "modal", "tencel"], "rapier", 90)
print(f"  {'Fiber':<12} {'Ne':>6} {'EPI':>6} {'PPI':>6} {'GSM_est':>9} {'CF':>8} {'Conf%':>7}")
print(f"  {'-'*12} {'-'*6} {'-'*6} {'-'*6} {'-'*9} {'-'*8} {'-'*7}")
for c in comps:
    print(f"  {c['fiber']:<12} {c['recommended_ne']:>6} {c['recommended_epi']:>6} "
          f"{c['recommended_ppi']:>6} {c['estimated_gsm']:>9} {c['cover_factor']:>8} {c['confidence_score']:>7}")

sub("Available end-uses")
for eu in list_end_uses():
    print(f"  {eu['end_use']:<15} {eu['gsm_range']:<20} {eu['ne_range']:<15} {eu['description']}")

sub("Available fiber types")
for ft in list_fiber_types():
    print(f"  {ft['fiber']:<12} Ne×{ft['ne_multiplier']:.2f}  density×{ft['density_multiplier']:.2f}  {ft['note']}")


# ═══════════════════════════════════════════════════════════════════
# 2. SHADE RECIPE PREDICTOR
# ═══════════════════════════════════════════════════════════════════

section("MODULE 2 — SHADE RECIPE PREDICTOR  (NEW in v2.0)")

sub("Example A: Navy blue on cotton (reactive dye, 2 kg fabric)")
rec_s1 = predict_shade_recipe(
    color_input="#1B3A6B",
    fabric_weight_g=2000,
    fiber_type="cotton",
    mlr=10
)
print(f"  Color hex            : {rec_s1['color_hex']}")
print(f"  Color L*a*b*         : {rec_s1['color_lab']}")
print(f"  Shade description    : {rec_s1['shade_description']}")
print(f"  Dye class            : {rec_s1['dye_class']}")
print(f"  ΔE* accuracy est.    : {rec_s1['delta_e_estimate']}")
print(f"  Fixation rate        : {rec_s1['fixation_rate_%']}%")
print(f"  Liquor volume        : {rec_s1['liquor_volume_L']} L (MLR {rec_s1['mlr']}:1)")
print(f"\n  Recipe (% owf):")
for k, v in rec_s1["recipe_percent"].items():
    print(f"    {k:<20}: {v}%")
print(f"\n  Recipe (grams):")
for k, v in rec_s1["recipe_grams"].items():
    print(f"    {k:<30}: {v} g")
print(f"\n  Auxiliaries:")
for k, v in rec_s1["auxiliaries_g"].items():
    print(f"    {k:<30}: {v} g")
print(f"\n  Process note: {rec_s1['process_note']}")
if rec_s1["warnings"]:
    for w in rec_s1["warnings"]:
        print(f"  ⚠  {w}")

sub("Example B: Burgundy on wool (acid dye, 500 g)")
rec_s2 = predict_shade_recipe(
    color_input="#800020",
    fabric_weight_g=500,
    fiber_type="wool",
    mlr=15
)
print(f"  Color                : {rec_s2['color_hex']}  |  L*a*b* {rec_s2['color_lab']}")
print(f"  Dye class            : {rec_s2['dye_class']}")
print(f"  Shade                : {rec_s2['shade_description']}")
print(f"  Recipe (% owf)       : {rec_s2['recipe_percent']}")
print(f"  Recipe (grams)       : {rec_s2['recipe_grams']}")

sub("Example C: Mint green on polyester (disperse dye, 1 kg)")
rec_s3 = predict_shade_recipe("#A8D8B9", 1000, "polyester", mlr=8)
print(f"  Color                : {rec_s3['color_hex']}")
print(f"  Shade                : {rec_s3['shade_description']}")
print(f"  Recipe (% owf)       : {rec_s3['recipe_percent']}")
print(f"  ΔE* estimate         : {rec_s3['delta_e_estimate']}")
print(f"  Fixation             : {rec_s3['fixation_rate_%']}%")

sub("Example D: Shade QC comparison (produced vs target)")
qc = compare_shade_accuracy("#1C3B6C", "#1B3A6B")
print(f"  Produced hex         : {qc['produced_hex']}")
print(f"  Target hex           : {qc['target_hex']}")
print(f"  ΔE*                  : {qc['delta_e']}")
print(f"  ΔL*                  : {qc['delta_L']}  (+ = too light)")
print(f"  Δa*                  : {qc['delta_a']}  (+ = too red)")
print(f"  Δb*                  : {qc['delta_b']}  (+ = too yellow)")
print(f"  Verdict              : {qc['verdict']}")
print(f"  Recommendation       : {qc['recommendation']}")

sub("Example E: Input via Lab* values")
rec_s4 = predict_shade_recipe(
    color_input=(30.0, 15.0, -40.0),
    fabric_weight_g=3000,
    fiber_type="cotton",
    input_format="lab",
    mlr=12
)
print(f"  Lab* input → hex     : {rec_s4['color_hex']}")
print(f"  Shade                : {rec_s4['shade_description']}")
print(f"  Recipe (% owf)       : {rec_s4['recipe_percent']}")

sub("Example F: Color science utilities — hex ↔ RGB ↔ Lab*")
sample_hex = "#FF6633"
r, g, b = hex_to_rgb(sample_hex)
print(f"  hex_to_rgb('{sample_hex}')  : R={r}, G={g}, B={b}")
reconstructed = rgb_to_hex(r, g, b)
print(f"  rgb_to_hex({r},{g},{b})   : {reconstructed}")
lab = rgb_to_lab(r, g, b)
print(f"  rgb_to_lab(...)            : L*={lab[0]}, a*={lab[1]}, b*={lab[2]}")
back_rgb = lab_to_rgb(*lab)
print(f"  lab_to_rgb(...)            : R={back_rgb[0]}, G={back_rgb[1]}, B={back_rgb[2]}")
de_val = delta_e(lab, rgb_to_lab(255, 102, 51))
print(f"  delta_e(orange vs similar) : ΔE* = {de_val}")

sub("Available dye classes")
for dc in list_dye_classes():
    print(f"  {dc['dye_class']:<12} fix:{dc['typical_fix_rate_%']}%  "
          f"max:{dc['shade_limit_%_owf']}%owf  fibers: {', '.join(dc['compatible_fibers'])}")


# ═══════════════════════════════════════════════════════════════════
# 3. CARBON FOOTPRINT CALCULATOR
# ═══════════════════════════════════════════════════════════════════

section("MODULE 3 — CARBON FOOTPRINT CALCULATOR  (NEW in v2.0)")

sub("Example A: Conventional cotton reactive-dyed fabric (Bangladesh factory)")
cf1 = calculate_carbon_footprint(
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
print(f"  Total CO₂e           : {cf1['total_co2e_kg_per_kg']} kg CO₂e / kg fabric")
print(f"  Total batch CO₂e     : {cf1['total_co2e_kg']} kg CO₂e  ({cf1['fabric_weight_kg']} kg fabric)")
print(f"  Water footprint      : {cf1['water_footprint_L']:,} L  ({cf1['water_footprint_L_per_kg']:,} L/kg)")
print(f"  Sustainability rating: {cf1['sustainability_rating']} — {cf1['rating_description']}")
print(f"\n  Stage breakdown (kg CO₂e per kg):")
for stage, val in cf1["breakdown_kg_per_kg"].items():
    bar = "█" * int(val * 4)
    print(f"    {stage:<45}: {val:>6}  {bar}")
print(f"\n  vs Industry average  : {cf1['comparison']['industry_avg_cotton_reactive']} kg CO₂e/kg")
print(f"  vs Best-in-class     : {cf1['comparison']['best_in_class_estimate']} kg CO₂e/kg")
print(f"  vs Avg (difference)  : {cf1['comparison']['vs_industry_avg_pct']:+.1f}%")
print(f"\n  Reduction tips:")
for tip in cf1["reduction_tips"]:
    print(f"  → {tip}")

sub("Example B: Sustainable alternative — TENCEL, pigment dye, solar EU")
cf2 = calculate_carbon_footprint(
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
print(f"  Total CO₂e           : {cf2['total_co2e_kg_per_kg']} kg CO₂e / kg fabric")
print(f"  Water footprint      : {cf2['water_footprint_L']:,} L")
print(f"  Sustainability rating: {cf2['sustainability_rating']} — {cf2['rating_description']}")
print(f"  vs Cotton reactive   : {cf2['comparison']['vs_industry_avg_pct']:+.1f}%")

sub("Example C: Wool luxury suiting (India factory, air freight)")
cf3 = calculate_carbon_footprint(
    fiber_type="wool",
    fabric_weight_kg=100,
    spinning_method="ring",
    fabric_formation="weaving_rapier",
    dyeing_process="acid_exhaust",
    finishing="softener_only",
    country="india",
    transport_mode="air_freight",
    transport_distance_km=8000,
)
print(f"  Total CO₂e           : {cf3['total_co2e_kg_per_kg']} kg CO₂e / kg fabric")
print(f"  Sustainability rating : {cf3['sustainability_rating']} — {cf3['rating_description']}")
offset = carbon_offset_cost(cf3["total_co2e_kg"], price_per_tonne_usd=20)
print(f"  Carbon offset cost   : ${offset['offset_cost_usd']} USD  ({offset['tonnes_co2e']} tonnes CO₂e @ $20/t)")
print(f"\n  Reduction tips:")
for tip in cf3["reduction_tips"]:
    print(f"  → {tip}")

sub("Example D: Fiber comparison table (fiber stage only, 1000 kg)")
fibers_comp = compare_fiber_footprints(1000)
print(f"  {'Fiber':<22} {'CO₂e/kg':>9} {'CO₂e total':>12} {'Water L/kg':>12} {'Rating':>7}")
print(f"  {'-'*22} {'-'*9} {'-'*12} {'-'*12} {'-'*7}")
for f in fibers_comp:
    print(
        f"  {f['fiber']:<22} {f['co2e_kg_per_kg']:>9.2f} "
        f"{f['co2e_kg_total']:>12.0f} {f['water_L_per_kg']:>12,} {f['fiber_stage_rating']:>7}"
    )

sub("Discovery helpers")
print(f"\n  Dyeing processes (sorted by CO₂e):")
for dp in list_dyeing_processes_carbon():
    print(f"    {dp['process']:<25}: {dp['co2e_kg_per_kg']} kg CO₂e/kg")

print(f"\n  Fabric formations (sorted by CO₂e):")
for ff in list_fabric_formations():
    print(f"    {ff['process']:<25}: {ff['co2e_kg_per_kg']} kg CO₂e/kg")

print(f"\n  Finishing processes (sorted by CO₂e):")
for fp in list_finishing_processes():
    print(f"    {fp['process']:<25}: {fp['co2e_kg_per_kg']} kg CO₂e/kg")

print(f"\n  Countries / grid emission factors:")
for co in list_countries_carbon():
    print(f"    {co['country']:<15}: {co['kg_co2e_per_kwh']} kg CO₂e/kWh")


# ═══════════════════════════════════════════════════════════════════
# 4. YARN MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 4 — YARN  (v1.1 core)")

sub("Count conversions")
print(f"  ne_to_tex(30)        : {ne_to_tex(30):.4f} Tex")
print(f"  tex_to_ne(20)        : {tex_to_ne(20):.4f} Ne")
print(f"  tex_to_denier(20)    : {tex_to_denier(20):.1f} Denier")
print(f"  denier_to_tex(180)   : {denier_to_tex(180):.4f} Tex")
print(f"  ne_to_denier(30)     : {ne_to_denier(30):.2f} Denier")

sub("Yarn quality metrics")
print(f"  cv_percentage(1.5, 30)         : {cv_percentage(1.5, 30):.2f}% CV  (unevenness)")
print(f"  cv_percentage(0.8, 40)         : {cv_percentage(0.8, 40):.2f}% CV  (fine yarn)")
print(f"  csp(count=30, strength=80)     : {csp(30, 80)} CSP")
print(f"  csp(count=40, strength=95)     : {csp(40, 95)} CSP  (fine yarn, higher quality)")


# ═══════════════════════════════════════════════════════════════════
# 5. FABRIC MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 5 — FABRIC  (v1.1 core)")

sub("GSM & fabric weight")
print(f"  gsm(50g, 0.5×0.5m)            : {gsm(50, 0.5, 0.5):.1f} g/m²")
print(f"  gsm(30g, 0.5×0.5m)            : {gsm(30, 0.5, 0.5):.1f} g/m²  (lightweight)")
print(f"  fabric_weight(200, 1.5m, 100m): {fabric_weight(200, 1.5, 100):.0f} g  ({fabric_weight(200,1.5,100)/1000:.1f} kg)")

sub("Cover factor")
print(f"  warp_cover_factor(60, 40)      : {warp_cover_factor(60, 40):.4f}")
print(f"  weft_cover_factor(50, 40)      : {weft_cover_factor(50, 40):.4f}")
print(f"  cover_factor(60, 50, 40)       : {cover_factor(60, 50, 40):.4f}  (total)")
print(f"  cover_factor(80, 70, 60)       : {cover_factor(80, 70, 60):.4f}  (fine shirting)")

sub("Shrinkage")
print(f"  shrinkage_percent(100, 96)     : {shrinkage_percent(100, 96):.2f}%  (warp)")
print(f"  shrinkage_percent(100, 98)     : {shrinkage_percent(100, 98):.2f}%  (weft)")
print(f"  shrinkage_percent(50, 49)      : {shrinkage_percent(50, 49):.2f}%  (synthetic)")


# ═══════════════════════════════════════════════════════════════════
# 6. DYEING MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 6 — DYEING  (v1.1 core)")

sub("Basic dyeing calculations")
print(f"  dye_required(1000g, 2%)        : {dye_required(1000, 2):.1f} g dye")
print(f"  dye_required(5000g, 3.5%)      : {dye_required(5000, 3.5):.1f} g dye  (dark shade)")
print(f"  liquor_required(5kg, MLR=10)   : {liquor_required(5, 10):.1f} L")
print(f"  liquor_required(20kg, MLR=8)   : {liquor_required(20, 8):.1f} L")
print(f"  chemical_required(1000g, 5%)   : {chemical_required(1000, 5):.1f} g")

sub("Salt & soda ash (reactive dyeing)")
print(f"  salt_required(10kg, shade 0.5%): {salt_required(10, 0.5)} g/L  (light shade)")
print(f"  salt_required(10kg, shade 2%)  : {salt_required(10, 2)} g/L  (medium shade)")
print(f"  salt_required(10kg, shade 4%)  : {salt_required(10, 4)} g/L  (dark shade)")
print(f"  soda_ash_required(1000g)       : {soda_ash_required(1000):.1f} g  (20% owf default)")
print(f"  soda_ash_required(1000g, 15%)  : {soda_ash_required(1000, 15):.1f} g")


# ═══════════════════════════════════════════════════════════════════
# 7. DYEING ADVANCED MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 7 — DYEING ADVANCED  (v1.1 core)")

sub("Dye exhaustion & fixation")
print(f"  dye_exhaustion(100, 20)        : {dye_exhaustion(100, 20):.1f}%  (80% absorbed)")
print(f"  dye_exhaustion(100, 35)        : {dye_exhaustion(100, 35):.1f}%  (medium exhaust)")
print(f"  dye_fixation(75, 100)          : {dye_fixation(75, 100):.1f}%  (reactive cotton)")
print(f"  dye_fixation(92, 100)          : {dye_fixation(92, 100):.1f}%  (disperse polyester)")

sub("Liquor ratio & chemical utilization")
print(f"  liquor_ratio(5kg, 50L)         : 1:{liquor_ratio(5, 50):.1f}  (standard)")
print(f"  liquor_ratio(10kg, 80L)        : 1:{liquor_ratio(10, 80):.1f}  (low liquor)")
print(f"  chemical_utilization(90, 100)  : {chemical_utilization(90, 100):.1f}%")
print(f"  chemical_utilization(110, 100) : {chemical_utilization(110, 100):.1f}%  (excess used)")

sub("Wash fastness")
print(f"  wash_fastness_efficiency(100, 92)  : {wash_fastness_efficiency(100, 92):.1f}%  retention (good)")
print(f"  wash_fastness_efficiency(100, 75)  : {wash_fastness_efficiency(100, 75):.1f}%  retention (poor)")


# ═══════════════════════════════════════════════════════════════════
# 8. COSTING MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 8 — COSTING  (v1.1 core)")

sub("Yarn & process cost")
print(f"  yarn_cost(100kg, $3.50/kg)     : ${yarn_cost(100, 3.5):.2f}")
print(f"  yarn_cost(250kg, $4.20/kg)     : ${yarn_cost(250, 4.2):.2f}  (polyester yarn)")
print(f"  process_cost(500, 200, 100)    : ${process_cost(500, 200, 100):.2f}  (mat+labor+OH)")

sub("Pricing & break-even")
print(f"  profit_price(1000, 20%)        : ${profit_price(1000, 20):.2f}")
print(f"  profit_price(2500, 15%)        : ${profit_price(2500, 15):.2f}")
print(f"  break_even_units(10000, 50, 30): {break_even_units(10000, 50, 30):.0f} units")
print(f"  break_even_units(50000, 80, 55): {break_even_units(50000, 80, 55):.0f} units")


# ═══════════════════════════════════════════════════════════════════
# 9. COSTING ADVANCED MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 9 — COSTING ADVANCED  (v1.1 core)")

sub("Per-meter & energy costs")
print(f"  cost_per_meter(5000, 200m)     : ${cost_per_meter(5000, 200):.2f} /m")
print(f"  cost_per_meter(12000, 500m)    : ${cost_per_meter(12000, 500):.2f} /m")
print(f"  energy_cost(5kW, 8h, $0.15)   : ${energy_cost(5, 8, 0.15):.2f}")
print(f"  energy_cost(15kW, 16h, $0.12) : ${energy_cost(15, 16, 0.12):.2f}  (rapier loom)")

sub("Depreciation & margin")
print(f"  depreciation(100000, 10yr)     : ${depreciation(100000, 10):,.2f} /year")
print(f"  depreciation(250000, 15yr)     : ${depreciation(250000, 15):,.2f} /year")
print(f"  profit_margin(1200, 1000)      : {profit_margin(1200, 1000):.2f}%")
print(f"  profit_margin(3450, 3000)      : {profit_margin(3450, 3000):.2f}%")

sub("Total manufacturing cost (TMC)")
tmc = total_manufacturing_cost(5000, 2000, 1500)
print(f"  total_manufacturing_cost(5000, 2000, 1500): ${tmc:,}")
tmc2 = total_manufacturing_cost(12000, 5000, 3500)
print(f"  total_manufacturing_cost(12000, 5000, 3500): ${tmc2:,}")


# ═══════════════════════════════════════════════════════════════════
# 10. PRODUCTION MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 10 — PRODUCTION  (v1.1 core)")

sub("Efficiency & production rate")
print(f"  efficiency(900, 1000)          : {efficiency(900, 1000):.1f}%")
print(f"  efficiency(750, 1000)          : {efficiency(750, 1000):.1f}%  (low)")
print(f"  production_rate(500kg, 8h)     : {production_rate(500, 8):.2f} kg/hour")
print(f"  production_rate(1200m, 10h)    : {production_rate(1200, 10):.1f} m/hour")
print(f"  machine_utilization(7h, 8h)    : {machine_utilization(7, 8):.2f}%")

sub("Daily production target (spinning frame)")
dpt = daily_production_target(8, 85, 14000, 30)
print(f"  daily_production_target(8h, 85%, 14000rpm, Ne30): {dpt} kg/spindle/shift")
dpt2 = daily_production_target(8, 90, 18000, 20)
print(f"  daily_production_target(8h, 90%, 18000rpm, Ne20): {dpt2} kg/spindle/shift")


# ═══════════════════════════════════════════════════════════════════
# 11. WASTAGE MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 11 — WASTAGE  (v1.1 core)")

sub("Wastage percentage")
print(f"  wastage_percentage(100kg, 92kg)    : {wastage_percentage(100, 92):.2f}%")
print(f"  wastage_percentage(500kg, 465kg)   : {wastage_percentage(500, 465):.2f}%")

sub("Material planning with wastage")
m1 = material_required_with_wastage(950, 5)
print(f"  material_required_with_wastage(950kg, 5%)  : {m1:.2f} kg raw material needed")
m2 = material_required_with_wastage(1000, 8)
print(f"  material_required_with_wastage(1000kg, 8%) : {m2:.2f} kg raw material needed")


# ═══════════════════════════════════════════════════════════════════
# 12. UNIT CONVERSION MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 12 — UNIT CONVERSIONS  (v1.1 core)")

sub("Weight conversions")
print(f"  kg_to_lbs(10)                  : {kg_to_lbs(10):.4f} lbs")
print(f"  lbs_to_kg(22)                  : {lbs_to_kg(22):.4f} kg")

sub("Length conversions")
print(f"  inch_to_meter(60)              : {inch_to_meter(60):.4f} m  (60\" fabric)")
print(f"  meter_to_inch(1.524)           : {meter_to_inch(1.524):.2f} inches")
print(f"  cm_to_inch(100)                : {cm_to_inch(100):.4f} inches")
print(f"  inch_to_cm(39.37)              : {inch_to_cm(39.37):.4f} cm")

sub("Fabric weight conversions")
print(f"  gsm_to_oz_yd2(200)             : {gsm_to_oz_yd2(200):.4f} oz/yd²")
print(f"  oz_yd2_to_gsm(5.9)             : {oz_yd2_to_gsm(5.9):.2f} g/m²")

sub("Yarn count conversions")
print(f"  ne_to_nm(30)                   : {ne_to_nm(30):.3f} Nm")
print(f"  nm_to_ne(50)                   : {nm_to_ne(50):.4f} Ne")

sub("Temperature conversions")
print(f"  celsius_to_fahrenheit(130)     : {celsius_to_fahrenheit(130):.1f}°F  (disperse dyeing)")
print(f"  fahrenheit_to_celsius(212)     : {fahrenheit_to_celsius(212):.1f}°C  (boil)")


# ═══════════════════════════════════════════════════════════════════
# 13. QUALITY CONTROL MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 13 — QUALITY CONTROL  (v1.1 core)")

sub("Moisture tests")
print(f"  moisture_regain(110g, 100g)    : {moisture_regain(110, 100):.2f}%  (cotton std ~8%)")
print(f"  moisture_regain(117g, 100g)    : {moisture_regain(117, 100):.2f}%  (wool std ~16%)")
print(f"  moisture_content(110g, 100g)   : {moisture_content(110, 100):.4f}%")

sub("Absorbency & pilling")
print(f"  absorbency_rate(300g, 100g)    : {absorbency_rate(300, 100):.1f}%  (excellent)")
print(f"  absorbency_rate(150g, 100g)    : {absorbency_rate(150, 100):.1f}%  (moderate)")
for score in [1, 2, 3, 4, 5]:
    print(f"  pilling_resistance_grade({score})    : {pilling_resistance_grade(score)}")


# ═══════════════════════════════════════════════════════════════════
# 14. SPINNING MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 14 — SPINNING  (v1.1 core)")

sub("Twist measurements")
print(f"  yarn_twist_tpi(200 twists, 10\"): {yarn_twist_tpi(200, 10):.1f} TPI")
print(f"  yarn_tpm(20 TPI)               : {yarn_tpm(20):.2f} TPM")
print(f"  yarn_tpm(25 TPI)               : {yarn_tpm(25):.2f} TPM  (fine yarn)")

sub("Imperfection index (IPI)")
ipi1 = yarn_imperfection(12, 10, 30, 50)
print(f"  yarn_imperfection(U%=12, thin=10, thick=30, neps=50): IPI = {ipi1}")
ipi2 = yarn_imperfection(9, 3, 15, 20)
print(f"  yarn_imperfection(U%=9, thin=3, thick=15, neps=20):   IPI = {ipi2}  (better quality)")

sub("Efficiency & draft")
print(f"  spinning_efficiency(80, 100)   : {spinning_efficiency(80, 100):.1f}%")
print(f"  spinning_efficiency(92, 100)   : {spinning_efficiency(92, 100):.1f}%  (excellent)")
print(f"  draft(0.5 Ne roving, 30 Ne)    : {draft(0.5, 30):.1f}×")
print(f"  draft(0.8 Ne roving, 40 Ne)    : {draft(0.8, 40):.1f}×")


# ═══════════════════════════════════════════════════════════════════
# 15. WEAVING MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 15 — WEAVING  (v1.1 core)")

sub("Loom efficiency")
print(f"  loom_efficiency(850, 1000)     : {loom_efficiency(850, 1000):.1f}%")
print(f"  loom_efficiency(930, 1000)     : {loom_efficiency(930, 1000):.1f}%  (air-jet)")

sub("Break rates")
print(f"  warp_break_rate(5, 2000 ends)  : {warp_break_rate(5, 2000):.4f}%  (per 100 ends)")
print(f"  weft_break_rate(3, 10000 picks): {weft_break_rate(3, 10000):.4f}%  (per 100 picks)")

sub("Defect rate & production per loom")
print(f"  fabric_defect_rate(10, 500m)   : {fabric_defect_rate(10, 500):.4f} defects/meter")
ppl = production_per_loom(600, 85, 60, 60)
print(f"  production_per_loom(600rpm, 85%, 60EPI, 60\"): {ppl} m/hour")
ppl2 = production_per_loom(800, 92, 80, 63)
print(f"  production_per_loom(800rpm, 92%, 80EPI, 63\"): {ppl2} m/hour  (air-jet)")


# ═══════════════════════════════════════════════════════════════════
# 16. TESTING MODULE
# ═══════════════════════════════════════════════════════════════════

section("MODULE 16 — TESTING  (v1.1 core)")

sub("Mechanical tests")
print(f"  tensile_strength(500N, 10mm²)  : {tensile_strength(500, 10):.1f} N/mm²  (MPa)")
print(f"  tensile_strength(800N, 20mm²)  : {tensile_strength(800, 20):.1f} N/mm²")
print(f"  elongation_percent(130mm, 100) : {elongation_percent(130, 100):.1f}%  (at break)")
print(f"  elongation_percent(115mm, 100) : {elongation_percent(115, 100):.1f}%  (less elastic)")
print(f"  bursting_strength(200kPa, 10cm²): {bursting_strength(200, 10):.1f}")

sub("Durability & stiffness")
print(f"  abrasion_index(2g, 100g)       : {abrasion_index(2, 100):.2f}%  loss (durable)")
print(f"  abrasion_index(8g, 100g)       : {abrasion_index(8, 100):.2f}%  loss (less durable)")
print(f"  stiffness_index(bending=3.5cm) : {stiffness_index(3.5):.4f}  (bending length³)")

sub("Color fastness")
for grade in [1, 2, 3, 4, 5]:
    print(f"  color_fastness_grade({grade})        : {color_fastness_grade(grade)}")


# ═══════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════

section("textilecalc v2.0 — COMPLETE SUMMARY")
print("""
  ┌──────────────────────────────────────────────────────────────────┐
  │  #   Module               Key Functions                         │
  ├──────────────────────────────────────────────────────────────────┤
  │  1   yarn_recommender     recommend_yarn_count                   │
  │      (NEW v2.0)           compare_yarn_options                   │
  │                           list_end_uses, list_fiber_types        │
  ├──────────────────────────────────────────────────────────────────┤
  │  2   shade_recipe         predict_shade_recipe                   │
  │      (NEW v2.0)           compare_shade_accuracy                 │
  │                           hex_to_rgb, rgb_to_lab, delta_e        │
  │                           rgb_to_hex, lab_to_rgb, list_dye_classes│
  ├──────────────────────────────────────────────────────────────────┤
  │  3   carbon_footprint     calculate_carbon_footprint             │
  │      (NEW v2.0)           compare_fiber_footprints               │
  │                           carbon_offset_cost                     │
  │                           list_fiber_types_carbon                │
  │                           list_dyeing_processes_carbon           │
  │                           list_fabric_formations                 │
  │                           list_finishing_processes               │
  │                           list_countries_carbon                  │
  ├──────────────────────────────────────────────────────────────────┤
  │  4   yarn                 ne_to_tex, tex_to_ne, ne_to_denier     │
  │                           tex_to_denier, denier_to_tex           │
  │                           cv_percentage, csp                     │
  ├──────────────────────────────────────────────────────────────────┤
  │  5   fabric               gsm, fabric_weight, shrinkage_percent  │
  │                           warp_cover_factor, weft_cover_factor   │
  │                           cover_factor                           │
  ├──────────────────────────────────────────────────────────────────┤
  │  6   dyeing               dye_required, liquor_required          │
  │                           chemical_required, salt_required       │
  │                           soda_ash_required                      │
  ├──────────────────────────────────────────────────────────────────┤
  │  7   dyeing_advanced      dye_exhaustion, dye_fixation           │
  │                           liquor_ratio, chemical_utilization     │
  │                           wash_fastness_efficiency               │
  ├──────────────────────────────────────────────────────────────────┤
  │  8   costing              yarn_cost, process_cost, profit_price  │
  │                           break_even_units                       │
  ├──────────────────────────────────────────────────────────────────┤
  │  9   costing_advanced     cost_per_meter, energy_cost            │
  │                           depreciation, profit_margin            │
  │                           total_manufacturing_cost               │
  ├──────────────────────────────────────────────────────────────────┤
  │  10  production           efficiency, production_rate            │
  │                           machine_utilization                    │
  │                           daily_production_target                │
  ├──────────────────────────────────────────────────────────────────┤
  │  11  wastage              wastage_percentage                     │
  │                           material_required_with_wastage         │
  ├──────────────────────────────────────────────────────────────────┤
  │  12  unit_conv            kg↔lbs, inch↔meter, cm↔inch            │
  │                           gsm↔oz_yd2, Ne↔Nm                     │
  │                           celsius↔fahrenheit                    │
  ├──────────────────────────────────────────────────────────────────┤
  │  13  qc                   moisture_regain, moisture_content      │
  │                           absorbency_rate, pilling_resistance    │
  ├──────────────────────────────────────────────────────────────────┤
  │  14  spinning             yarn_twist_tpi, yarn_tpm               │
  │                           yarn_imperfection, spinning_efficiency │
  │                           draft                                  │
  ├──────────────────────────────────────────────────────────────────┤
  │  15  weaving              loom_efficiency, warp_break_rate       │
  │                           weft_break_rate, fabric_defect_rate    │
  │                           production_per_loom                    │
  ├──────────────────────────────────────────────────────────────────┤
  │  16  testing              tensile_strength, elongation_percent   │
  │                           bursting_strength, abrasion_index      │
  │                           stiffness_index, color_fastness_grade  │
  └──────────────────────────────────────────────────────────────────┘

  16 modules | 60+ functions | Zero external dependencies
  Pure Python 3.7+ | Author: Abdul Malek | Version: 2.0.0
""")
