---
title: "Tiverton and Devon Astronomical Society - Lecture on On Orbit Manufacturing and Quantized Inertia"
authors: [Richard Arundal, Jasper Graham-Jones, M. McCulloch]
year: 2023
type: talk
venue: "Tiverton and Devon Astronomical Society lecture (PEARL conference proceeding)"
doi: null
arxiv: null
url: "https://pearl.plymouth.ac.uk/secam-research/1399"
open_access: true
license: all-rights-reserved
files: [slides.pdf, citation.bib]
status: supports
tags: [talk, slides, plymouth, on-orbit-manufacturing, capacitor, propulsion, lab-test, darpa, not-peer-reviewed]
---

# Tiverton and Devon Astronomical Society - Lecture on On Orbit Manufacturing and Quantized Inertia

<!-- local-only-note -->
> 📁 **Local only:** `slides.pdf` (licence `all-rights-reserved`) is kept out of the public repository. The openly licensed `paper.pdf` is included.

**Citation:** Arundal, R., Graham-Jones, J. & McCulloch, M. (2023). *Tiverton and Devon Astronomical Society - Lecture on On Orbit Manufacturing and Quantized Inertia*. Lecture slides, University of Plymouth (School of Engineering, Computing and Mathematics), deposited in PEARL 2023-02-03. https://pearl.plymouth.ac.uk/secam-research/1399

The stored `slides.pdf` has 86 pages. PDF pages 1–2 are PEARL cover sheets (copyright notice and citation). **The slides start on PDF page 3.** Page numbers below are PDF page numbers. The deck is a public lecture, not peer-reviewed; PEARL files it as a conference proceeding. The PEARL cover sheet says all content is protected by copyright, so the copy is treated as all-rights-reserved.

**TL;DR:** A two-part public lecture given in February 2023. Arundal (with Graham-Jones) presents a PhD-style research programme on on-orbit manufacture (OOM) of spacecraft struts and trusses and a cost/logistics tool (OOMSAT), and identifies propulsion as a bottleneck. McCulloch then presents QI and the results of a University of Plymouth symmetric-capacitor test campaign (Jul 2022 – Jan 2023). He reports weight changes of up to 10 mg (0.1 mN) that reverse when the capacitor is flipped, a claimed 0.3 N/kW, and late results "close to QI predictions". His conclusion slide says lab tests have shown thrust "(probably!)".

## What the lecture covers

### Part 1: On-orbit manufacture (pp. 3–28, appendix pp. 69–86)
- Defines OOM as "Spacecraft building Spacecraft…In Space". The current focus is making a space-qualified strut that can be assembled into trusses attached to customer satellites (p. 5). OOM is compared with on-orbit servicing.
- Motivations: infrastructure for colonisation and resource acquisition, larger telescopes and antenna reflectors, and interstellar "world ships" (pp. 7–22).
- Material sources: recycled plastics, salvaged space debris, asteroid mining and lunar aluminium from regolith (pp. 9–13).
- Example product: an antenna reflector frame grown strut by strut around an electronics module (pp. 14, 17). Mission concepts include staged builds and rendezvous, OOM during a voyage, and lunar/Mars ground facilities (pp. 19–23).
- A technology roadmap from concept through lab prototype to an orbital demonstrator (p. 18).
- **OOMSAT** (OOM System Architecture Tool). A default scenario uses a 50 kg micro-satellite, 80% freight allocation, aluminium (2710 kg/m³) pipes 1000 mm × 25 mm with a 3 mm wall, Isp 1000 s, Δv 10 km/s, $125/kg propellant and $2750 plant operating cost per yield (pp. 24, 71). Logistics results show that the breakeven price per pipe falls steeply as specific impulse rises above a few hundred seconds (pp. 25–27, 75, 78–80).
- Bridge to Part 2: moving OOM freight is a significant challenge, propellant volume takes up cargo space, and QI is presented as "a potential opportunity" for propulsion (p. 28).
- Appendix: OOMSAT algorithm and logistics app, a research roadmap, and two mission specifications. One is a LEO (250 km) laser-welded telescope-frame facility with 500 W and 100 kg. The other is a lunar-orbit casting facility with 5000 W and 2.5 t (pp. 69–86).

### Part 2: Quantised inertia (McCulloch, pp. 29–66)
- Background slide (p. 30): BSc York 1991, PhD Liverpool 1995, Met Office 1998–2008, "2008-now. Lecturer in Geomatics … at Plymouth University". He says he has "published 26 papers proposing quantised inertia & two books".
- Standard QI case: galaxy rotation and arguments against dark matter (pp. 31–32, 37), inertia from Unruh radiation damped by horizons (pp. 33–34), the low-acceleration formula m′ = m(1 − 2c²/(aΘ)) (p. 36), the uncertainty-principle derivation (p. 38), and the 153-galaxy SPARC fit (p. 40).
- Cites Lynch et al. 2021 (Phys. Rev. D 104, 025015) as "Unruh Radiation was Confirmed Last Year" (p. 35).
- Propulsion: "If We Understand Inertia Then We Can Control It" (p. 41), the DARPA project (p. 42), and the Becker & Bhatt capacitor results (pp. 43–46).
- Plymouth "Quantized Inertia Horizon Engine Development & Laboratory Setup" (pp. 47–56), test results (pp. 57–63), applications and an interstellar mission (pp. 64–65), and conclusions (p. 66).

