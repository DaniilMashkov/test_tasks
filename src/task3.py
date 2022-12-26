from .task3_class.operation import CollectInstances
import json


def get_operations() -> None:
    with open('data/operations.json', 'r') as file:
        operations = CollectInstances(json.load(file))
        operations.sort_data()
        [print(x) for x in operations.lst[:5]]

