import pandas as pd
import my_text_rank as m
import sys
import numpy as np
print(sys.argv[0])

# stop_word = [line.strip() for line in open('../stopwords/mystopword.txt', 'r', encoding='utf-8')]
# stopwords = stop_word + [line.strip() for line in open('../stopwords/stopwordsKor.txt', 'r', encoding='utf-8')]
stopwords = [line.strip() for line in open('../stopwords/stopwordsKor.txt', 'r', encoding='utf-8')]
mecab_path = "/Users/george/Desktop/dev_n/pakage_/mecab-0.996-ko-0.9.2/mecab-ko-dic-2.1.1-20180720"
corpus = pd.read_csv('/Users/george/testData/food_saf.csv')

doc_1 = '''
영국의 작가 코난 도일이 쓴 추리 소설 셜록 홈즈 시리즈의 주인공. 현재까지 인간이 창조한 캐릭터 중에서 가장 성공한 인물 중 하나이다.
[3] 양산 끝에 '그저 그런 기믹'에 불과하게 된 드라큘라와는 달리, 다양하게 재창조되었으나 원작자가 만든 고유의 인격과 독특한 매력을 
유지하는 불사조 같은 캐릭터. 특히 친구인 존 왓슨과의 콤비는 그야말로 역사에 길이 남을 명콤비라 할 수 있다.
탐정 캐릭터의 대명사이자 탐정 캐릭터들을 한 단계 진화시킨 캐릭터라고 평가받는다. 과거의 탐정들이 단순히 사건 푸는 기계에 불과했다면, 
홈즈는 그런 탐정 캐릭터들에게 인간다운 개성을 부여하는 시발점이 되었다.
셜록 홈즈 이전에 손꼽을만한 탐정 캐릭터라면 최초의 탐정이라고 할 수 있는 에드거 앨런 포의 오귀스트 뒤팽과 에밀 가보리오가 창조한 최초의 장편 추리소설 
주인공 타바레와 르코크인데 뒤팽은 고전 추리물의 전범을 겨우 단편 3개로 완성한 엄청난 캐릭터지만 단편 3개에만 등장하는 캐릭터라서 캐릭터 
자체의 묘사나 매력은 희미하다. 르코크 시리즈는 탐정의 무대를 장편으로 확대하고 본격적인 캐릭터성을 부여했지만 여전히 르코크와 그 스승 타바레를 
제외하면 개성이 부족했고, 르코크는 그 개성이 끈덕진 형사지 탁월한 탐정이 아니라서 카타르시스가 부족했다.
다른 작가들은 말 할 필요도 없다. 도일 이전의 추리물 작가인 윌키 콜린스의 한 단편을 보면, 사건을 해결하는 인물이 마지막에 등장해서 
그 전에 다른 인물이 한 활동을 보고 단서를 알아낸 뒤 사건을 해결하는 게 전부다. 성격 묘사도 그저 무뚝뚝하고 '사건만 해결하면 그만'이라는 듯한
 태도를 보이며 정확하게 추리하지 못하는 인물에 대한 경멸을 나타내는 것이 전부. 이에 비하면 홈즈는 성격이 훨씬 사람답다. 
 그런데 지금은 이러한 홈즈가 사람 같지 않다고 비판받기도 하는 것이 아이러니한 점.
작가인 코난 도일은 셜록 홈즈라는 인물이 실제로 존재했다는 느낌을 주기 위해 여러 가지의 장치를 해놓았다. 가령 작품 속에서 홈즈의 친구 왓슨은 
홈즈가 해결한 사건들을 글로 정리해 세상에 발표하는 작업을 한다. 이를 통해 독자들은 왓슨이 작중에서 발표한 글을 실제로 읽고 있다는 
느낌을 받게 되고, 마치 셜록 홈즈라는 인물이 실제로 존재했었다는 인상을 가지게 된다. 작중 배경이나 명칭은 거의 실존하는 것이거나, 실존하는 인명이나 지명을 고의로 바꾼 느낌(정확히는 사실)이다.[4] 잠시 등장하는 것에 불과한 수많은 인물들의 성격이나 직업도 사실감 있게 묘사한다. 셜록 홈즈 시리즈를 직접 읽어보면 알겠지만, 인물이나 배경, 날씨 묘사의 분량이 상당히 많고 구체적이다.
당연하게도 당시에 셜록 홈즈 시리즈를 꾸준하게 연재했던 스트랜드 매거진에 사건 해결을 의뢰하는 사람들의 편지가 수두룩하게 왔었다고 한다. 
그 인기는 아직도 엄청나서 2008년의 조사에 따르면 영국인의 약 58%가 셜록 홈즈는 실존 인물이라고 믿었다고 하며, 셜록 홈즈 시리즈는 
정식으로 출판된 지 130년이 넘어가는 지금까지 단 한 번도 절판된 적이 없다.셜록 홈즈와 그와 관련된 창작물을 연구하고 숭배하는 이들을 셜로키언, 혹은 홈지언이라고 부른다. 전자는 미국, 후자는 영국의 팬들을 이르는 말. 
특히 미국에서 셜록 홈즈의 인기는 이미 당대에도 엄청나서, 1920년 기준으로 미국 출판업자들이 도일에게 단어 하나 당 1달러[5]씩 계산하는 
방식으로 판권 값을 지불했다고 한다.
'''
doc_2 = '''현대 추리물에 등장하는 탐정의 모델이 되었으며, 특히 일본 소설이나 만화의 탐정 형상에 지대한 영향을 미쳤다. 그러나 후대 탐정들과는 
궤도를 달리하는데, 극중 홈즈가 지향하는 수사 기법은 과학 수사와 합리적인 증거 수집 및 분석이다.[91] 작품을 통틀어 처음으로 홈즈가 등장하는 장면에서 그는 혈액을 검출할 수 있는 시약 실험에 성공해서 기뻐하는 모습으로 묘사된다. 보통 작가들이 캐릭터를 첫 등장시킬 때 해당 캐릭터의 테마를 부각시킨다는 점에서 볼 때, 홈즈의 과학 우선적인 면을 강조했다고 볼 수 있다.[92] 실제 작품을 읽어보면 홈즈의 사건 수사 방식은 온갖 자료나 증거들을[93] 조사해서 과학적 결론을 내리는 것이 많다는 것을 알 수 있다.
이와 더불어, 작중에서 홈즈는 "범인은 반드시 범행 후에 증거를 남긴다." 라는 사실을 은연 중에 누누이 강조한다. 지금이야 지극히 상식적인 말로 
들릴지 모르겠지만, 이 작품이 나온 건 1차 세계 대전이 터지기도 훨씬 전이다. 과학 수사라는 게 두 차례 세계 대전 이후 본격적으로 자리를 잡은 사실을 생각하면, 셜록 홈즈는 현대 범죄 수사 기법의 효시를 표현했다고 해도 과언이 아니다.
다만 원작을 보면 과학 수사를 하긴 하지만 그렇게 체계적이지는 않다. 일례로 발자국은 세밀하게 보지만 지문은 신경 쓴 적이 거의 없다. 
그러나 이도 변명의 여지가 있는 게, 지문이 수사 기법으로 활용된 것이 20세기(1901년, 런던 스코틀랜드 야드에 처음으로 지문감식반이 설치됨.)
부터라서 아무리 셜록 홈즈(라기보다는 작가인 코난 도일)라도 알려지지 않던 수사 기법을 쓰기는 어려웠을 것이다.
[94] 지문이 핵심 증거로 심도있게 다뤄지는 최초의 장편인 리처드 오스틴 프리먼의 붉은 엄지손가락 지문은 1907년 작이다.
오히려 "노우드의 건축업자"(1903년 작)에서 보듯이 홈즈는 당시까지는 생소한 지문에 관한 수사 기법을 대중들에게 일찍 소개한 편이므로
(원래 지문 수사 기법을 소개하는 사람은 담당 경찰이었던 레스트레이드 경감이고 홈즈는 그 지문이 살인 사건 수사 이후에 찍혔다는 것을 증거로 
범죄 자체가 조작임을 밝혀내는 역할이다.) 이 부분은 홈즈의 잘못이라 하기 어렵다.[95]
이러나저러나 홈즈가 소설에서 과학 수사를 강조한 것은 사실이고, 미국의 한 탐정은 "소설 속에서 셜록 홈즈가 쓰는 방법은 현실에서도 통한다.
"[96]라고 말할 정도로 신빙성이 있다.
'''
doc_short = '''현대 추리물에 등장하는 탐정의 모델이 되었으며, 특히 일본 소설이나 만화의 탐정 형상에 지대한 영향을 미쳤다. 
 극중 홈즈가 지향하는 수사 기법은 과학 수사와 합리적인 증거 수집 및 분석이다.'''
