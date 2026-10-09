<div align="center">

# Khaled Mohamed Elamin Suliman, PhD

### Assistant Professor and Principal Investigator · Faculty of Pharmacy, Kumamoto University
**Elamin Laboratory for AI Precision Medicine**

Multi-omics integration and machine learning to identify the target —
molecular biology and in vivo models to test whether it is real.

[![Publications](https://img.shields.io/badge/Publications-55%2B-1f4e79?style=flat-square)](#selected-research-programs)
[![Citations](https://img.shields.io/badge/Citations-~1%2C150-1f4e79?style=flat-square)](https://orcid.org/0000-0001-9555-1814)
[![h-index](https://img.shields.io/badge/h--index-18-1f4e79?style=flat-square)](https://www.scopus.com/authid/detail.uri?authorId=57797410200)
[![Lab](https://img.shields.io/badge/Lab-10_researchers-1f4e79?style=flat-square)](#background)

[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--9555--1814-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0000-0001-9555-1814)
[![Scopus](https://img.shields.io/badge/Scopus-57797410200-E9711C?style=flat-square&logo=elsevier&logoColor=white)](https://www.scopus.com/authid/detail.uri?authorId=57797410200)
[![SciProfiles](https://img.shields.io/badge/SciProfiles-2153611-004B87?style=flat-square)](https://sciprofiles.com/profile/2153611)
[![Google Scholar](https://img.shields.io/badge/Google_Scholar-Profile-4285F4?style=flat-square&logo=googlescholar&logoColor=white)](https://scholar.google.com/citations?user=oyrk6pwAAAAJ)
[![Email](https://img.shields.io/badge/khaled@kumamoto--u.ac.jp-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:khaled@kumamoto-u.ac.jp)

</div>

---

## What I work on

Precision medicine has a measurement problem and an inference problem, and the
field tends to treat only the second as interesting. We can now profile a
person across genome, transcriptome, microbiome, metabolome, and immune
compartment. What we cannot yet do reliably is say which of the patterns in
that data are properties of the patient rather than properties of the assay,
the batch, or the analyst's choice of threshold.

My work sits on that boundary: integration and machine learning methods that
extract real biological structure from multi-omic data, and the controls that
tell us when they have not.

The program is not purely computational. I direct a ten-person laboratory at
Kumamoto University spanning genomics, metabolomics, computational chemistry,
molecular biology, and biosafety level 2 and 3 virology, which means a
predicted target can be tested in primary human cells and in murine models
inside my own group.

---

*Publication and citation figures retrieved from Google Scholar and Scopus, October 2026.*

---

## Selected research programs

| Program | What it does | Output |
|---|---|---|
| **Multi-omics integration and targeted protein degradation** | Cluster-guided integration of a colon adenocarcinoma cohort directing proteolysis-targeting chimera (PROTAC) design against KRAS G12D | *International Journal of Molecular Sciences*, 2026 · pipeline open-source |
| **Reproducibility and artifact control in omics** | Validation fixtures separating genuine biological signal from intensity artifacts in human immunodeficiency virus (HIV) proteomic data, after a conventional analysis produced a confident conclusion the controls did not support | Code released open-source |
| **Precision oncology and vaccine antigen prioritization** | Multi-omics integration for breast cancer antigen prioritization and precision messenger RNA (mRNA) vaccine design, with regional clinical partners | [`Relic-multiomic-breast-cancer-vaccine-development`](https://github.com/ElaminKhaled-AI-Lab/Relic-multiomic-breast-cancer-vaccine-development) |
| **Antiviral discovery** | Target prioritization and natural-product screening for HIV-1 latency reversal, validated in primary human CD4-positive T cells | *Frontiers in Pharmacology*, 2025 (co-first author) |

---

## How I work

Three commitments shape every project in the laboratory.

**Every analysis step carries a control capable of failing**, and the failure
condition is written into the code rather than left to the analyst's judgment.
The characteristic failure of high-dimensional omics is a result that is highly
significant and entirely an artifact of detectability.

**Every pipeline is version-controlled and publicly released**, because a
method that cannot be rerun by a stranger is a claim rather than a result.

**Every computational prediction is stated as a hypothesis with a named
experiment that would refute it** — and where the laboratory can run that
experiment, it does.

I report the results that do not survive. A predictive score of my own was
withdrawn after it failed a properly matched background control, and the
control was published alongside the withdrawal. An antigen class label I had
assigned was refuted by proteomic validation. These appear in the work because
a repository that shows only successes is not a record of what happened.

---

## Open source

Analysis code, configuration, and derived result tables for each program are
published with version-pinned environments and documented data freeze dates.
Pipelines are built to be rerun by someone who was not in the room when they
were written.

---

## Technical stack

**Machine learning and AI**
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)

Interpretable models (gradient boosting, random forests, elastic net) · deep
learning (graph neural networks, transformer architectures, convolutional
networks) · generative modeling (variational autoencoders, diffusion models) ·
reinforcement learning for molecular design · dimensionality reduction and
unsupervised clustering · model interpretability (SHAP, feature attribution) ·
cross-validation design and leakage control

**Multi-omics integration**
Genomics, transcriptomics, metabolomics, and proteomics integration ·
multi-cohort and synthetic cohort integration · molecular subtype discovery and
patient stratification · batch-effect detection and correction · biomarker and
therapeutic target prioritization · clinical phenotype integration · artifact
controls and falsifiable validation fixtures

**Computational chemistry and drug design**
Structure-based and ligand-based design · molecular docking (AutoDock Vina,
Glide, MOE) · molecular dynamics · MM-GBSA and MM-PBSA binding free energy ·
pharmacophore modeling · QSAR · ADMET prediction · multi-billion-compound
virtual screening · PROTAC and targeted protein degradation design ·
Schrödinger Maestro · KNIME

**Infrastructure**
![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![Nextflow](https://img.shields.io/badge/Nextflow-0DC09D?style=flat-square&logo=nextflow&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=flat-square)

R (Bioconductor, tidyverse) · Bash · Nextflow and nf-core workflow development ·
RNA-seq and The Cancer Genome Atlas (TCGA) analysis pipelines · reproducible
research environments · high-performance and cloud computing

**Experimental methods**
Molecular cloning · PCR · gene transfection and knockdown · CRISPR-Cas9 target
validation · Western blotting · flow cytometry · ELISA · fluorescence
microscopy · immunohistochemistry · HPLC · NMR · two-dimensional,
three-dimensional spheroid, and primary human cell culture · murine disease and
xenograft models · BSL-2 and BSL-3 containment

---

## Funding

| Role | Program | Period | Award |
|---|---|---|---|
| Co-Principal Investigator | AMED-SCARDA Vaccine and New Modality R&D Program — orthopoxvirus vaccine modernization, with KM Biologics Co., Ltd. | 2023–2027 | JPY 250,000,000 (≈USD 1.6M) |
| Principal Investigator | Co-creation Phylomedica Unit — deep learning for rare-disease drug development | 2026–2029 | JPY 4,500,000 |
| Principal Investigator | Kumamoto University Alumni Association — AI-driven antiviral discovery for HIV and SARS-CoV-2 | 2024–2026 | JPY 5,000,000 |
| Principal Investigator | Kumamoto University Grant-in-Aid for Scientific Research | 2022–2024 | JPY 1,000,000 |
| Co-Principal Investigator | Amabile Research Promotion Project | 2022–2023 | JPY 3,000,000 |
| Project Lead | Useful and Unique Natural Products for Drug Discovery (UpRod) | 2020–2022 | JPY 5,000,000 |

Within AMED-SCARDA I lead the AI-supported small-molecule discovery and
adjuvant screening workstream.

---

## Background

| | |
|---|---|
| **PhD, Pharmaceutical and Life Sciences** | Kumamoto University, Japan, 2018 — *Design and Evaluation of Novel Methylated Beta-Cyclodextrin Systems as Antitumor Agents for Colon Cancer*; full MEXT doctoral scholarship |
| **MSc, Pharmaceutical Sciences** | University of Khartoum, Sudan, 2013 |
| **BPharm (Honours)** | National Ribat University, Khartoum, Sudan, 2009 |

Assistant Professor and Principal Investigator, Kumamoto University, since 2021.
Previously postdoctoral fellow in the Kumamoto University–Taisho Pharmaceutical
joint program in translational pharmacology.

I supervise seven graduate students and three junior scientists, and have taught
approximately 43 credit hours of university courses across twelve years in
Sudan and Japan. Active research partnerships in Japan, Saudi Arabia, Indonesia,
Sudan, and Türkiye.

---

## Contact

📍 Faculty of Pharmacy, Kumamoto University, 5-1 Oe-honmachi, Chuo-ku, Kumamoto 862-0973, Japan
✉️ khaled@kumamoto-u.ac.jp · ☎️ +81-96-371-4809
🗣️ Arabic (native) · English (full professional) · Japanese (business level)

**ORCID** [0000-0001-9555-1814](https://orcid.org/0000-0001-9555-1814) · **Scopus** [57797410200](https://www.scopus.com/authid/detail.uri?authorId=57797410200) · **SciProfiles** [2153611](https://sciprofiles.com/profile/2153611) · **Google Scholar** [oyrk6pwAAAAJ](https://scholar.google.com/citations?user=oyrk6pwAAAAJ)

Interested in collaborations on multi-omics target discovery, cancer vaccine
design, and antiviral discovery — particularly where a dataset exists and the
analysis does not.
