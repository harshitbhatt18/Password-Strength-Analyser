# Password Strength Analyzer

A sophisticated web-based password strength analysis tool built with Flask that evaluates password security and generates strong passwords. The application provides real-time feedback on password quality, checking against common passwords, complexity requirements, and security best practices.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **Password Strength Testing**: Comprehensive password analysis with scoring system
- **Common Password Detection**: Checks against 10,000+ most common passwords
- **Complexity Analysis**: Evaluates use of lowercase, uppercase, digits, and special characters
- **Length Validation**: Ensures passwords meet minimum length requirements
- **Pattern Detection**: Identifies repeated character sequences
- **Secure Password Generator**: Creates strong, customizable passwords
- **Real-time Feedback**: Provides actionable suggestions for improvement
- **Modern UI**: Clean, responsive interface with visual strength indicators

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Password Scoring System](#-password-scoring-system)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Demo

The Password Strength Analyzer evaluates passwords based on multiple criteria:

- **Weak Password**: Score ≤ 3 (e.g., "password123")
- **Moderate Password**: Score 4-5 (e.g., "Pass1234!")
- **Strong Password**: Score ≥ 6 (e.g., "P@ssw0rd#2024!")

## 💻 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/harshitbhatt18/Password-Strength-Analyser.git
   cd Password-Strength-Analyser
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 📖 Usage

### Testing Password Strength

1. Enter a password in the input field
2. Click "Test Password" button
3. View the comprehensive analysis including:
   - Overall strength level (Weak/Moderate/Strong)
   - Numerical score (0-9)
   - Detailed feedback and improvement suggestions

### Generating Strong Passwords

1. Click "Generate Strong Password" button
2. Optionally specify:
   - **Password Length**: 10-128 characters (default: 16)
   - **Required Characters**: Specific characters to include
3. Click "Generate Password"
4. The generated password will be automatically populated in the input field

## 📁 Project Structure

```
Password-Strength-Analyser/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── 10k_most_common.txt        # Dictionary of common passwords
├── README.md                   # Project documentation
│
├── templates/
│   └── index.html             # Main HTML template
│
└── static/
    ├── style.css              # Stylesheet
    └── script.js              # Client-side JavaScript
```

## 🔍 Password Scoring System

The password strength is calculated based on the following criteria:

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Not Common** | +1 | Password not in common passwords list |
| **Length** | 1-3 | 6-8 chars (+1), 9-10 chars (+2), 11+ chars (+3) |
| **Complexity** | 1-4 | Lowercase only (+1), Upper+Lower (+2), Upper+Lower+Digits (+3), All types (+4) |
| **No Sequences** | +1 | No repeated character sequences (e.g., "aaa", "111") |

**Total Maximum Score**: 9 points

**Strength Levels**:
- **0-3 points**: Weak ❌
- **4-5 points**: Moderate ⚠️
- **6-9 points**: Strong ✅

## 🛠️ Technologies Used

- **Backend**: Python 3.x, Flask 3.0.0, Gunicorn (Production Server)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Password Analysis**: Regular expressions, string operations
- **Security**: Common password dictionary validation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - feel free to use it for personal or commercial projects.

<div align="center">
Made with ❤️ by Harshit Bhatt
</div>

