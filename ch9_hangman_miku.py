'''
미쿠와 승부! 아이돌 이름 맞추기 게임. MSPGOTHIC 폰트 (특히 size 14)에서 UTF-8아트가 깨지지 않고 나올 것
'''

import random

MIKUPICS = ['''

　　　　　　　　　　　　　　　 _＿＿__　　　　　　----､___
　　　　　　　　　　　　　 　 |｀＼　　 ｀＼／: : : : : : : : : : :｀丶
　　　　　　　　　　　　　 　 |　 | ＼　 ／: : :／⌒＾: : : : : : : : :＼＿＿＿_ __
　　　　　　　　　　　　　 　 |　　　　〉: : : : : : : : : : : : : : : :⌒' : : ヽ　　 ／｀｀〉
　　　　　　　　　　　　　　　　　＼/: : : /: : : : : : : : : : : : : : : :,: : : :〈／' 　 /
　　　　　　　　　 　 　 　 　 ∨　/ : : :/: : /: : : : : : :.∧|: : : : :, : : : :∨　 /
　　　　　　　　　　　　　　 　 |∨; : : : : : /: : : : : : : /　:|: : : : :| : : : i: V /
　　　　　　　　　　 　 　 　 　 -‐‐=ミ| :/＼:./: : : :/　　|八: : :| : : : i: :|/
　　　　　　　　 　 　 　 ／　　　 ＼　}/∨|/〈_:_／ 　 - ─＼｣ : : : i: :|
　　　　　　　　　　　　/　　　　＼　}/ ﾏﾆ=ミ　 　 　 ｧ芋ｋ.　 | : : : i: :|
　　　　　　　　　　　 ,ﾞ　　　＼　_イ_／　　　 　 　 　 rJxj　}} | : : : i: :|　　　　낙승이다냐!
　　 　 　 　 　 　 　 ;　　_＞‐r1 : |八 : : :　　　　　　 Vン　ﾉｲ : | : i: :|
　　　　　　　　　　　{　 ´　　 | | : :|∧＼　　　 　 ′　: : : .厶i: : | : i: :|
　　　　　 　 　 　 　 l　　　　 { ﾚi :|. : ゝ 　　ｰ　､__, 　 　 /: :.j: : | : i: :|:
　 　 　 　 　 　 　 　 l　 　 　 V l八: :V介　　　　　　 . イ: :|八: :| : i: :|
　　　　　　　　　　　 ∧　　　　ﾏﾍ「＼｢∧　＞ｰ=≦{二＞＜_∨￢i:人
　　　　　　　　　　　 | ﾊ.　　　　∨|＼ 　 ｝　　　 　 _／　/　　 ｀ヽ 　 ∧
　　　　　　　　　　　 | /l__　　 　 | |　 丶ｰ-　 　 -/ {　 /　/　/　ハ　/∧
　　　　　　　　　　　　 │ ＼ 　 ﾘ |　 　 ＼_ 　 ／＼ ｰ{__〈__/__/　 ∨ /∧
　　　　　　　　　　　││　　＼ﾉ　 　 　 　 しく　　 /⌒'┘ーﾍ　　　∨/ ハ
　　　　　　　　　　　││　　//　 ∧　 　 〈. 　 　 /∧＿___∧∧.　　 〈＼　}
　　　　　　　　　　　∧人　　/ 　　 ∧　　　　 　 /（　　　　　 ,）∧　　∧ ∨''','''


　　　　　　　　　　　　　　　　| ]＼
　 　 　 　 　 　아 　 　 　 　 | ]　 ＼　　 　 　 　 　 　 　 ／[|
　　　　 　 　 　직 　　　 　 　 | ]　　　＞-─ : : ─-　__／　 [|
　 　 　 　 　 　한 　 　 　 　 | ］　／ 　 . . . . . . . . ＼ .＼ 　[|
　　　　 　 　 　번 　　　　　　7／ ／. . : : : : :l : : : : .丶　＼[|
　 　 　 　 　 　실 　　　　　 /..:.／:.:.:.:.:.:./.:.:.八.:.:.:.:.:.:.:.: |: : :.ヽ
　　　　 　 　 　수 　　　　　.: :.:.:./.:.:＼.:/.: :/　 ＼.:.: |: : |:.:.:.: : .
　　　　　　　 　했 　 　 　 .: :.:.:/|／|／|/|/ 　 ノ＾＼|＼| .:.:!.:. :
　　　　 　 　 　을 　　　　 |/|:.:|／|￣|＼　　 ／|￣|＼│.: !.:. :
　　　　　　　　 뿐 　 ,rヘ、　|.:.|＼|＿|／　　 ＼|＿|／│.:.ｊ.:.:.:
.　　　　 　 　 　이　 辷／＼|: ｊ 〃〃　_人___, 〃〃　イ .:/.:.:/
　　　　　　　　 다.　　 ＼ 　 |:｛　　　　 V __ノ　　　　　ｊ.:./.:.:/
　　　　　　　 　냐！　　　＼ﾉi个o｡.　　　　 　 　 　 イり/ｊ／　　 /７
　 　 　 　 　 　 　 　 　 　 　＼ 　 　￣了‰*‰*7/　｀ヽ、　　 / /
　　　　　　　　 　 　 　 　 　 　 ＼__/ 　}＼*‰∠〈　、 　 ＼　/ /
　　　　　　　　　　　　　　　　　 　 ｛　　}......｀¨´........＼＼　　 ＼/
　　　　　　　　　　　　　　　　　 　 ｛ 　,√]＞-＜ﾆﾆﾆ＼＼　　 ＼
　　　　　 　　　　 　 　 　 　 　 　 └イ....../¨丁¨..........＼..`ｰ个fう＾
　　　　　　 　 　 　 　 　 　 　 　 ／../...../.......ｊ.....................＼....｝｝''','''


　　　　　　　　　　　　　　　　　　　　　　 　 __________
　　　　　　　　　　　　　　　　　　 　 　 ´: : : : : : : : : ｀丶、
　　　　　　　　　　　　 　 r―-　､／ : : : : : : : : : : : : : : :＞ｰ──┐
　　　　　　　　　　　　 　 |´＼　　＞ : : : : : : : : : : : : : : :＼　／　｀|
　　　　　　　　　　　　 　 | 　 ::〉: : : :／ : : : : : : : : : : ＼ : : 〈::. 　 /
　　　　　　　　　　　　 　 ∨::/: : : :/: : / : : : : : : : : : : :ハ: : :∨::/
　　　　 　 　 　 　 　 　 　 ∨ : : :/: : : : : : : : : : :|　: : :＼|: : : :∨
　 　 　 　 　 　 　 　 　 　 /: :| : ,: : : ::| : : : : : : ∧: : : : : |: : : : :,
　　　　　　　　 　 　 　 　 ,: : :|: :l＼: : |: :/: :| : /　∨＼／: : : : :!
　　　　　 　 　 　 　 　 　 |/: :|: :|:/|≧トミ_/|_/　､_ｘ≦ﾊ:|: : : :|│　　　아... 아직이다냐!
　　　　　　　　　 　 　 　 /: : :l : :〃 しﾊ　 　 　 ´しﾊ ∨|: : : :|│
　　　　　　　　　　　　　 ; : :|: lハ{{.　Vソ　　　　　Vソ　}}ﾚ宀宀|＿＿＿r冖冖､
　　　　　　　　　　 　 　 | : :|: : :∧　:.::::　　　,　 　 ::::.:　儿_____丿 　 　 ｢Ｌ.. ノ＾|
　　　　　　　　　　 　 　 | : '|: : :lｰﾍ　　　　　　 　 　 　 |　　 　 |　　 　 |　　 　 |
　　　　　　　　　　 　 　 |/ :|: : : : : : ..　　ﾏ　　　^) 　 ｲ|＿　＿|＿　＿|＿　＿|｀ヽ
　　　　　　　　　　　　　　 八::. : :∨:个ト 　 __　　イ: / |　　 　 |　　 　 | 　 　 │ ∧
　　　　　　　　 　 　 　 　 　 ∨＼{＼レ〉　　　　 〈／|/|　　 　 |　　 　 |　　 　 |　 　〉
　　　　　　　　　　　　　＿＿____,,..r＜　　　　　　 　 ＞|＿　＿|＿　＿|＿　＿|/　/
　　　　　　　　　　　／ . . . . . . . .人　 丶　　　　 rく　｀|　　 　 |　　 　 |　　 　 |／ﾍ
　　　　　　 　 　 　 . . . . . . . . . . . . .＼　　　　　 _／{_ﾉ|　　 　 |　　 　 |　　 　 |. . . |
　　　　　　　　　 / . . .|: . . . . . . . . . . . ￣￣し´. . . .｀'┴──xー―‐┴― ─|. . . |
　　 　 　 　 　 _/. . . 八 . ./. . . . . . . . . . . . . ヽ. . . . _＿／|／{{　　　 　 　 　 ∧. ..ﾉ
.　　　　　　 ／ . . . . . . .∨. . . . . . . . . . . . .. . . .＼く　　 ／. . . ＼　　　____,／. .／''','''


　　　　　　　　　　‐━━─　　　　　　　　　　　　　　 　 -‐‐─＜⌒＼ｰ-
.　　　 　 　 ／　 ´￣￣￣ ＼＼　　　　　　　　　　／ : ／⌒ : : ＾＼: : ＼ : :＼
　　　　　／／　: : : : : : : : :-=ﾍ∧　　　　　 　 　 . : : :/: : : : : : : : : : : : : : ヽ : : ヽ
.　　 　 /::/: : : : : : : : : : : : : :-=ﾔ::,　　　　　　　/ : : : : : : : : : : |: : : : : : : : : : : : : :,
　　　 /::/: : : : : :／⌒ヽｰ-　: : :|:::ﾄ 　　　　　 /: : : : : : : / : : 八 |＼.:│: : : : | : : i
　 　 √': : : : : :/　　　　　　　￣|:::|　 　 　 　 ; : : : : : |: /|: : /_, 斗≪:│: : : i | : : |
　　　|:::|=-: : : :|　　 　 ,　 　 . : ﾘ :;　　 ＼　 │: : :| :/|≫トく　　 Jiｈ Y| : : : ｉ | : : |
　　　|:::l=-: : : : ､_＿／ . : : : : /::/:　　 　 ＼ | : :i人|〃Jｈ　　　 Ｖソﾉ'| : : : ｉ | : : |　아직... 아직 한 번 기회가...
　　　ﾔ:ﾏ=-: : :　 ｀丶､ : : : : .: .: : : .　　　 　 丶_:ｉ :ハヽVｿ,　　　　 :::　| : : : ｉ | : : |    답은 이거다냐...!
.　　　ﾔ::ﾏ=ｰ　　　　　 ＼／／.: : : .　　　　　　　「トﾐ} :::　__　 -ｖ､ 　 厶|: : :ｉ | : : |
　　　　＼＼＿＿＿＿／／ : : : : : : . 　 　 　 　 |l|ﾆ]]　　∨　　　}　　 │ : |/ : ｉ |
.　　　　　 　 ー━━一　￣￣( 二)‐-､)＿: : : . //ﾆ)ゝ　　　　　ノ 　 ｲ/ : :/ : /|/
　　　　　　　　　　　　　　　　/ ,ﾆつ ／ ）　 ＞＜ﾆイ: : :|＞　.._　 イ　/ : :/|／
　　　　　　　　　　　 　 　 　 {/,二つトく |　　　　 V八|: ::|∨＼∧　 ∠: イ>orｰｧー…=ミ
　　　　　　　　　　　　　　　　{/ﾆつ ［,　ﾘ　　　　　　　＼|:_＞oノ}　　　 　 8リ'/　　　　　 ＼
　　　　 　 　 　 　 　 　 　 　 ﾏ|│　[　/　　　　　　 ／￣　|/8　　　　　 //／　　　　/
　　　　　　 　 　 　 　 　 　 ／||│　l ∧ 　 　 　 ／ 　 　 八 |　　　 　 /／
　　　　　　　　　　　　　　 〈_(二(＿ﾉ ﾚ1　　 　 / 　 　 　 　 `8ﾆ二ﾆ8く　 xﾆﾆx 　　|
　　　 　 　 　 　 　 　 　 　 ∨∧__,／ ∧　　／　　＼∨　　　 (･ω･)　　｛｛ ※｝｝＼|''','''



　　　 　 　 i＼　　　　　　　　　　　　　　　　　미쿠는 자신을
　　　 　 　 {　 ＼　　　　　　　　　　　굽히지 않ㅇㅏ...
　　　　　　 ∨　 乂_　　　　　　　　　　 　 　 　 　 　 ri
　 　 　 　 　 〉／⌒ヾ>　　　　　 　 　 　 　 　 　 　 , |.!ミ､
　　　　　　 〃　　 ,.:-─::-..､　 　 　 　 　 　 　 　 '/〈 　 ﾉ
　　　　　　.{.{　 .rｲ´￣ミ､＼ ＼　　　　　　　　 　 '//|　.|
　　r≦´￣从 /j:::}::::::::::::::Vハ::::ヽ　　　　　　　　 .'//|　 !
　　 ＼　　　>':/::/::i:::::::;::::::}:::::}::::::}　.､　　　　　_＿ '/L.._|
　　　　≧f´／::/:::/:::::::{::::/::::::!:::::乂ノ}　　　 <Y从}/,}､... ¨７
　　　　　 从x'/:::/:::::;i::::Y⌒ヾx／⌒７广￣¨７￣￣　　 　{
　　　　　　ヾ廴斗zｲ:|:::::}　　 fﾟ 　 　 i' 　 　 ,'　　　 _.｡s≦´
　　　　　　　　ｰ=彡ム斗　./j}　　　 {　　 .,厶斗: ´|
　　 　 　 　 　 　 　 '//｛／.从 　 　 ∨ ハ＿ｆ⌒ヽＬ,　　　　　,r=ミ:､
　　 　 　 　 　 　 　 '//[_／　　　　　 ∨　}　 ｀ヾ､　/ 　 　.／:::::::::::::::.
　　　　　　　　　　　 '//!　　､　　 　 　 ヽ/＿二=彡　　.／:::ﾚ⌒≧x､i
　　　　　　　　　　 　 '/∧　　＼　　　 　乂 　　　 　 ／::::::: {　　　　_,レ＜⌒:.
　　 　 　 　 　 　 　 　 '/∧　　　｀≧=-　:._ ヽ. 　 ／:::::::::::::::} , ::＜´:::::::/::::::::: i
　　　　　　　 　 　 　 　 '//＼　　　　　　　　＼ｖ':::::::::::;＞:::´:::::::::::::::::::;:::::::::::::: |
　　　　　　　　 　 　 　 　 '//∧　　　　,　　　　 ,＞:'了::::::::::::::::::::::::::::::{/⌒≧:､|
　　　 　 　 　 　 　 　 　 　 '//∧　　 /　　　　/　./´:::::::::::::::::::::::::::;＞.{　　　　 |
　　　　　　　　　　　　　　 　 '//∧　/　　　　/　/ :::::::::::::::::::::::; i ´　.从　 　 　 |
　　　　　　　　　　　　　　　　　 '//X＿＿. イ　/::::::::::::::::::::／/ }　　.| ∧　　　 .|
　　　　　　　　　　　　　　 　 　 　 '{ ＼　　　／ :::::::::::::::;イ //r┴i　 {　'∧　　　|
　　　　　　　　　　　　　　　　　　 ∧／ヽ.／}:::::::::::::::::〃///厶ミvﾍ__V}　,i　　　|
　　　　　　　　　　　　　　　　　　ム,}　_｡s≦｀≧=-彳'/////＼＼ﾟｰ=癶､.}　 　 |
　　　　　　　　　　　　　　　　　　　 ￣　　　　'/////// '　.'///＼＼ 　　} ! . 　 |
　　　　　　　　　　　　　　　　　　　　　　　　　　'　 　' 　 　 　 '///,ﾟ ｰ=彳 | 　　.|ﾉ}
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 　 '//////{⌒ﾐ彡べ
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　'///{ミx｡､　　 ｀≧s｡
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　'//｀≧s｡三三z彡’ ''']

