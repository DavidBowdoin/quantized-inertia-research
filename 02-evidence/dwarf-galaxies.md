---
title: "Ultra-faint dwarf galaxies"
tags: [dwarf-galaxies, dark-matter, mond, velocity-dispersion]
verdict: supported-by-author-only
---

# Ultra-faint dwarf galaxies

## The phenomenon and the data
- Milky Way ultra-faint dwarf satellites have velocity dispersions far above what their visible mass can bind under Newtonian gravity.
- Implied dark-to-visible mass ratios reach about 2600× for Segue 1 and 3600× for Triangulum II, as cited in [McCulloch 2017](../01-papers/2017-mcculloch-dwarf-galaxies/README.md).
- Observed dispersions used there (km/s): Triangulum II 5.1 (+4.1/−1.4), Segue 1 3.7 (+1.4/−1.1), Ursa Major II 6.7 ± 1.4, Coma Berenices 4.6 ± 0.8, Boötes II 10.5 ± 7.4, Boötes I 5.7 ± 3.3, Canes Venatici II 4.6 ± 1.0, Leo IV 3.3 ± 1.7, Canes Venatici I 13.9 (+3.2/−2.5), Ursa Major I 9.3 (+11.7/−1.2), Hercules 5.0 ± 1.0.
- Visible masses assume M/L = 1.95, with roughly a factor-of-2 uncertainty.
- Rotationally supported discs show a minimum baryonic mass of about 10⁹ M☉ within 500 pc (McGaugh et al. 2010, used in [McCulloch 2010](../01-papers/2010-mcculloch-minimum-accelerations/README.md)).

## Mainstream explanation(s)
- **Dark-matter-dominated halos.** The dwarf-galaxy paper does not compare QI with halo fits.
- **Binary-star inflation of small-sample dispersions:**
  - Triangulum II was revised to **< 3.4 km/s** (90% confidence) after a binary was identified (Kirby et al. 2017, ApJ 838, 83, [arXiv:1703.02978](https://arxiv.org/abs/1703.02978)).
  - Boötes II's value was likely inflated by a radial-velocity binary (Ji et al. 2016, [arXiv:1510.07632](https://arxiv.org/abs/1510.07632)).
  - The paper itself notes that binaries may explain the excess in Segue 1, Boötes II, Leo IV and Hercules.
- **MOND** treats dwarf satellites with the external field effect (EFE) of the Milky Way, which the QI paper omits by argument.

## QI's prediction
- **Minimum disc mass.** [McCulloch 2010](../01-papers/2010-mcculloch-minimum-accelerations/README.md): M_dark = 2c²r²/(GΘ) gives a minimum apparent disc mass of 1.1 × 10⁹ M☉ within 500 pc (observed ~10⁹ M☉). Lighter pressure-supported ellipticals (~10⁷ M☉) are explained only qualitatively.
- **Velocity dispersions.** [McCulloch 2017, Ap&SS 362, 57](../01-papers/2017-mcculloch-dwarf-galaxies/README.md), with Θ = 8.8 × 10²⁶ m:

  $$ v = \left(\frac{2GMc^2}{\Theta}\right)^{1/4} $$

  - Predicted values (km/s): Tri II 2.2, Seg 1 2.1, UMa II 3.8, Com Ber 3.8, Boo II 2.7, Boo I 6.3, CVn II 4.5, Leo IV 4.6, CVn I 10.5, UMa I 5.2, Her 6.6.
  - RMS differences from observation: **Newton 6.5, MOND 3.6, QI 3.2 km/s**. The paper says QI "slightly outperforms MoND" with no adjustable parameter.
  - Same formula as McCulloch 2012 for galaxies and clusters ([2012-mcculloch-galactic-scales](../01-papers/2012-mcculloch-galactic-scales/README.md)).

## Independent tests, critiques and null results
- **Deep-MOND form.** Eq. 11 is deep MOND with a₀ = 2c²/Θ ≈ 2.0 × 10⁻¹⁰ m s⁻². Every QI value is the MOND value × (2.0/1.2)^¼ ≈ 1.14. The comparison therefore shows only that a larger a₀ fits these 11 systems slightly better (editorial check in the README).
- **Speed vs dispersion.** The paper compares a circular-orbit speed with line-of-sight dispersions. It uses no dispersion-supported prefactor and omits the EFE.
- **Revised data.** Two key data points have since been revised downward because of binaries, and both were cases where the observed value lay above QI. With Tri II below 3.4 km/s, QI's 2.2 km/s is no longer under-predicting that system.
- **Same Θ caveat as for rotation curves.** Earlier papers used Θ = 2.6–2.7 × 10²⁶ m ([galaxy-rotation](galaxy-rotation.md)).
- **Theoretical basis.** Renda 2019 and Dickmann & Dickmann 2023 question it ([derivation](derivation.md)).
- Hernandez et al. 2019 cite this paper (as McCulloch 2017, Ap&SS 362, 57) and call the vacuum/dark-energy route "unsatisfactory" ([2018-hernandez-bounding-curvature](../01-papers/2018-hernandez-bounding-curvature/README.md)).
- No independent group has tested QI on dwarf galaxies in the sources collected here.

## Assessment
On 11 ultra-faint dwarfs, McCulloch's QI formula fits slightly better than MOND with the standard a₀ (RMS 3.2 vs 3.6 km/s). It is much better than Newton with visible matter only, but the comparison has three weaknesses:
- The QI formula is mathematically deep MOND with a larger a₀.
- The dispersion modelling is simplified, and the external field effect is left out.
- Several of the dispersions used have since been revised downward because of binary stars.

The paper's own statement that "it is not known if quantised inertia is consistent with Solar system data" also limits the claim. The result is a modest, author-only consistency check, not a discriminating test.

## Sources
- [2017-mcculloch-dwarf-galaxies](../01-papers/2017-mcculloch-dwarf-galaxies/README.md)
- [2010-mcculloch-minimum-accelerations](../01-papers/2010-mcculloch-minimum-accelerations/README.md)
- [2012-mcculloch-galactic-scales](../01-papers/2012-mcculloch-galactic-scales/README.md)
- [2017-pickering-resonant-cavity](../01-papers/2017-pickering-resonant-cavity/README.md)
- [2018-hernandez-bounding-curvature](../01-papers/2018-hernandez-bounding-curvature/README.md)
- [2019-renda-sceptical](../03-criticism/2019-renda-sceptical/README.md)
- [2018-mcculloch-dark-matter-scitrends](../07-media/2018-mcculloch-dark-matter-scitrends/README.md)
- Kirby et al. 2017, [arXiv:1703.02978](https://arxiv.org/abs/1703.02978); Ji et al. 2016, [arXiv:1510.07632](https://arxiv.org/abs/1510.07632) (as cited in the dwarf-galaxies README)
- Related evidence: [galaxy-rotation](galaxy-rotation.md), [globular-clusters](globular-clusters.md)
