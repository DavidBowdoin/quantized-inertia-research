---
title: "Earth flyby anomaly"
tags: [flyby-anomaly, solar-system, spacecraft-navigation]
verdict: contested
---

# Earth flyby anomaly

## The phenomenon and the data
- Several spacecraft showed small, unexplained changes in asymptotic speed after Earth gravity-assist flybys: **Δv∞ ≈ 1–10 mm/s**, with uncertainties as small as 0.05–0.1 mm/s ([Iorio 2015](../01-papers/2015-iorio-solar-system-anomalies/README.md)).
- Values used by McCulloch (from Anderson et al. 2008, *PRL* 100, 091102; [2008-mcculloch-flyby-anomalies-mnras](../01-papers/2008-mcculloch-flyby-anomalies-mnras/README.md)):

| Flyby | Observed Δv (mm/s) |
|---|---|
| Galileo-I (1990) | 3.92 ± 0.08 |
| Galileo-II (1992) | −4.6 ± 0.08 (corrected for atmospheric drag) |
| NEAR (1998) | 13.46 ± 0.13 |
| Cassini (1999) | −2 |
| Rosetta (2005) | 1.8 ± 0.05 |
| Messenger (2005) | 0.02 ± 0.05 |

- **Null flybys:**
  - Rosetta's 2nd and 3rd Earth flybys showed no anomaly ([Iorio 2015](../01-papers/2015-iorio-solar-system-anomalies/README.md)).
  - EPOXI showed zero anomaly, as McCulloch himself reported ([2011-mcculloch-tajmar-effect](../01-papers/2011-mcculloch-tajmar-effect/README.md), p. 7).
  - A reconstruction of Juno's October 2013 flyby found no anomalous velocity change at or near perigee (Thompson et al., AAS 14-435, [NTRS 20160008163](https://ntrs.nasa.gov/citations/20160008163)). Iorio notes that Anderson's empirical formula had predicted ~7 mm/s for Juno.
- **Empirical fit:** Anderson et al.'s formula Δv∞/v∞ = (2Ω⊕R⊕/c)(cos δ_in − cos δ_out). It does not contain G and "failed to account for the null result" of the later Rosetta flybys.

## Mainstream explanation(s)
- There is no accepted explanation. Iorio (2015) writes that "No doubts exist on the existence of such an anomaly" and that it "has always resisted any attempt of explanation". He adds that Pioneer-type thermal models "do not seem" to work for it.
- Several conventional and gravitational proposals exist, but "none has proved itself fully satisfactorily so far".
- Iorio's general test for any new-physics explanation has two parts:
  - It must be confirmed independently of the flyby data.
  - It must explain why bound Earth satellites show nothing.
- The later null flybys (Rosetta 2/3, EPOXI, Juno) are consistent with modelling or data artifacts as well as with a selective effect. The READMEs here do not settle which.

## QI's prediction
- **JBIS 2008** ([2008-mcculloch-flyby-anomalies-jbis](../01-papers/2008-mcculloch-flyby-anomalies-jbis/README.md)):
  - **Mechanism:** inertia collapses for ~10⁻⁷ s when the craft's acceleration relative to the galactic centre (approximated by the Sun) passes near zero.
  - **Predictions:** Galileo 2.6, NEAR 1.2, Cassini 1.4 and Rosetta 1.9 mm/s, against observed 3.92, 13.46, 0.11 and 1.82 mm/s.
  - **Sensitivity to H:** the paper itself says the result "succeeds for only a very narrow range of values of H".
    - H = 2.33 × 10⁻¹⁸ s⁻¹ works.
    - H = 2.30 × 10⁻¹⁸ s⁻¹ gives jumps below 1 mm/s.
    - H ≥ 2.34 × 10⁻¹⁸ s⁻¹ gives negative jumps.
  - The author later described the paper as mostly superseded (flagged as unverified in its README).
