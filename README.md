```markdown
# Dotcoin BOT

🔗 **Register Here**: [DotCoin](https://t.me/dotcoin_bot?start=r_1719410244)

[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/shadowscripters)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ShadowScripts1)

## Table of Contents
- [Warning](#warning)
- [Available Features](#available-features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Thank You](#thank-you)

## Warning

All risks associated with using this bot are borne by the user.

## Available Features
- ✅ Auto Gacha
- ✅ Auto Tap Max Score
- ✅ Auto Clear Task
- ✅ Auto Upgrade Energy
- ✅ Multi Account Support

## Installation

### Prerequisites
- **Python 3.12**: [Download Python 3.12](https://www.python.org/downloads/)
- **Pip**: Ensure pip (Python package installer) is installed. It typically comes with Python.
- **Git**: Install Git from [git-scm.com](https://git-scm.com/).

### Step-by-Step Guide
1. **Clone the Repository**  
   Open your terminal and navigate to the directory where you want to clone the repository:
   ```bash
   cd ~/Documents/Projects
   ```
   Clone the repository:
   ```bash
   git clone https://github.com/ShadowScripts1/TG-dotcoin.git
   ```
   Then, navigate into the directory:
   ```bash
   cd TG-dotcoin
   ```

2. **Install Required Modules**  
   Install the necessary Python modules:
   ```bash
   pip install requests colorama
   ```

3. **Set Up Resource Override**  
   - Open Telegram Web or Telegram Desktop.
   - Open Developer Tools (`F12` or right-click and select "Inspect").
   - Go to the "Network" tab.
   - Set up a resource override with the following values:
     - **Tab URL**: `*`
     - **FROM**: `https://telegram.org/js/telegram-web-app.js`
     - **TO**: `https://ktnff.tech/universal/telegram-web-app.js`

4. **Retrieve Authorization Token**  
   - In Developer Tools, still in the "Network" tab, search for `get_user_info`.
   - Find the request and copy the **Authorization** header (excluding `Bearer`).

5. **Create `tokens.txt`**  
   - In the `TG-dotcoin` directory, create a file named `tokens.txt`.
   - Paste the authorization token into `tokens.txt` and save it.

## 🚀 How to Use
Run the bot with:
```bash
python bot.py
```
Make sure your authorization tokens are correctly set up in `tokens.txt`.

## Thank You
If you enjoy using this bot, please consider giving it a star on GitHub!
```