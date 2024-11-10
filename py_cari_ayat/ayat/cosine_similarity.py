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

    query_ayat_sets = set(queries_normalized)
    merged_sets = set(queries_normalized)
    merged_words: str = ''
    merged_words_index_start: str = ''
    is_verse_merged: bool = False
    for idx, kata in enumerate(similar_ayat_katas):
        if is_verse_merged == False and (kata.surat_id == similar_ayat_katas[idx -1].surat_id) and (kata.ayat == similar_ayat_katas[idx -1].ayat) and ((int(kata.index)-1) == int(similar_ayat_katas[idx -1].index)):
            merged_words_index_start = str(similar_ayat_katas[idx -1].index)
            merged_words = similar_ayat_katas[idx -1].kata
            is_verse_merged = True
        else:
            merged_sets = set(queries_normalized)
            merged_words: str = ''
            merged_words_index_start: str = ''
            is_verse_merged = False

        query_ayat_sets.update(set(kata.normalized))
        similarity_kata: float = calculate_cosine_similarity(list(query_ayat_sets), queries_normalized, kata.normalized)
        if similarity_kata > 45:
            kata.similarity = similarity_kata
            results.append(kata)

        if is_verse_merged:
            merged_sets.update(set(kata.normalized))
            merged_words = f'{merged_words} {kata.kata}'
            kata_merged_words: Kata = Kata(merged_words, f'{merged_words_index_start}-{kata.index}', kata.surat, kata.surat_id, kata.ayat)
            similarity_merged: float = calculate_cosine_similarity(list(merged_sets), queries_normalized, kata_merged_words.normalized)
            if similarity_merged > 45:
                kata_merged_words.similarity = similarity_merged
                results.append(kata_merged_words)

    return results

# calculating cosine similarity formula in sections
# query_similar being the x and ayat_similar the y
def calculate_cosine_similarity(query_ayat_sets: list[str], query: str, ayat: str) -> float:
    query_similar: list[int] = [
        sum(1 for query_char in query if query_char == merged_char) 
        for merged_char in query_ayat_sets
    ]
    ayat_similar: list[int] = [
        sum(1 for ayat_char in ayat if ayat_char == merged_char) 
        for merged_char in query_ayat_sets
    ]

    bottom_left_formula: float = math.sqrt(sum(val**2 for val in query_similar))
    bottom_right_formula: float = math.sqrt(sum(val**2 for val in ayat_similar))
    bottom_formula: float = bottom_left_formula * bottom_right_formula

    if bottom_formula == 0:
        return 0.00
    top_formula: float = sum(q * a for q, a in zip(query_similar, ayat_similar))

    return round((top_formula / bottom_formula) * 100, 2)