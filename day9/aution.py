
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
auction_bids={}
is_aution=True
while is_aution:
    name=input("What is you name?: ")
    bid=int(input("What is you bid?: "))
    auction_bids[name]=bid
   
    bidders=input("Are there other bidders? 'yes' or 'no' ")
    if bidders=="no":
        bid_winner=max(auction_bids.items(),  key=lambda x: x[1])
        bid_value=max(auction_bids.values())
        print(f"The winner is {bid_winner[0]} with a bid of ${bid_value}")
        is_aution=False
        break
    
