
def calculate_score(base_score, is_hard_level):
    if is_hard_level == True:
        base_score = base_score*2
        return base_score
    else:
        return base_score

print(calculate_score(12, False))