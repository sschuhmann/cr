from typing import List, Callable
from .models import *

def filter_multimedia(demand: Demand, available_cars):
    pass

def filter_luggage(demand: Demand, available_cars):
    pass

def rank_distance(demand: Demand, available_cars, score_factor=1):
    pass


def find_match(demand: Demand, available_cars:  List[Car], rankers: List[Callable] = [], filters: List[Callable] = []):
    if not rankers:
        rankers = [rank_distance]

    if not filters:
        filters = [filter_multimedia, filter_luggage]

    for filter in filters:
        available_cars = filter(demand, available_cars)

    results = []

    for i in rankers:
        rank = i(demand, available_cars)
        results = rank

    return available_cars[results.index(max(results))]