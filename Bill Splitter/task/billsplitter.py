# write your code here
import random
print("Enter the number of friends joining (including you):")
friend_count = int(input())

if friend_count <= 0:
    print("No one is joining for the party")
else:
    friends = dict()
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(friend_count):
        name = input()
        friends[name] = 0
    print("Enter the total bill value:")
    bill_value = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    use_lucky = input()
    if use_lucky == "Yes":
        lucky_person = random.choice(list(friends.keys()))
        print(f"\n{lucky_person} is the lucky one!")
        split_value = round(bill_value / (friend_count - 1), 2)
        for person in friends:
            if person != lucky_person:
                friends[person] = split_value

    else:
        print("\nNo one is going to be lucky")
        split_value = round(bill_value / friend_count, 2)
        for friend in friends:
            friends[friend] = split_value
    print(friends)
    