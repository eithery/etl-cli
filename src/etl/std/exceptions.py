#
# (C) Eithery Lab, 2023
# Contains custom exceptions
#
class InvalidResultException(Exception):
    def __init__(self, message="Invalid Result value"):
        super().__init__(message)
