## 🏦 Bank Management System
Welcome to my Bank Management System — a super clean, interactive, and user-friendly console application built using Python.
This project simulates core retail banking operations right inside your terminal. It skips the headache of setting up a heavy database by running entirely in-memory, which means your accounts, balances, and deposits stay alive dynamically while your program runs. It’s snappy, easy to read, and packed with interactive terminal elements! 🚀

# ⚡ Key Banking Features :-
- Seamless Account Creation: Spin up a new bank account instantly by assigning a unique account number, naming the holder, and depositing an initial balance. (The app features built-in verification to stop anyone from stealing an existing account number!).
- Dynamic Cash Deposits: Top up an account instantly. The system securely locates the profile, prints a quick verification name check, and safely rolls the money into your balance.
- Bulletproof Withdrawals: Cash out safely! The core ledger performs immediate transaction checks to safeguard account stability. It completely blocks any overdraft attempts if funds run low, but will let you withdraw your exact balance down to Rs. 0!
- Instant Balance Enquiry: Pull up an official balance report on demand showing the owner's title-cased name and current liquid funds.
- Crash-Resistant Input Guards: Built with smart input monitoring to prevent the terminal from crashing if a user accidentally types text into numeric fields (like choice menus or cash values).

# 🛠️ Tech Highlights :-
- Language: Pure Python 3.10+ using structured condition loops.
- Memory Architecture: Uses a synchronized, multi-array system tracking arrays of matching index IDs (account_numbers, account_names, and account_balances) to handle lightning-fast lookups.
- Text Formatting: Features built-in string title-casing (.title()), transforming messy terminal inputs like "dhrubo das" into clean, formal display records like "Dhrubo Das".
