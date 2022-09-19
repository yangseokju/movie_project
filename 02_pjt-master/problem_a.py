import requests
import json

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=9198ea87f7de9b2dba9436007a2e502b&language=ko-KR&page=1&region=KR'

    params = {
    'name': 'michael',
    'country_id': 'KR',
    }
    
    response = requests.get(URL, params=params).json()

    results = len(response.get('results'))
    return results

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
