class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_LENGTH = 5
VALID_DOMAINS = [".com", ".bg", ".net", ".org"]

while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) < EMAIL_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = "." + email.split(".")[-1]

    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
