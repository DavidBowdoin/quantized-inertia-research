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
| 3 | [The EPR paradox and the uncertainty principle](01-papers/2021-mcculloch-epr-paradox/README.md) | 2021 | Modern Physics Letters B 35(04), 2150072 | [doi:10.1142/s021798492150072x](https://doi.org/10.1142/s021798492150072x) | World Scientific: pay-per-view, a library, or ask the authors |
| 3 | [A Novel Quantum Thrust from Capacitors](01-papers/2026-mcculloch-quantum-thrust-capacitors/README.md) | 2026 | SSRN preprint (not peer-reviewed) | [doi:10.2139/ssrn.6313698](https://doi.org/10.2139/ssrn.6313698) | Ask the author |
| 3 | [How Quantised Inertia Gets Rid Of Dark Matter](07-media/2018-mcculloch-dark-matter-scitrends/README.md) | 2018 | Science Trends (popular article) | [doi:10.31988/scitrends.8056](https://doi.org/10.31988/scitrends.8056) | Page removed and not archived: ask McCulloch |
| 2 | [Propulsive Forces using High-Q Asymmetric High Energy Laser Resonators](01-papers/2017-taylor-laser-resonators/README.md) | 2017 | Journal of the British Interplanetary Society 70:238-243 | [link](https://bis-space.com/shop/?p=9802) | British Interplanetary Society shop, or ask the author |
| 2 | [Is it possible to implement a holographic equivalence principle?](01-papers/2022-gine-holographic-equivalence/README.md) | 2022 | Europhysics Letters 137(1), 19002 | [doi:10.1209/0295-5075/137/19002](https://doi.org/10.1209/0295-5075/137/19002) | IOP/EPL: pay-per-view, a library, or ask the authors |
| 2 | [On the Possible Anisotropy of the Unruh Radiation. Part II: Massive Scalar Field in (3+1)D Space-Time](01-papers/2022-kholupenko-unruh-anisotropy-2/README.md) | 2022 | Gravitation and Cosmology 28(2), 139-152 | [doi:10.1134/S0202289322020074](https://doi.org/10.1134/S0202289322020074) | Pleiades/Springer: pay-per-view, a library, or ask the authors |
| 2 | [Quantised Accelerations: From Anomalies to New Physics](07-media/2024-mcculloch-quantised-accelerations/README.md) | 2024 | Polaris Books |  | Book: buy, or borrow via interlibrary loan |
| 1 | [On the Possible Anisotropy of the Unruh Radiation. Part III: A Screened Detector](01-papers/2025-kholupenko-unruh-anisotropy-3/README.md) | 2025 | Gravitation and Cosmology 31(3), 353-365 | [doi:10.1134/S0202289325700239](https://doi.org/10.1134/S0202289325700239) | Pleiades/Springer: pay-per-view, a library, or ask the authors |
| 1 | [An Introduction to MiHsC / quantised inertia](07-media/2014-mcculloch-mihsc-101/README.md) | 2014 | Physics from the Edge (blog; masthead now 'Physics with an edge') | [link](https://physicsfromtheedge.blogspot.com/2014/01/mihsc-101.html) | Ask the author |
| 1 | [Physics from the Edge: A New Cosmological Model for Inertia](07-media/2014-mcculloch-physics-from-edge/README.md) | 2014 | World Scientific | [doi:10.1142/9122](https://doi.org/10.1142/9122) | World Scientific book: buy, or borrow via interlibrary loan |
| 1 | [Quantized Inertia is Nonsense](07-media/2022-fleming-qi-nonsense/README.md) | 2022 | YouTube (Ray Fleming channel, @rayfleming2053) | [link](https://www.youtube.com/watch?v=dM2sBIza_Yg) | Ask the author |
| 1 | [The Problems of Quantized Inertia](07-media/2025-uruena-problems-quantized-inertia/README.md) | 2025 | Independent Physics (independentphysics.com blog) | [link](https://independentphysics.com/the-problems-of-quantized-inertia/) | Ask the author |
| 0 | [Kinematics suggest large masses for high redshift galaxies](07-media/2025-mcgaugh-kinematics-high-redshift/README.md) | 2025 | Triton Station (blog) | [link](https://tritonstation.com/2025/02/10/kinematics-suggest-large-masses-for-high-redshift-galaxies/) | Ask the author |

_13 sources without a PDF. "Flags" = `[!UNVERIFIED]` markers in the README; higher means the full text would settle more._
<!-- END AUTO-MISSING -->
