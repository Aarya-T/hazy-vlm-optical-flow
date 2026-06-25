# Phase 4 - Baseline Optical Flow Evaluation

## Dataset

* KITTI 2015
* Evaluation subset: 200 image pairs
* Synthetic haze generated using a depth-based atmospheric scattering model
* Evaluation metric: **Endpoint Error (EPE)**

---

## Haze Levels

* Clean
* Light (β = 0.2)
* Medium (β = 0.5)
* Dense (β = 0.8)
* Extreme (β = 1.2)

---

# GMA Results

| Haze Level |   EPE    |
|------------|---------:|
| Clean      | 0.569204 |
| Light      | 1.033081 |
| Medium     | 2.406350 |
| Dense      | 4.753935 |
| Extreme    | 8.052250 |

### Observation

EPE increases with haze density:

0.569204 → 1.033081 → 2.406350 → 4.753935 → 8.052250

GMA shows strong robustness under haze and maintains relatively low error even under severe degradation.

---

# RAFT Results

| Haze Level |    EPE   |
|------------|---------:|
| Clean      | 0.630337 |
| Light      | 1.152133 |
| Medium     | 2.283783 |
| Dense      | 4.262314 |
| Extreme    | 7.391664 |

### Observation

EPE increases with haze density:

0.630337 → 1.152133 → 2.283783 → 4.262314 → 7.391664

RAFT demonstrates the strongest overall robustness to haze among all evaluated models.

---

# SEA-RAFT Results

| Haze Level |      EPE |
|------------|---------:|
| Clean      | 2.161742 |
| Light      | 2.284000 |
| Medium     | 6.731014 |
| Dense      | 10.616711 |
| Extreme    | 16.551012 |

### Observation

EPE increases with haze density:

2.161742 → 2.284000 → 6.731014 → 10.616711 → 16.551012

SEA-RAFT exhibits significant degradation under medium-to-extreme haze conditions.

---

# Flow-Anything Results

| Haze Level |      EPE |
|------------|---------:|
| Clean      | 2.245281 |
| Light      | 2.980493 |
| Medium     | 5.289282 |
| Dense      | 7.616165 |
| Extreme    | 11.693092 |

### Observation

EPE increases steadily with haze density:

2.245281 → 2.980493 → 5.289282 → 7.616165 → 11.693092

Flow-Anything performs noticeably better than SEA-RAFT and WAFT under haze, although it remains behind RAFT and GMA.

---

# WAFT Results

| Haze Level |    EPE   |
|------------|---------:|
| Clean      | 2.627175 |
| Light      | 3.485687 |
| Medium     | 6.096277 |
| Dense      | 9.932874 |
| Extreme    | 14.847132 |

### Observation

EPE increases with haze density:

2.627175 → 3.485687 → 6.096277 → 9.932874 → 14.847132

WAFT performs reasonably under haze but does not match the robustness of RAFT, GMA, or Flow-Anything.

---

# Overall Model Comparison

| Haze Level | GMA          | RAFT         | SEA-RAFT  | Flow-Anything |   WAFT   |
|------------|---------:    |---------:    |---------: |---------:     |---------:|
| Clean      | **0.569204** | 0.630337     | 2.161742  | 2.245281      | 2.627175 |
| Light      | **1.033081** | 1.152133     | 2.284000  | 2.980493      | 3.485687 |
| Medium     | 2.406350     | **2.283783** | 6.731014  | 5.289282      | 6.096277 |
| Dense      | 4.753935     | **4.262314** | 10.616711 | 7.616165      | 9.932874 |
| Extreme    | 8.052250     | **7.391664** | 16.551012 | 11.693092     | 14.847132 |

---

# Ranking Under Extreme Haze

| Rank   | Model         |       EPE    |
|--------|---------------|--------------|
| 1      | RAFT          | **7.391664** |
| 2      | GMA           | 8.052250     |
| 3      | Flow-Anything | 11.693092    |
| 4      | WAFT          | 14.847132    |
| 5      | SEA-RAFT      | 16.551012    |

---

# Key Findings

* Optical-flow performance degrades consistently as haze density increases.
* All evaluated models exhibit increasing EPE under stronger haze conditions.
* RAFT achieves the lowest EPE under medium, dense, and extreme haze.
* GMA achieves the best performance under clean and light haze conditions.
* Flow-Anything performs better than both WAFT and SEA-RAFT across all haze levels.
* WAFT performs competitively but does not match RAFT, GMA, or Flow-Anything under severe haze.
* SEA-RAFT exhibits the largest performance degradation under dense and extreme haze.

---

# Failure Case Analysis

Three representative examples were selected to visualize the effect of severe haze on optical-flow estimation.

## Sample 000000

* Extreme haze reduces scene visibility and image contrast.
* Coarse motion patterns remain detectable.
* Object boundaries become less distinct.
* Distant scene regions become increasingly ambiguous.

## Sample 000050

* Large moving objects remain detectable.
* Motion regions become less separated from the background.
* Road and background texture information is significantly reduced.
* Fine motion structures become harder to estimate.

## Sample 000100

* Severe haze causes strong visibility degradation in distant regions.
* Motion boundaries become less precise.
* Flow fields become smoother and less detailed.
* Large homogeneous motion regions emerge due to reduced correspondence information.

### Summary

Across all selected examples:

* Haze reduces image contrast and scene visibility.
* Texture information progressively disappears as haze density increases.
* Motion boundaries become less distinct.
* Distant regions become increasingly difficult to match reliably.
* Flow estimates become smoother and less detailed under severe degradation.

These observations are consistent with the quantitative evaluation, where EPE increases steadily with haze density across all evaluated models.

The visual results support the hypothesis that haze negatively impacts optical-flow estimation and motivate the use of haze-aware guidance mechanisms in later phases of the project.

---

# Baseline Selection

## Objective

Determine the strongest optical-flow baseline before introducing the proposed VLM-guided haze-aware optical-flow framework.

## Findings

| Haze Level | Best Model |
|------------|------------|
| Clean      | GMA        |
| Light      | GMA        |
| Medium     | RAFT       |
| Dense      | RAFT       |
| Extreme    | RAFT       |

---

## Conclusion

Among all evaluated models, **RAFT consistently achieves the lowest EPE under medium, dense, and extreme haze conditions**, which are the primary operating conditions of interest for this research.

Although **GMA** performs slightly better under clean and light haze conditions, **RAFT demonstrates superior robustness as visibility degradation becomes severe**.

Therefore, **RAFT is selected as the primary baseline model** for subsequent VLM-guided haze-aware optical-flow experiments.

GMA is retained as a strong secondary baseline for comparison during later phases of the project.
