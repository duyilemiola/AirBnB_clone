#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a Review class"""

=======
"""Defines the Review class."""
>>>>>>> 8f984e8bc64ff190baab0ef0a90cff0f3aa44787
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """Class for managing review objects"""
=======
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """
>>>>>>> 8f984e8bc64ff190baab0ef0a90cff0f3aa44787

    place_id = ""
    user_id = ""
    text = ""
