from fastapi import APIRouter

from logic.algorithm import search_number
from logic.randoms import random_number
from logic.validate.validation import validate

game = APIRouter()

result_search = {
    "random_number": ''.join(random_number()),
    "attempt": 0,
    "used_numbers": []
}


@game.post("/game")
def play_game(number: str):
    if not validate(number):
        return "Mistake enter, try again"
    elif number == result_search["random_number"]:
        final_attepmt = result_search["attempt"]
        result_search.update({"random_number": ''.join(random_number()), "attempt": 0, "used_numbers": []})
        return f"{number} You win, {final_attepmt} attempts"
    result_search["attempt"] += 1
    result_search["used_numbers"] += [search_number(number, result_search["random_number"])]
    return result_search["used_numbers"]
