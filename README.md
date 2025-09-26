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

- **AI & Perception:** Depth vision via RealSense D455, cube detection via Raspberry Pi Camera Module 3.  
- **Navigation:** Lidar scanning and obstacle avoidance.  
- **Control:** Ackermann steering with servo, rear-wheel drive with encoder feedback.  
- **Safety:** Button-controlled start, obstacle stopping logic, LiPo power safety margin.  
- **Teamwork:** Integration of software, hardware, and presentation.  

---

## 🏁 Conclusion

By combining precise hardware design, intelligent software logic, and teamwork, **MegTech** has built a competitive and reliable solution for the **WRO 2025 Future Engineers category**.  
Our documentation is aimed at making our work transparent and reproducible, supporting the WRO goal of collaboration and inspiration among robotics teams worldwide.  
