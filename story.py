myName = "Annie"
myEyes = "blue"
myMoney = 10
myPets = 12
myFriends = 5

myFriendsAndPets = myFriends + myPets
myMoneyFriends = myMoney * myFriends
myPetsAndFriendsAfterDeath = (myPets - 2) + myFriends
myMoney2myFriends = myMoney / myFriends


print "Hi my name is", myName, "and I have", myEyes, "eyes."
print "I have %d friends and %d friends and pets." % (myFriends, myFriendsAndPets)
print "I can spend $",myMoneyFriends, "on my friends."
print "If 2 of my pets died I would have %d pets and friends." % myPetsAndFriendsAfterDeath
print "If I divice my money by my friends I get $", myMoney2myFriends,"."
