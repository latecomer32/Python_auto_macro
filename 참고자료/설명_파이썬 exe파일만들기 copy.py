#터미널에서 CMD 탭에 가서 'pip install pyinstaller' 를 입력하면 pyautogui 모듈을 설치한다.
#사용법1
# 계속해서 터미널 cmd 탭에서 'pyinstaller -w .\파일명.py' 후 엔터를 누르면
#만들기 시작한다. 몇분 걸린다
#dist 폴더 들어가면 여러 파일 중에 파일명.응용프로그램 파일이 있다
#이 방법의 특징은 dist폴더 채로 써야하므로 용량이 크다.
#하지만 응용프로그램 실행속도는 빠르다.

#사용법2
#사용법1 대로 하면 dist내 파일이 여러개 생기므로
#'pyinstaller -w-F .\파일명.py'후 엔터 치면하면
#dist 폴더에 들어가면 파일 하나로만 완성된다.(파일 실행시 시간이 좀 오래걸린다.)
#이방법은 dist폴더 내 응용프로그램만 존재하나 내부적으로 여러 파일을 압축해놓은 상태로
#실행을 위한 전체 용량은 작지만 실행할때마다 내부적으로 압축 해제 후 실행되므로
#프로그램 실행속도가 느리다