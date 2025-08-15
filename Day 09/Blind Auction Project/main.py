import art
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        if highest_bid < bidding_dictionary[bidder]:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids={}
continue_bidding = True
while continue_bidding:
    name = input("what is your name?: ")
    price = int(input("Whats is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' to continue or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
