import json
from pprint import pprint

def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.
    a = []
    new_data_2 = movie.get('genre_ids') # [18,80]
    for i in range(len(genres_list)):
        for j in new_data_2:
            if genres_list[i]['id'] == j:
                a.append(genres_list[i]['name'])

    new_data = {
        'genre_names' : a[::-1],
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'poster_path': movie.get('poster_path'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')
    }
    return new_data

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data\movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data\genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
