# CPU Baseline Performance Results

Measured Values:

- Latency: 106.15 ms
- FPS: 98.9
- CPU Usage: 78.8 %
- Throughput: 98.9 frames/sec
- Power estimation: 3.58 Watts
  
Derived Metrics:
## 🔌 Power Estimation Logic

The implementation runs on a **Zynq-7000 SoC (ARM Cortex-A9)**.

Typical processor power characteristics:

- **Idle Power (P_idle)** ≈ 2.0 W  
- **Maximum Load Power (P_max)** ≈ 4.0 W  

To estimate actual power consumption under measured CPU load, we scale power linearly based on CPU utilization.

---

## 📐 Power Estimation Formula

P = P_idle + (CPU_usage × (P_max − P_idle))

---

## 🔢 Substituting Measured Values

Measured CPU Usage = 78.8 % = 0.788  

P = 2.0 + (0.788 × (4.0 − 2.0))  
P = 2.0 + (0.788 × 2.0)  
P = 2.0 + 1.576  
P ≈ **3.576 W**

- Frames per minute: 5934
- Frames per hour: 356,040

![alt](https://github.com/nilophertaj/Real-Time-Object-Detection-Zynq/blob/805083e361f8d781c50cd2a26bdd593765b721f8/assets/Screenshot%202026-02-19%20213621.png)
Observation:

The CPU-only implementation achieves near real-time performance but utilizes high CPU resources and exhibits higher latency.