- **MNRAS Letters 2008** ([2008-mcculloch-flyby-anomalies-mnras](../01-papers/2008-mcculloch-flyby-anomalies-mnras/README.md)):
  - **Mechanism:** the acceleration is now taken relative to all the mass of the spinning Earth, with mean value a = (0.07 v_e²/R) cos φ. The predicted velocity change is

  $$ dv' = \frac{\beta\pi^2 R c^2}{0.07\, v_e^2\, \Theta}\left(\frac{v_2\cos\phi_1 - v_1\cos\phi_2}{\cos\phi_1\cos\phi_2}\right) = 2.8\times10^{-7}\left(\frac{v_2\cos\phi_1 - v_1\cos\phi_2}{\cos\phi_1\cos\phi_2}\right) $$

  - **Predictions** (mm/s): Galileo-I 2.9 ± 0.6, Galileo-II −0.9 ± 0.2, NEAR 20.1 ± 4.0, Cassini 0.9 ± 0.2, Rosetta 3.2 ± 0.6, Messenger −1.3 ± 0.2.
  - **Agreement:** the paper reports agreement for three of six flybys. The others are off by 1–3 mm/s.
  - **Correlation:** r = 0.94, "not significant at the 5% level" (p ≈ 30%).
  - **Further prediction:** larger anomalies for slower-spinning, larger bodies, with the Rosetta Mars flyby (2007) as a test (about double Earth's anomaly). No check of this prediction was found.
  - **Unbound-only restriction:** the paper concedes that the model "only seems to apply to unbound trajectories and the reason for this is unknown". Otherwise it would conflict with laboratory equivalence-principle tests.
- **Later admissions:**
  - McCulloch (2011) reported EPOXI's zero anomaly where MiHsC predicted a large one, and attributed it to EPOXI's larger periapse (49,835 km).
  - He added that fits improve "if the accelerations within the Sun are assumed to be 1 m/s². It is not known whether this value is realistic." ([2011-mcculloch-tajmar-effect](../01-papers/2011-mcculloch-tajmar-effect/README.md))

## Independent tests, critiques and null results
- No independent group has reproduced McCulloch's flyby calculations. The JBIS paper explicitly asks that "other specialist groups can reproduce these results".
- **Changing definition of acceleration:** the two 2008 papers define the acceleration that enters MiHsC differently (galactic centre or Sun vs. the rotating Earth's particles), and both differ from the 2007 Pioneer paper. This is a modelling choice that critics can read as an extra degree of freedom.
- **Null flybys:** Juno (2013), EPOXI and the later Rosetta flybys constrain all flyby-anomaly models. The EPOXI null was a failed MiHsC prediction.
- **Iorio (2015)** cites McCulloch 2008 among the modified-gravity proposals, none of which is "fully satisfactory".
- **Press coverage:** articles presented flyby prediction as a QI success ([2016-mittechreview-flyby-emdrive](../07-media/2016-mittechreview-flyby-emdrive/README.md), [2016-register-emdrive-inertia](../07-media/2016-register-emdrive-inertia/README.md)). Koberlein criticised uncritical repetition of such claims ([2017-koberlein-doing-it-wrong](../07-media/2017-koberlein-doing-it-wrong/README.md)).

## Assessment
The early flyby anomalies are real features of the tracking data and have no accepted explanation, so the phenomenon itself is still open. Later, better-documented flybys (Juno, EPOXI, Rosetta 2/3) show no anomaly, which makes any physical effect harder to sustain. QI's 2008 MNRAS model reproduces the latitude dependence of Anderson's empirical formula and gets three of six flybys within error. However, its overall correlation is not statistically significant. The earlier JBIS model depended on tuning H to about 1%. The theory must also be restricted, without explanation, to unbound trajectories, and it predicted an EPOXI anomaly that was not seen. Only McCulloch has published the QI flyby calculation, so this counts at most as weak, author-only support for QI on an unresolved anomaly.

## Sources
- [2008-mcculloch-flyby-anomalies-jbis](../01-papers/2008-mcculloch-flyby-anomalies-jbis/README.md)
- [2008-mcculloch-flyby-anomalies-mnras](../01-papers/2008-mcculloch-flyby-anomalies-mnras/README.md)
- [2011-mcculloch-tajmar-effect](../01-papers/2011-mcculloch-tajmar-effect/README.md) (EPOXI admission)
- [2015-iorio-solar-system-anomalies](../01-papers/2015-iorio-solar-system-anomalies/README.md)
- [2017-taylor-laser-resonators](../01-papers/2017-taylor-laser-resonators/README.md) (cites flybys as motivation)
- [2016-mittechreview-flyby-emdrive](../07-media/2016-mittechreview-flyby-emdrive/README.md), [2016-register-emdrive-inertia](../07-media/2016-register-emdrive-inertia/README.md), [2017-koberlein-doing-it-wrong](../07-media/2017-koberlein-doing-it-wrong/README.md)
- Juno 2013 reconstruction: Thompson et al., AAS 14-435, [NTRS 20160008163](https://ntrs.nasa.gov/citations/20160008163)
- Related evidence: [pioneer-anomaly](pioneer-anomaly.md), [lab-tests](lab-tests.md)
