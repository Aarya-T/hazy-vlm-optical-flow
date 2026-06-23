# Phase 4 - SEA-RAFT Baseline Evaluation

## Dataset

* KITTI (200 image pairs)
* Synthetic haze levels:

  * Clean
  * Light (β = 0.2)
  * Medium (β = 0.5)
  * Dense (β = 0.8)
  * Extreme (β = 1.2)

## Model

* SEA-RAFT
* Checkpoint: Tartan-C-T-TSKH-kitti432x960-M

## Results

| Haze Level | F1-all   | EPE       |
| ---------- | -------- | --------- |
| Clean      | 0.807870 | 2.161742  |
| Light      | 1.311301 | 3.652213  |
| Medium     | 2.421844 | 6.731014  |
| Dense      | 3.805468 | 10.616711 |
| Extreme    | 6.294545 | 16.551012 |

## Observation

Optical flow performance degrades as haze density increases.

EPE trend:

Clean → Light → Medium → Dense → Extreme

2.161742 → 3.652213 → 6.731014 → 10.616711 → 16.551012


