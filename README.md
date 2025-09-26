# MegTech — WRO 2025 Future Engineers

This repository documents **Megatron Technologies (MegTech)** and our autonomous vehicle developed for the **World Robot Olympiad™ 2025 — Future Engineers Category** under the theme *“The Future of Robots”*.  
It contains our engineering progress, vehicle design, wiring, code logic, photos, and demonstration video.  

Our main objective is to create a reliable, intelligent, and competitive self-driving car that not only performs well in the competition but also contributes to the robotics community by sharing open knowledge and engineering insights.

---

## 👥 The Team

Our team, **MegTech**, unites three motivated members, each bringing distinct knowledge and passion to robotics and technology.  
Our main goal is to work in harmony, combining individual strengths to both learn from one another and achieve greater results together.  
By collaborating closely, we strive to advance our skills in **AI, programming, hardware design, and system integration**.  

We are dedicated to enhancing the **intelligence, performance, and dependability** of our project.  
We believe that persistence, creativity, and strong teamwork are the driving forces that will help us build an innovative and competitive solution.  

---

### Official Team Photo
<p align="center">
  <img src="Team%20Photos/Official%20Team%20Photo.jpg" width="600"/>
</p>

---

### Aydin Sulkhaev
<table>
<tr>
<td width="300">
  <img src="Team%20Photos/Sulkhaev%20Aydin.JPG" width="250"/>
</td>
<td>
  
**Role:** Captain & AI / Programming Engineer  

Aydin is the captain of the MegTech team and an **AI & programming engineer**.  
His main focus is on developing algorithms that give the robot the ability to analyze its environment and make autonomous decisions.  
By integrating **artificial intelligence with control systems**, he ensures that the robot not only reacts quickly but also learns from the data it collects.  

His leadership role also involves coordinating the team’s workflow and making sure the project moves forward efficiently.  

</td>
</tr>
</table>

---

### Elman Teneshov
<table>
<tr>
<td width="300">
  <img src="Team%20Photos/Teneshov%20Elman.jpg" width="250"/>
</td>
<td>

**Role:** Hardware Engineer  

Elman is the team’s **hardware engineer**, responsible for the structural and electronic foundations of the robot.  
He works on **designing, assembling, and optimizing** the hardware components to guarantee stability and precision during real-world operation.  

By testing and improving the mechanical and electrical systems, he ensures that the robot’s performance remains reliable and consistent under various conditions.  

</td>
</tr>
</table>

---

### Mahammad Ahkmadov
<table>
<tr>
<td width="300">
  <img src="Team%20Photos/Akhmedov%20Mahammad.jpg" width="250"/>
</td>
<td>

**Role:** Software Engineer & Marketing Coordinator  

Mahammad plays a dual role as **software engineer and marketing coordinator**.  
On the technical side, he contributes to the programming of system components, ensuring smooth communication between hardware and software.  

At the same time, he manages the **presentation and outreach** of the team’s work, making sure MegTech’s progress is well-documented and shared effectively.  
His versatility helps bridge the gap between technology development and project communication.  

</td>
</tr>
</table>

---

## 🚗 Vehicle Overview

<p align="center">
  <img src="Vehicle%20Photos/View.jpg" width="500"/>
</p>

### Specifications
- **Dimensions:** 25 cm (L) × 13.5 cm (W) × 11 cm (H)  
- **Weight:** 1.100 kg  
- **Voltage Range:** 11.1 V – 22.2 V (4S LiPo, 14.8 V, 4000 mAh, 60C)  
- **Drive System:** Rear-wheel drive (single DC motor with encoder)  
- **Steering Geometry:** Ackermann steering (servo-controlled front axle)  
- **Main Controller:** Raspberry Pi 5  
- **Motor Driver:** L298N H-Bridge  
- **Sensors:** Intel RealSense D455 (depth vision), LDROBOT D500 Lidar  
- **Additional Safety:** Soft bumper for impact absorption  

The LiPo battery capacity ensures the robot can complete **both tasks with over 50% charge remaining**, and it can be fully recharged during breaks, guaranteeing smooth operation for the entire competition.

---

## ⚙️ Motor Axle System  

Our vehicle uses a **single DC motor with encoder** connected to a **shared rear axle**.  
The transmission is achieved **through gears**, allowing efficient torque delivery to both wheels.  
Since the wheels are mechanically linked by the axle, they always rotate evenly, ensuring stable straight-line movement.  

