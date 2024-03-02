class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.__min_length = min_length
        self.__mails = mails
        self.__domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.__min_length

    def __is_mail_valid(self, mail):
        return mail in self.__mails

    def __is_domain_valid(self, domain):
        return domain in self.__domains

    def validate(self, email):
        username, rest = email.split('@')
        mail, domain = rest.split('.')
        return self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)

# test code
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
