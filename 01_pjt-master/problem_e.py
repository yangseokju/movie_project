import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    de_movie = []
    for i in movies:
        movie_id = i['id']
        movie = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movies_list = json.load(movie)          
        if movies_list['release_date'][5:7] == '12':
            de_movie.append(movies_list['title'])
    return de_movie

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