doc_eng = '''
is a fictional private detective created by British author Sir Arthur Conan Doyle. Referring to himself 
 a "consulting detective" in the stories, Holmes is known for his proficiency with observation, deduction,
  forensic science, and logical reasoning that borders on the fantastic, which he employs when 
  investigating cases for a wide variety of clients, including Scotland Yard.
First appearing in print in 1887's A Study in Scarlet, the character's popularity became widespread 
with the first series of short stories in The Strand Magazine, beginning with "A Scandal in Bohemia" 
in 1891; additional tales appeared from then until 1927, eventually totalling four novels and 56 short 
stories. All but one are set in the Victorian or Edwardian eras, between about 1880 and 1914. Most are 
narrated by the character of Holmes's friend and biographer Dr. John H. Watson, who usually accompanies 
Holmes during his investigations and often shares quarters with him at the address of 221B Baker Street, 
London, where many of the stories begin.
Though not the first fictional detective, Sherlock Holmes is arguably the best known.[1] By the 1990s 
there were already over 25,000 stage adaptations, films, television productions and publications 
featuring the detective,[2] and Guinness World Records lists him as the most portrayed literary 
human character in film and television history.[3] Holmes's popularity and fame are such that many have 
believed him to be not a fictional character but a real individual;[4][5] numerous literary and fan 
societies have been founded on this pretense. Avid readers of the Holmes stories helped create the 
modern practice of fandom.[6] The character and stories have had a profound and lasting effect 
on mystery writing and popular culture as a whole, with the original tales as well as thousands 
written by authors other than Conan Doyle being adapted into stage and radio plays, television, 
films, video games, and other media for over one hundred years.
'''
#데이터는 나무위키 셜록홈 자료즈
text = doc_1
text_2 = corpus['contents'][5]
text_ = pd.read_csv('~/testData/seoul_city_complaints_2019_2021.csv')
text_seoul = ''.join(text_['ask'])
print(f'type {type(text_seoul)} {len(text_seoul)}')
#print(text_2)
stm = m.SimpleTextRank(STOPWORD=stopwords, MECABPATH=mecab_path)
#result_1 =stm.process(text)
result_2 =stm.network_process(text_seoul)
print("="*20)
#print(f'scores : {result_1}')
print(f'network scores: {result_2}')

# a =stm._word_tokenize(text)
# n,t =stm.build_keywords(a)
# print(f'count node: {len(n)} nodes 후보 : {n}')
# print(f'count tokens :{len(t)}전체 token : {t}')

'''
# myt = m.Mytextrank(stopword=stopwords, mecab_path=mecab_path)
# result = myt.build_keywords(text)
# myt.make_graph(*result)
'''