idols = '''Nana Abe
Karin Domyoji
Rina Fujimoto
Anzu Futaba
Shiki Ichinose
Kyoko Igarashi
Sae Kobayakawa
Miho Kohinata
Sachiko Koshimizu
Miku Maekawa
Kanako Mimura
Frederica Miyamoto
Yukari Mizumoto
Yuka Nakano
Chieri Ogata
Mayu Sakuma
Momoka Sakurai
Noriko Shiina
Uzuki Shimamura
Yukino Aihara
Erika Akanishi
Miyako Anzai
Kanna Ariura
Fuka Asano
Clarice
Tsubaki Egami
Yao Fueifuei
Mai Fukuyama
Miyo Harada
Mirei Hayasaka
Rena Hyodo
Akiha Ikebukuro
Kana Imai
Setsuna Imura
Koharu Koga
Shinobu Kudo
Nene Kurihara
Wakaba Kusakabe
Misato Manaka
Saya Matsubara
Arisa Mochida
Azuki Momoi
Atsumi Munakata
Sakura Muramatsu
Hasumi Nagatomi
Hitomi Niwa
Michiru Ohara
Yuriko Ohnishi
Yuu Ohta
Kurumi Ohnuma
Saori Okuyama
Yuuki Otokura
Haena Ryoo
Kotoka Saionji
Satomi Sakakibara
Hiromi Seki
Hotaru Shiragiku
Seika Suzumiya
Miyabi Tsukimiya
Kiyora Yanagi
Miyuki Yanase
Chika Yokoyama
Kozue Yusa
Anastasia
Kanade Hayami
Karen Hojo
Haruna Kamijo
Nao Kamiya
Ranko Kanzaki
Mizuki Kawashima
Ryo Matsunaga
Miyu Mifune
Nono Morikubo
Asuka Ninomiya
Minami Nitta
Fumika Sagisawa
Chie Sasaki
Rin Shibuya
Syuko Shiomi
Koume Shirasaka
Arisu Tachibana
Riina Tada
Kaede Takagaki
Chinatsu Aikawa
Hina Araki
Nanami Asari
Honoka Ayase
Tomo Fujii
Hajime Fujiwara
Yoriko Furusawa
Toko Hattori
Helen
Shino Hiiragi
Megumi Ijuin
Juney
Kate
Manami Kiba
Aya Kirino
Tsukasa Kiryu
Ayaka Kishibe
Chinami Komuro
Chiaki Kurokawa
Layla
Sarina Matsumoto
Chizuru Matsuo
Midori Mizuno
Seira Mizuki
Hijiri Mochizuki
Yume Narumiya
Honami Nishikawa
Izumi Ohishi
Yasuha Okazaki
Yukimi Sajo
Shiori Sena
Rei Shinohara
Kako Takafuji
Reiko Takahashi
Noa Takamine
Ai Togo
Mutsumi Ujiie
Otoha Umeki
Rumi Wakui
Makino Yagami
Yumi Aiba
Miria Akagi
Ayame Hamaguchi
Yuki Himekawa
Akane Hino
Mio Honda
Yuko Hori
Syoko Hoshi
Nina Ichihara
Mika Jougasaki
Rika Jougasaki
Sanae Katagiri
Natsuki Kimura
Kirari Moroboshi
Takumi Mukai
Emi Namba
Yui Ohtsuki
Shizuku Oikawa
Kaoru Ryuzaki
Shin Sato
Nagisa Aino
Mary Cochran
Naho Ebihara
Misaki Etou
Cathy Graham
Ayuna Hamakawa
Yujin Im
Hinako Kita
Mahiro Kitagawa
Yuzu Kitami
Ibuki Komatsu
Reina Koseki
Shiho Makihara
Itsuki Manabe
Kumiko Matsuyama
Risa Matoba
Sana Miyoshi
Tomoe Murakami
Meiko Namiki
Hikaru Nanjo
Natalia
Kai Nishijima
Sora Nonomura
Kiyomi Saejima
Yoko Saito
Eve Santaclaus
Marina Sawada
Ema Senzaki
Aoi Shuto
Natsumi Soma
Umi Sugisaka
Ako Tsuchiya
Tomoka Wakabayashi
Miu Yaguchi
Tokiko Zaizen'''.lower().split('\n')

