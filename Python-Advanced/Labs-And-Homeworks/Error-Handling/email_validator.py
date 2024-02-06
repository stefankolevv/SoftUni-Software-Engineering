import re


class NameTooShortError(Exception):
    def __init__(self, message='Name must be more than 4 characters'):
        super().__init__(message)


class MustContainAtSymbolError(Exception):
    def __init__(self, message='Email must contain @'):
        super().__init__(message)


class InvalidDomainError(Exception):
    def __init__(self, message='Domain must be one of the following: .com, .bg, .org, .net'):
        super().__init__(message)


class InvalidNameError(Exception):
    def __init__(self, message='Name must contain only letters, digits and underscores'):
        super().__init__(message)


while True:
    email = input()
    pattern = r'\w+'

    if email == 'End':
        break

    if len(email.split('@')[0]) <= 4:
        raise NameTooShortError()

    if '@' not in email:
        raise MustContainAtSymbolError()

    if re.findall(pattern, email.split('@')[0])[0] != email.split('@')[0]:
        raise InvalidNameError()

    domain = email.split('.')[-1]
    valid_domains = ['com', 'bg', 'org', 'net']

    if domain not in valid_domains:
        raise InvalidDomainError()

    print('Email is valid')
