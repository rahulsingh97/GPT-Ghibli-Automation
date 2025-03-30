# 🚀 Ghibli-Styled ChatGPT Automation using Selenium

Welcome to the **Ghibli Style Generator** automation project! 🎨✨  
This project uses Python, Selenium, and Chrome to automatically log in to ChatGPT, upload a file, and send a prompt — all hands-free! 🖱️🧙‍♂️



## 📦 Prerequisites

### ✅ Python 3.7 or higher

Make sure Python is installed. You can verify it by running:

```bash
python --version
```

If not installed, download it from [python.org](https://www.python.org/downloads/)

---

## 🧪 Setting up a Virtual Environment (Recommended)

To keep dependencies clean and isolated:

```bash
python -m venv env
env\Scripts\activate  # Windows
# OR
source env/bin/activate  # macOS/Linux
```

---

## 📥 Install Required Packages

Once your environment is activated, run:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, run:

```bash
pip install selenium undetected-chromedriver fake_useragent pandas
```

---

## 🌐 Install ChromeDriver

You **must match** the ChromeDriver version with your **Chrome version**.

### 👇 Check Your Chrome Version:
Go to `chrome://settings/help` in your browser and note the version (e.g. `134.0.6998.178`).

### 🔗 Download ChromeDriver:
1. Visit 👉 [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
2. Scroll to your version and download the **ChromeDriver** for your OS (e.g., `chromedriver-win64.zip`)
3. Extract it and place `chromedriver.exe` in a known location like:

```plaintext
C:\candy\chromedriver\
```

---

## ⚙️ Add ChromeDriver to System PATH (Windows)

1. Press `Win + R`, type `sysdm.cpl`, press Enter.
2. Go to **Advanced > Environment Variables**
3. Under **System variables**, select `Path`, then click **Edit**
4. Click **New** and paste:
   ```
   C:\candy\chromedriver\
   ```
5. Press OK on all windows to save.

### ✅ Confirm Installation

In a new command prompt:

```bash
chromedriver --version
```

You should see the driver version print out.

---

## 🧪 Verify Selenium Works

Run this small test to check:

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)
driver.quit()
```

---

## 🚦 Running the Program

After installing everything:

```bash
python app.py
```

> 🛑 The script will prompt you to **solve CAPTCHA** and **press Enter** when ready.

---

## ❓ What This Script Does

- Opens Chrome with a spoofed user agent.
- Logs into ChatGPT.
- Uploads an image to ChatGPT.
- Sends a prompt like “Ghibli style for this image.”
- All this... **automatically** 🤖

---

## 💡 Want to Learn More?

Start here:
- [Selenium with Python Docs](https://selenium-python.readthedocs.io/)
- [Undetected ChromeDriver GitHub](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
- [Fake UserAgent Docs](https://pypi.org/project/fake-useragent/)

---

## 🧹 Troubleshooting

- **`chromedriver` not found?** ➜ Recheck PATH setup.
- **Version mismatch?** ➜ Ensure ChromeDriver version exactly matches Chrome browser.
- **CAPTCHA issues?** ➜ These are manual. Solve and continue.
- **"Element not found"?** ➜ Wait times may need tuning (`sleep()` durations).

---

## 🧠 Tip:
> Want a clean reset? Delete `./user-data-dir/` folder to clear Chrome profile & re-login.

---

Made with ❤️ by Rahul Singh  
*“A little automation goes a long way.”*
```

