# Python Programming Lab Practicals

Source: the uploaded Marwadi University Python Programming (05CS2104) lab manual, 2025–26.

This archive contains 59 numbered practical folders. Each folder has `main.py` and a short README. Practical 57 includes a sample `login.txt`; Practical 58 includes sample `file1.txt` and `file2.txt`.

## Run a practical

1. Install Python 3.10 or newer.
2. Extract this ZIP file.
3. Open a terminal in the required `Practical-NN` folder.
4. Run `python main.py`.

## Dependencies and environment

- Practicals 1–31 and 47–59 primarily use Python standard-library modules.
- Practicals 32–35 require MySQL Server and `mysql-connector-python`. The source code connects to localhost, user `root`, empty password, database `python`; adjust these values for your installation.
- Practicals 36–41 require `pandas` and `matplotlib`.
- Practicals 42–45 require `python-whois` and internet access.
- Practical 46 requires `dnspython` and DNS/internet access. Its source code uses `socket` and `dns.resolver` (not the `dig` shell command named in the objective).
- Practical 48 scans the listed ports on localhost. Only scan systems you own or are authorized to test.
- Practical 51 uses `ping`; behavior depends on OS/network/firewall settings.

Install optional third-party packages with:

```bash
python -m pip install mysql-connector-python pandas matplotlib python-whois dnspython
```

## Source fidelity and validation

The scripts are transcribed from the uploaded manual. Practical 10 had one stray leading space before its first top-level statement; that formatting issue was removed so the file compiles. Other code has not been silently redesigned. Some practical objectives and source implementations differ; consult the original manual and your instructor.

A Python syntax compilation check was run on all 59 `main.py` files. This does not mean environment-dependent programs (MySQL, WHOIS, DNS, plotting, network scanning) were executed end-to-end.
