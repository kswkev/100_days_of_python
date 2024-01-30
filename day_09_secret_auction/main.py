
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
more_bidders = "yes"
while more_bidders == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    bids[name] = bid

highest_bid = 0
highest_bidder = ""
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
