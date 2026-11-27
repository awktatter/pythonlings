# Exercise: Loops 10
# I AM  DONE
#
# Combine looping techniques to process `transactions`.
# Each transaction is a dict with keys "amount" (int) and "type" ("credit" or "debit").
# Build `summary` as a list of dicts, one per transaction, with keys:
#   "index"   : 1-based position (use enumerate)
#   "amount"  : the original amount
#   "balance" : running balance so far (credits add, debits subtract)
# Skip any transaction whose amount is 0 (use continue).
# Starting balance is 0.

transactions = [
    {"amount": 100, "type": "credit"},
    {"amount": 0,   "type": "debit"},
    {"amount": 40,  "type": "debit"},
    {"amount": 200, "type": "credit"},
    {"amount": 60,  "type": "debit"},
]
summary = []
balance = 0
# write your for loop here (use enumerate, continue, and update balance)
for i, tx in enumerate(transactions, start=1):
    if tx["amount"] == 0:
        continue
    if tx["type"] == "credit":
        balance += tx["amount"]
    else:
        balance -= tx["amount"]

    entry = { "index": i, "amount": tx["amount"], "balance": balance }
    summary.append(entry)