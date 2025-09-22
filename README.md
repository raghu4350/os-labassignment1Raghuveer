# Lab Experiment Sheet-1

# OS Lab Assignment 1 - Process Creation and Management

## 📘 Course Information
- **Course Code & Name**: ENCS351 - Operating System  
- **Program**: B.Tech CSE, AI/ML, Data Science, Cyber, FSD, UX/UI  
- **Experiment Title**: Process Creation and Management Using Python OS Module  

---

## 🎯 Objectives
- Simulate Linux process management operations using Python  
- Replicate `fork()`, `exec()`, and process state inspections  
- Demonstrate zombie and orphan process scenarios  
- Inspect process details from `/proc`  
- Demonstrate priority scheduling with `nice()` values  

---

## 📝 Tasks
1. **Process Creation Utility**  
   Create N child processes using `os.fork()`. Each child prints its PID, Parent PID, and a custom message. Parent waits for all children.  

2. **Command Execution Using exec()**  
   Each child process executes a Linux command (`ls`, `date`, `ps`).  

3. **Zombie & Orphan Processes**  
   - Zombie: Parent skips `wait()` after fork.  
   - Orphan: Parent exits before child finishes.  

4. **Inspecting Process Info from /proc**  
   Input PID → show process name, state, memory usage, executable path, and open file descriptors.  

5. **Process Prioritization**  
   Create CPU-intensive processes with different `nice()` values and observe scheduler impact.  

---

## 📂 Files in Repository
- `process_management.py` → Python code implementing all 5 tasks  
- `output.txt` → Sample output log from execution  
- `report.pdf` → Report with objectives, code snapshot, and results  
- `README.md` → Documentation and usage instructions  

---

