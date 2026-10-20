# PDFs to obtain manually

These sources are in the repository, but their README was written from an abstract, a publisher page or secondary reports, because no full text could be downloaded automatically. Supplying the PDF lets the README be rebuilt from the full text: real equations, page-numbered quotes, figures, and fewer `[!UNVERIFIED]` flags.

The table below is generated. Rerun `python3 -I _tools/build_missing_list.py` after adding a file, and the source drops off the list.

## Ways to get them (cheapest first)
1. **Ask the authors.** It's free and usually works. ResearchGate's "Request full text" button sends the request for you.
   - **McCulloch** (Plymouth): via his blog, [physicsfromtheedge.blogspot.com](https://physicsfromtheedge.blogspot.com).
   - **Giné** (Universitat de Lleida) also covers the six Giné papers.
   - **Tajmar's group** (TU Dresden, Space Propulsion group) covers Tajmar 2018 and 2020, Kößling 2019 and Neunzig 2022. TU Dresden also hosts conference versions of several of these; ask whether a published or accepted version can be shared.
   - **Kholupenko** (Ioffe Institute) for the three *Gravitation and Cosmology* papers.
   - **Millis** (Tau Zero Foundation) for the 2017 Acta Astronautica paper.
2. **Use a library.**
   - **University library:** many let walk-in visitors read online journals on site.
   - **Public library:** its interlibrary loan service can order individual articles, often free or cheap.
3. **Find free legal copies.** The [Unpaywall](https://unpaywall.org) browser extension finds them automatically.
4. **Pay per article,** typically $30–45; DeepDyve rents articles more cheaply.

Avoid shadow-library sites, which infringe copyright.

## Once you have a file
1. Save it as `paper.pdf` in that source's folder (`slides.pdf` for a talk). Downloads in `~/Downloads` or on a USB drive are fine: just say where they are.
2. Record its licence in `_tools/licenses.json`. Paywalled copies and author manuscripts are `LOCAL`; only CC-licensed published versions are `PUBLIC`. Then run `python3 -I _tools/apply_local_only.py`, so local-only files never reach the public repo. `python3 -I _tools/check_license.py --doi <doi>` helps decide.
3. Rebuild the README from the full text (see [AGENTS.md](AGENTS.md)), then run `build_index.py`, `build_master_index.py` and this list's script.

## Still missing
<!-- BEGIN AUTO-MISSING -->
| Flags | Source | Year | Venue | Link | How to get it |
|---|---|---|---|---|---|
| 3 | [Thrust measurements of microwave-, superconducting- and laser-type emdrives](03-criticism/2022-neunzig-emdrive-thrust/README.md) | 2022 | Acta Astronautica 195:583-595 | [doi:10.1016/j.actaastro.2022.02.014](https://doi.org/10.1016/j.actaastro.2022.02.014) | Elsevier (ScienceDirect): pay-per-view, a library, or ask the authors |
| 3 | [Cosmological Consequences of the Holographic Scenario](01-papers/2012-gine-cosmological-holographic/README.md) | 2012 | International Journal of Theoretical Physics 52(1), 53-61 | [doi:10.1007/s10773-012-1298-0](https://doi.org/10.1007/s10773-012-1298-0) | Springer: pay-per-view, a library, or ask the authors |
| 3 | [Gravity from the uncertainty principle](01-papers/2014-mcculloch-gravity-uncertainty/README.md) | 2014 | Astrophysics and Space Science 349(2), 957-959 | [doi:10.1007/s10509-013-1686-9](https://doi.org/10.1007/s10509-013-1686-9) | Springer: pay-per-view, a library, or ask the authors |
| 3 | [Casimir effect and the uncertainty principle](01-papers/2018-gine-casimir-uncertainty/README.md) | 2018 | Modern Physics Letters A 33(24):1850140 | [doi:10.1142/S0217732318501407](https://doi.org/10.1142/S0217732318501407) | World Scientific: pay-per-view, a library, or ask the authors |
| 3 | [On the Possible Anisotropy of the Unruh Radiation. Part I: Massless Scalar Field in (1+1)D Space-Time](01-papers/2019-kholupenko-unruh-anisotropy-1/README.md) | 2019 | Gravitation and Cosmology 25(3):213-225 | [doi:10.1134/S0202289319030071](https://doi.org/10.1134/S0202289319030071) | Pleiades/Springer: pay-per-view, a library, or ask the authors |
| 3 | [The EPR paradox and the uncertainty principle](01-papers/2021-mcculloch-epr-paradox/README.md) | 2021 | Modern Physics Letters B 35(04), 2150072 | [doi:10.1142/s021798492150072x](https://doi.org/10.1142/s021798492150072x) | World Scientific: pay-per-view, a library, or ask the authors |
| 3 | [How Quantised Inertia Gets Rid Of Dark Matter](07-media/2018-mcculloch-dark-matter-scitrends/README.md) | 2018 | Science Trends (popular article) | [doi:10.31988/scitrends.8056](https://doi.org/10.31988/scitrends.8056) | Page removed and not archived: ask McCulloch |
| 2 | [The holographic scenario, the modified inertia and the dynamics of the universe](01-papers/2012-gine-holographic-modified-inertia/README.md) | 2012 | Modern Physics Letters A 27(34):1250208 | [doi:10.1142/S0217732312502082](https://doi.org/10.1142/S0217732312502082) | World Scientific: pay-per-view, a library, or ask the authors |
| 2 | [Inertial mass from Unruh temperatures](01-papers/2016-gine-unruh-temperatures/README.md) | 2016 | Modern Physics Letters A 31(17), 1650107 | [doi:10.1142/S0217732316501078](https://doi.org/10.1142/S0217732316501078) | World Scientific: pay-per-view, a library, or ask the authors |
| 2 | [Inertial mass of an elementary particle from the holographic scenario](01-papers/2017-gine-inertial-mass-holographic/README.md) | 2017 | International Journal of Modern Physics A 32(6n07), 1750043 | [doi:10.1142/S0217751X17500439](https://doi.org/10.1142/S0217751X17500439) | World Scientific: pay-per-view, a library, or ask the authors |
| 2 | [Inertial frames and breakthrough propulsion physics](01-papers/2017-millis-inertial-frames/README.md) | 2017 | Acta Astronautica 138, 85-94 | [doi:10.1016/j.actaastro.2017.05.028](https://doi.org/10.1016/j.actaastro.2017.05.028) | Elsevier (ScienceDirect): pay-per-view, a library, or ask the authors |
| 2 | [Propulsive Forces using High-Q Asymmetric High Energy Laser Resonators](01-papers/2017-taylor-laser-resonators/README.md) | 2017 | Journal of the British Interplanetary Society 70:238-243 | [link](https://bis-space.com/shop/?p=9802) | British Interplanetary Society shop, or ask the author |
| 2 | [Hawking effect and Unruh effect from the uncertainty principle](01-papers/2018-gine-hawking-unruh-uncertainty/README.md) | 2018 | EPL 121(1):10001 | [doi:10.1209/0295-5075/121/10001](https://doi.org/10.1209/0295-5075/121/10001) | IOP/EPL: pay-per-view, a library, or ask the authors |
| 2 | [On the Possible Anisotropy of the Unruh Radiation. Part II: Massive Scalar Field in (3+1)D Space-Time](01-papers/2022-kholupenko-unruh-anisotropy-2/README.md) | 2022 | Gravitation and Cosmology 28(2), 139-152 | [doi:10.1134/S0202289322020074](https://doi.org/10.1134/S0202289322020074) | Pleiades/Springer: pay-per-view, a library, or ask the authors |
| 2 | [Quantised Accelerations: From Anomalies to New Physics](07-media/2024-mcculloch-quantised-accelerations/README.md) | 2024 | Polaris Books |  | Book: buy, or borrow via interlibrary loan |
| 1 | [The SpaceDrive project - Thrust balance development and new measurements of the Mach-Effect and EMDrive Thrusters](04-experiments/2019-kossling-spacedrive-balance/README.md) | 2019 | Acta Astronautica 161:139-152 | [doi:10.1016/j.actaastro.2019.05.020](https://doi.org/10.1016/j.actaastro.2019.05.020) | Elsevier (ScienceDirect): pay-per-view, a library, or ask the authors |
| 1 | [Proposed Versions of Quantized-Inertia Drives](01-papers/2024-stauffer-qi-drive-versions/README.md) | 2024 | ResearchGate 377926730 (self-published; not peer-reviewed); mirrored at rocketslinger.com/Quant_Inert/ | [link](https://www.researchgate.net/publication/377926730_Proposed_Versions_of_Quantized-Inertia_Drives) | ResearchGate: download in a browser (free login) |
| 1 | [On the Possible Anisotropy of the Unruh Radiation. Part III: A Screened Detector](01-papers/2025-kholupenko-unruh-anisotropy-3/README.md) | 2025 | Gravitation and Cosmology 31(3), 353-365 | [doi:10.1134/S0202289325700239](https://doi.org/10.1134/S0202289325700239) | Pleiades/Springer: pay-per-view, a library, or ask the authors |
| 1 | [Experiments for Testing Quantized Inertia Theories](01-papers/2025-stauffer-qi-experiments/README.md) | 2025 | ResearchGate 388117533 (self-published; not peer-reviewed); mirrored at rocketslinger.com/Quant_Inert2/ | [link](https://www.researchgate.net/publication/388117533_Experiments_for_Testing_Quantized_Inertia_Theories) | ResearchGate: download in a browser (free login) |
| 1 | [Physics from the Edge: A New Cosmological Model for Inertia](07-media/2014-mcculloch-physics-from-edge/README.md) | 2014 | World Scientific | [doi:10.1142/9122](https://doi.org/10.1142/9122) | World Scientific book: buy, or borrow via interlibrary loan |
| 0 | [Put strong limits on all proposed theories so far assessing electrostatic propulsion: Does a charged high-voltage capacitor produce thrust?](03-criticism/2020-tajmar-capacitor-thrust/README.md) | 2020 | Journal of Electrostatics 107:103477 | [doi:10.1016/j.elstat.2020.103477](https://doi.org/10.1016/j.elstat.2020.103477) | Elsevier (ScienceDirect): pay-per-view, a library, or ask the authors |
| 0 | [The SpaceDrive project – Developing revolutionary propulsion at TU Dresden](04-experiments/2018-tajmar-spacedrive/README.md) | 2018 | Acta Astronautica 153:1-5 | [doi:10.1016/j.actaastro.2018.10.028](https://doi.org/10.1016/j.actaastro.2018.10.028) | Elsevier (ScienceDirect): pay-per-view, a library, or ask the authors |

_22 sources without a PDF. "Flags" = `[!UNVERIFIED]` markers in the README; higher means the full text would settle more._
<!-- END AUTO-MISSING -->