Although the motor is equipped with an encoder, in our current implementation **encoder feedback is not used** — the system runs at fixed motor speeds controlled via the L298N H-Bridge.  

---

## 🛞 Ackermann Steering System  

The steering mechanism is based on a **servo-driven rack-and-pinion system** using the **MG996R servo motor**.  
- In the *Open Challenge*, the steering angle can vary between **0° and 180°**, allowing flexible maneuvering.  
- In the *Obstacle Challenge*, the steering is automatically calculated depending on sensor feedback.  

The two **front wheels are mechanically linked** by a steering rack, which is directly connected to the servo.  
While it does not implement a perfect mathematical Ackermann geometry, the system provides a **practical steering wheel chassis** with sufficient accuracy for both challenges.  

---

## 🔋 Power and Sense Management  

Power distribution is designed to be **simple and reliable**:  
- The **14.8 V LiPo battery (4S, 4000 mAh, 60C)** directly powers the **L298N motor driver**.  
- A **voltage regulator** converts battery output to **5 V**, supplying the Raspberry Pi 5 and all sensors.  
- The **DC motor** operates at ~12 V, receiving input directly through the L298N driver.  

**Protection & Safety**  
- The Raspberry Pi 5 includes a built-in fuse, ensuring the main controller is safeguarded.  
- The only vulnerable component is the L298N, which serves as the primary motor interface.  

**Sensor and Control Management**  
- All sensors (Intel RealSense D455, LDROBOT Lidar) are processed **in real time on the Raspberry Pi 5**, with no additional microcontrollers.  
- The **Raspberry Pi directly controls both the DC motor and the servo** via the L298N and PWM outputs, ensuring minimal latency and a clean system architecture.  

---

## 🔌 Wiring

A complete wiring diagram is provided in PDF format:  
[📄 WiringScheme.pdf](Scheme/WiringScheme.pdf)

---

## 🧠 Code Logic

### Task 1 — Autonomous Laps with Turning
The first task focuses on driving forward, detecting obstacles, and completing a set number of laps.  
The program is triggered by pressing a button, ensuring the race only starts when intended.  

**Main logic flow:**
1. **System Initialization**  
   - Raspberry Pi 5 starts RealSense depth camera pipeline.  
   - Motors, servo, and button are initialized.  
   - Safety reset ensures motors are stopped and servo is centered.  

2. **Start Condition**  
   - Robot waits for the physical button press.  
   - Button press sets a global flag and starts the race sequence.  

3. **Forward Movement**  
   - Robot drives forward at a set speed.  
   - Constantly checks distance from the RealSense depth camera.  
   - If an obstacle is detected closer than **90 cm**, the robot stops.  

4. **Turning**  
   - After stopping, the robot performs a turn in a predefined direction (left or right, configurable by variable).  
   - Servo adjusts steering angle.  
   - Motor powers the rear wheels for a short time to complete the turn.  
   - After turning, the servo is reset to center.  

5. **Lap Counter**  
   - This process repeats for the configured number of laps (4 laps).  
   - After finishing, all systems reset and the robot stops safely.  

This approach ensures **repeatable and safe behavior** while respecting the competition’s rule of using only **one motor for the driving axle**.  

👉 Full code: [task1.py](Source%20Codes/task1.py)

---

### Task 2 — [To be added]
The code and logic explanation for **Task 2** will be uploaded and documented closer to the competition.  

---

## 📹 Vehicle Demonstration

A video of the robot driving autonomously is available in the repository:  
[📺 Vehicle Video](Vehicle%20Video/Video%20link.txt)

---

## 📚 Knowledge Base

- **AI & Perception:** Depth vision, Object&Colour detection, Speed control.  
- **Navigation:** Real-time scanning and obstacle avoidance.  
- **Control:** Ackermann steering with servo, rear-wheel drive with encoder feedback.  
- **Safety:** Button-controlled start, obstacle stopping logic, LiPo power safety margin.  
- **Teamwork:** Integration of software, hardware, and presentation.  

---

## 🏁 Conclusion

By combining precise hardware design, intelligent software logic, and teamwork, **MegTech** has built a competitive and reliable solution for the **WRO 2025 Future Engineers category**.  
Our documentation is aimed at making our work transparent and reproducible, supporting the WRO goal of collaboration and inspiration among robotics teams worldwide.  
