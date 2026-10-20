---
title: "Theoretical derivation of QI (the formula m_i = m(1 − 2c²/aΘ) and its foundations)"
tags: [derivation, unruh-radiation, casimir, uncertainty-principle, information-theory, holographic, renda, dickmann]
verdict: contested
---

# Theoretical derivation of QI

## The claim and what is at stake
- Every QI prediction in this repository rests on one formula:

  $$ m_i = m\left(1 - \frac{2c^2}{|a|\Theta}\right) \qquad \left(\text{originally } m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{a\Theta}\right),\ \beta \approx 0.2\right) $$

  - **Galaxies and wide binaries:** a minimum acceleration of 2c²/Θ.
  - **Pioneer and flyby anomalies:** modified inertia at low acceleration.
  - **Propulsion:** horizon asymmetry.
- The "no adjustable parameters" claim depends on two things: whether the formula is derived rather than assumed, and on how Θ is fixed.
- **Values of Θ used:**
  - 2.6–2.7 × 10²⁶ m (2007–2012);
  - 4.3 × 10²⁶ m (Pickering 2017);
  - 8.8 × 10²⁶ m (2017 onward);
  - 4.4 × 10²⁶ m as the Hubble radius (2019);
  - a photon-specific Θ = 2c²/a (2022 light bending).

  See [galaxy-rotation](galaxy-rotation.md) and the individual papers.

## Mainstream view
- **Equivalence principle.** Inertial and gravitational mass are equal to high precision. Gundlach et al. found no violation of F = ma down to 5 × 10⁻¹⁴ m s⁻² ([2010-turyshev-pioneer-review](../01-papers/2010-turyshev-pioneer-review/README.md)). Dickmann & Dickmann quote ~10⁻¹³ m s⁻² for the same test ([2023-dickmann-casimir-contradicts](../03-criticism/2023-dickmann-casimir-contradicts/README.md)).
- **Unruh effect.** It is a QFT prediction for uniformly accelerated detectors, and in the idealised case it is an isotropic thermal bath.
  - Milgrom (1999) argued that isotropy prevents Unruh radiation from causing inertia (cited in [2020-mcculloch-horizon-widths](../01-papers/2020-mcculloch-horizon-widths/README.md)).
  - Direct observation is debated. Lynch et al. 2023 report acceleration-temperature thermal emission in neutron decay, which they describe as classical ([2023-lynch-accelerated-electron-thermometer](../01-papers/2023-lynch-accelerated-electron-thermometer/README.md)).
- **Koberlein (2017):** Unruh radiation is far too weak at ordinary accelerations and isotropic, so it cannot produce inertia ([2017-koberlein-doing-it-wrong](../07-media/2017-koberlein-doing-it-wrong/README.md)).
- **Granade (in Jalopnik 2016):** the theory requires photons to have inertial mass and inertial mass to differ from gravitational mass ([2016-jalopnik-emdrive](../07-media/2016-jalopnik-emdrive/README.md)).

## QI's derivations (chronological)

