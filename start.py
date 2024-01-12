
succ_count = 0;fail_count = 0
typing_list = ['무궁화', '꽃이', '피었습니다.', 'The']
for list_item in typing_list:
    print(list_item)
    typing_input = input(">>:")
    if list_item == typing_input:
        succ_count +=1
    else:
        fail_count +=1
    print('타이핑 연습 종료! 정답: ',succ_count,' 오류: ',fail_count)