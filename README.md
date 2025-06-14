# Instagram Comment Automation 🤖

A Python script using Selenium to automate comments on Instagram posts. This tool logs into your account and posts multiple comments on a specified post.

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)](https://www.selenium.dev/)

## Features ✨
- 🔐 Automatic Instagram login
- 💬 Mass comment posting
- ⏳ Randomized delays to mimic human behavior
- 🛡️ Error handling for robust execution
- 🚫 Anti-bot detection measures

## Prerequisites 📋
- Python 3.7+
- Chrome browser installed
- ChromeDriver matching your Chrome version

## Installation ⚙️

*** 1. Clone the repository***
```bash
git clone https://github.com/SoorajTechie/Instagram-Comment-Automation.git
cd instagram-comment-bot
```
*** 2. Install dependencies:
   pip install selenium


### Configuration ⚡###
*** Edit the following variables in the script ***
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"
POST_URL = "https://www.instagram.com/p/EXAMPLE_POST/"  
COMMENT_TEXT = "Your comment text"
COMMENT_COUNT = 10  # Number of comments to post
