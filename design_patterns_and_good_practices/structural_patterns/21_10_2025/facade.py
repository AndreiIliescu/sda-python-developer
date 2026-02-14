""" FACADE

Ofera o interfata simplificata pt. un sistem complex.
Scop: folosit cand vrem sa ascundem complexitatea interna a mai multor clase.
Creaza un punct unic de acces pt. client. """

# ex.1
class DeliveryService:
    def deliver_product(self, product_id, amount, recipient):
        pass


class PaymentService:
    def pay(self, product_id, amount):
        pass


class ProductAvailabilityService:
    def is_available(self, product_id):
        pass


class OrderFacade:
    def __init__(self, delivery_service, payment_service, product_availability_service):
        self._delivery_service = delivery_service
        self._payment_service = payment_service
        self._product_availability_service = product_availability_service

    def place_order(self, product_id, amount, recipient):
        if self._product_availability_service.is_available(product_id):
            self._payment_service.pay(product_id, amount)
            self._delivery_service.deliver_product(product_id, amount, recipient)


# ex.2
class Encryptor:
    def encrypt(self, to_encrypt):
        pass


class BCryptEncryptor(Encryptor):
    def encrypt(self, to_encrypt):
        return f"encrypting {to_encrypt} with BCrypt"


class SCryptEncryptor(Encryptor):
    def encrypt(self, to_encrypt):
        return f"encrypting {to_encrypt} with SCrypt"


class NoOpEncryptor(Encryptor):
    def encrypt(self, to_encrypt):
        return to_encrypt


class Encryptors:
    def encrypt_without_modification(self, to_encrypt):
        pass

    def encrypt_with_bcrypt(self, to_encrypt):
        pass

    def encrypt_with_scrypt(self, to_encrypt):
        pass


class EncryptionFacade(Encryptors):
    def __init__(self, scrypt_encryptor, bcrypt_encryptor, noop_encryptor):
        self._scrypt_encryptor = scrypt_encryptor
        self._bcrypt_encryptor = bcrypt_encryptor
        self._noop_encryptor = noop_encryptor

    def encrypt_without_modification(self, to_encrypt):
        return self._noop_encryptor.encrypt(to_encrypt)

    def encrypt_with_bcrypt(self, to_encrypt):
        return self._bcrypt_encryptor.encrypt(to_encrypt)

    def encrypt_with_scrypt(self, to_encrypt):
        return self._scrypt_encryptor.encrypt(to_encrypt)
