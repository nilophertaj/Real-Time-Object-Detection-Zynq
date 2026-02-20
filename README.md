# 🏆 Bharat AI-SoC Student Challenge
A project-based virtual challenge to ignite innovation in AI-driven System-on-Chip (SoC) design.

## Real-Time Object Detection using Hardware-Accelerated CNN
---

## 🎯 Challenge Context

This project is developed under the **Arm Bharat AI SoC Challenge**,  
specifically addressing:

### 🧠 Problem Statement 5  
**Real-Time Object Detection Using Hardware-Accelerated CNN on Xilinx Zynq FPGA with Arm Processor**

The objective is to design and implement a CNN inference system on a Xilinx Zynq SoC, leveraging FPGA acceleration to demonstrate measurable performance improvement over a CPU-only implementation.

---

# 📌 Project Overview

This project implements a real-time object detection system using a hardware/software co-design approach on a Zynq SoC.

The system partitions tasks intelligently:

| Component | Responsibility |
|------------|----------------|
| 🖥 Arm Processor (PS) | Image capture, preprocessing, control logic, post-processing |
| ⚡ FPGA Fabric (PL) | Accelerates CNN operations (Convolution, Activation, Pooling) |

The final system demonstrates:

- Real-time inference
- Performance comparison
- Hardware acceleration benefits
- Efficient FPGA resource utilization

---

# 🏗 Target Hardware Platform

| Hardware | Details |
|-----------|----------|
| SoC | Xilinx Zynq-7000 |
| Board | ZedBoard |
| Processor | ARM Cortex-A9 |
| FPGA | Programmable Logic Fabric |
| Input | USB Camera |
| Output | Display / Serial Console |

---

# 🧠 Implementation Strategy

## 🔹 Part 1 – CPU-Only Baseline

- CNN runs entirely on ARM processor
- Serves as performance reference
- Measures latency, FPS, CPU usage

## 🔹 Part 2 – Hardware-Accelerated CNN

- Convolution layers offloaded to FPGA
- Designed using Vivado / Vitis HLS
- ARM + FPGA operate collaboratively
- Achieves significant performance improvement

---

# 🛠 Software & Tools Used

| Category | Tools |
|----------|--------|
| FPGA Design | Vivado, Vitis HLS |
| Embedded Software | Vitis |
| AI Model | Lightweight CNN / YOLO |
| Image Processing | OpenCV |
| Control Logic | Python / C++ |

---


---

# 📦 Key Deliverables Achieved

✔ Working FPGA-accelerated CNN prototype  
✔ CPU vs Hardware performance benchmarking  
✔ Hardware/Software co-design implementation  
✔ Real-time inference demonstration  
✔ Quantitative performance validation  

---

# 🎓 Learning Outcomes

- Embedded Edge AI pipeline understanding  
- Practical FPGA acceleration using HLS  
- ARM–FPGA co-design experience  
- Performance optimization & analysis  
- Trade-off evaluation (Power vs Performance vs Flexibility)  

---

# 🔮 Conclusion

This project successfully demonstrates that offloading CNN computation to FPGA fabric significantly improves inference speed while reducing CPU utilization, validating the effectiveness of heterogeneous SoC architectures for edge AI applications.

---

## 👨‍💻 Developed for  
**Arm Bharat AI SoC Challenge – Problem Statement 5**
## Team Details: 
- Team Members : Nilopher Taj B, Rupesh K, Gayathri K
- Mentor : Dr.R.Avudaiammal, Professor
- Institute : St. Joseph's College of Engineering, Chennai

