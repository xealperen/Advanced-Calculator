# 🧮 Modern Dark-Theme Python Calculator

An iOS-inspired, sleek desktop calculator built using **Python** and **Tkinter**. It combines a clean dark UI with a secure string-parsing evaluation mechanism to perform real-time arithmetic calculations safely.

![Python Version](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GUI Framework](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Interface & Layout Structure](#-interface--layout-structure)
- [Security & Input Validation](#-security--input-validation)
- [Quick Start & Usage](#-quick-start--usage)
- [Code Architecture](#-code-architecture)
- [Tech Stack](#-tech-stack)
- [Author](#-author)

---

## 📖 Overview

This project is a lightweight desktop calculator application designed with modern aesthetics in mind. It mimics classic mobile calculator interfaces while leveraging native Python libraries (`tkinter` and `re`) to ensure high performance without requiring external third-party dependencies.

---

## ✨ Key Features

- **Dark Mode Aesthetic:** Crafted using `#1C1C1C` background hues, contrast text colors, and `#FF9500` accent buttons for an iOS-like look and feel.
- **Full Keypad Controls:** Numeric inputs (0-9), basic operators (`+`, `-`, `*`, `/`), clear display (`C`), and compute trigger (`=`).
- **Input Sanitization & Safe Evaluation:** Restricts evaluation inputs using strict Regular Expressions (`re`) to protect against unsafe execution.
- **Graceful Error Handling:** Immediately detects syntax errors or invalid mathematical sequences and outputs a clear `"Geçersiz İfade"` alert on the display.
- **Zero External Dependencies:** Completely standalone—runs out of the box with any standard Python 3 installation.

---

## 🎨 Interface & Layout Structure

The layout is structured using a precise 5x4 Grid Layout system:

| Row | Column 0 | Column 1 | Column 2 | Column 3 |
| :-: | :------: | :------: | :------: | :------: |
| **0** | <td colspan="4"> **Display Panel (`Entry`)** </td> |
| **1** | `1` | `2` | `3` | `/` |
| **2** | `4` | `5` | `6` | `*` |
| **3** | `7` | `8` | `9` | `-` |
| **4** | `C` | `0` | `=` | `+` |

---

## 🔒 Security & Input Validation

Unlike naive implementations using un-sanitized `eval()`, this application implements a two-layer security approach:

1. **Regex Pattern Match:** Validates that the input string strictly contains allowed mathematical characters (`0-9`, `+`, `-`, `*`, `/`, `(`, `)`, `.`, and spaces).
   ```python
   re.fullmatch(r"[0-9+\-*/(). ]+", ifade)
