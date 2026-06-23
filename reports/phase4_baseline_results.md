# Phase 4 - Baseline Optical Flow Evaluation

## Dataset

* KITTI 2015
* Evaluation subset: 200 image pairs
* Synthetic haze generated using depth-based atmospheric scattering model

## Haze Levels

* Clean
* Light (β = 0.2)
* Medium (β = 0.5)
* Dense (β = 0.8)
* Extreme (β = 1.2)

---

## SEA-RAFT Results

| Haze Level |   F1-all |       EPE |
| ---------- | -------: | --------: |
| Clean      | 0.807870 |  2.161742 |
| Light      | 1.311301 |  3.652213 |
| Medium     | 2.421844 |  6.731014 |
| Dense      | 3.805468 | 10.616711 |
| Extreme    | 6.294545 | 16.551012 |

### Observation

EPE increases with haze density:

2.161742 → 3.652213 → 6.731014 → 10.616711 → 16.551012

---

## RAFT Results

| Haze Level |   F1-all |       EPE |
| ---------- | -------: | --------: |
| Clean      | 0.630337 |  1.471205 |
| Light      | 1.152133 |  3.065316 |
| Medium     | 2.283783 |  6.752227 |
| Dense      | 4.262314 | 12.497252 |
| Extreme    | 7.391664 | 19.879711 |

### Observation

EPE increases with haze density:

1.471205 → 3.065316 → 6.752227 → 12.497252 → 19.879711

---

## RAFT vs SEA-RAFT Comparison

| Haze Level |  RAFT EPE | SEA-RAFT EPE | Better Model |
| ---------- | --------: | -----------: | ------------ |
| Clean      |  1.471205 |     2.161742 | RAFT         |
| Light      |  3.065316 |     3.652213 | RAFT         |
| Medium     |  6.752227 |     6.731014 | SEA-RAFT     |
| Dense      | 12.497252 |    10.616711 | SEA-RAFT     |
| Extreme    | 19.879711 |    16.551012 | SEA-RAFT     |

---

## Key Findings

* Optical flow performance degrades as haze density increases.
* Both RAFT and SEA-RAFT show increasing EPE and F1-all with stronger haze.
* RAFT performs better on clean and light haze conditions.
* SEA-RAFT performs better under medium, dense, and extreme haze.
* SEA-RAFT appears more robust under severe visibility degradation.



## Failure Case Analysis

Three representative examples were selected to visualize the effect of severe haze on optical-flow estimation.

### Sample 000000

* Extreme haze reduces scene visibility and image contrast.
* Coarse motion patterns remain detectable.
* Object boundaries become less distinct.
* Distant scene regions become more ambiguous.

### Sample 000050

* Large moving objects such as trucks remain detectable.
* Motion regions become less separated from the background.
* Road and background texture information is significantly reduced.
* Fine motion structure becomes harder to estimate.

### Sample 000100

* Severe haze causes strong visibility degradation in distant regions.
* Motion boundaries become less precise.
* Flow fields become smoother and less detailed.
* Large homogeneous motion regions appear due to reduced correspondence information.

### Summary

Across all selected examples:

* Haze reduces image contrast and scene visibility.
* Texture information is progressively lost as haze density increases.
* Motion boundaries become less distinct.
* Distant regions become increasingly difficult to match reliably.
* These observations are consistent with the quantitative evaluation, where both RAFT and SEA-RAFT exhibit increasing EPE and F1-all as haze density increases.

The visual results support the hypothesis that haze negatively impacts optical-flow estimation and motivate the use of haze-aware guidance mechanisms in later phases of the project.


## Baseline Selection

### Objective

Determine the strongest baseline model before introducing the proposed VLM-guided haze-aware optical-flow method.

### Findings

| Haze Level | Better Model |
|------------|------------- |
| Clean      | RAFT         |
| Light      | RAFT         |
| Medium     | SEA-RAFT     |
| Dense      | SEA-RAFT     |
| Extreme    | SEA-RAFT     |

### Conclusion

RAFT achieves lower EPE on clean and light haze conditions. However, SEA-RAFT achieves lower EPE under medium, dense, and extreme haze conditions, which are the primary conditions of interest for this research.

Therefore, SEA-RAFT is selected as the primary baseline for future VLM-guided haze-aware optical-flow experiments due to its superior robustness under severe visibility degradation.