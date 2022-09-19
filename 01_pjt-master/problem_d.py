import json

def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    num_max = 0

    for i in movies:
        movie_id = i['id']
        movie = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movies_list = json.load(movie)        
        num_d = movies_list['revenue'] # 영화들의 수익을 num에 저장
        if num_max < num_d:
            num_max = num_d
            max_movie = movies_list.get('title')
    return max_movie

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
