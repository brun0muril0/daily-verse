# Daily Verse - Daily Bible Verse Messenger

### 📖 Overview

**Daily Verse** is a simple yet powerful Python script that sends a daily Bible verse via WhatsApp using the Twilio API. Every time the script runs, it fetches a random Bible verse and sends it to a specified phone number or a group of numbers. It's a great way to start your day with inspiration, or share God's word with others.

---

### 🔧 Features

- **Daily Bible Verse**: Get a random verse from the Bible API.
- **Twilio Integration**: Use Twilio to send messages via WhatsApp.
- **Configurable Recipients**: Send verses to multiple recipients or groups.
- **Environment Variables**: Secure handling of sensitive information (Twilio credentials) via `.env`.

---

### 📋 Requirements

- **Python 3.x** 
- **Twilio Account**: You need a Twilio account to send messages through WhatsApp.
- **Python Libraries**: 
    - `requests` (for making HTTP requests)
    - `twilio` (for interacting with Twilio API)
    - `python-dotenv` (for managing environment variables)

---

### 🛠️ Installation

1. Clone this repository to your local machine:
   
   ```bash
   git clone https://github.com/brun0muril0/daily-verse.git

2. Navigate to the project directory:
   
   ```bash
   cd daily-verse

3. Create a virtual environment (recommended):

   ```bash
   python3 -m venv venv

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

5. Create a .env file at the root of the project and add your Twilio credentials:

   ```bash
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_WHATSAPP_NUMBER=from_number
   RECIPIENT_NUMBERS=to_number,to_number,to_number...

6. Create a .env file at the root of the project and add your Twilio credentials:

   ```bash
   python daily_verse.py

---

### 🌱 How it works

- **Fetching the verse**: The script makes a request to Bible API to retrieve a random Bible verse.
- **Formatting the message**: The verse is formatted into a clean, readable message with the verse text and reference.
- **Sending the message**: Twilio’s WhatsApp API sends the message to the specified number(s) using the credentials provided in the`.env`.

---

### 🚀 Contributing
Feel free to open issues or pull requests if you'd like to contribute to this project. Contributions, suggestions, and improvements are always welcome!

---

### 📬 Contact
- Author: Bruno Murilo
- GitHub: [@brunomurilo](https://github.com/brun0muril0)
- Linkedin: [Bruno Murilo](https://www.linkedin.com/in/bruno-murilo/)



