def gather_credits(credits_needed, *args):
    current_credits = 0
    courses = []
    for key, value in args:
        if current_credits >= credits_needed:
            break
        else:
            if key in courses:
                continue
            current_credits += int(value)
            courses.append(key)
    if current_credits >= credits_needed:
        return f"""Enrollment finished! Maximum credits: {current_credits}.
Courses: {', '.join(sorted([str(el) for el in courses]))}"""
    else:
        credits_shortage = credits_needed - current_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
