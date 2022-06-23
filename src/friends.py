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

