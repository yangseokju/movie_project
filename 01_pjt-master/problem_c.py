import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  

    new_list = []                
    for i in movies: # 영화들 .. ... ...
        a = []
        new_data_2 = i.get('genre_ids') # 영화 각각의
        for j in range(len(genres_list)):
            for k in new_data_2:
                if genres_list[j]['id'] == k:
                    a.append(genres_list[j]['name'])

        new_data = {
            'genre_names' : a[::-1],
            'id': i.get('id'),
            'overview': i.get('overview'),
            'poster_path': i.get('poster_path'),
            'title': i.get('title'),
            'vote_average': i.get('vote_average')
    }
        new_list.append(new_data)
    return new_list
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data\movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data\genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
