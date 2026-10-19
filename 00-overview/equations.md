---
title: "Key equations of Quantized Inertia"
type: overview
updated: 2026-10-18
---

# Key equations of Quantized Inertia

This page collects the formulas used in the core QI/MiHsC papers. For each one it gives a short derivation sketch, defines the symbols and names the paper it comes from. The numbers were recomputed for this repository (`python3`, CODATA constants) and checked against the values printed in the papers. Where the two disagree, the difference is flagged. For the plain-language picture, see [what-is-qi.md](what-is-qi.md).

## 0. Symbols and constants

| Symbol | Meaning | Value used here |
|---|---|---|
| *c* | speed of light | 2.998 × 10⁸ m s⁻¹ |
| ħ, *h* | reduced / ordinary Planck constant | 1.055 × 10⁻³⁴ J s / 6.626 × 10⁻³⁴ J s |
| *k*, k_B | Boltzmann constant | 1.381 × 10⁻²³ J K⁻¹ |
| *G* | gravitational constant | 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² |
| *H*, H₀ | Hubble constant | 2.3 × 10⁻¹⁸ s⁻¹ in 2007 (≈ 71 km s⁻¹ Mpc⁻¹) |
| Θ | "Hubble diameter", the cosmic length in QI | 2c/H ≈ 2.6 × 10²⁶ m (2007–2016; printed as 2.7 × 10²⁶ m) or 8.8 × 10²⁶ m (co-moving diameter; 2017 on) |
| *a*, \|a\| | acceleration (QI uses its modulus, relative to surrounding matter) | — |
| m, m_g | ordinary / gravitational mass | — |
| m_i, m_I | inertial mass (QI-modified) | — |
| β | Wien constant 1/x₅, where x₅ ≈ 4.965 solves 5(1 − e⁻ˣ) = x | 0.2014 (rounded to 0.2 in the papers) |
| λₘ | peak wavelength of the Unruh spectrum | — |
| a₀ | MOND acceleration constant (empirical) | 1.2 × 10⁻¹⁰ m s⁻² |
| l_P, m_P | Planck length / mass | 1.616 × 10⁻³⁵ m / 2.176 × 10⁻⁸ kg |

---

## 1. Ingredients (standard physics)

**Unruh temperature** (Unruh 1976; used in every QI paper):

$$ T = \frac{\hbar a}{2\pi c k_B} $$

