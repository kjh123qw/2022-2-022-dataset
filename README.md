# 목차

1. 소개
2. 데이터
3. AI 모델 정보

---

# 1. 소개

1.1 과제 명

- `22년 인공지능 학습용 데이터 구축 사업`

1.2 개요

1.2.1 데이터 명

- `인터페이스(자판/음성)별 고빈도 오류 교정 데이터`

1.3 주관사

- (주)유핏

1.4 참여사

- 메가스터디교육(주)
- (주)세명소프트
- (사)한국에듀테크산업협회
- (주)솔트룩스이노베이션

---

# 2. 데이터

2.1 데이터 버전

- `1.0 (23.12.22)`

2.2 데이터 다운로드

- AIHUB : <데이터 개방 전>

2.3 데이터 개요

2.3.1 데이터 설명

- 한글 입력 인터페이스(일반 키보드, 스마트폰 쿼티, 음성 입력 시스템)에서 특징적으로 나타나는 오탈자 및 띄어쓰기 등 오류를 탐지하고 적절한 맞춤법으로의 자동 전환을 학습하기 위한 데이터

2.3.2 데이터 활용 분야

- 맞춤법 교정 및 음성 인식 오류 교정 분유, 입력장치 보조기구(S/W) 등의 분야에서 활용

2.3.3 데이터 수량

| 구분 | 소계 | 비율 |
|:---:|---:|---:|
| 오탈자 | 110,000 | 55% |
| 맞춤법 오류 | 60,000 | 30% |
| 음성 인식기 오류 | 30,000 | 15% |

2.3.4 데이터 구성 파일 구조

<table>
<thead>
  <tr>
    <th colspan="2">데이터 폴더 구조</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="2"> 띄어쓰기문장부호오류</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-</td>
    <td>띄어쓰기문장부호오류.json</td>
  </tr>
  <tr>
    <td colspan="2">맞춤법오류</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-</td>
    <td>맞춤법오류_SNS.json</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-</td>
    <td>맞춤법오류_자유게시판.json</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-</td>
    <td>맞춤법오류_질문게시판.json</td>
  </tr>
  <tr>
    <td colspan="2">오탈자</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-</td>
    <td>오탈자오류.json</td>
  </tr>
  <tr>
    <td colspan="2">음성인식기오류</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-</td>
    <td>음성인식기오류.json</td>
  </tr>
  <tr>
    <td colspan="2">자동생성오류</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-</td>
    <td>자동생성오류.json</td>
  </tr>
  <tr>
    <td colspan="2">자주틀리는맞춤법오류</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;-</td>
    <td>자주틀리는맞춤법오류.json</td>
  </tr>
</tbody>
</table>

2.3.5 데이터 구성 정보

