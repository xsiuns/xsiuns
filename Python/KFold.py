"""
Copyright (c) 2025 [Your Name or GitHub Username]
This script is licensed under the MIT License.
See the LICENSE file for more details.
"""


from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
import numpy as np


iris = load_iris() ##꽃잎정보
features = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=156)
skfold = StratifiedKFold(n_splits=3)

# print(features.shape[0], type(features)) #150개 데이터

# 5개의 폴드 세트로 분리하는 KFold 객체와 폴드 세트별 정확도를 담을 리스트 객체 생성
kfold = KFold(n_splits=5) # 150개 데이터를 5개로 나눔, 학습용 4/5, 검증용 1/5
cv_accuracy = []
print('붓꽃 데이트 세트 크기:', features.shape[0]) #150개 데이터

n_iter = 0
# KFold 객체의 split()를 호출하면 폴드 별 학습용, 검증용 테스트의 로우 인덱스를 array로 반환
for train_index, test_index in skfold.split(features, label):
    # KFold.split()으로 반환된 인덱스를 이용해 학습용, 검증용 테스트 데이터 추출
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    
    # 학습 및 예측
    dt_clf.fit(X_train, y_train)
    pred = dt_clf.predict(X_test)
    n_iter += 1
    
    # 반복 시마다 정확도 측정
    accuracy = np.round(accuracy_score(y_test, pred), 4)
    train_size = X_train.shape[0]
    test_size = X_test.shape[0]
    print('\n#{0} 교차 검증 정확도: {1}, 학습 데이터 크기: {2}, 검증 데이터 크기: {3}'
          .format(n_iter, accuracy, train_size, test_size))

    cv_accuracy.append(accuracy) #평균구하기용
    
# 개별 iteration별 정확도를 합하여 평균 정확도 계산
print('\n## 교차 검증별 정확도:', np.round(cv_accuracy, 4))
print('\n## 평균 검증 정확도:', np.mean(cv_accuracy))