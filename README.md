# PyTweetCli

### Overview

PyTweetCli is a lightweight Python script for seamless Twitter tweet retrieval via the command line. Easily fetch tweets by username or keyword with simplicity and efficiency.

### Features

- Command-line interface for quick tweet retrieval
- Fetch tweets by username, keyword or link
- Lightweight and user-friendly

### Requirements

To run pyTweetCli, you need to have the following dependencies installed:
- [Python 3.11.6](https://www.python.org/downloads/)
- Selenium
- Pandas

### Getting Started

1. Clone the repository:
```bash
git clone https://github.com/imbngy/pyTweetCli.git
```

2. Navigate to the project directory:
```bash
cd PyTweetCli
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
py main.py
```

The script will launch a headless Chrome browser, navigate to twitter.com, and scrape tweets by given input.

### Usage

You can run the script with:
```bash
py main.py
```

or by adding a link argument:
```bash
py main.py -l https://twitter.com/tweet-link/example
```

Both cases it will ask you for a username, or email, and a password:
```bash
Enter your username/email:
Enter your password:
```

When you don't pass an argument, it will ask if you want to search by keyword or by user:
```bash
Select a search mode: 
1. Search by keyword
2. Search by user

Enter a number:
```
When searching by user, simply put whatever comes after the @, for example:
```bash
Enter the desired username: elonmusk
```

### Output

PyTweetCli provides output in two ways:

- **CSV File**: The script generates a CSV file with the fetched tweet data.
- **Command Line**: The fetched tweets are also displayed in the command-line interface.

Enhance your tweet harvesting experience with PyTweetCli!

### Contributing

Found a bug or have a suggestion? Open an issue or contribute to make PyTweetCli even better.
