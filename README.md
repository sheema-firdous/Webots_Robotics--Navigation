# 🧭 Directional Movement Robot using Inertial Unit and GPS (Webots)

This project implements a robot controller in Webots where the robot first rotates to a target orientation using the **Inertial Unit (compass)** and then moves in a straight line towards a calculated **GPS coordinate**. The logic is structured to make the robot follow a desired direction and stop after reaching a certain distance.

---

## ✨ Features

- 🎯 Rotates the robot by a specified angle (e.g., 90°)
- 🚶 Moves forward by a specified distance (e.g., 0.2 meters)
- 📍 Uses **Inertial Unit** for angle tracking and **GPS** for position tracking
- ⛔ Stops precisely when the desired destination is reached
- 🔄 Converts orientation angles from negative to a normalized 0–360° system

---

## 📊 Parameters & Thresholds

- `degrees = 90` → How much to rotate the robot
- `distance = 0.2` → How far to move after rotating
- `angle_threshold = 1` → Acceptable error margin for rotation
- `distance_threshold = 0.002` → Precision for destination checking

---

## 🧠 Logic Breakdown

1. **Initialization**:
   - Enable GPS and Inertial Unit sensors
   - Allow sensors to stabilize before use

2. **Yaw Calculation**:
   - Get yaw angle using the Inertial Unit
   - Convert yaw to a 0–360° format for consistency

3. **Rotation Phase**:
   - Rotate in place until the yaw angle reaches the desired target within a threshold

4. **Translation Phase**:
   - Move straight forward until the GPS coordinates match the calculated target location

5. **Stop**:
   - When target position is reached, stop both wheels and end the simulation loop

---

## 🛠️ How to Run

1. Open your `.wbt` world in Webots containing the robot with:
   - `left wheel motor`, `right wheel motor`
   - `inertial unit`, `gps`
2. Attach the controller script to the robot.
3. Start the simulation and observe the robot rotate and move to the target position.

---

## 🧪 Example Output

Turning 90 degrees Start: 135 Target: 45 Final coordinate: [0.141, 0.141] Current position: [0.0, 0.0, 0.0] ... Goal reached. Final position: [0.1409, 0.1408, 0.0]

---

---

## 👩‍💻 Developers Information

Developed by **[Sheema Firdous](https://www.linkedin.com/in/sheema-firdous-67b9b8181/)**  
as part of the **Cognitive Systems and Robotics** module assessment  at **[Sheffield Hallam University](https://www.shu.ac.uk/)**

Supervised by [Dr. Samuele Vinanzi](https://www.linkedin.com/in/samuelevinanzi/)

This project demonstrates the practical application of NAVIGATION in Cognitive and Autonomous robotics using Webots and Python.