<table>
<thead>
  <tr>
    <th><span style="font-weight:bold">번호</span></th>
    <th><span style="font-weight:bold">항목명</span></th>
    <th><span style="font-weight:bold">타입</span></th>
    <th><span style="font-weight:bold">필수</span></th>
    <th><span style="font-weight:bold">설명</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>info</td>
    <td>object</td>
    <td>Y</td>
    <td>데이터셋 정보</td>
  </tr>
  <tr>
    <td>1-1</td>
    <td>-.description</td>
    <td>string</td>
    <td>Y</td>
    <td>데이터셋 명</td>
  </tr>
  <tr>
    <td>1-2</td>
    <td>-.data_name</td>
    <td>string</td>
    <td>Y</td>
    <td>데이터셋 한글명</td>
  </tr>
  <tr>
    <td>1-3</td>
    <td>-.data_description</td>
    <td>string</td>
    <td>Y</td>
    <td>데이터셋 상세설명</td>
  </tr>
  <tr>
    <td>1-4</td>
    <td>-.creator</td>
    <td>string</td>
    <td>Y</td>
    <td>데이터셋 생산자</td>
  </tr>
  <tr>
    <td>1-5</td>
    <td>-.distributor</td>
    <td>string</td>
    <td>Y</td>
    <td>데이터셋 제공자</td>
  </tr>
  <tr>
    <td>1-6</td>
    <td>-.version</td>
    <td>string</td>
    <td>Y</td>
    <td>데이터셋 버전</td>
  </tr>
  <tr>
    <td>2</td>
    <td>data</td>
    <td>array</td>
    <td>Y</td>
    <td>데이터 목록</td>
  </tr>
  <tr>
    <td>2-1</td>
    <td>-.metadata_info</td>
    <td>object</td>
    <td>Y</td>
    <td>데이터 메타 정보</td>
  </tr>
  <tr>
    <td>2-1-1</td>
    <td>-.-.id</td>
    <td>string</td>
    <td>Y</td>
    <td>데이터 고유 식별자</td>
  </tr>
  <tr>
    <td>2-1-2</td>
    <td>-.-.source</td>
    <td>string</td>
    <td></td>
    <td>데이터 출처</td>
  </tr>
  <tr>
    <td>2-1-3</td>
    <td>-.-.date</td>
    <td>int</td>
    <td></td>
    <td>게시글 작성일</td>
  </tr>
  <tr>
    <td>2-1-4</td>
    <td>-.-.gender</td>
    <td>string</td>
    <td></td>
    <td>게시글 작성자 성별</td>
  </tr>
  <tr>
    <td>2-1-5</td>
    <td>-.-.age</td>
    <td>int</td>
    <td></td>
    <td>게시글 작성자 나이</td>
  </tr>
  <tr>
    <td>2-1-6</td>
    <td>-.-.interface</td>
    <td>string</td>
    <td></td>
    <td>작성자 인터페이스</td>
  </tr>
  <tr>
    <td>2-1-7</td>
    <td>-.-.keyboard</td>
    <td>string</td>
    <td></td>
    <td>작성자 키보드</td>
  </tr>
  <tr>
    <td>2-2</td>
    <td>-.annotation</td>
    <td>object</td>
    <td>Y</td>
    <td>라벨링 정보</td>
  </tr>
  <tr>
    <td>2-2-1</td>
    <td>-.-.err_sentence</td>
    <td>string</td>
    <td>Y</td>
    <td>오류 문장</td>
  </tr>
  <tr>
    <td>2-2-2</td>
    <td>-.-.err_sentence_spell</td>
    <td>string</td>
    <td>Y</td>
    <td>오류 문장 음소</td>
  </tr>
  <tr>
    <td>2-2-3</td>
    <td>-.-.cor_sentence</td>
    <td>string</td>
    <td>Y</td>
    <td>교정 문장</td>
  </tr>
  <tr>
    <td>2-2-4</td>
    <td>-.-.cor_sentence_spell</td>
    <td>string</td>
    <td>Y</td>
    <td>교정 문장 음소</td>
  </tr>
  <tr>
    <td>2-2-5</td>
    <td>-.-.reg_date</td>
    <td>int</td>
    <td></td>
    <td>수집일</td>
  </tr>
  <tr>
    <td>2-2-6</td>
    <td>-.-.errors</td>
    <td>array</td>
    <td>Y</td>
    <td>요류 정보</td>
  </tr>
  <tr>
    <td>2-2-6-1</td>
    <td>-.-.-.err_idx</td>
    <td>int</td>
    <td>Y</td>
    <td>오류 식별자</td>
  </tr>
  <tr>
    <td>2-2-6-2</td>
    <td>-.-.-.err_location</td>
    <td>int</td>
    <td>Y</td>
    <td>오류 위치</td>
  </tr>
  <tr>
    <td>2-2-6-3</td>
    <td>-.-.-.err_text</td>
    <td>string</td>
    <td>Y</td>
    <td>오류 어휘</td>
  </tr>
  <tr>
    <td>2-2-6-4</td>
    <td>-.-.-.cor_text</td>
    <td>string</td>
    <td>Y</td>
    <td>교정 어휘</td>
  </tr>
  <tr>
    <td rowspan="2">2-2-6-5</td>
    <td rowspan="2">-.-.-.err_details</td>
    <td>object</td>
    <td rowspan="2">Y</td>
    <td>오탈자, 음성 인식기 오류 : object 타입의 오류 유형 정보</td>
  </tr>
  <tr>
    <td>array</td>
    <td>그 외의 오류 : array 타입의 오류 유형 정보</td>
  </tr>
  <tr>
    <td>2-2-6-5-1</td>
    <td>-.-.-.-.choseong</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 초성</td>
  </tr>
  <tr>
    <td>2-2-6-5-1-1</td>
    <td>-.-.-.-.-.insert</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 입력 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-1-2</td>
    <td>-.-.-.-.-.delete</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 삭제 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-1-2</td>
    <td>-.-.-.-.-.replace</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 대체 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-2</td>
    <td>-.-.-.-.joongseong</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 중성</td>
  </tr>
  <tr>
    <td>2-2-6-5-2-1</td>
    <td>-.-.-.-.-.insert</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 입력 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-2-2</td>
    <td>-.-.-.-.-.delete</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 삭제 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-2-3</td>
    <td>-.-.-.-.-.replace</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 대체 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-3</td>
    <td>-.-.-.-.jongseong</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 종성</td>
  </tr>
  <tr>
    <td>2-2-6-5-3-1</td>
    <td>-.-.-.-.-.insert</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 입력 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-3-2</td>
    <td>-.-.-.-.-.delete</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 삭제 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-3-3</td>
    <td>-.-.-.-.-.replace</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 대체 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-4</td>
    <td>-.-.-.-.spacing</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 공백</td>
  </tr>
  <tr>
    <td>2-2-6-5-4-1</td>
    <td>-.-.-.-.-.insert</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 입력 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-4-2</td>
    <td>-.-.-.-.-.delete</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 삭제 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-4-3</td>
    <td>-.-.-.-.-.replace</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 대체 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-5</td>
    <td>-.-.-.-.mark</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 문장부호</td>
  </tr>
  <tr>
    <td>2-2-6-5-5-1</td>
    <td>-.-.-.-.mark</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 문장부호</td>
  </tr>
  <tr>
    <td>2-2-6-5-5-2</td>
    <td>-.-.-.-.mark</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 문장부호</td>
  </tr>
  <tr>
    <td>2-2-6-5-5-3</td>
    <td>-.-.-.-.mark</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 문장부호</td>
  </tr>
  <tr>
    <td>2-2-6-5-6</td>
    <td>-.-.-.-.number</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 숫자</td>
  </tr>
  <tr>
    <td>2-2-6-5-6-1</td>
    <td>-.-.-.-.-.insert</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 입력 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-6-2</td>
    <td>-.-.-.-.-.delete</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 삭제 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-6-3</td>
    <td>-.-.-.-.-.replace</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 대체 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-7</td>
    <td>-.-.-.-.alphabet</td>
    <td>object</td>
    <td></td>
    <td>편집거리 알고리즘 정보 - 영문자</td>
  </tr>
  <tr>
    <td>2-2-6-5-7-1</td>
    <td>-.-.-.-.-.insert</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 입력 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-7-2</td>
    <td>-.-.-.-.-.delete</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 삭제 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-5-7-3</td>
    <td>-.-.-.-.-.replace</td>
    <td>int</td>
    <td></td>
    <td>편집거리 알고리즘 대체 횟수</td>
  </tr>
  <tr>
    <td>2-2-6-6</td>
    <td>-.-.-.edit_distance</td>
    <td>int</td>
    <td>Y</td>
    <td>오류 어휘, 교정 어휘 편집거리</td>
  </tr>
