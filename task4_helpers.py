def calculate_score(gem_count, gem_type):
    if gem_type == "normal":
        price = gem_count * 10
        return price
    elif gem_type == "bomb":
        price = gem_count * 25
        return price
    else:
        price = gem_count * 5
        return price

