from utils import read_file, get_fastest_search_alg, determine_overal_champion

# Prepared different test data
first_article = read_file("first_article.txt")
first_article_existing_word = "firstIndex"
first_article_missing_word = "happy"

second_article = read_file("second_article.txt")
second_article_existing_word = "recommendation"
second_article_missing_word = "unhappy"

# First article existing word search tests
first_article_existing_word_champion = get_fastest_search_alg(
    "first article existing word", first_article, first_article_existing_word
)

# First article missing word search tests
first_article_existing_word_champion = get_fastest_search_alg(
    "first article missing word", first_article, first_article_missing_word
)

# Second article existing word search tests
second_article_existing_word_champion = get_fastest_search_alg(
    "second article existing word", second_article, second_article_existing_word
)

# Second article missing word search tests
second_article_existing_word_champion = get_fastest_search_alg(
    "second article missing word", second_article, second_article_missing_word
)

overal_test_champion = determine_overal_champion(
    [
        first_article_existing_word_champion,
        second_article_existing_word_champion,
        second_article_existing_word_champion,
        second_article_existing_word_champion,
    ]
)

print("Conclusion: ")
print(f"The fastest sorting algorithm based on all tests is: {overal_test_champion}")
