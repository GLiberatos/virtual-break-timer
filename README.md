# 🧭 Virtual Break Timer

**A polished, trainer-focused countdown and break-management tool built with Flask, HTML/CSS, and JavaScript.**

Designed for virtual and hybrid classrooms, the Virtual Break Timer provides instructors with a clean, modern interface to manage class start times, breaks, lab sessions, and custom countdowns — fully optimized for Microsoft Teams screen sharing, with zero scrollbars and a consistent card-style UI.

---

## 🚀 Features

### 🎯 Instructor-Only Control

* Trainers share the timer through Microsoft Teams (or any screen-sharing tool)
* Students cannot interact with or modify the timer

### ⏱️ Clean, High-Visibility Countdown Timer

* Large, high-contrast timer display
* Automatically adjusts urgency:

  * ⚠️ **Warning** under 5 minutes
  * 🔥 **Urgent** under 1 minute (pulse animation)

### 📌 One-Click Preset Timers

Includes built-in timers for:

* **Class Starts** (30 minutes)
* **Coffee Break** (15 minutes)
* **Lunch Break** (60 minutes)
* **Lab Session** (30 minutes)

### ⚙️ Advanced Custom Timer Panel

* Custom time duration
* Custom title
* Custom description/agenda
* “Coming Up Next” section
* Seamless expansion panel with **zero scrollbars**

### 🖼️ Auto-Rotating Backgrounds

* Rotates images every 30 seconds
* Designed for:

  * Branding
  * Promotions
  * Classroom announcements

### 🔔 Audio Alerts

* 5-second alert when timer reaches zero
* Audio unlocks automatically on first interaction (browser-compliant)

### 🎨 Consistent Visual Design

* Matching Welcome + Timer screens
* Status pill badge
* Hover tooltips for all icons
* Centered welcome screen; left-aligned timer screen when active
* Zero scrollbars anywhere in the application

---

## 🛠️ Tech Stack

| Component  | Technology                              |
| ---------- | --------------------------------------- |
| Backend    | **Flask (Python)**                      |
| Frontend   | **HTML, CSS, JavaScript**               |
| Icons      | **Font Awesome**                        |
| Audio      | MP3 alert                               |
| Images     | Rotating background gallery             |
| Deployment | Any environment supporting Python/Flask |

---

## 📁 Project Structure

```
/project-root
│
├── app.py                 # Flask backend server
├── index.html             # Main UI
├── styles.css             # Primary stylesheet
├── timer.js               # Frontend timer logic
│
├── /static
│   ├── styles.min.css     # minified CSS
│   ├── timer.min.js       # minified JS
│
├── /logo
│   └── Logo.png
│
├── /images                # Background images
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
│
└── /sound
    └── classic_alarm_clock.mp3
```

---

## 📦 Installation

### 1. Install Requirements

```bash
pip install flask
```

### 2. Run the Application

```bash
python app.py
```

### 3. Access the Timer

Visit:

```
http://localhost:5000
```

Or on your LAN:

```
http://YOUR-IP:5000
```

---

## 🧪 Usage Guide

### Start a preset timer

Click any icon:

* 📅 Class Starts
* ☕ Coffee Break
* 🍔 Lunch Break
* 🧪 Lab Session

### Create a Custom Timer

1. Click the **gear icon**
2. Set:
   * Hours & minutes
   * Title
   * Description
   * Next-up message
3. Click **Save**
4. Timer loads automatically

### Audio Notification

First click unlocks browser-restricted audio policy.

---

## 👤 Author

**George Liberatos**
Lead Systems Engineer
Cloud & Infrastructure | Flask Developer | Training Technology Specialist

---

## ⭐ Contributions

Pull requests and feature suggestions are welcome.
For major changes, open an issue first to discuss your approach.

---

## 📝 License

Released under the **MIT License**.

---
