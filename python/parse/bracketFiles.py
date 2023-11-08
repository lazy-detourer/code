def parse(str):
  count = 0 # 괄호 갯수 카운트
  item = '' # 현재파싱중인 항목
  list = [] # 전체 결과
  ignore = False # 가장 바깥쪽 괄호를 무시하기 위한 변수
  

  for char in str: # 문자열 전체 순회

    if count == 0 and char == ' ': # 괄호가 없고 공백일 때 자르기
      list.append(item)
      item = '' # 다음 파싱을 위해 초기화
      ignore = False
      continue

    if char == '{': # 괄호 깊이 증가
      count = count + 1
      if item == '' and count == 1: # 누적중인 내용이 없는데 괄호부터 등장한 경우 체크
        ignore = True # 괄호 닫기도 무시하도록 기억
        continue # 괄호 열기 무시되도록 continue

    if char == '}': # 괄호 깊이 감소
      count = count - 1
      if ignore and count == 0: # 무시하게 되어 있는지 확인
        continue
    
    item = item + char # 파일명 누적

  list.append(item) # 공백없이 가장 마지막 항목 처리

  print()
  print('input:', str)
  print('result:', list)

parse('{E:/test_3/{3 3 3}.png}')
parse('{E:/test 1}')
parse('E:/test_1/3.png E:/test_1/1.png E:/test_1/2.png')
parse('E:/test_2/.1.png {E:/test_2/2 2.png} {E:/test_2/3 3 3.png}')
parse('E:/test_3/{1}.png {E:/test_3/{3 3 3}.png} {E:/test_3/2{ }2.png}')

# https://www.clien.net/service/board/cm_app/18409654