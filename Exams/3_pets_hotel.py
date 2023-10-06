def accommodate_new_pets(capacity, weight_limit, *args):
    animal_dict = {}
    result = []
    for animal, weight in args:
        if capacity <= 0:
            result.append(f"You did not manage to accommodate all pets!")
            break

        if weight <= weight_limit:
            if animal not in animal_dict:
                animal_dict[animal] = 0
            animal_dict[animal] += 1
            capacity -= 1
        else:
            continue

    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    sorted_dict = sorted(animal_dict.items(), key=lambda kvp: kvp[0])
    result.append('Accommodated pets:')
    [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted_dict]
    return '\n'.join(result)


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
