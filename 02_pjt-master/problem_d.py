import requests
from pprint import pprint

def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.
    id_list = []
    title_list = []
    try:
        URL = f'https://api.themoviedb.org/3/search/movie?api_key=9198ea87f7de9b2dba9436007a2e502b&language=ko-KR&query={title}&page=1&include_adult=false&region=KR'
        response = requests.get(URL).json()
        results = response.get('results')
        movie_id = results[0]['id']
        
        URL = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=9198ea87f7de9b2dba9436007a2e502b&language=ko-KR&page=1'
        response = requests.get(URL).json()
        results1 = response.get('results')
        for i in range(len(results1)):
            title_list.append(results1[i]['title'])
        return title_list
    except:
        return None
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
