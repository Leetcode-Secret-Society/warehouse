from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_ratings = {}
        self.food_cruisine_map = {}
        self.cuisines_order = defaultdict(list)

        for i in range(len(foods)):
            self.food_ratings[foods[i]] = ratings[i] * -1
            self.food_cruisine_map[foods[i]] = cuisines[i]
            heappush(self.cuisines_order[cuisines[i]], (ratings[i] * -1, foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating * -1
        cuisine = self.food_cruisine_map[food]
        heappush(self.cuisines_order[cuisine], (newRating * -1, food))

    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food = self.cuisines_order[cuisine][0]
            if self.food_ratings[food] != rating:
                heappop(self.cuisines_order[cuisine])
            else:
                return food
