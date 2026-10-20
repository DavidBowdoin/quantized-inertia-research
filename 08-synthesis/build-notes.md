---
title: "Build notes: issues found while reading the sources"
tags: [synthesis, notes]
---

# Build notes

Raw issues collected while building the source folders (Oct 2026). Each one is expanded, with citations, in the relevant source README or evidence note. Kept here for traceability.

- Θ (Hubble diameter) value varies: 2.6e26 m in early papers vs 8.8e26 m in 2017 SPARC paper → affects "no free parameter" claim.
- 2016 relativity/uncertainty paper: printed masses match h/(cΔx) not ħ/(cΔx); electron result follows from Compton-wavelength definition (editorial check).
- 2015 PiP EmDrive: inconsistent cavity length 0.325 vs 0.345 m; geometry differs from EPL version.
- Gine 2016 Unruh temps: abstract 29% vs later-cited 26%.
- Dwarf galaxies 2017: QI formula has deep-MOND form; later data revisions (Triangulum II, Boötes II binaries) weaken key data points.
- Proton radius 2017: puzzle largely resolved by 2019 measurements.
- Iorio 2015, Smolin 2017: cite QI only in passing — not endorsement.
- Pickering 2017 page citation mismatch.
- Flyby: EPOXI showed zero anomaly (McCulloch 2011 admits); Juno flyby null result (NTRS 20160008163).
- Podkletnov 2011: arXiv text says published Physics Procedia version contains an error.
- Tajmar effect papers: Graham et al. 2008 null result (arXiv:0806.2271) for the effect itself.
- 2014 gravity-from-uncertainty: McCulloch's 2016 paper admits derivation is circular (p.8).
- Turyshev 2010 review names McCulloch only once (p.93).
- 2018 propellantless propulsion table: emdrive pred 4.2 mN vs 16 mN obs; MET 29–92 µN vs ~50 µN; capacitor 12 vs 14 mN (but Dresden later null on emdrive/capacitors).
- Haug 2018: viXra, numerical match circular (ħc/m_p² = G by definition).
- Hernandez 2018 bounding curvature: mentions McCulloch once, critically.
- Wide binaries: McCulloch & Lucio 2019 used Hernandez v1 (83 binaries); v3 has 81. Banik 2024 / Pittordis & Sutherland 2019 contrary.
- Giné & Luciano 2020 EUP: physically motivated case gives quadratic, not QI's linear, correction.
- Horizon widths 2020: swapped Δx labels, sign error Eq.15; Hikari journals on Beall's list.
- Information theory 2020: result depends on log2 choice.
- Rindler horizons 2019: typo for cosmic radius.
- Nano-materials 2020: assumed 1 mm wall far thicker than the 129 nm cavity.
- Haug 2021: different g_min (5.18e-11), not QI's.
- Light bending 2022: factor 2 from assuming 2c²/Θ = GM/r² for photons; deflection angle not computed.
- Proxima Centauri 2024: Kervella+2017 shows Newtonian bound orbit; Banik & Kroupa 2019.
- JuMBOs 2025: nature of JuMBOs disputed (Luhman 2024; NIRSpec 2025).
- Chae 2023, Hernandez 2024 review: QI not mentioned.
- Symmetric capacitors 2021: content only via blog, F = 0.00014 IA/d².
- Overview agent formula audit (see 00-overview/equations.md discrepancies): Θ 2.6/2.7e26 → 8.8e26 in 2017 (2c²/Θ 6.9e-10 → 2.0e-10); old Θ explains 2012's 30–54% rotation overprediction; 2013 Eq.8 implies 1.27 c²/(aΘ) not 2; 2016 prefactor 26% high fixed in 2020 by redefinition; Renda F(a) peaks ~2.17 near 1.2e-9; Dickmann: force ∝ a⁴.
- IVO claimed 45 mN/W ≈ 1e7 × Higgins 3.33 µN/kW limit.
- Giné 2016/2017/2020 co-authored with McCulloch → not independent.
- McCulloch replies: Renda — thanked May 2020; 30 Aug 2026 accepted peak-only point, claims same formula re-derived via uncertainty principle / horizon information erasure. Dickmann — no reply. Turyshev — 6 objections (1 May 2012). Banik — "backwards" (30 Aug 2026), doesn't address contamination. Tajmar laser — Al casing cancels thrust (27 Apr 2021); Dresden 2022 follow-up removed casing etc., still only photon thrust. 23 Jan 2022: light thrusters failed, capacitors work.
- Kößling 2019 journal: "no final conclusions"; IAC-18: "only thermal drifts".
- Samsonov: viXra, tests Shawyer not QI. White 2016: QI not mentioned. Banik's QI-falsification sentence relies on Pittordis & Sutherland 2019.

## Added 2026-10-19 (full texts supplied by the owner)
- EmDrives & dielectrics (2017): printed eq. 13 has the opposite sign to eq. 2 (table follows eq. 2); NASA predictions within ~1–6× (not 1–3×); n chosen per test (1.46 vs 6.16) despite the "no adjustable parameters" claim.
- Information loss (2017): mixes the two Θ values (7×10⁻¹⁰ m/s² implies 2.6×10²⁶ m, while eq. 17 uses 8.8×10²⁶ m); the "within 8%" agreement with QI holds only near a ≈ 2c²/Θ.
- Giné & Luciano (2021): state that McCulloch 2007/2013 and Giné & McCulloch 2016 use a wrong integration factor and an unjustified energy-density volume; their own k ≃ 1.2 consistency is partly by construction; Hubble-scale term neglected.
- Proxima Centauri (2024): the MOND comparison (Beech 0.424 km/s) is deep-MOND without an external field; QI eq. 5 is the same formula with a₀ → 2c²/Θ.
- Symmetric capacitors (2021): the blog formula F = 0.00014 IA/d² is not in this preprint (it follows from the 2022 preprint's eq. 5); applying its eq. 6 to Tajmar & Schreiber's 90 µm capacitor predicts ~8 mg, ~28× their 0.3 mg null limit; internal inconsistencies (n = 1.2 vs 1.49, gap 1 µm vs 10–120 µm axis, 180 vs 216 N).
- QI thrust as an asymmetric Casimir effect (2022): author calls the revision "hindsight"; under it the Dresden laser/fibre nulls no longer test QI; fibre-loop (≈11/17 vs 20/40 nN) and Madrid (500 vs 250) numbers don't reproduce from its own inputs; "71 N/kW" is 71 N/W.
- Soli (2021): no new experiment; reinterprets a Thorlabs datasheet and CERN channelling data; admits its key ingredient (soft NCSUSY-breaking terms) is missing.
- Tiverton lecture (Feb 2023): Plymouth in-air digital-scale capacitor tests, "up to 10 mg", heated stack (~50 °C), correlation 0.71 with predictions; conclusion "Lab tests have shown thrust (probably!)"; 10 mg at 1 W ≈ 0.1 N/kW (not 0.3) and only ~2–7× Dawn's ion drive (not 15×); conditions match Dresden's artefact list; no IVO / OTP-2 content.