| Year | Route | Result | Caveats in the sources |
|---|---|---|---|
| 2007 | Unruh spectrum with allowed λ_n = 2Θ/n; linear factor F = 1 − λ_m/4Θ | Formula with β = 0.2 | F is *assumed*: "The assumptions made in equation (6) and (7) have not individually been verified" ([2007](../01-papers/2007-mcculloch-pioneer-anomaly/README.md)) |
| 2013 | Asymmetric Casimir effect between the Rindler horizon (c²/a) and the Hubble horizon | F ∝ −a; m_i ≈ 5.5 × 10⁻⁸ kg per "particle" (~2.5 m_P) | Uses only the peak wavelength; A/V = 1/l_P is chosen by hand; real particle masses not explained ([2013](../01-papers/2013-mcculloch-asymmetric-casimir/README.md)) |
| 2014 | Gravity from the uncertainty principle | F = GMm/r² | Circular: m_P = √(ħc/G) is defined with G in the 2014 text itself (p. 2), though the paper does not flag it; McCulloch called it "circular reasoning" only in 2016 ([2014](../01-papers/2014-mcculloch-gravity-uncertainty/README.md)) |
| 2016 | Unruh temperatures (Giné & McCulloch) | 2.799 × 10⁻⁸ kg, within 29% of m_P | Still a Planck-length cube with peak-only u = hc/λV (Renda); later "26%" (Giné 2017) mis-copies the mass as 2.75 × 10⁻⁸ kg (editorial check: formula gives 2.81 × 10⁻⁸ kg = 1.29 m_P); Giné & Luciano 2021 say the azimuthal integration factor is wrong ([2016-gine](../01-papers/2016-gine-unruh-temperatures/README.md), [2017-gine](../01-papers/2017-gine-inertial-mass-holographic/README.md)) |
| 2016 | Mass-energy + uncertainty energy conserved; Δx set by horizons | Formula × 2πβ ≈ 1.26; electron 9.1 × 10⁻³¹ kg | Printed masses follow h/(cΔx), not ħ/(cΔx), so the electron "prediction" is the Compton-wavelength definition (editorial check) ([2016](../01-papers/2016-mcculloch-relativity-uncertainty/README.md)) |
| 2017 | Holographic (Giné) | "Exact" mass of a Planck *particle*, √(hc/2G) = √π m_P ≈ 1.77 m_P | M_i = c²r/2G is the assumed Schwarzschild relation (the paper says so); target switched from m_P; the paper also says the 2013/2016 route "does not give correct results for an elementary particle" ([2017-gine](../01-papers/2017-gine-inertial-mass-holographic/README.md)) |
| 2017 | Mass + energy + information conserved (EMI) | Quantised inertia at very high a (qualitative) | Abstract only ([2017-info-loss](../01-papers/2017-mcculloch-information-loss/README.md)) |
| 2019/20 | Uncertainty principle with horizon *half-circumferences* (Giné 2018 trick) | Formula "exactly" | Choice not derived; McCulloch later: "no good justification for using the width"; Hikari venue; label and sign slips ([2020-widths](../01-papers/2020-mcculloch-horizon-widths/README.md), [2018-gine-hawking](../01-papers/2018-gine-hawking-unruh-uncertainty/README.md)) |
| 2020 | Landauer erasure of "bits" between object and horizon | Formula exactly | Depends on using log₂ (not ln) and on the bit-counting choice; paper concedes QI "not yet mathematically complete" ([2020-info](../01-papers/2020-mcculloch-information-theory/README.md)) |
| 2020 | Extended uncertainty principles (Giné & Luciano) | Linear QI form only from a physically unclear EUP (Case II); the natural de Sitter EUP gives a *quadratic* correction | Parameters fixed by matching to MOND ([2020-eup](../01-papers/2020-gine-luciano-eup-modified-inertia/README.md)) |
| 2021 | Planck-size resonant parts and quantum fluctuations (Giné & Luciano) | Two models, consistency discussed | Abstract only ([2021-fluct](../01-papers/2021-gine-luciano-inertia-fluctuations/README.md)) |

- **Related work:**
  - Haug 2018 (viXra) reinterprets the gravity derivation. Its numerical match ħc/m_P² = G is true by definition ([2018-haug](../01-papers/2018-haug-mcculloch-derivation/README.md)).
  - Giné 2011/2012 link MiHsC to Verlinde's holographic gravity ([2011](../01-papers/2011-gine-pioneer-holographic/README.md), [2012](../01-papers/2012-gine-holographic-modified-inertia/README.md)).
  - Soli 2021 is a poster on IKKT matrix models ([2021-soli](../01-papers/2021-soli-ikkt-qi/README.md)).
  - Pickering 2017 proposes a resonant-cavity Θ ([2017-pickering](../01-papers/2017-pickering-resonant-cavity/README.md)).
  - The 2014 book is [2014-mcculloch-physics-from-edge](../07-media/2014-mcculloch-physics-from-edge/README.md).
- **Equivalence-principle argument.** QI papers argue that torsion balances cannot see the effect, because rigidly connected masses share the same acceleration relative to distant matter ([2011-mcculloch-tajmar-effect](../01-papers/2011-mcculloch-tajmar-effect/README.md)). They also argue that the terrestrial correction is ~10⁻²¹ ([2020-eup](../01-papers/2020-gine-luciano-eup-modified-inertia/README.md)). The flyby papers concede that the effect must be confined to unbound trajectories for an unknown reason ([2008-mnras](../01-papers/2008-mcculloch-flyby-anomalies-mnras/README.md)).

