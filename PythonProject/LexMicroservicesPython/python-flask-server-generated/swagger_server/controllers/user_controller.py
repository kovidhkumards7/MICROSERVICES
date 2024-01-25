import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def add_user(body):  # noqa: E501
    """Add a new user to the validator Application

     # noqa: E501

    :param body: User object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_users():  # noqa: E501
    """Finds all Users

    Provide details of all customers # noqa: E501


    :rtype: User
    """
    return 'do some magic!'


def validate_user(body):  # noqa: E501
    """validates user data

     # noqa: E501

    :param body: User object that needs to be added to the database
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
