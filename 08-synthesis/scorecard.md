---
title: "Quantized Inertia: scorecard"
tags: [synthesis, scorecard]
as_of: 2026-10-18
---

# Quantized Inertia: scorecard (as of October 2026)

> **Editorial.** This page is our own analysis. It is built from the source READMEs and the [evidence notes](../02-evidence/INDEX.md), and every row links to them. Where we did our own arithmetic, we say so.

## 1. The literature at a glance

| | Count | Notes |
|---|---|---|
| Sources catalogued | 94 | 61 papers · 9 critiques/null results · 4 experiment reports · 20 books/press |
| Theory papers by McCulloch (alone or with co-authors) | ~36 | 2007–2025. Mostly *Astrophys. Space Sci.*, *EPL*, *MNRAS*, *Progress in Physics*, *Mod. Phys. Lett.* |
| Independent papers that **support** QI | ~6 | Pickering 2017, Taylor 2017, Giné (sole-author papers), Giné & Luciano 2020/21, Haug 2018 (viXra), Soli 2021. Giné's 2016/17/20 papers are co-authored with McCulloch, so we do not count them as independent |
| Independent papers that **test** a QI prediction | 3–4 | Neunzig et al. 2021/22 (lasers, fibre loops), Tajmar & Schreiber 2020 (capacitors), Banik et al. 2024 (wide binaries; its QI conclusion rests on Pittordis & Sutherland 2019) |
| Of those, positive results | **0** | The only positive lab claim (Bhatt & Becker 2018, a digital scale) is from McCulloch's own group and has not been independently replicated |
| Published critiques of the derivation | 2 | Renda 2019 (*MNRAS*), Dickmann & Dickmann 2023 |
| Papers that cite QI in passing | many | Smolin 2017, Cadoni 2019, Iorio 2015, Turyshev 2010, Hernandez 2018: cited as one idea among many, which is not an endorsement |

## 2. Claim by claim

| # | Claim | QI prediction | Independent confirmation? | Status | Strength of QI case |
|---|---|---|---|---|---|
| 1 | [Pioneer anomaly](../02-evidence/pioneer-anomaly.md) | 6.9 × 10⁻¹⁰ m s⁻² | Anomaly explained by thermal recoil | ❌ mainstream-explained | Weak: the original motivating case is gone, and QI also predicted an inner-Solar-System effect that isn't seen |
| 2 | [Flyby anomaly](../02-evidence/flyby-anomaly.md) | 3/6 flybys within error | No; EPOXI and Juno null | ⚠️ contested | Weak |
| 3 | [Galaxy rotation](../02-evidence/galaxy-rotation.md) | MOND-like, a₀ = 2c²/Θ | No independent published fit. Our [A1 refit](../09-analysis/a1-sparc-rar-refit/README.md): fixed Θ = 8.8 × 10²⁶ m over-predicts deep-MOND accelerations by 17–32% | 🟩 author-only | **Moderate**: it is a real, interesting coincidence (a₀ ≈ cH/2π), but it carries over MOND's successes *and* its problems |
| 4 | [Wide binaries](../02-evidence/wide-binaries.md) | Flat Δv, no external field effect | Disputed; Banik 19σ for Newton | ⚠️ contested | Weak to moderate: even the pro-anomaly groups favour MOND *with* an external field effect, which QI lacks |
| 5 | [Dwarf galaxies](../02-evidence/dwarf-galaxies.md) | Deep-MOND, larger a₀ | No | 🟩 author-only | Weak: key data points were later revised (binary stars) |
| 6 | [Cosmic acceleration](../02-evidence/cosmic-acceleration.md) | ~cH | No | 🟩 author-only | Weak: order of magnitude only, with no H(z) fit |
| 7 | [Cosmology](../02-evidence/cosmology.md) | Toy model | No | 🟩 author-only | Weak: no CMB spectrum or structure formation; Bullet Cluster unaddressed (see [dark-matter](../05-context/dark-matter.md)) |
| 8 | [EmDrive](../02-evidence/emdrive.md) | mN-level thrust | **Tested: null** | ❌ refuted-or-null | The data it explained were artefacts |
| 9 | [Propulsion / lab thrust](../02-evidence/propulsion.md) | Laser, capacitor, IVO | **Tested: null** (≥ 10⁴ below the prediction) | ❌ refuted-or-null | Strongest evidence *against* QI |
| 10 | [Derivation](../02-evidence/derivation.md) | m_i = m(1 − 2c²/aΘ) | Two critiques; partial concession by McCulloch (2026 blog) | ⚠️ contested | Weak: the original derivation is flawed; the newer derivations have not been assessed |
| 11 | [Other anomalies](../02-evidence/other-anomalies.md) | Tajmar, Podkletnov, proton radius… | Underlying effects withdrawn or resolved | ❌/🟩 | Weak |

## 3. Bottom line

1. **QI's best evidence is a numerical coincidence it shares with MOND.** The acceleration scale 2c²/Θ falls near MOND's a₀ ≈ 1.2 × 10⁻¹⁰ m s⁻² and near cH₀. That coincidence is genuine and widely noticed (Milgrom pointed it out in 1983). It does not single out QI over other horizon-based or entropic MOND-like models (see [mond](../05-context/mond.md)).
2. **"No adjustable parameters" is weaker than claimed.** Θ has taken values from 2.6 to 8.8 × 10²⁶ m across papers (a factor of 3.4). With the early value, galaxy rotation speeds were over-predicted by 30–54% (2012). The later value does much better, but our own refit of the SPARC data ([A1](../09-analysis/a1-sparc-rar-refit/README.md), editorial) finds it still too high by 17–32% at low acceleration and clearly worse than a one-parameter fit (ΔBIC ≈ +420). Per-galaxy fits ([A1b](../09-analysis/a1b-sparc-per-galaxy/README.md)) confirm this. The data prefer Θ ≈ 1.2–1.4 × 10²⁷ m, which is neither value QI has used ([equations.md](../00-overview/equations.md#7-discrepancies-and-inconsistencies-between-papers)). Choosing between cosmological length scales after seeing the data is in effect one discrete free parameter.
3. **Every independent controlled test of QI's distinctive predictions has been null.** Those predictions are laboratory and propulsion thrust: lasers, fibre loops, capacitors and EmDrive cavities. QI is unusual among MOND-like ideas in predicting effects in the lab, which makes it more falsifiable, and so far those tests have gone against it.
4. **The theoretical foundation is disputed.** Renda (2019) and Dickmann & Dickmann (2023) argue the derivation fails, and McCulloch accepted part of Renda's point in 2026. The newer derivations (uncertainty principle, information erasure) have not been reviewed independently, and they depend on choices such as Δx = half the horizon circumference and log₂.
5. **The mainstream challenges to any no-dark-matter theory still apply**: Bullet Cluster lensing, CMB acoustic peaks, structure formation. We found **no QI calculation** of any of these.

**Overall verdict:** an interesting, falsifiable, MOND-like phenomenology. Its astrophysical support comes almost entirely from its author, its laboratory predictions have failed independent tests, and its derivation is contested. It is not ruled out as a description of low-acceleration astrophysics, but no evidence currently favours it over MOND or ΛCDM.

See also: [open questions](open-questions.md) · [what we could do next](ideas-and-tests.md) · [raw build notes](build-notes.md)
