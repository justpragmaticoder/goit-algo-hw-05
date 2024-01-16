import os
import codecs
import timeit
from algorithms.boyer_moore_search import boyer_moore_search
from algorithms.kmp_search import kmp_search
from algorithms.rabin_karp_search import rabin_karp_search

EXECUTION_QTY = 100


def read_file(file_name: str):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_fastest_search_alg(
    test_name: str, text: str, target: str, executionQty=EXECUTION_QTY
):
    results = {
        "Boyer Moore Search": timeit.timeit(
            lambda: boyer_moore_search(text, target), number=executionQty
        ),
        "Knuth Morris Pratt Search": timeit.timeit(
            lambda: kmp_search(text, target), number=executionQty
        ),
        "Rabin Karp Search": timeit.timeit(
            lambda: rabin_karp_search(text, target), number=executionQty
        ),
    }

    print(f"{test_name} search test: ".upper())

    for algorithm, execution_time in results.items():
        print(f"Algorithm: {algorithm}, Execution Time: {execution_time}")

    min_time_algorithm, min_time = min(results.items(), key=lambda x: x[1])

    print(
        f"Fastest sorting algorithm for {test_name} search is {min_time_algorithm} with result: {min_time}\n"
    )

    return min_time_algorithm, min_time


def determine_overal_champion(champions):
    champion_counts = {}
    for champion, _ in champions:
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return max(champion_counts, key=champion_counts.get)
