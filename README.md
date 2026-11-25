# Python Programming Lab Manual

**Marwadi University · Faculty of Computer Applications**  
**Course:** Python Programming (05CS2104)  
**Program:** M.Sc. (Cyber Security & Cyber Law) · **Semester:** 1 · **Academic year:** 2025–26

This repository organizes all 59 practicals from the uploaded lab manual.

## Download all practicals

[Download the Python practicals archive](python-practicals.tar.gz)

Extract the archive. It contains a `python-practicals/` folder with 59 numbered practical folders, each containing a `main.py` file. Sample input files are included for Practicals 57 and 58.

## Run a practical

1. Install Python 3.10 or newer.
2. Extract the archive and open the folder for the practical you want.
3. Open a terminal in that practical's folder.
4. Run:

   ```bash
   python main.py
   ```

Some programs ask for keyboard input. Run each program from its own folder so relative input files are found.

## Practical index

- **Practical 01:** Python Program to Print Hello World.
- **Practical 02:** Python program to do arithmetical operations
- **Practical 03:** Python program to swap two variables
- **Practical 04:** Python Program to Find the Factorial of a Number
- **Practical 05:** Python Program to Print the Fibonacci sequence
- **Practical 06:** Python program to print the elements of an array
- **Practical 07:** Python program to print the largest element and smallest element in an array
- **Practical 08:** Python program to add two matrix using array and function
- **Practical 09:** Python Program to concatenate two strings
- **Practical 10:** Python Programs to perform various operations on Strings using functions
- **Practical 11:** Python Programs to demonstrate use of list and various functions of it
- **Practical 12:** Python Programs to demonstrate use of tuple and various functions of it
- **Practical 13:** Python Programs to demonstrate the use of dictionary and various functions of it
- **Practical 14:** Python Programs to create a function (Make your own assumptions)
- **Practical 15:** Python Programs to demonstrate use of various arguments which can be passed to functions
- **Practical 16:** Python Program to demonstrate the use of class
- **Practical 17:** Python Program to demonstrate the concept of inner class
- **Practical 18:** Python program to demonstrate the use of methods
- **Practical 19:** Python program to demonstrate various types of methods
- **Practical 20:** Method overloading by adding two numbers and three numbers using the same method name
- **Practical 21:** Method overriding using a parent class Animal and a child class Dog
- **Practical 22:** Single inheritance using classes Animal and Dog
- **Practical 23:** Various forms of inheritance
- **Practical 24:** Handle division by zero using try and except
- **Practical 25:** Handle invalid input entered by the user
- **Practical 26:** Use try–except–else block
- **Practical 27:** Use try–except–finally block
- **Practical 28:** Demonstrate use of modules
- **Practical 29:** Demonstrate the use of file handling
- **Practical 30:** Demonstrate the use of various modes of files
- **Practical 31:** Demonstrate the use of regular expression
- **Practical 32:** Connect Python with MySQL database
- **Practical 33:** Create a table, insert records, retrieve and display records
- **Practical 34:** Update records into a MySQL table and display records
- **Practical 35:** Delete records from a MySQL table and display records
- **Practical 36:** Demonstrate the use of DataFrames in Python
- **Practical 37:** Different ways of creating DataFrames
- **Practical 38:** Create Pie chart
- **Practical 39:** Create histogram
- **Practical 40:** Create bar graph
- **Practical 41:** Create Line graph
- **Practical 42:** Perform a WHOIS lookup for a given domain name
- **Practical 43:** Accept a domain name and show basic WHOIS information
- **Practical 44:** Display the domain registrar name using WHOIS
- **Practical 45:** Display the domain creation date using WHOIS
- **Practical 46:** Use DNS lookup to find the IP address and DNS A records
- **Practical 47:** Detect emails using regular expressions
- **Practical 48:** Simple port scanner using socket
- **Practical 49:** Generate hash values using hashlib
- **Practical 50:** Check files in a directory using os
- **Practical 51:** Ping scanner to show IP up or down
- **Practical 52:** Generate a random password
- **Practical 53:** Generate a six-digit One-Time Password (OTP)
- **Practical 54:** Encode and decode a message using Base64
- **Practical 55:** Identify suspicious keywords in a URL
- **Practical 56:** Identify potentially risky file extensions
- **Practical 57:** Read a sample security log and count failed login attempts
- **Practical 58:** Check whether two files contain identical data
- **Practical 59:** Identify the category of an IP address

## Dependencies

Install third-party packages only if you plan to run the practicals that use them:

```bash
python -m pip install -r requirements.txt
```

- Practicals 32–35: MySQL Server must be installed and running. Create a database named `python`. The manual's connection settings are `localhost`, user `root`, empty password; update them in the scripts for your local MySQL configuration. Run Practical 33 before Practicals 34 and 35.
- Practicals 36–41: Pandas and Matplotlib. Chart programs open a graphical plot window.
- Practicals 42–45: WHOIS package and internet access. WHOIS servers may rate-limit requests or return incomplete data.
- Practical 46: DNS/network access and dnspython. The objective mentions the `dig` command, but the manual's source code uses Python `socket` and `dns.resolver`; it does not execute `dig`.
- Practical 48: The supplied port scanner targets `127.0.0.1` and checks only the listed local ports. Scan only systems you own or have permission to test.
- Practical 51: The supplied ping command redirects output to `nul`, which is Windows-specific. On Linux/macOS, change it to `/dev/null`. Ping may be blocked by firewall or network settings.
- Practicals 52–53: The manual uses Python `random`; this is suitable for a basic demonstration, not for security-sensitive passwords or authentication OTPs. Use `secrets` in real applications.
- Practicals 57–58: Sample `login.txt`, `file1.txt`, and `file2.txt` files are included in their respective practical folders.

## Notes about the supplied manual

The practical source code is kept close to the uploaded manual. The scripts were checked for Python syntax, but not all were executed in their required environments (for example, MySQL, WHOIS, DNS, or graphical plotting).

A few objective/source mismatches in the manual are worth noting:
- Practical 8 mentions an array and function, while its source uses nested lists and loops without defining a function.
- Practical 17 says “inner class”, but its source defines `University` and `Student` as separate top-level classes.
- Practical 46 says to use `dig`, but its source uses `socket` and `dns.resolver`.
- Practical 59 checks `ipaddress.is_private` and prints private/public; it does not separately print every possible IP category.

Review the practical and your instructor's requirements before submitting or changing the code.

## License

No license has been specified. Unless a license is added, normal copyright rules apply.
