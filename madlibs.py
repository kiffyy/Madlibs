adjective = input("Adjective: ")
food = input("Food:")
color = input("color:")
name = input("Name:")
adj2 = input("Another Adjective:")
sport = input("Sport:")
pet = input("Animal:")
verb = input("Past verb:")
activity = input("activity:")

madlibs = 'Today is such a {adjective} day. I had {food} for lunch and it was so {color}.' \
          'Did you know that {name} is a {adj2}? and she plays {sport} everyday.' \
          ' i was a {pet} when i {verb} my first {activity}'.format(adjective=adjective, food=food, color=color, name=name,
                                                                    adj2=adj2, sport=sport, pet=pet, verb=verb,
                                                                    activity=activity)

print(madlibs)
