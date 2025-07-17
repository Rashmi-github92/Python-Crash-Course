guests = ['SRK', 'Donald Trump', 'Modi', 'Deepika']
print(f"Only two people will be invited for dinner)")
shrink_guest = guests.pop()
shrink_guest_2 = guests.pop()
print(f"Sorry you're not invited for dinner {shrink_guest.title()}.")
print(f"Sorry you're not invited for dinner {shrink_guest_2.title()}.")
print(f"Dear {guests[0]}, you're still invited for dinner!")
print(f"Dear {guests[1]}, you're still invited for dinner!")
del guests[0]
del guests[0]
print(guests)
len(guests)



 