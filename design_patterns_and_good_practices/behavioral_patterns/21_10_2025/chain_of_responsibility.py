import random


""" CHAIN OF RESPONSIBILITY """

# Interfata comuna pt. datele de autentificare
class Credentials:
    def get_credentials(self, user_id):
        pass                                                      # Metoda abstracta - va fi implementata in clasele derivate


# Implementarea pt. AWS Token
class AWSSignature(Credentials):
    def get_credentials(self, user_id):
        return "98f92d42-66c7-4ce4-a834-087a783133e7"             # Returneaza un Token AWS fictiv


# Implementarea pt. Bearer Token
class BearerToken(Credentials):
    def get_credentials(self, user_id):
        return "1/mZ1edKKACtPAb7zGlwSzvs72PvhAbGmB8K1ZrGxpcNM"    # Returneaza un Token Bearer fictiv


# Implementarea pt. Username + password
class UserNameAndPasswordCredentials(Credentials):
    def get_credentials(self, user_id):
        return "andrew:Andrew_123"                                # Returneaza credentiale de tip user/parola


# Interfata comuna pt. toate tipurile de handler-e
class AuthenticationHandler:
    def authenticate(self, credentials):
        pass                                                      # Metoda abstracta - va fi suprascrisa

    def supports(self, cls):
        pass                                                      # Metoda care verfica daca handler-ul poate procesa
                                                                  # tipul de credentiale


# Handler pt. autentificarea AWS
class AWSAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):                            # Verifica daca poate gestiona tipul de credentiale
            return self.authenticate_in_aws(credentials)          # Incearca autentificarea AWS
        else:
            return False                                          # Daca nu poate returneaza "False"

    def supports(self, cls):
        return isinstance(cls, AWSSignature)                      # Verifica daca obiectul este de tip AWS Signature

    def authenticate_in_aws(self, credentials):
        return random.randint(1, 3) == 1                    # Simuleaza o autentificare reusita cu probabilitatea 1/3


# Handler pt. autentificarea Bearer Token
class BearerTokenAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):                            # Verifica daca poate gestiona tipul Bearer
            return self.is_token_valid(credentials)               # Incearca validarea token-ului
        else:
            return False                                          # Daca nu poate returneaza "False"

    def supports(self, cls):
        return isinstance(cls, BearerToken)                       # Verifica daca obiectul este de tip BearerToken

    def is_token_valid(self, credentials):
        return random.randint(1, 3) == 2                    # Simuleaza o autentificare reusita cu probabilitatea 2/3


# Handler pt. autentificarea cu Username si Password
class UserNameAndPasswordAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):                            # Verifica daca poate gestiona tipul respectiv
            return self.is_password_valid(credentials)            # Incearca validarea parolei
        else:
            return False                                          # Daca nu poate returneaza "False"

    def supports(self, cls):
        return isinstance(cls, UserNameAndPasswordCredentials)    # Verifica tipul obiectului

    def is_password_valid(self, credentials):
        return random.randint(1, 3) == 3                    # Simuleaza o autentificare reusita cu probabilitatea 3/3


class ChainAuthenticationElement:
    def __init__(self, authentication_handler, next=None):
        self._authentication_handler = authentication_handler      # Stocheaza handler-ul curent
        self._next = next                                          # Facem referinta la urmatorul element din lant

    def authenticate(self, credentials):
        if self._authentication_handler.authenticate(credentials):
            print(f"Authentication using handler {credentials.__class__.__name__}")
            return True
        else:
            return self._next and self._next.authenticate(credentials)


def main():
    # Cream cele 3 tipuri de handler-e
    authentication_handler_unp = UserNameAndPasswordAuthenticationHandler()
    authentication_handler_bearer = BearerTokenAuthenticationHandler()
    authentication_handler_aws = AWSAuthenticationHandler()

    # Construim lantul: [Username/Password] -> [Bearer] -> [AWS]
    last_element = ChainAuthenticationElement(authentication_handler_aws)                        # Ultimul din lant
    middle_element = ChainAuthenticationElement(authentication_handler_bearer, last_element)     # Al doilea
    first_element = ChainAuthenticationElement(authentication_handler_unp, middle_element)       # Primul

    # Incercam autentificarea cu toate tipurile de credentiale
    first_element.authenticate(AWSSignature())
    first_element.authenticate(UserNameAndPasswordCredentials())
    first_element.authenticate(BearerToken())


if __name__ == '__main__':
    main()
