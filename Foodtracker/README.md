# 내가 먹은 음식의 칼로리(Calories) 기록 및 계산하기
> Flask, Html, Sqlite

## foodtracker 파일 구조
* foodtracker
  * main
    * routes.py
  * templates
    * add.html
    * index.html
    * view.html
  * static
    * img
    * bs
  * __init.py
  * models.py
<br/>

***

### 기본 페이지 및 목록 페이지 - 'index.html' -
URL : '/'

<img src="https://user-images.githubusercontent.com/103489352/219947622-35e7081f-b022-4d9f-9b42-80ccc6c849a1.png" width="70%" height="50%" alt="메인 페이지"></img><br/>

### 음식 추가 페이지 (지방, 탄수화물, 단백질) - 'add.html' -
URL : '/add'

<img src="https://user-images.githubusercontent.com/103489352/219947646-68309cce-bbc0-4efc-af98-fa2940e5048a.png" width="70%" height="50%" alt="추가 페이지"></img><br/>

### 달력 세부사항 페이지 (지방, 탄수화물, 단백질, 칼로리) - 'view.html' -
URL : '/view/<int:food_id>'

<img src="https://user-images.githubusercontent.com/103489352/219947725-9bd62e3d-c8f5-46ee-aa7a-440f53301a9b.png" width="70%" height="50%" alt="달력 세부사항 페이지"></img><br/>
