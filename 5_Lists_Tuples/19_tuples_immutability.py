welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Budgie", "Never Turn Your Back on a Friend", 1974
imelda = "More Mayhem", "Imelda May", 2010
metallica = "Metallica", "Master of Puppets", 1986

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
# metallica[0] = "Master of puppets":  Tuples are immutable. You cannot assign a new value to an element of a tuple. Because they do not have the overhead of the methods to change them, tuples are generally faster than lists.

metallica2 = list(metallica)  # Convert tuple to list
metallica2[0] = "Master of puppets"
print(metallica2)