## QI claims made

### Theory and background
- QI is "the first mechanistic model for inertial mass", predicts galaxy rotation without dark matter, and is "the first lab-testable cosmology" (p. 66).
- **DARPA:** "I was contacted by DARPA. I applied for funding & was awarded $1.3M". The slide is headed "DARPA Project, 2018-Now", with the aim "to demonstrate scalable thrust from QI in the lab" (p. 42). The Dresden null results from the same programme are not mentioned.

### Capacitor thrust (Becker & Bhatt, 2018)
- Becker & Bhatt's set-up is shown as 5000 V, 10 µA, 2.5 cm plates and 10–60 µm dielectric. The slide asks: "Susceptibility to electronic artefacts or tension of cables?" (p. 43).
- QI explanation: the capacitor plates reverse the usual Unruh-radiation gradient behind an accelerated electron, so the electron "gets an extra kick forward which is translated to the anode" (p. 44).
- The force formula F ≈ 0.00014 IA/d² is credited to McCulloch's 2021 ResearchGate preprint and compared with Becker & Bhatt's data (p. 45).
- **"Experimentum Crucis – Rindler Horizons are Real!"** (p. 46): a metal baffle inserted inside the computed Rindler-horizon distance (about 2 cm for a 17–24 µm capacitor) gives "equal and opposite" thrust, and beyond it the force is again towards the anode. The slide calls this "direct proof the cause is quantised inertia". No data are shown on the slide. This matches the "blocker" result in Becker & Bhatt's preprint.

### Plymouth test campaign (pp. 47–63)
- **Set-up.** The slides are headed "May-Feb 2023" (p. 47). The campaign used a non-vacuum test chamber with a wooden frame, a capacitor resting on a 3U-CubeSat mock superstructure above a digital scale, and Galinstan (Ga-In-Sn) liquid-metal reservoirs for invertible ("flippable") contacts (pp. 49, 52–53). Stack designs date from June 2022. The "Toastie V3" acrylic press dates from 21 Sep 2022 (pp. 50–51). A 25 µm Kapton dielectric came on 25 Sep 2022, and that date also records "bullet hole" capacitor damage attributed to heated air pockets (pp. 54–55). From 2 Oct 2022 a suspended lightbulb was used to preheat the stack to about 50 °C, to be removed before testing (p. 56). A 150–200 mm separation from the scale was used to limit electrostatic effects (p. 52).
- **Thrust (p. 58):** "Thrusts of up to 10mg are being regularly seen and reverse on flipping the capacitor. 10mg is 0.1mN." The authors say the 1 W of heating gives "a thrust to power ratio of 0.3 N/kW", "15 times better than ion drives, without fuel!". A log-scale timeline (15 Jul 2022 – Jan 2023) plots observed mass change against two QI predictions, with "Correlation = 0.71".
- **Comparison with theory (p. 59):** the predicted/observed ratio was "erratic" in phase 1 (Jul–Sep 2022), with ratios from about −6 to +11. It improved after shielding, Galinstan and "Vitrek" equipment were added in phase 2. With heating above 50 °C, the phase 3 results (runs x176, x179, Jan 2023) "are now close to QI predictions".
- **Comparison with Becker & Bhatt (p. 60):** three recent runs (x176, x177, x179) lie on the observed = predicted line on a log–log plot, together with the earlier B&B point.
- **Separation and area test (p. 61):** 4 × 4 cm plates with 16 µm and 8 µm separations are said to agree reasonably with the predicted lines. The slide adds: "However, the larger plates (10cm, yellow) should produce more thrust…", meaning the 10 cm, 25 µm capacitors fell below prediction. Some 16 µm runs (x70, x72) gave negative weight changes of up to about −7 mg.
- **Artefacts considered (p. 62):**
  - Buoyancy from heated air pockets is said to be excluded by flipping.
  - Body forces are said to be "mostly excluded" by the Galinstan contacts.
  - Radiation pressure from a 42 W bulb is put at 0.014 mg.
  - Earth's magnetic field force is put at about 1.5 × 10⁻⁷ N, against 10⁻⁴ N observed.
  - "An electrostatic force was identified and subtracted from runs 106-150."
  - Wire–wire magnetic interactions are said to be "way too small".
- **Comparison with Dawn (p. 63):** Dawn's ion drive gave 90 mN from 2100 W. The slide contrasts this with "~0.1 mN (10mg) at Plymouth" for a ~3 kg 3U CubeSat with no propellant using 1 W, which would take a 3U craft from 0–60 mph in 10 days.

