#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Arbitrary Arguements"""


from pet import Pet


class Dog(Pet):
    """The Sub Class for Pets."""

    def __init__(self, has_shots=False, **kwargs):
        """The constuctor for the Dog subclass.

        Args:
            has_shots(bool): Indicates if dog has shots, defaults to False.
            kwargs (mixed): Dictionary arguments from Pet() class.

        Attributes:
            has_shots(bool): Indicates if dog has shots, defaults to False.
            ge: (int): Age of the pet in years.Defaults to None.
            birthyear (int): Year the pet was born. Defaults to None.
            weight (int): Weight of the pet in kg. Defaults to None.
            length (int): Length of the pet in cm. Defaults to None.
            color (str): Color of the pet. Defaults to None.
            owner (str, optional): Name of the pet's owner, defaults to None.
        """
        self.has_shots = has_shots
        self.birthyear = kwargs.get('birthyear', None)
        self.weight = kwargs.get('weight', None)
        self.length = kwargs.get('length', None)
        self.color = kwargs.get('color', None)
        self.owner = kwargs.get('owner', None)
