---
title: "Laboratory tests of QI"
tags: [lab-test, null-result, tu-dresden, unruh-radiation, equivalence-principle, tajmar-effect, capacitor-thrust]
verdict: refuted-or-null
---

# Laboratory tests of QI

This note collects every laboratory measurement or proposal in the repository that bears directly on QI. For the device-level discussion of thrust claims, see [emdrive](emdrive.md) and [propulsion](propulsion.md). For the anomalies QI was used to explain, see [other-anomalies](other-anomalies.md).

## The phenomenon and the data

| Test | What was measured | Result | Source |
|---|---|---|---|
| Asymmetric copper/silver cavities, BART LED cavity, 4 Taylor laser resonators, fibre loops (DARPA-funded, TU Dresden) | Thrust on a sub-nN inverted double-pendulum balance in vacuum, 0.3–1.5 W | Only photon thrust (~1–2 nN). BART: (0.22 ± 4.13) nN vs 2700 nN claimed. QI limited "by at least 4 orders of magnitude" | [2022-neunzig-laser-resonators](../03-criticism/2022-neunzig-laser-resonators/README.md) |
| Same, after McCulloch's objections: Al case removed, tapered metal cone, loop outside chamber with no metal within 80 m | Thrust | Taylor-Light + cone: (1.01 ± 0.30)/(1.62 ± 0.26) nN vs QI 482/822 nN. Loop: ≤ 0.09 ± 0.18 µN vs 0.34–2.23 µN | [2022-neunzig-emdrive-thrust](../03-criticism/2022-neunzig-emdrive-thrust/README.md) |
| EmDrive replicas (Dresden), including superconducting | Thrust | Noise only: 10–30 nN (copper cavities, below photon thrust); 0.08–0.54 µN for the superconducting cavity (above photon thrust, but ~300× below PQ/c) | [2021-tajmar-emdrive-false-positive](../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2022-neunzig-emdrive-thrust](../03-criticism/2022-neunzig-emdrive-thrust/README.md) |
| Field-emission symmetric capacitors (Bhatt & Becker 2018, digital scale, 507 readings) | Weight change | ~1 mN anode-directed, reverses with insulated conductor behind cathode | [2018-bhatt-capacitor-thrust](../04-experiments/2018-bhatt-capacitor-thrust/README.md) |
| Clean capacitor set-up (Tajmar & Schreiber 2020; mu-metal box, liquid-metal feeds, ±0.3 mg) | Weight change | < 0.3 mg vs 6.8 mg from a fit to Bhatt & Becker. Ruled out "by an order of magnitude", with replication caveats | [2020-tajmar-capacitor-thrust](../03-criticism/2020-tajmar-capacitor-thrust/README.md) |
| Laser in shielded fibre-optic loop on a pendulum (Universidad de Alcalá, Pérez-Díaz; DARPA-funded) | Thrust | Blog 2020: 1–4 µN, "inconclusive", pendulum "subject to significant artefacts". McCulloch 2022: 10000 ± 6000 nN vs 20 nN predicted, "an artefact". Cited as "Paper submitted" (2021); no publication found | [2022-mcculloch-qi-thrust-casimir](../01-papers/2022-mcculloch-qi-thrust-casimir/README.md), [2023-quantizedinertia-website](../07-media/2023-quantizedinertia-website/README.md) |
| Plymouth capacitor tests (blog only) | Weight change | ~10 mg, "1/3 of the force predicted". "14%" of 22 tests showed thrust | [2021-mcculloch-symmetric-capacitors](../01-papers/2021-mcculloch-symmetric-capacitors/README.md) |
| Tajmar effect (spinning cooled rings, laser gyros, Seibersdorf) | Gyro/ring acceleration ratio | 3 ± 1.2 × 10⁻⁸ (clockwise), 1.5 ± 1.2 × 10⁻⁸ (anticlockwise). Not reproduced elsewhere | [2010](../01-papers/2010-mcculloch-tajmar-effect-explained/README.md), [2011](../01-papers/2011-mcculloch-tajmar-effect/README.md) |
| Podkletnov effect (rotating superconducting disc) | Weight loss | 0.05–0.07% static, 0.3–0.5% rotating. Single lab; NASA Marshall (Li et al. 1997) and Woods et al. 2001 did not find it | [2011-mcculloch-podkletnov-effect](../01-papers/2011-mcculloch-podkletnov-effect/README.md) |
| Unruh-type thermal emission | Photon spectra from radiative neutron decay (RDK II) | Consistent with a 1D Planck spectrum (reduced χ² 0.89–1.1 for the best choice) | [2023-lynch-accelerated-electron-thermometer](../01-papers/2023-lynch-accelerated-electron-thermometer/README.md) |

