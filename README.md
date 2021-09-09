# brew

This is my brewing software.

Each recipe is a python program that subclasses the brew.Recipe class and instantiates instance variables defining ingredients, mash schedule and other parameters.

Usage: Recipe.py [-i] [-r]

- Without flags, the design and calculations are shown, as well as the brew log.
- With the -i flag, a Recipe_instructions.html file is created.
- With the -r flag, a Recipe_recipe.html file is created.