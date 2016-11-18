'''두가지 선택지와 각각의 선택지에 따른 두가지 엔딩, 도합 4개의 멀티엔딩으로 구성된 인터랙티브 노벨'''

import random, time

def displayIntro():
    print('   프로듀서는 열중하던 서류 작업에서 잠시 눈을 떼고 뻐근해진 손목을 주물렀다. 그의 눈에')
    print('들어온 손목시계는 오후 한시를 막 지나가고 있었다.')
    print('  \'두 시부터 후타바 씨의 스케쥴이 시작되는구나. 슬슬 행사장까지 이동을 해야 할텐데... ')
    print('후타바 씨는 구내식당을 이용하고 온다고 했었지. 마중을 나갈까?\'')
    print('프로듀서는 자리에서 몸을 일으키다 말고 잠시 생각에 잠겼다.')
    print('  \'아니지, 지난 번 데코레이션 때처럼 자칫 서로 엇갈렸다가 곤란해질지도 모른다.\'')
    print('약간 난처한 기분이 된 프로듀서는 버릇대로 손바닥을 뒷목에 붙이며 가볍게 입술을 깨물었다.')

def chooseAct():
    act = ''
    while act != '1' and act != '2':
        print('[자리에서 기다리려면 1, 안즈를 맞으러 가려면 2를 입력하세요]')
        act = input()

    return act

def checkAct(chosenAct):
    if chosenAct is '1':
        print('프로듀서는 자리에서 잠시 기다리기로 했다.')
        time.sleep(2)
        print('눈을 감고 건조해진 눈을 잠시 쉬게 하며 기다리면')
        time.sleep(2)
        print('조만간 저 문을 두드리는 소리가 들리며')
        time.sleep(2)
        print('후타바 씨의 불만스런 목소리가 이렇게 들려올 것이다.')
        time.sleep(2)
        print('\'뭐야, 기껏 출근했더니 이동하자고 부르지 않네? 이대로 안즈 퇴근해버린다구..?\'')
        time.sleep(2)
        print('...')
        time.sleep(2)
        print('...')
        time.sleep(2)

        goodEnding = random.randint(1,2)
        if chosenAct == str(goodEnding):
            print('\"저기, 프로듀서. 설마 자는거야?\"')
            print('\"아, 아닙니다, 후타바 씨. 이동하시죠.\"')
            print('...눈을 감고 상상해본 후타바씨의 목소리가 아무래도 상상이 아니었던 것 같다.')
            print('서둘러 수트케이스와 자동차 열쇠를 챙겨 후타바씨와 함게 사무실을 나섰다.')
        else:
            print('무섭게 울리는 핸드폰 진동에 눈을 떠보니 시간은 오후 두 시 오 분을 지나고 있었다.')
            print('아찔함에 시야가 다시 검게 변해갔지만, 정신을 붙들고 전화를 받았다.')
            print('\"정말로 죄송합니다, 사고가 있었습니다. 바로 대응해 나가도록 하겠습니다. 예, 예! 알겠습니다. 죄송합니다.\"')
            print('내일 다시 출근할 수 있을까...')

    if chosenAct is '2':
        print('프로듀서는 안즈를 맞으러 가기로 했다.')
        time.sleep(2)
        print('집무실을 나서자 후타바 씨의 휴대폰이 프로젝트 룸 테이블에 뒹굴고 있는 것이 보인다.')
        time.sleep(2)
        print('식당에는 게임기만 들고 내려간 모양이다.')
        time.sleep(2)
        print('오늘 구내식당의 점심은 이전에 후타바 씨가 호평을 했던 메뉴였던 것이 기억난다.')
        time.sleep(2)
        print('\'으으... 프로듀서, 한 숫갈, 한 숫갈만 더 먹고 갈게에-\'')
        time.sleep(2)
        print('-라고, 투정하듯 말해보는 후타바 씨의 얼굴이 그려졌다.')
        time.sleep(2)
        print('...')
        time.sleep(2)
        print('...')
        time.sleep(2)

        goodEnding = random.randint(1,2)
        if chosenAct == str(goodEnding):
            print('\"으으, 프로듀서, 한 숫갈, 한 숫갈만 더 먹고 갈게에-\"')
            print('\"입에 넣으시고 이동하면서 드시도록 하세요.\"')
            print('\"에에, 이제부터 일할텐데 차분히 식사정도는 하게 해 달라구-\"')
            print('\"끝나고 나면 디저트라도 같이 드시지요. 그리고 여기 후타바 씨 짐입니다.\"')
            print('투덜대는 후타바 씨를 재촉하며, 행사장으로의 경로를 스마트폰에 입력했다. 여유가 있다면')
            print('근처에서 입가심 할만한 간식도 살 수 있겠지. ')
        else:
            print('구내식당에서 후타바 씨는 물론, 그를 만난 사람 조차 없다고 한다. 혹시나 싶어 메이드 카페의 아베 씨에게')
            print('물어봐도 고개를 가로저을 뿐이었다. 혹시나 싶어 다시 사무실에 들어왔지만 후타바 씨의 스마트폰과 짐은 그대로였다.')
            print('\"죄송합니다. 사고가 있어 정시에 도착하지 못할 것 같습니다. 아닙니다. 예. 아주 조금만 늦춰주십시오. 죄송합니다. 부탁드립니다.\"')
            print('주최측에 조율을 부탁드리는 전화를 해 두며 회사를 돌아다녔지만 어디에서도 후타바 씨의 흔적은 보이지 않았다.')
            print('\'이를 어쩐다...\'')

playAgain = 'yes'
while playAgain =='yes':

    displayIntro()

    chosenAct = chooseAct()

    checkAct(chosenAct)

    print('다시 한번 플레이하시겠습니까? (yes 혹은 no)')
    playAgain = input()
print('플레이해주셔서 감사합니다!')