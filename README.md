## :one: AutoWriteREADME란?
[백준](https://www.acmicpc.net/), [프로그래머스](https://programmers.co.kr/), [SWEA](https://swexpertacademy.com/main/main.do)를 통해 공부한 알고리즘 개인 풀이를 쉽게 저장하고 관리해주는 [백준허브](https://github.com/BaekjoonHub/BaekjoonHub)를 사용 하다가, 레포지토리의 README에 풀이한 플랫폼과 레벨, 문제 번호를 자동으로 정리해주는 프로그램이 있으면 좋을 것 같아 만들게 되었습니다.

<br/>

## :two: 정리 사진
![](https://github.com/SSangRRae/AutoWriteREADME/blob/main/assets/readme_image/%EC%98%88%EC%8B%9C.png)

<br/>

## :three: 사용법

1. 원하는 위치에 AutoWriteREADME 레포지토리 **clone** 하기  
`git clone https://github.com/SSangRRae/AutoWriteREADME.git`

2. 원하는 위치에 자신의 문제 풀이 레포지토리 **clone** 하기  
`git clone https://github.com/{백준허브로 업로드되는 레포지토리.git}`

3. 필요한 패키지 라이브러리 설치 ([gitpython](https://gitpython.readthedocs.io/en/stable/))  
`pip install gitpython`

4. clone 한 AutoWriteREADME 정보 변경 **(github.py 파일)**
    - 자신의 github username, repository 이름 변경 (userName, repository)  
    ![](https://github.com/SSangRRae/AutoWriteREADME/blob/main/assets/readme_image/%EC%A0%95%EB%B3%B4_%EB%B3%80%EA%B2%BD_1.png)

    - clone 한 문제 풀이 레포지토리 경로(:star: 절대경로) 변경 (localDir)  
    ![](https://github.com/SSangRRae/AutoWriteREADME/blob/main/assets/readme_image/%EC%A0%95%EB%B3%B4_%EB%B3%80%EA%B2%BD_2.png)

5. main.py 실행  
`python3 main.py`

<br/>

## :four: 동작원리
1. 자신의 문제 풀이 레포지토리를 pull 합니다.
2. 백준허브로 업로드 된 문제의 플랫폼, 레벨, 문제 번호를 파싱합니다.
3. README.md 파일에 파싱된 정보들을 작성합니다.
4. 작성이 완료된 README.md 파일을 add, commit, push 합니다. 

<br/>

## :five: 느낀점
- 스스로 필요하다고 느껴서 만들어 본 프로그램인데, 개발에 대한 재미를 다시 한번 느끼게 되었다.😊 
- 이후에는 다른 사람들이 더욱 편하게 사용할 수 있도록 변경할 수 있는 부분을 고민 후 차근차근 고쳐볼까 한다.