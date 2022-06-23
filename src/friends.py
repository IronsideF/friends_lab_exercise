def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    snacks = person["favourites"]["snacks"]
    for snack in snacks:
        is_favourite = False
        if snack == food:
            is_favourite = True
            break
    return is_favourite

def add_friend(person, friend):
    friend_list = person["friends"]
    friend_list.append(friend)

def remove_friend(person, friend):
    friend_list = person["friends"]
    friend_list.remove(friend)

def total_money(person_list):
    total = 0
    for person in person_list:
        total += person["monies"]
    return total

def lend_money(lender, reciever, loan_amount):
    lender["monies"] = lender["monies"] - loan_amount
    reciever["monies"] = reciever["monies"] + loan_amount


def all_favourite_foods(list):
    snacks_total = []
    for person in list:
        snacks_total += person["favourites"]["snacks"]
    return snacks_total

def find_no_friends(people):
    for person in people:
        if person["friends"] == []:
            return [person]

def unique_favourite_tv_shows_manual(people):
    tv_shows = []
    for person in people:
        is_duplicate = False
        for show in tv_shows:
            if person["favourites"]["tv_show"] == show:
                is_duplicate = True
        if not is_duplicate:
            tv_shows.append(person["favourites"]["tv_show"])
        else:
            pass
    return tv_shows

def unique_favourite_tv_shows(people):
    unique_tv_list =[]
    for person in people:
        if person["favourites"]["tv_show"] not in unique_tv_list:
            unique_tv_list.append(person["favourites"]["tv_show"])
    return unique_tv_list