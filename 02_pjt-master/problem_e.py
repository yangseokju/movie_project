import requests
from pprint import pprint

def credits(title):
    pass 
    # 여기에 코드를 작성합니다.
    try:
        movie_dict = {'cast':[],'crew':[]}

        URL = f'https://api.themoviedb.org/3/search/movie?api_key=9198ea87f7de9b2dba9436007a2e502b&language=ko-KR&query={title}&page=1&include_adult=false&region=KR'
        response = requests.get(URL).json()
        results = response.get('results')
        movie_id = results[0]['id']

        URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=9198ea87f7de9b2dba9436007a2e502b&language=ko-KR'
        response = requests.get(URL).json()
        cast = response.get('cast')
        crew = response.get('crew')

        for i in range(len(cast)):
            if cast[i]['cast_id'] < 10:
                movie_dict['cast'].append((cast[i]['name']))

        for j in range(len(crew)):
            if crew[j]['department'] == 'Directing':
                movie_dict['crew'].append((crew[j]['name']))
           
        return movie_dict

    except:
        return None




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
