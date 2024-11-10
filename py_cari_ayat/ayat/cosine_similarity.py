import math
from typing import Any

from py_cari_ayat.models.ayat import Ayat
from py_cari_ayat.models.kata import Kata

def get_similar(queries: str) -> list[Any]:
    kata_queries: list[Kata] = [Kata(query) for query in queries.split(' ')]
    queries_normalized: str = ''.join(kata.normalized for kata in kata_queries)
    ayats: list[Ayat] = Ayat.query.all()
    similar_ayat_katas: list[Kata] = []
    results: list[Kata] = []
    for ayat in ayats:
        similar_ayat_katas.extend([
            kata_ayat
            for kata_ayat in ayat.katas
            for kata_query in kata_queries
            if kata_ayat.phonetic_code == kata_query.phonetic_code
        ])

    for idx, kata in enumerate(similar_ayat_katas):
        query_ayat_merged = set(queries_normalized)
        query_ayat_merged.update(set(kata.normalized))
        similarity_kata: float = calculate_cosine_similarity(list(query_ayat_merged), queries_normalized, kata.normalized)
        if similarity_kata > 45:
            kata.similarity = similarity_kata
            results.append(kata)

    return results

# calculating cosine similarity formula in sections
# query_similar being the x and ayat_similar the y
def calculate_cosine_similarity(query_ayat_merged: list[str], query: str, ayat: str) -> float:
    query_similar: list[int] = [
        sum(1 for query_char in query if query_char == merged_char) 
        for merged_char in query_ayat_merged
    ]
    ayat_similar: list[int] = [
        sum(1 for ayat_char in ayat if ayat_char == merged_char) 
        for merged_char in query_ayat_merged
    ]
    print(query, ayat, query_ayat_merged)

    bottom_left_formula: float = math.sqrt(sum(val**2 for val in query_similar))
    bottom_right_formula: float = math.sqrt(sum(val**2 for val in ayat_similar))
    bottom_formula: float = bottom_left_formula * bottom_right_formula

    if bottom_formula == 0:
        return 0.00
    top_formula: float = sum(q * a for q, a in zip(query_similar, ayat_similar))

    return round((top_formula / bottom_formula) * 100, 2)