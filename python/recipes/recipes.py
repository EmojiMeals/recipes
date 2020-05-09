from copy import deepcopy
import json
import pkg_resources

_recipes = json.loads(pkg_resources.resource_string('recipes', 'resources/recipes.json'))

def recipes():
    return deepcopy(_recipes)
