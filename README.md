# 🤖 Customer Service Automation Chatbot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

💬 An intelligent chatbot solution for automating customer support processes, combining Python backend with PHP web interface.

## 📋 Table of Contents
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)

## ✨ Features

### Core Functionality
- **Conversation Automation** - Handles common customer inquiries without human intervention
- **Process Integration** - Connects with support systems for ticket generation
- **Interaction Logging** - Maintains complete conversation history

### Technical Features
- **Multi-platform Support** - Works across web and messaging platforms
- **Natural Language Processing** - Basic intent recognition for query understanding
- **Database Integration** - MySQL backend for data persistence

## 🛠 Technology Stack

### Backend
- ![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
- ![Selenium](https://img.shields.io/badge/Selenium-4.0+-43B02A?logo=selenium&logoColor=white)

### Frontend
- ![PHP](https://img.shields.io/badge/PHP-8.0%2B-777BB4?logo=php&logoColor=white)
- ![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)

### Development Tools
- ![XAMPP](https://img.shields.io/badge/XAMPP-8.1%2B-FB7A24?logo=xampp&logoColor=white)
- ![Git](https://img.shields.io/badge/Git-2.35%2B-F05032?logo=git&logoColor=white)

## 🏗 System Architecture
```
chatbot-python/
├── .git/              # Version control configuration
├── bot.py             # Core chatbot logic (Python)
├── chromedriver.exe   # Browser automation driver
├── index.php          # Web interface (PHP)
└── pasta/             # Resource files
    ├── config/        # Configuration files
    ├── lib/           # Library dependencies
    └── logs/          # Conversation logs
```

## 📦 Prerequisites

### Required Software
- [XAMPP 8.1+](https://www.apachefriends.org/download.html) (Apache, MySQL, PHP)
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### System Requirements
- Windows 10/11 or Linux
- 4GB RAM minimum
- 500MB disk space

## 🔧 Installation

1. **Environment Setup**
   ```bash
   # Install XAMPP and start MySQL/Apache services
   # Install Python and add to PATH
   ```

2. **Clone Repository**
   ```bash
   git clone https://github.com/your-repo/chatbot-python.git
   cd chatbot-python
   ```

3. **Install Dependencies**
   ```bash
   pip install selenium==4.0.0
   ```

## ⚙ Configuration

1. **Database Setup** 🗄️
   - Create MySQL database via phpMyAdmin
   - Import any provided SQL schema files

2. **Environment Variables** 🔧
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASS=
   DB_NAME=chatbot_db
   ```

## 🚀 Usage

### ▶️ Running the Chatbot
```bash
python bot.py
```

### 🌐 Accessing Web Interface
```
http://localhost/chatbot-python/index.php
```

### ⚙️ System Management
- Start/stop services through XAMPP Control Panel
- Monitor logs in `pasta/logs/` directory 📝

---

🤖 Developed with ❤️ by Pedro | 📌 [Contribute](CONTRIBUTING.md)
