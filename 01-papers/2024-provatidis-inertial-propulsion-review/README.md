---
title: "Inertial Propulsion Devices: A Review"
authors: [Christopher G. Provatidis]
year: 2024
type: paper
venue: "Eng 5(2), 851-880"
doi: 10.3390/eng5020046
arxiv:
url: "https://doi.org/10.3390/eng5020046"
open_access: true
license: CC-BY-4.0
files: [paper.pdf]
status: neutral
tags: [propulsion, review, inertial-drive, momentum-conservation, ivo]
---

# Inertial Propulsion Devices: A Review

**Citation:** Provatidis, C. G. (2024). *Inertial Propulsion Devices: A Review*. Eng, 5(2), 851–880. https://doi.org/10.3390/eng5020046 (published 13 May 2024; open access). The PDF was retrieved from MDPI's file server (mdpi-res.com). A preprint version is at https://doi.org/10.20944/preprints202401.1841.v1.

**TL;DR:** This is a critical, largely historical review of mechanical "inertial propulsion" devices (rotating or oscillating masses, gyroscopes, Dean drives and similar), from ancient athletes' halteres to modern patents. Its conclusion is that a single inertial-drive "shot" is possible, but "the repetition of the same cycle is impossible unless an external force is exerted upon it". QI appears in one paragraph of the Discussion. There it is presented as a non-Newtonian approach some researchers have turned to, alongside an account of the DARPA grant and IVO Ltd's Barry-1 satellite, which lost contact.

## Key claims
- Newton's second and third laws, and conservation of linear momentum, mean the centre of mass of an isolated system moves at constant velocity. Repeated inertial propulsion in vacuum is therefore impossible.
- On water or frictional ground, limited or even unlimited motion is possible, because external forces (water, friction) act. The maximum distance scales with √(motor speed) and cos(initial polar angle).
- For gyroscopes, the lift in the first half-period cancels the downward force in the second half.
- In satellites, rotating masses can change orientation (attitude control) but cannot displace the centre of mass.
- On QI (Section 6, p. 868): "Since Newtonian mechanics do not allow for the development of repeated inertial propulsion, some researchers have turned to non-Newtonian or Modified Newtonian Dynamics (MoND) considerations."
  - The review notes McCulloch's QI (formerly MiHsC, 2007), its use to explain Podkletnov's reported weight loss, the 2018 DARPA grant, and the collaboration with IVO Ltd on a "pure electric thruster for satellites that claimed to use zero fuel".
  - It also notes Barry-1's power-system issues after launch (11 November 2023) and the loss of all communication (9 February 2024).
- The review mentions "a similar device" independently patented by Charles Buhler (NASA).

## Key equations
From Appendix A (contra-rotating masses on a cart), the vertical resultant of the two centrifugal forces is
$$ F = 2m\omega^2 r\sin\theta $$

## Data used
- A literature and patent survey. Google Scholar gives about 278 hits for "inertial propulsion", and 536 including patents.

## Results & predictions
- No new experimental results. The review concludes that propellantless propulsion by internal rotating masses alone cannot produce sustained thrust in vacuum.
- QI is not evaluated technically. The review only reports its history and the IVO outcome.

## Figures
No figures extracted. The review's figures are device schematics, not result plots.

## Notable quotes
> "While the shot of an apparently stationary object into a vacuum is possible using an inertial drive, the repetition of the same cycle is impossible unless an external force is exerted upon it." (p. 869)

> "Mike McCulloch developed a theory of Quantized Inertia (QI) [200], formerly known by the acronym MiHsC [201] in 2007, aiming at human space travel [201]." (p. 868)

## Criticisms & responses
- No critiques of this review were found in a brief search.
- **Note:** the review groups QI with "non-Newtonian or Modified Newtonian Dynamics" approaches to inertial propulsion. QI thrust proposals involve electromagnetic or quantum-vacuum mechanisms (asymmetric cavities, capacitors), not the purely mechanical rotating-mass devices that are the review's main subject.
- **IVO / Barry-1 coverage:** [2024-debrief-ivo-failure](../../07-media/2024-debrief-ivo-failure/README.md), [2024-futurism-ivo-contact-lost](../../07-media/2024-futurism-ivo-contact-lost/README.md), [2023-debrief-ivo-launch](../../07-media/2023-debrief-ivo-launch/README.md).

## Related
- Evidence: [propulsion](../../02-evidence/propulsion.md), [lab-tests](../../02-evidence/lab-tests.md)
- Sources: [2017-millis-inertial-frames](../2017-millis-inertial-frames/README.md), [2011-mcculloch-podkletnov-effect](../2011-mcculloch-podkletnov-effect/README.md), [2018-mcculloch-propellantless-propulsion](../2018-mcculloch-propellantless-propulsion/README.md), [2021-mcculloch-symmetric-capacitors](../2021-mcculloch-symmetric-capacitors/README.md), [2018-plymouth-darpa](../../07-media/2018-plymouth-darpa/README.md), [2024-debrief-ivo-failure](../../07-media/2024-debrief-ivo-failure/README.md)
