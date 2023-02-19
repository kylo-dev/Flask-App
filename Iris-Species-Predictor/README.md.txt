# flask를 이용하여 머신러닝 모델 웹 배포하기
> Iris 붓꽃 데이터 예측을 위해 분류 모델 
+ RandomForestClassifier 
+ KNeighborsClassifier 
+ SVC

```
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Instantiate the model
clf = RandomForestClassifier()
knn = KNeighborsClassifier()
svm = SVC()
```

***
## flask-iris web
<p>기본 페이지</p>
<img src="https://user-images.githubusercontent.com/103489352/219936481-332ac85f-c036-42e0-a70c-ed79d0e08840.png" width="500px" height="450px" title="기본 페이지" alt="기본 페이지"></img><br/>
<p>예측 페이지</p>
<img src="https://user-images.githubusercontent.com/103489352/219936601-23890813-20d3-4f34-8400-e123ae3717d1.png" width="500px" height="450px" title="예측 페이지" alt="예측 페이지"></img>