## Independent tests and critiques
- **Renda 2019, MNRAS 489, 881** ([2019-renda-sceptical](../03-criticism/2019-renda-sceptical/README.md)) is the first peer-reviewed critique. It reports "two major flaws":
  1. Summing the discrete Unruh modes inside the Hubble cavity numerically does *not* give the linear F(a). Instead F → 1 above 10⁻⁸ m s⁻², F → 0 below a₀, with a peak F ≈ 2.17 at 1.2 × 10⁻⁹ m s⁻², a behaviour "never ... measured or predicted".
  2. The 2013/2016 inertia derivation puts all the energy in the peak mode. At classical accelerations that mode carries almost none of it.

  Renda says the flaws "will require a major rethinking of the whole theory". He does not test data.
- **McCulloch's response.** He thanked Renda for "the first serious criticism of QI". He accepts the peak-wavelength point and points to the uncertainty-principle and information-erasure derivations instead (blog, 2020 and 2026). No peer-reviewed reply was found, and no one has published an assessment of whether the newer routes escape Renda's objections.
- **Dickmann & Dickmann 2023**, Kinematics & Physics of Celestial Bodies 39, 356 ([2023-dickmann-casimir-contradicts](../03-criticism/2023-dickmann-casimir-contradicts/README.md)): summing all modes on both sides gives a net Unruh-pressure force **∝ a⁴, not a**, which contradicts Newton's second law. They "refute" QI as an explanation of inertia, though not vacuum-based inertia in general. No McCulloch response was found.
  - Editorial caveats in the README: the treatment of the cosmic-horizon side as an unbounded continuum, and the a-independence of the mode sum.
- **Kholupenko 2019/2022/2025** (Gravitation & Cosmology; [Part I](../01-papers/2019-kholupenko-unruh-anisotropy-1/README.md), [II](../01-papers/2022-kholupenko-unruh-anisotropy-2/README.md), [III](../01-papers/2025-kholupenko-unruh-anisotropy-3/README.md)): standard-QFT analyses arguing that Unruh radiation can be anisotropic and non-thermal. Part I (2019) gets this without any detector model, from a finite integration volume or finite light-speed spreading of the Rindler metric. Backward-hemisphere (horizon-side) quanta vanish, and an extra deceleration force ∝ a² (1+1D) results. The paper explicitly questions Giné & McCulloch's (2016) Casimir-cutoff mechanism and calls its own anisotropy "of different origin" (p. 214). Parts II and III add directional (II) and screened (III) detectors; Part III predicts a reaction force on the detector. This is *qualitatively* in line with QI's premise and relevant to Milgrom's isotropy objection, but it is not a derivation or test of QI.
- **Independent horizon-based MOND derivations** (Smolin 2017; Cadoni & Tuveri 2019; Hernandez et al. 2019) reach a₀ ~ cH by different routes. They cite McCulloch only in passing, and Hernandez et al. do so critically ([2017-smolin](../01-papers/2017-smolin-mond-quantum-gravity/README.md), [2019-cadoni](../01-papers/2019-cadoni-long-range-qg/README.md), [2018-hernandez](../01-papers/2018-hernandez-bounding-curvature/README.md)).
- **No relativistic field theory.** No covariant formulation or Lagrangian of QI appears in the sources. Critics note the lack of a single consistent framework ([2017-mcculloch-information-loss](../01-papers/2017-mcculloch-information-loss/README.md)).

## Assessment
QI's formula has been "derived" in at least seven different ways. The original Unruh-spectrum route assumed its key linear factor. When that factor is computed from the stated premises, it comes out differently (Renda), and the full-spectrum radiation-pressure force has the wrong dependence on acceleration (Dickmann & Dickmann). The later uncertainty-principle and information-theory derivations reach the formula exactly only through specific choices:
- the horizon half-circumference;
- log₂ instead of ln;
- a particular way of counting bits;