### Applications (pp. 64–65)
- Station keeping and OOM, fuel-free satellites, flying cars, hovering structures, inertial damping, "Energy from the vacuum", 100 AU in 2 years, and interstellar travel.
- **Proxima Centauri mission:** a SAFE-400 fission reactor (512 kg, 100 kW) drives a 5 kg QI horizon drive at an assumed **10 N/kW**, giving 1000 N on a 567 kg craft. The slide works this out to 1.6 m/s², 0.5c in 3 years, and about 11.6 years Earth time (10.6 ship time) to Proxima b. The 10 N/kW is about 30× the 0.3 N/kW claimed from the lab.

### Mentions checked
- **IVO Ltd** and Richard Mansell are **not mentioned** in the deck. There is no mention of the Quantum Drive or any in-orbit test.
- **"OTP"**: the four case-insensitive text-layer matches are all inside the word "Foot**p**rint" ("Footprint") in the OOMSAT algorithm diagrams (pp. 73–74). They do not refer to Rogue Space Systems' OTP satellites or anything else. The deck has no mention of OTP-2.
- No Tajmar/Dresden results are shown.

## Editorial checks (our arithmetic, not the source's)
- 10 mg × g ≈ 0.098 mN. At the stated 1 W that is about **0.1 N/kW**, not the 0.3 N/kW stated on p. 58. The 0.3 figure would need about 30 mg per watt, or under 0.33 W of input. The 1 W is described as heating power. The deck does not give the electrical input power of the Plymouth capacitors. For comparison, the Becker & Bhatt set-up shown on p. 43 (10 µA at 5000 V) would draw 0.05 W.
- Using the deck's own Dawn figures (p. 63), 90 mN / 2.1 kW ≈ 0.043 N/kW. "15 times better" would need about 0.64 N/kW. At 0.1 N/kW the ratio is about 2.3×, and at 0.3 N/kW about 7×.
- A photon rocket gives 3.3 µN/kW, so 0.1 N/kW is about 3 × 10⁴ times the photon limit.
- The 0–60 mph in 10 days figure is consistent with 0.1 mN on 3 kg (about 9.4 days).
- These are weight changes on a digital scale in air, near kV electrodes, with a heated stack. Those are the conditions where Dresden's artefact list applies (buoyancy and convection from heating, electrostatic and cable forces). The deck itself subtracts an electrostatic artefact from 45 runs and reports that the 10 cm plates did not scale as predicted.

## Notable quotes
> "Thrusts of up to 10mg are being regularly seen and reverse on flipping the capacitor." (p. 58)

> "This is direct proof the cause is quantised inertia." (p. 46, on the Rindler-horizon baffle test)

> "Lab tests have shown thrust (probably!). The next stage is as yet unclear…" (p. 66)

## Criticisms & responses
- No criticism is addressed in the deck beyond its own artefact slide (p. 62).
- The single clean independent capacitor test, Tajmar & Schreiber 2020, used a Faraday/mu-metal box, an on-board HV supply and Galinstan feeds. It found < 0.3 mg against 6.8 mg predicted from a fit to Becker & Bhatt, a claim "ruled out by an order of magnitude" with replication caveats: [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md). The Plymouth set-up borrows Galinstan contacts but runs in air with an exposed scale and heating.
- DARPA-funded Dresden tests of QI laser resonators and fibre loops found no thrust at nN level, at least four orders of magnitude below QI predictions: [2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md). The lecture's DARPA slide (p. 42) does not mention them.
- The Becker & Bhatt preprint on which the capacitor case rests is not peer-reviewed and used a consumer digital scale: [2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md).
- The Plymouth results appear here only as slides, and no paper with methods or raw data was located. McCulloch's blog reported earlier Plymouth runs as about 10 mg, "only 1/3 of the force predicted" (see [propulsion.md](../../02-evidence/propulsion.md)). By Feb 2023 the deck reports agreement for the heated runs.

## Related
- Evidence: [propulsion.md](../../02-evidence/propulsion.md), [lab-tests.md](../../02-evidence/lab-tests.md), [galaxy-rotation.md](../../02-evidence/galaxy-rotation.md)
- Sources: [2018-bhatt-capacitor-thrust](../../04-experiments/2018-bhatt-capacitor-thrust/README.md), [2021-mcculloch-symmetric-capacitors](../../01-papers/2021-mcculloch-symmetric-capacitors/README.md), [2022-mcculloch-qi-thrust-casimir](../../01-papers/2022-mcculloch-qi-thrust-casimir/README.md), [2020-tajmar-capacitor-thrust](../../03-criticism/2020-tajmar-capacitor-thrust/README.md), [2022-neunzig-laser-resonators](../../03-criticism/2022-neunzig-laser-resonators/README.md), [2024-mcculloch-proxima-centauri](../../01-papers/2024-mcculloch-proxima-centauri/README.md)
- People/orgs: [mike-mcculloch.md](../../06-people-orgs/mike-mcculloch.md), [darpa-2018-award.md](../../06-people-orgs/darpa-2018-award.md), [ivo-ltd.md](../../06-people-orgs/ivo-ltd.md) (not mentioned in the deck), [university-of-plymouth.md](../../06-people-orgs/university-of-plymouth.md)
