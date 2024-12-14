
def has_permission(user_info, accessing_data):
    res = {"movies": False, "books": False, "games": False}
    for info in user_info:
        item, permission = info.split("_")
        if item == "*":
            if permission == "allow":
                res["movies"] = True
                res["books"] = True
                res["games"] = True
            else:
                res["movies"] = False
                res["books"] = False
                res["games"] = False
        if permission == "allow":
            res[item] = True
        else:
            res[item] = False



    return res[accessing_data]



print(has_permission({'books_allow', 'movies_deny'}, 'movies'))
print(has_permission({'books_allow', 'movies_deny'}, 'books'))
print(has_permission({'*_allow', 'books_allow', 'movies_deny'}, 'games'))
print(has_permission({'*_allow', '*_deny'}, 'movies'))