**Peak wavelength of the Unruh spectrum** (Wien's law with T as above; [2007](../01-papers/2007-mcculloch-pioneer-anomaly/README.md) Eq. 3):

$$ \lambda_m = \frac{hc}{x_5 k_B T} = \frac{4\pi^2\beta c^2}{a} $$

**Rindler horizon distance** for proper acceleration *a* (Rindler 2001; [2013](../01-papers/2013-mcculloch-asymmetric-casimir/README.md)):

$$ d_R = \frac{c^2}{a} $$

| *a* (m s⁻²) | T (K) | λₘ (m) | c²/a (m) |
|---|---|---|---|
| 9.81 (Earth surface) | 4.0 × 10⁻²⁰ | 7.3 × 10¹⁶ | 9.2 × 10¹⁵ |
| 6.9 × 10⁻¹⁰ | 2.8 × 10⁻³⁰ | 1.0 × 10²⁷ | 1.3 × 10²⁶ |
| 1.0 × 10⁻¹⁰ | 4.1 × 10⁻³¹ | 7.1 × 10²⁷ | 9.0 × 10²⁶ |

*At 9.81 m s⁻², the peak Unruh wavelength (7.3 × 10¹⁶ m) is already about 8 times the Rindler distance (9.2 × 10¹⁵ m).*

---

## 2. The original MiHsC formula (2007)

Source: [McCulloch 2007, MNRAS 376, 338](../01-papers/2007-mcculloch-pioneer-anomaly/README.md) ([astro-ph/0612599](https://arxiv.org/abs/astro-ph/0612599)).

**Assumption 1** is a Hubble-scale Casimir effect. Only wavelengths that fit twice the Hubble diameter are allowed:

$$ \lambda_n = \frac{2\Theta}{n}, \qquad n = 1, 2, 3, \dots, \qquad \Theta = \frac{2c}{H} $$

**Assumption 2** is that the "allowed" part of the spectrum scales *linearly* with the peak wavelength. F = 1 when λₘ → 0 (continuous spectrum) and F = 0 when λₘ → 4Θ:

$$ F = 1 - \frac{\lambda_m}{4\Theta} $$

**Assumption 3** is that inertial mass is proportional to the Unruh energy that is sampled. This gives m_I = F·m_g. Substituting λₘ:

$$ m_I = m_g\left(1 - \frac{\beta\pi^2 c^2}{a\,\Theta}\right) $$

**Pioneer equation of motion** ([2007](../01-papers/2007-mcculloch-pioneer-anomaly/README.md) Eqs. 10–12). Setting m_I a = GM☉m_g/r² gives

$$ a = \frac{GM_\odot}{r^2} + \frac{\beta\pi^2 c^2}{\Theta} = \frac{GM_\odot}{r^2} + \tfrac{1}{2}\beta\pi^2\,cH \approx \frac{GM_\odot}{r^2} + 0.99\,cH $$

The paper predicts an anomaly of 6.9 ± 3.5 × 10⁻¹⁰ m s⁻². The observed value was 8.74 ± 1.33 × 10⁻¹⁰ m s⁻².

**"Milgrom break" acceleration** ([2007](../01-papers/2007-mcculloch-pioneer-anomaly/README.md) Eq. 4). This is the acceleration at which λₘ = Θ:

$$ a = \frac{4\pi^2\beta c^2}{\Theta} \approx 2.6 \times 10^{-9}\ \text{m s}^{-2} $$

(The paper prints "26 × 10⁻¹⁰".)

---

## 3. The rounded form and the minimum acceleration (2010–2013)

Sources: [2010 EPL 90, 29001](../01-papers/2010-mcculloch-minimum-accelerations/README.md), [2012 Ap&SS 342, 575](../01-papers/2012-mcculloch-galactic-scales/README.md) ([1207.7007](https://arxiv.org/abs/1207.7007)) and [2013 EPL 101, 59001](../01-papers/2013-mcculloch-asymmetric-casimir/README.md) ([1302.2775](https://arxiv.org/abs/1302.2775)). All three print:

$$ m_I = m_g\left(1 - \frac{\beta\pi^2c^2}{|a|\Theta}\right) \sim m_g\left(1 - \frac{2c^2}{|a|\Theta}\right) $$

βπ² is 1.974 with β = 0.2 and 1.988 with β = 0.2014.

**Minimum acceleration** ([2010](../01-papers/2010-mcculloch-minimum-accelerations/README.md)). Take the orbit equation (1 − 2c²/|a|Θ)·a = GM/r². With M → 0 a non-zero solution remains:

$$ a = \frac{GM}{r^2} + \frac{2c^2}{\Theta}\,\hat{a} \quad\Rightarrow\quad a_{\min} = \frac{2c^2}{\Theta}, \qquad M_{\text{dark, apparent}} = \frac{2c^2 r^2}{G\Theta} $$

With Θ = 2c/H this becomes **a_min = cH**.

**Galaxy rotation, the Tully–Fisher relation** ([2012](../01-papers/2012-mcculloch-galactic-scales/README.md) Eqs. 2–9). Split the total acceleration into a mean part *a* and a local part a′:

$$ \left(1 - \frac{2c^2}{(|a|+|a'|)\Theta}\right)a = \frac{GM}{r^2} $$

Then *assume* a′ = 2c²/Θ at the galaxy's edge and a ≪ a′. This gives

$$ a^2 = \frac{GM|a'|}{r^2} \;\Rightarrow\; v^4 = GM|a'| = \frac{2GMc^2}{\Theta} $$

The paper uses a′ = 6.7 ± 0.6 × 10⁻¹⁰ m s⁻². For comparison, MOND's deep limit is v⁴ = GMa₀.

**Asymmetric Casimir force** ([2013](../01-papers/2013-mcculloch-asymmetric-casimir/README.md) Eqs. 2–11). A Rindler-scale cut acts from behind, u_left = u(1 − λa cosθ/4c²), and a Hubble-scale cut acts from the front, u_right = u(1 − λ/4Θ). The radiation pressure is F = uA/3. Integrating over angles gives

$$ dF_x = \frac{2\pi u\lambda A}{3}\left(\frac{1}{4\Theta} - \frac{\pi a}{16c^2}\right) \;\xrightarrow{\;a\ \text{large}\;}\; dF_x = -\frac{\pi^2 u\lambda A a}{24c^2} $$

With u = hc/(λV) and A/V = 1/l_P:

$$ F = -\frac{\pi^2 h}{24 c\, l_P}\,a \;\Rightarrow\; m_i \sim \frac{\pi^2 h}{24 c\, l_P} \approx 5.5\times10^{-8}\ \text{kg} \approx 2.5\,m_P $$

The paper calls this "about twice the Planck mass". [Giné & McCulloch (2016, MPLA)](../01-papers/2016-gine-unruh-temperatures/README.md) corrected the factor of two, to F = −π²hAa/(48cV), which gives ≈ 2.8 × 10⁻⁸ kg ≈ 1.29 m_P (as reported by Renda 2019).

---

## 4. Rederivations from horizons and the uncertainty principle (2016–2020)

**2016** ([EPL 115, 69001](../01-papers/2016-mcculloch-relativity-uncertainty/README.md); [1610.06787](https://arxiv.org/abs/1610.06787)). Assume that mass-energy *plus* the Heisenberg energy ħc/Δx is conserved:

$$ m_1c^2 + \frac{\hbar c}{\Delta x_1} = m_2c^2 + \frac{\hbar c}{\Delta x_2} \;\Rightarrow\; dm = \frac{\hbar}{c}\left(\frac{1}{\Delta x_2} - \frac{1}{\Delta x_1}\right) $$

Let horizons set the uncertainty: Δx₂ = c²/a (Rindler) and Δx₁ = Θ/2 (cosmic). Then

$$ dm = \frac{\hbar a}{c^3}\left(1 - \frac{2c^2}{a\Theta}\right) = 2\pi\beta\, m\left(1 - \frac{2c^2}{a\Theta}\right),\qquad 2\pi\beta \approx 1.26 $$

The bracket matches the earlier papers, but the overall magnitude is about 26% too large. The paper puts this down to treating the Rindler horizon as a sphere.

**2017** ([MPLA 32, 1750148](../01-papers/2017-mcculloch-information-loss/README.md), with Giné) derives the same bracket from information lost behind the Rindler and Hubble horizons.

**2020** ([Adv. Stud. Theor. Phys. 14, 1](../01-papers/2020-mcculloch-horizon-widths/README.md), with Giné). Take Δx to be half the horizon circumference, πc²/a and πΘ/2, and use ΔEΔx ~ ħc/2:

$$ \Delta E = \frac{\hbar c}{2}\left(\frac{a}{\pi c^2} - \frac{2}{\pi\Theta}\right) = \frac{\hbar a}{2\pi c}\left(1 - \frac{2c^2}{a\Theta}\right) = k_B T_{\text{Unruh}}\left(1 - \frac{2c^2}{a\Theta}\right) \;\Rightarrow\; m_i = m\left(1 - \frac{2c^2}{a\Theta}\right) $$

The paper says this gives the formula "exactly".

**MOND comparison** ([2020](../01-papers/2020-mcculloch-horizon-widths/README.md)). MOND's "simple" interpolation function, read as modified inertia, is

$$ m_i = \frac{m}{1 + a_0/a} = m\left(1 - \frac{a_0}{a} + \frac{a_0^2}{a^2} - \dots\right) $$

Its first two terms equal QI if a₀ → 2c²/Θ. (The PDF prints the third term with a minus sign, which is wrong for this series.)

---

## 5. Galaxy-scale relations (2017 onward)

Source: [McCulloch 2017, Ap&SS 362, 149](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md) ([1709.04918](https://arxiv.org/abs/1709.04918)), with Θ = 8.8 × 10²⁶ m.

**Radial acceleration relation** (Eqs. 6–8), starting from the 2012 force balance with |a′| = 2c²/Θ:

$$ a^2 = \frac{GM(|a| + |a'|)}{r^2} \;\Rightarrow\; a_{\text{pred}} = a_{\text{bar}}\sqrt{1 + \frac{2c^2}{a_{\text{bar}}\Theta}} $$

At large a_bar this is Newtonian. In the deep limit it becomes a = √(a_bar·2c²/Θ), the deep-MOND form with a₀ → 2c²/Θ ≈ 2.0 × 10⁻¹⁰ m s⁻².

The paper compares this with the empirical McGaugh et al. (2016) fit, a_obs = a_bar/(1 − e^(−√(a_bar/a₀))).

**Redshift dependence** (Eqs. 9, 12):

$$ \Theta_z = \frac{\Theta_{\text{now}}}{1+z} \;\Rightarrow\; v^4 = \frac{2GMc^2(1+z)}{\Theta_{\text{now}}} $$

So QI predicts stronger "missing-mass" effects at high redshift.

---

## 6. Numerical values

Computed with c = 2.998 × 10⁸ m s⁻¹:

| Θ (m) | Origin | 2c²/Θ (m s⁻²) | βπ²c²/Θ (β = 0.2014) | ÷ a₀ (1.2 × 10⁻¹⁰) | 1 − m_i/m at g = 9.81 |
|---|---|---|---|---|---|
| 2.607 × 10²⁶ | 2c/H, H = 2.3 × 10⁻¹⁸ s⁻¹ (the actual value of 2c/H for the 2007 H) | 6.90 × 10⁻¹⁰ (= cH) | 6.85 × 10⁻¹⁰ | 5.75 | 7.0 × 10⁻¹¹ |
| 2.7 × 10²⁶ | as printed in 2007, 2012, 2013 | 6.66 × 10⁻¹⁰ | 6.62 × 10⁻¹⁰ | 5.55 | 6.8 × 10⁻¹¹ |
| 8.8 × 10²⁶ | co-moving diameter (2017+) | 2.04 × 10⁻¹⁰ | 2.03 × 10⁻¹⁰ | 1.70 | 2.1 × 10⁻¹¹ |

Related numbers:
- cH₀/2π (Milgrom's coincidence) is about 1.1 × 10⁻¹⁰ m s⁻² for H₀ ≈ 70 km s⁻¹ Mpc⁻¹, close to a₀.
- m_i/m = 0.5 at |a| = 4c²/Θ, i.e. 1.4 × 10⁻⁹ (old Θ) or 4.1 × 10⁻¹⁰ m s⁻² (new Θ).
- For M = 10¹¹ M☉, v⁴ = 2GMc²/Θ gives v ≈ 307 km s⁻¹ (Θ = 2.7 × 10²⁶ m) or 228 km s⁻¹ (Θ = 8.8 × 10²⁶ m). Deep MOND gives v⁴ = GMa₀ ≈ (200 km s⁻¹)⁴.

![m_i/m versus acceleration](../assets/diagrams/low-acceleration-regime.svg)

---

## 7. Discrepancies and inconsistencies between papers

| # | Issue | Where |
|---|---|---|
| 1 | **The value of Θ changes.** 2c/H with H = 2.3 × 10⁻¹⁸ s⁻¹ is 2.61 × 10²⁶ m, but 2007, 2012 and 2013 print 2.7 × 10²⁶ m. The 2007 result of 6.9 × 10⁻¹⁰ matches 2.61 × 10²⁶. The 2012 result of 6.7 × 10⁻¹⁰ matches 2.7 × 10²⁶. The 2017 SPARC paper says the earlier papers used "2.6 × 10²⁶ m". From 2017 Θ = 8.8 × 10²⁶ m (co-moving diameter), which is ≈ 3.4 × larger and reduces the key scale from ≈ 6.9 to ≈ 2.0 × 10⁻¹⁰ m s⁻². [Renda 2019](../03-criticism/2019-renda-sceptical/README.md) uses Θ = 2.607 × 10²⁶ m but quotes a₀ = 2c²/Θ = 2 × 10⁻¹⁰ m s⁻², which is the 8.8 × 10²⁶ m value. | [2007](../01-papers/2007-mcculloch-pioneer-anomaly/README.md), [2012](../01-papers/2012-mcculloch-galactic-scales/README.md), [2017](../01-papers/2017-mcculloch-galaxy-rotations-sparc/README.md) |
| 2 | **βπ² vs 2.** The exact 2007 coefficient is βπ² ≈ 1.97–1.99. Papers from 2010 on round it to 2. In the 2016 and 2020 derivations the bracket is "2" exactly, by construction. | 2007 vs 2010+ |
| 3 | **Overall prefactor.** The 2016 derivation gives 2πβ·m(…) (≈ 1.26 m, 26% too large). The 2020 derivation removes this by choosing Δx = half-circumference instead of radius. | [2016](../01-papers/2016-mcculloch-relativity-uncertainty/README.md), [2020](../01-papers/2020-mcculloch-horizon-widths/README.md) |
| 4 | **The 2013 mechanism does not reproduce the 2c²/Θ coefficient if taken literally.** *Our reading:* the bracket in Eq. 8, (1/4Θ − πa/16c²), equals −(πa/16c²)(1 − 4c²/(π\|a\|Θ)). That implies a correction of ≈ 1.27 c²/(\|a\|Θ), not 2c²/(\|a\|Θ). The paper drops the term ("we can neglect this MiHsC term") and does not compare the coefficients. | [2013](../01-papers/2013-mcculloch-asymmetric-casimir/README.md) |
| 5 | **The inertial mass in 2013 is off by a factor of two.** The 2013 Planck-scale estimate gives ≈ 2 m_P. It was corrected to ≈ 1.29 m_P in 2016 (Giné & McCulloch). Renda 2019 argues that the energy-density substitution u = hc/λV used in both is itself invalid. Dickmann & Dickmann (2023) sum all the modes and find that the net force scales as a⁴ instead of a ([critique](../03-criticism/2023-dickmann-casimir-contradicts/README.md)). | [2013](../01-papers/2013-mcculloch-asymmetric-casimir/README.md), [2016 Giné](../01-papers/2016-gine-unruh-temperatures/README.md) |
| 6 | **The shape of F(a).** Renda's discrete-spectrum calculation gives an F(a) with a maximum F ≈ 2.17 near 1.2 × 10⁻⁹ m s⁻², not the monotonic linear F of 2007. | [Renda 2019](../03-criticism/2019-renda-sceptical/README.md) |
| 7 | **Sign typo** in the MOND series expansion (+a₀²/a² printed as −). | [2020](../01-papers/2020-mcculloch-horizon-widths/README.md) |
| 8 | **Wording.** Θ is called both "Hubble diameter" (2c/H) and "twice the Hubble distance". Waves are said to fit "twice the Hubble diameter" (λₙ = 2Θ/n). The 2013 figure puts the cosmic horizon at Θ/2. These are consistent if Θ = 2c/H is read as a diameter. | 2007, 2012, 2013 |

## Related
- [what-is-qi.md](what-is-qi.md) · [glossary.md](glossary.md) · [timeline.md](timeline.md)