</tbody>
</table>

2.3.6 데이터 구성 예시

<table>
<thead>
  <tr>
    <th><span style="font-weight:bold">구분</span></th>
    <th colspan="4"><span style="font-weight:bold">예시</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="20">오탈자</td>
    <td>인터페이스</td>
    <td colspan="3">pc</td>
  </tr>
  <tr>
    <td>키보드</td>
    <td colspan="3">쿼티</td>
  </tr>
  <tr>
    <td>작성자 나이</td>
    <td colspan="3">16</td>
  </tr>
  <tr>
    <td>오류 문장</td>
    <td colspan="3">굳가 몇켤레인지 개수를 세어보렴, 어렵지않을거야~</td>
  </tr>
  <tr>
    <td>교정 문장</td>
    <td colspan="3">구두가 몇 켤레인지 개수를 세어보렴. 어렵지 않을 거야!</td>
  </tr>
  <tr>
    <td>오류 위치</td>
    <td colspan="3">0</td>
  </tr>
  <tr>
    <td>오류 어휘</td>
    <td colspan="3">굳가</td>
  </tr>
  <tr>
    <td>교정 어휘</td>
    <td colspan="3">구두가</td>
  </tr>
  <tr>
    <td rowspan="10">오류 유형</td>
    <td rowspan="3">초성</td>
    <td>insert</td>
    <td>1</td>
  </tr>
  <tr>
    <td>delete</td>
    <td>0</td>
  </tr>
  <tr>
    <td>replace</td>
    <td>0</td>
  </tr>
  <tr>
    <td rowspan="3">중성</td>
    <td>insert</td>
    <td>0</td>
  </tr>
  <tr>
    <td>delete</td>
    <td>0</td>
  </tr>
  <tr>
    <td>replace</td>
    <td>0</td>
  </tr>
  <tr>
    <td rowspan="3">종성</td>
    <td>insert</td>
    <td>0</td>
  </tr>
  <tr>
    <td>delete</td>
    <td>0</td>
  </tr>
  <tr>
    <td>replace</td>
    <td>1</td>
  </tr>
  <tr>
    <td>…</td>
    <td>…</td>
    <td>…</td>
  </tr>
  <tr>
    <td>편집 거리</td>
    <td colspan="3">2</td>
  </tr>
  <tr>
    <td>…</td>
    <td colspan="3">…</td>
  </tr>
  <tr>
    <td rowspan="11">맞춤법 오류</td>
    <td>데이터 출처</td>
    <td colspan="3">질문게시판</td>
  </tr>
  <tr>
    <td>작성자 성별</td>
    <td colspan="3">M</td>
  </tr>
  <tr>
    <td>작성자 나이</td>
    <td colspan="3">18</td>
  </tr>
  <tr>
    <td>오류 문장</td>
    <td colspan="3">고냥 날짜 맞춰서 기출만하면될까요?</td>
  </tr>
  <tr>
    <td>교정 문장</td>
    <td colspan="3">그냥 날짜 맞춰서 기출만 하면 될까요?</td>
  </tr>
  <tr>
    <td>오류 위치</td>
    <td colspan="3">0</td>
  </tr>
  <tr>
    <td>오류 어휘</td>
    <td colspan="3">고냥</td>
  </tr>
  <tr>
    <td>교정 어휘</td>
    <td colspan="3">그냥</td>
  </tr>
  <tr>
    <td>오류 유형</td>
    <td colspan="3">유사 모양</td>
  </tr>
  <tr>
    <td>편집 거리</td>
    <td colspan="3">1</td>
  </tr>
  <tr>
    <td>…</td>
    <td colspan="3">…</td>
  </tr>
  <tr>
    <td rowspan="18">음성 인식기 오류</td>
    <td>입력 엔진</td>
    <td colspan="3">STT_ENGINE_01</td>
  </tr>
  <tr>
    <td>오류 문장</td>
    <td colspan="3">컴찰 인사 논란니 또마 위에 오를 것으로 보니다.</td>
  </tr>
  <tr>
    <td>교정 문장</td>
    <td colspan="3">검찰 인사 논란이 도마 위에 오를 것으로 보입니다.</td>
  </tr>
  <tr>
    <td>오류 위치</td>
    <td colspan="3">0</td>
  </tr>
  <tr>
    <td>오류 어휘</td>
    <td colspan="3">컴찰</td>
  </tr>
  <tr>
    <td>교정 어휘</td>
    <td colspan="3">검찰</td>
  </tr>
  <tr>
    <td rowspan="10">오류 유형</td>
    <td rowspan="3">초성</td>
    <td>insert</td>
    <td>0</td>
  </tr>
  <tr>
    <td>delete</td>
    <td>0</td>
  </tr>
  <tr>
    <td>replace</td>
    <td>1</td>
  </tr>
  <tr>
    <td rowspan="3">중성</td>
    <td>insert</td>
    <td>0</td>
  </tr>
  <tr>
    <td>delete</td>
    <td>0</td>
  </tr>
  <tr>
    <td>replace</td>
    <td>0</td>
  </tr>
  <tr>
    <td rowspan="3">종성</td>
    <td>insert</td>
    <td>0</td>
  </tr>
  <tr>
    <td>delete</td>
    <td>0</td>
  </tr>
  <tr>
    <td>replace</td>
    <td>0</td>
  </tr>
  <tr>
    <td>…</td>
    <td>…</td>
    <td>…</td>
  </tr>
  <tr>
    <td>편집 거리</td>
    <td colspan="3">1</td>
  </tr>
  <tr>
    <td>…</td>
    <td colspan="3">…</td>
  </tr>
</tbody>
</table>

---

# 3. AI 모델 정보

3.1 AI 모델 임무

- `한글 오류 교정 임무(Korean Error Correction Task)`

3.2 AI 모델

- [BART (gogamza/kobart-base-v2)](https://huggingface.co/gogamza/kobart-base-v2)

3.3 AI 모델 라이센스

- `modified MIT` 자세한 내용은 LICENSE 파일 확인