def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)

    genre_total_play_dict = {}
    genre_index_play_dict = {}

    # 1. genre 별 총 play 횟수 뽑기
    # 3. genre 내 곡 별 play 횟수 뽑기
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_dict[genre].append([i, play])

    # 2. 총 횟수가 높은 장르부터 앞에 오게 정렬
    sorted_genre_total_play_dict = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)

    result = []

    for genre, total_play in sorted_genre_total_play_dict:
        sorted_genre_index_play_array = sorted(genre_index_play_dict[genre], key=lambda item: item[1], reverse=True)

        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count == 2:
                break

            result.append(index)
            genre_song_count += 1

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))