## Mainstream explanation(s)
- **Thrust claims:** experimental artefacts. TU Dresden reproduced a NASA-like ~1 µN/W EmDrive signal from mounting and thermal effects, and caught a false positive caused by a vaporising protective film. For capacitors, the known artefacts are corona and ion wind, wire bending, buoyancy and EM coupling.
- **Tajmar and Podkletnov effects:** not established. Neither has been replicated by an independent laboratory. A Canterbury ring-laser search (Graham et al. 2008) found no signal, though Tajmar et al. ([arXiv:0806.2271](https://arxiv.org/abs/0806.2271)) describe it as less sensitive.
- **Equivalence of inertial and gravitational mass:** confirmed to high precision. Turyshev & Toth note that Gundlach et al. found no violation of F = ma down to 5 × 10⁻¹⁴ m s⁻² ([2010-turyshev-pioneer-review](../01-papers/2010-turyshev-pioneer-review/README.md)).
- **Lynch et al.:** the authors describe their result as classical ("thermal Larmor") radiation tied to acceleration. It does not test QI's horizon cutoff or modified inertia.

## QI's prediction
- **Photon-cavity thrust:** F = PQL/c(1/w_small − 1/w_big), or worst-case F ≈ PS/c, where S is the number of round trips ([2015-mcculloch-emdrive-epl](../01-papers/2015-mcculloch-emdrive-epl/README.md); Dresden's adaptation). For the Dresden devices: copper cavities ~9×, silver ~39×, Taylor resonators 500–908× photon thrust.
- **Capacitors:** F = N_eħc/(2ns²) with N_e = I/q in the July 2021 preprint ([2021-mcculloch-symmetric-capacitors](../01-papers/2021-mcculloch-symmetric-capacitors/README.md)). The blog-reported F = 0.00014 IA/d² is not in that copy, but follows (editorial check) from F = π²PQcA/(240v²d²) in the 2022 preprint ([2022-mcculloch-qi-thrust-casimir](../01-papers/2022-mcculloch-qi-thrust-casimir/README.md)).
- **Tajmar effect:**
  - **2010:** ratio −1.78 ± 0.25 × 10⁻⁸ (gyro counter-rotating), with mirror-image behaviour predicted for the southern hemisphere.
  - **2011, revised frame:** 2.67 ± 0.24 × 10⁻⁸ clockwise and 1.34 ± 0.12 × 10⁻⁸ anticlockwise, which accounts for the parity asymmetry. This revision replaced the 2010 southern-hemisphere prediction.
- **Podkletnov effect:** 0.03% of g with the AC field (about half the observed effect) and 0.042% with rotation, 28× smaller than observed. MiHsC also predicts that the effect vanishes outside the cryostat, which contradicts the reported vertical column.
- **Proposed but not performed:**
  - A particle at 0.9c in a 1 km ring, irradiated at 22 km wavelength, should show increased inertia ([2010-mcculloch-minimum-accelerations](../01-papers/2010-mcculloch-minimum-accelerations/README.md)).
  - A spinning disc above ~1.43 × 10¹⁰ m s⁻² should hide part of Earth's gravity ([2019-mcculloch-rindler-horizons](../01-papers/2019-mcculloch-rindler-horizons/README.md)).
  - Self-levitating 129 nm cavities ([2020-mcculloch-nano-materials](../01-papers/2020-mcculloch-nano-materials/README.md)).
  - Cooled bodies radiating slightly below Stefan–Boltzmann, by 2.7 × 10⁻²⁰ at 100 pK ([2007](../01-papers/2007-mcculloch-pioneer-anomaly/README.md)).
  - A "Casimir probe" ([2022-mcculloch-light-bending](../01-papers/2022-mcculloch-light-bending/README.md)).
- **Equivalence principle:** McCulloch argues that torsion-balance tests would not see MiHsC, because rigidly connected masses share the same acceleration relative to distant matter ([2011-mcculloch-tajmar-effect](../01-papers/2011-mcculloch-tajmar-effect/README.md), [2011-mcculloch-podkletnov-effect](../01-papers/2011-mcculloch-podkletnov-effect/README.md)). The 2008 flyby paper concedes that the variation would otherwise conflict with such tests ([2008-mcculloch-flyby-anomalies-mnras](../01-papers/2008-mcculloch-flyby-anomalies-mnras/README.md)).

## Independent tests, critiques and null results
- **The decisive test.** The DARPA-funded Dresden programme was the only purpose-built, independent test of QI thrust. Its result is null at the nN level, several orders of magnitude below QI's worst-case predictions. Using optical Q instead of the round-trip number S "would otherwise add another 4 orders of magnitude" of discrepancy.
- **McCulloch's response.** On his blog he initially attributed the null to the aluminium case and then to the vacuum chamber. Dresden tested both explanations, and both gave null results. In January 2022 he wrote that light-based QI thrusters "did not perform well" while electron-based (capacitor) ones did, revised the v = c assumption, and said "QI has not been falsified". No revised quantitative prediction for these devices has been published.
- **"Five of six labs" (advocacy site, July 2021).** quantizedinertia.com/tests says "Six labs have tested this. So far, five have shown some thrust", citing "Perez-Diaz et al., 2021" and, for the null, "Neunzig et al., 2021". The cited Alcalá result was never published, and McCulloch later called it "an artefact". The other claimed positives were unpublished, blog-reported or non-peer-reviewed in 2021. The lab identification is reconstructed (unverified) in [2023-quantizedinertia-website](../07-media/2023-quantizedinertia-website/README.md).
- **Capacitors.** The only positive capacitor results are a non-peer-reviewed preprint using a consumer scale near high voltage, plus unpublished IVO and Plymouth tests. The single clean independent replication found nothing, though it did not exactly reproduce the conditions.
- **Tajmar effect.** McCulloch's two papers change the reference frame between 2010 and 2011, which reverses a key prediction. The target effect itself is unreplicated.
- **Podkletnov effect.** MiHsC gets half the static effect, misses the rotational effect by 28×, and gets the spatial extent wrong. The arXiv version also says the published Physics Procedia version contains an error.
- **Unruh radiation.** QI depends on Unruh radiation being real and able to push on matter. Lynch et al. 2023 report thermal emission from an accelerated electron in neutron decay, but the agreement depends on the electron-energy distribution chosen: reduced χ² ranges from 0.89 to 37 across choices. The result does not test QI's specific claims.

## Assessment
QI makes clear laboratory predictions. The best-controlled tests, run by an independent group partly within McCulloch's own DARPA project, found nothing beyond classical photon pressure, even after the set-up changes McCulloch asked for. The remaining positive laboratory claims are of three kinds:
- capacitor weight changes reported in non-peer-reviewed or unpublished work, and not reproduced in a clean set-up;
- QI fits to the Tajmar and Podkletnov effects, which were never independently confirmed, and which QI reproduces only partially or after a change of reference frame;
- proposals that have not been carried out.

On the present evidence, every controlled laboratory test of QI is null.

## Sources
- [2022-neunzig-laser-resonators](../03-criticism/2022-neunzig-laser-resonators/README.md), [2022-neunzig-emdrive-thrust](../03-criticism/2022-neunzig-emdrive-thrust/README.md), [2021-tajmar-emdrive-false-positive](../03-criticism/2021-tajmar-emdrive-false-positive/README.md), [2020-tajmar-capacitor-thrust](../03-criticism/2020-tajmar-capacitor-thrust/README.md), [2016-samsonov-emdrive-null](../03-criticism/2016-samsonov-emdrive-null/README.md)
- [2018-bhatt-capacitor-thrust](../04-experiments/2018-bhatt-capacitor-thrust/README.md), [2016-white-eagleworks](../04-experiments/2016-white-eagleworks/README.md), [2018-tajmar-spacedrive](../04-experiments/2018-tajmar-spacedrive/README.md), [2019-kossling-spacedrive-balance](../04-experiments/2019-kossling-spacedrive-balance/README.md)
- [2010-mcculloch-tajmar-effect-explained](../01-papers/2010-mcculloch-tajmar-effect-explained/README.md), [2011-mcculloch-tajmar-effect](../01-papers/2011-mcculloch-tajmar-effect/README.md), [2011-mcculloch-podkletnov-effect](../01-papers/2011-mcculloch-podkletnov-effect/README.md)
- [2010-mcculloch-minimum-accelerations](../01-papers/2010-mcculloch-minimum-accelerations/README.md), [2019-mcculloch-rindler-horizons](../01-papers/2019-mcculloch-rindler-horizons/README.md), [2020-mcculloch-nano-materials](../01-papers/2020-mcculloch-nano-materials/README.md), [2021-mcculloch-symmetric-capacitors](../01-papers/2021-mcculloch-symmetric-capacitors/README.md), [2017-taylor-laser-resonators](../01-papers/2017-taylor-laser-resonators/README.md), [2015-mcculloch-emdrive-epl](../01-papers/2015-mcculloch-emdrive-epl/README.md), [2022-mcculloch-light-bending](../01-papers/2022-mcculloch-light-bending/README.md)
- [2023-quantizedinertia-website](../07-media/2023-quantizedinertia-website/README.md) (advocacy claims), [2025-stauffer-qi-experiments](../01-papers/2025-stauffer-qi-experiments/README.md) (hobbyist proposals; informal Newton's-cradle null)
- [2023-lynch-accelerated-electron-thermometer](../01-papers/2023-lynch-accelerated-electron-thermometer/README.md), [2010-turyshev-pioneer-review](../01-papers/2010-turyshev-pioneer-review/README.md), [2008-mcculloch-flyby-anomalies-mnras](../01-papers/2008-mcculloch-flyby-anomalies-mnras/README.md)
- Related evidence: [emdrive](emdrive.md), [propulsion](propulsion.md), [other-anomalies](other-anomalies.md), [derivation](derivation.md)