McCulloch himself calls the first of these weakly justified. Some of the derivations' "predictions" (G, the Planck mass, the electron mass) follow from definitions. Serious independent work on anisotropic Unruh radiation (Kholupenko) gives some qualitative support to the idea that horizons can make Unruh radiation one-sided, but it does not establish QI. The theoretical foundation is therefore actively contested: its original form has been shown to be flawed, and whether the replacements avoid those flaws has not been independently assessed.

## Sources
- Core QI derivations: [2007-mcculloch-pioneer-anomaly](../01-papers/2007-mcculloch-pioneer-anomaly/README.md), [2013-mcculloch-asymmetric-casimir](../01-papers/2013-mcculloch-asymmetric-casimir/README.md), [2014-mcculloch-gravity-uncertainty](../01-papers/2014-mcculloch-gravity-uncertainty/README.md), [2016-mcculloch-relativity-uncertainty](../01-papers/2016-mcculloch-relativity-uncertainty/README.md), [2016-gine-unruh-temperatures](../01-papers/2016-gine-unruh-temperatures/README.md), [2017-mcculloch-information-loss](../01-papers/2017-mcculloch-information-loss/README.md), [2020-mcculloch-horizon-widths](../01-papers/2020-mcculloch-horizon-widths/README.md), [2020-mcculloch-information-theory](../01-papers/2020-mcculloch-information-theory/README.md)
- Co-author / sympathetic work: [2011-gine-pioneer-holographic](../01-papers/2011-gine-pioneer-holographic/README.md), [2012-gine-holographic-modified-inertia](../01-papers/2012-gine-holographic-modified-inertia/README.md), [2017-gine-inertial-mass-holographic](../01-papers/2017-gine-inertial-mass-holographic/README.md), [2018-gine-casimir-uncertainty](../01-papers/2018-gine-casimir-uncertainty/README.md), [2018-gine-hawking-unruh-uncertainty](../01-papers/2018-gine-hawking-unruh-uncertainty/README.md), [2018-haug-mcculloch-derivation](../01-papers/2018-haug-mcculloch-derivation/README.md), [2020-gine-luciano-eup-modified-inertia](../01-papers/2020-gine-luciano-eup-modified-inertia/README.md), [2021-gine-luciano-inertia-fluctuations](../01-papers/2021-gine-luciano-inertia-fluctuations/README.md), [2021-soli-ikkt-qi](../01-papers/2021-soli-ikkt-qi/README.md), [2017-pickering-resonant-cavity](../01-papers/2017-pickering-resonant-cavity/README.md), [2021-mcculloch-epr-paradox](../01-papers/2021-mcculloch-epr-paradox/README.md)
- Independent related theory: [2019-kholupenko-unruh-anisotropy-1](../01-papers/2019-kholupenko-unruh-anisotropy-1/README.md), [2022-kholupenko-unruh-anisotropy-2](../01-papers/2022-kholupenko-unruh-anisotropy-2/README.md), [2025-kholupenko-unruh-anisotropy-3](../01-papers/2025-kholupenko-unruh-anisotropy-3/README.md), [2017-smolin-mond-quantum-gravity](../01-papers/2017-smolin-mond-quantum-gravity/README.md), [2019-cadoni-long-range-qg](../01-papers/2019-cadoni-long-range-qg/README.md), [2018-hernandez-bounding-curvature](../01-papers/2018-hernandez-bounding-curvature/README.md), [2023-lynch-accelerated-electron-thermometer](../01-papers/2023-lynch-accelerated-electron-thermometer/README.md)
- Criticism: [2019-renda-sceptical](../03-criticism/2019-renda-sceptical/README.md), [2023-dickmann-casimir-contradicts](../03-criticism/2023-dickmann-casimir-contradicts/README.md), [2017-koberlein-doing-it-wrong](../07-media/2017-koberlein-doing-it-wrong/README.md), [2016-jalopnik-emdrive](../07-media/2016-jalopnik-emdrive/README.md)
- Books: [2014-mcculloch-physics-from-edge](../07-media/2014-mcculloch-physics-from-edge/README.md), [2024-mcculloch-quantised-accelerations](../07-media/2024-mcculloch-quantised-accelerations/README.md)
- Related evidence: [galaxy-rotation](galaxy-rotation.md), [cosmic-acceleration](cosmic-acceleration.md), [lab-tests](lab-tests.md)
