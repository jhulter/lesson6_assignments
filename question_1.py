# Task 1

reviews = [ "This product is really good. I'm impressed with its quality.",
                   "The performance of this product is excellent. Highly recommended!",
                   "I had a bad experience with this product. It didn't meet my expectations.",
                   "Poor quality product. Wouldn't recommend it to anyone.",
                   "The product was average. Nothing extraordinary about it." ]

keywords = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]


for review in reviews:
    highlightedReview = review
    for keyword in keywords:
        highlightedReview = highlightedReview.replace(keyword, keyword.upper())
    print(highlightedReview)
# Task 2

positive_words_search = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words_search = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def word_tally(review):
    global positive_words_search
    global negative_words_search
    positive = sum(review.lower().count(word) for word in positive_words_search)
    negative = sum(review.lower().count(word) for word in negative_words_search)

    return positive, negative

for review in reviews:
    positive, negative = word_tally(review)
    print(f"Review: {review}")
    print(f"Positive words: {positive}")
    print(f"Negative words: {negative}")

print(word_tally(review))

# Task 3

def review_summary(review):
    summary = review[:30]
    if len(review) > 30:
        last_space_index = summary.rfind(' ')
        if last_space_index != -1:
            summary = summary[:last_space_index]
        summary += "…"
    return summary

for review in reviews:
    summary = review_summary(review)
    print(f"Review: {review}")
    print(f"Summary: {summary}")
