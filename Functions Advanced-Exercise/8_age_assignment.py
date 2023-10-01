def age_assignment(*args, **kwargs):
    peoples = {}
    for name in args:
        peoples[name] = kwargs[name[0]]
    result = sorted(peoples.items(), key=lambda x: x[0])
    final_result = []
    for name, age in result:
        final_result.append(f"{name} is {age} years old.")
    return "\n".join(final_result)


print(age_assignment("Peter", "George", G=26, P=19))