def getRandomIdol(idolList):
    #여기에서 위의 아이돌 리스트로부터 랜덤한 문자열을 가져옵니다
    idolIndex = random.randint(0, len(idolList) - 1)
    return idolList[idolIndex]

def displayBoard(MIKUPICS, missedLetters, correctLetters, secretName):
    print(MIKUPICS[len(missedLetters)])
    print()

    print('틀린 글자들:', end='  ')
    for letter in missedLetters:
        print(letter, end='  ')
    print()

    blanks = '_' * len(secretName)

    for i in range(len(secretName)): #빈칸을 맞게 추측한 글자로 채워줌

        if secretName[i] in correctLetters:
            blanks = blanks[:i] + secretName[i] + blanks[i+1:]

    for letter in blanks: #show the secret word with spaces in between each letter
            print(letter, end='  ')
    print()

def getGuess(alreadyGuessed):
    #이미 넣은 글자와 한글자가 아닌 글자를 추린다
    while True:
        print('이름을 맞춰보라냐.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('한 글자씩 맞춰보자냐.')
        elif guess in alreadyGuessed:
            print('이미 생각해본 글자다냐. 다른 걸 고르자냐.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('알파벳 글자로 맞춰야한다냐.')
        else:
            return guess

def playAgain():
    print('한 판 더 승부해보자냐! (yes 혹은 no)')
    return input().lower().startswith('y')

print('아스터리스크와 함께하는 아이돌 맞추기 놀이')
missedLetters = ''
correctLetters = ' '
secretName = getRandomIdol(idols)
gameIsDone = False

while True:
    displayBoard(MIKUPICS, missedLetters, correctLetters, secretName)

    #플레이어가 글자를 넣게 하자
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretName:
        correctLetters = correctLetters + guess

        #승리조건 체크
        foundAllLetters = True
        for i in range(len(secretName)):
            if secretName[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('맞았다냐! 아이돌 이름은 "' + secretName + '"였다냐! 우리가 이겼다냐!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #몫이 다 나가서 죽었는지

        if len(missedLetters) == len(MIKUPICS) - 1:
            displayBoard(MIKUPICS,  missedLetters, correctLetters, secretName)
            print(str(len(missedLetters))+'번이나 틀리다니 너무 많이 틀렸다냐...\n정답은"' + secretName + '"였다냐...')
            gameIsDone = True

    #한판 더?
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ' '
            gameIsDone = False
            secretName = getRandomIdol(idols)
        else:
            break
