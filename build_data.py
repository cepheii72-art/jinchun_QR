import json

data = [
    {
        "id": 1,
        "badge": "Exhibition Section 01",
        "title_en": "The Life of Yi Ha-gon",
        "title_ko": "이하곤 스토리텔링",
        "type": "story",
        "sections": [
            {
                "subtitle_en": "Origins and Early Life (1677–1707)",
                "subtitle_ko": "뿌리와 출생 (1677–1707)",
                "content_en": "Born in Yangchon, Chopyeong-myeon, Jincheon-gun, Chungcheongbuk-do Province, Yi Ha-gon cultivated his scholarship and artistic talents from an early age. His early poems in Dutacho celebrated nature and the landscapes of his hometown.",
                "content_ko": "충북 진천군 초평면 양촌에서 출생하여 어린시절부터 학문과 예술적 기질을 키워왔습니다. 두타초 초기 시편에서 자연과 고향 풍경을 노래하였습니다."
            },
            {
                "subtitle_en": "A Turning Point (1708)",
                "subtitle_ko": "전환의 순간 (1708)",
                "content_en": "After passing the civil service examination and earning the title of jinsa (literary licentiate), Yi Ha-gon chose to withdraw from public life rather than pursue an official career and devoted himself to scholarship and the arts.",
                "content_ko": "과거에 합격해 진사가 되었으나 벼슬을 포기하고 은거를 선택하며 학문과 예술에 몰두하기 시작하였습니다."
            },
            {
                "subtitle_en": "Seclusion and Scholarship (From 1709)",
                "subtitle_ko": "은거와 학문의 시기 (1709년 이후)",
                "content_en": "In Jincheon, Yi Ha-gon built Mangwollu, a pavilion that housed 10,000 books. There, he immersed himself in reading and scholarship while pursuing calligraphy and painting.",
                "content_ko": "진천에서 만권루를 세우고 장서 1만 권을 수집하고 학문과 서화에 전념하며 독서와 연구에 몰두하였습니다."
            },
            {
                "subtitle_en": "Travels and Excursions (1710s)",
                "subtitle_ko": "여행과 유람의 시기 (1710년대)",
                "content_en": "Yi Ha-gon traveled extensively across Korea, including to Geumgangsan Mountain and the Honam region. During his journeys, he visited Buddhist temples and captured his impressions of nature in poetry and painting.",
                "content_ko": "금강산 호남 등 전국을 유람하며 불교 사찰을 탐방하고 자연과 산수에 대한 감흥을 작품으로 남겼습니다."
            },
            {
                "subtitle_en": "Death and Legacy (1724)",
                "subtitle_ko": "사망과 유산 (1724)",
                "content_en": "Yi Ha-gon died in 1724, the year King Yeongjo ascended the throne. He left behind Dutacho, along with a substantial body of poetry, prose, calligraphy, paintings, and commentary. He is remembered as a quintessential literatus of the late Joseon dynasty who left a lasting mark on the history of Korean literature and art.",
                "content_ko": "이하곤 사망(영조 즉위년), 두타초와 수많은 시, 산문, 서화평을 남겨 후대에 전해지며 조선후기 문인의 전형으로 평가되며 문학·예술사적 가치를 확립하였습니다."
            }
        ]
    },
    {
        "id": 2,
        "badge": "Exhibition Section 02",
        "title_en": "The Evolution of the Book",
        "title_ko": "책의 발전사",
        "type": "story",
        "sections": [
            {
                "subtitle_en": "Handwritten Manuscripts",
                "subtitle_ko": "필사",
                "content_en": "With the invention of writing, knowledge, observations, and records of daily life were preserved and passed down through hand-copied manuscripts.",
                "content_ko": "문자가 생겨 쓰여 지기 시작하면서 지식, 사물, 생활 등에 관하여 필사로 한정되었습니다."
            },
            {
                "subtitle_en": "Woodblock Printing",
                "subtitle_ko": "목판본",
                "content_en": "As civilization advanced and education flourished, demand grew for books that could be produced in large quantities without errors. This led to the transition from the manuscript era to the age of printed books.",
                "content_ko": "인류문화의 발전과 입신양명을 위한 교육의 발달로 오탈자가 없는 책의 대량생산 요구에 따라 사본시대에서 간인본시대로 전환되었습니다."
            },
            {
                "subtitle_en": "Movable Type Printing",
                "subtitle_ko": "활자본",
                "content_en": "Book production evolved further with movable type, where individual characters were cast, arranged, and typeset to produce printed pages.",
                "content_ko": "한 자씩 혹은 몇 자씩 붙여 주조 또는 제작한 활자를 배열, 조판하여 찍어낸 책으로 발전하였습니다."
            },
            {
                "subtitle_en": "Electronic Books",
                "subtitle_ko": "전자책",
                "content_en": "With the advent of smartphones, tablets, and e-readers, books have taken on various digital forms, expanding the ways we read and enriching the reading experience.",
                "content_ko": "스마트폰, 태블릿, 전자책 리더기 등 디지털로 읽을 수 있는 책으로 다양한 형태로 확장되며 독서 경험을 확장하고 있습니다."
            }
        ]
    },
    {
        "id": 3,
        "badge": "Exhibition Section 03",
        "title_en": "Text on the Top Banner",
        "title_ko": "서가배너 글귀",
        "type": "poem",
        "stanzas": [
            {
                "en": "Warm spring waters\nShimmer in shades of blue.",
                "ko": "봄물 따뜻하여\n푸른 빛이 일렁이네"
            },
            {
                "en": "From time to time I visit,\nTo keep company with the moon above the mountains.",
                "ko": "때때로 찾아와\n산 위의 달과 노닌다오"
            },
            {
                "en": "Now and then, wind chimes echo\nFrom far beyond the clouds.",
                "ko": "때때로 들리는\n구름 너머 풍경 소리"
            },
            {
                "en": "Over the southern lake,\nWillows cast their shade.",
                "ko": "남쪽 호수에는 버드나무\n그늘 드리웠구나"
            },
            {
                "en": "Wanwigak lies shrouded\nIn mist and clouds.",
                "ko": "완위각이 구름안개에\n숨어있구나"
            },
            {
                "en": "The wind is calm,\nAnd the water unfurls like white silk.",
                "ko": "바람이 잔잔하니 물결은\n흰 비단을 펼친 듯"
            }
        ]
    },
    {
        "id": 4,
        "badge": "Exhibition Section 04",
        "title_en": "An Anecdote Concerning Wanwigak",
        "title_ko": "완위각 서화 수집의 일화",
        "type": "article",
        "paragraphs": [
            {
                "en": "Yi Ha-gon’s zeal for acquiring fine calligraphy and paintings was extraordinary. It is said that if he encountered a masterpiece while traveling, he would even trade the clothes off his back to obtain it.",
                "ko": "이하곤은 길을 가다가도 좋은 서화를 발견하면 입고 있던 옷을 벗어주고 살 정도로 좋은 서화에 대한 욕심이 대단하였다고 한다."
            },
            {
                "en": "One famous story involves Mangcheonjeodo, a painting by Jeong Seon. Yi Ha-gon and Shin Jeong-ha competed to acquire the painting, and Yi ultimately prevailed. The episode is recorded in his literary collection, Dutacho:",
                "ko": "그 예로 정선이 그린 <망천저도(輞川渚圖)>를 서로 가지기 위해 이하곤과 신정하(申靖夏)가 경쟁이 붙었다. 결국 이 그림은 이하곤이 차지하였다. 이에 대한 일화가 문집인 『두타초(頭陀草)』에 전한다."
            },
            {
                "is_quote": True,
                "en": "“When I look at this album, the brushwork is utterly free of vulgarity, and it deserves to be treasured. Ilwon does not understand painting and is therefore unfit to keep it, though his poetry is beautiful enough to complement the painting. [...]\n\nIn Wanwigak Pavilion, there are only a few dozen old paintings, none by recent artists. This shows that I have not collected many paintings and have not been eager to acquire them. Yet Jeongbo mocks me, saying that although I already possess many, I still covet more. He hopes that Ilwon’s affection for the painting will diminish so that he can profit from the situation, like the fisherman who benefits from the struggle between the snipe and the clam. But Ilwon is no child. Why would he let such a treasure slip away into the clouds and mist?\n\nJeongbo’s old habit has returned once again. I can only laugh.”",
                "ko": "“내가 이 화첩을 보건대 그 붓놀림이 전혀 속되지 않으니 마땅히 보배로 간직해야 한다. 일원(一源)은 그림을 알지 못하므로 이 화첩을 간직하기에 적합하지 않지만 그의 시가 아름다워 이 그림과 짝할 만하다. …\n\n우리집 완위각(宛委閣)에는 고작 수십 점의 오래된 그림이 있을 뿐 근래 여러 사람의 작품은 전혀 없다. 내가 모은 그림이 많지 않고 그림을 구하는 데 인색했음을 알 수 있다. 그런데 정보(正甫)는 지금 많으면서도 더욱 탐낸다며 나를 조롱하고 또 그림을 아끼는 일원의 마음이 줄어서 어부지리(漁父之利)의 성과를 거두고자 기대한다. 일원이 삼척동자(三尺童子)도 아닌데 어떻게 운무(雲霧) 속에 떨어뜨리겠는가.\n\n정보는 옛날 병이 과연 다시 도졌구나. 한바탕 웃노라.”"
            },
            {
                "en": "Wonbaek was the courtesy name of Jeong Seon (1676–1759), the painter of Mangcheonjeodo. Ilwon was the courtesy name of Yi Byeong-yeon (1671–1751), who owned the painting at the time. Jeongbo was the courtesy name of Shin Jeong-ha (1681–1716), who vied with Yi Ha-gon to acquire the painting. In his attempt to secure the painting, Shin Jeong-ha disparaged Yi Byeong-yeon as someone who did not understand painting and accused Yi Ha-gon of coveting yet another work despite already owning many.",
                "ko": "원백(元伯)은 그림을 그린 정선(鄭敾, 1676~1759)의 자이다. 일원(一源)은 이병연(李秉淵, 1671~1751)의 자로, 당시 이 그림을 소장하고 있었다. 정보(正甫)는 신정하(申靖夏, 1681~1716)의 자로, 이하곤과 이 그림을 서로 가지려고 한 사람이다. 신정하는 자신이 차지하기 위해 이병연에 대해 ‘그림을 잘 알지 못한다’, 이하곤에 대해 ‘많이 가진 사람이 욕심을 낸다’라고 험담을 하였다."
            },
            {
                "en": "Yi Ha-gon and Yi Byeong-yeon were fellow disciples of Kim Chang-hyeop and Kim Chang-heup. Shin Jeong-ha was a pupil of Bak Se-chae and was also close to Yi Byeong-yeon. Jeong Seon frequented Kim Chang-heup’s circle as a painter. The contest over Mangcheonjeodo was therefore less a serious conflict than a playful exchange among closely connected literati.",
                "ko": "이하곤이 김창협과 김창흡의 문하에서 수학하여 이병연은 동문(同門)이었고, 신정하는 박세채의 문인으로 이병연과 가까운 사이였다. 정선 역시 화사(畵師)로 김창흡의 문하에 드나들었다. 따라서 이 그림의 경쟁은 다소 장난기 있는 일화라고 할 수 있다."
            }
        ]
    },
    {
        "id": 5,
        "badge": "Exhibition Section 05",
        "title_en": "The Establishment of Wanwigak",
        "title_ko": "완위각의 설립",
        "type": "article",
        "paragraphs": [
            {
                "en": "Wanwigak was a library pavilion established by Yi Ha-gon (1677–1724) in Yangji Village, Chopyeong-myeon, Jincheon-gun. Wanwigak, believed to have been established by 1713, when Yi Ha-gon was 37, was regarded as one of the four great library pavilions of the Joseon dynasty. It was a cultural space where distinguished figures visited to read books and appreciate paintings. It housed a large collection of rare and valuable books and was popularly known as Mangwollu, or “Pavilion of Ten Thousand Volumes.”",
                "ko": "완위각(宛委閣)은 이하곤(李夏坤, 1677~1724)이 진천군 초평면 양지마을에 세운 장서루였다. 1713년 이하곤의 나이 37세 이전에 이미 형성되었던 것으로 추정되는 완위각은 조선시대 4대 장서루로 손꼽히는 곳이었으며, 명사가 찾아와 책을 보고 그림을 감상하던 공간이었다. 많은 진귀한 서적을 소장하여 속칭 만권루(萬卷樓)로도 불리던 문화공간이었다."
            },
            {
                "en": "The Gyeongju Yi clan first settled in Chopyeong-myeon through Yi Ha-gon’s great-grandfather, Yi Si-bal (1569–1626). After helping suppress the Japanese invasions of Korea and Yi Gwal’s Rebellion, Yi Si-bal was granted land in the Chopyeong area, where his descendants subsequently put down roots.",
                "ko": "진천군 초평면에 경주이씨가 정착한 것은 이하곤의 증조인 이시발(李時發, 1569~1626)이었다. 이시발이 임진왜란과 이괄의 난을 평정하면서 초평 일대의 땅을 하사받은 이후 그 후손들이 초평에 뿌리를 내렸다."
            },
            {
                "en": "Yi Ha-gon had an exceptional love of books and rarely put them down. At Wanwigak, he collected not only Confucian classics and historical works, but also fiction, medical texts, and books on divination. In one of his poems, he compared himself to a bookworm:",
                "ko": "유독 서적을 좋아하여 하루라도 손에서 책을 놓지 않았던 이하곤은 이곳에 서고를 세우고 경전과 역사서는 물론이고 소설, 의서, 점술서 등을 소장하였다. 그는 시에서 스스로를 좀벌레라고 비유하였다."
            },
            {
                "is_quote": True,
                "en": "“This old man, too, has a fondness for books;\nI know that in a former life I must have been two bookworms.”\n(老夫亦有耽書癖 知是前身兩蠧魚)",
                "ko": "“늙은 나도 책을 즐기는 버릇 있으니,\n전생에 두 마리 좀벌레였음을 알겠네.”\n(老夫亦有耽書癖 知是前身兩蠧魚)"
            },
            {
                "en": "The late Joseon scholar Yi Yu-won (1814–1888) traced the origins of Wanwigak to an anecdote concerning Yi Ha-gon’s ancestor, Yi Je-hyeon (1287–1367). While in Yanjing during the Yuan dynasty, Yi Je-hyeon established a reading hall called Mangwondang, or “Hall of Ten Thousand Volumes,” and stocked it with numerous books from ancient and contemporary times. There, he pursued scholarly studies and engaged in discussions with renowned Yuan scholars of the time, including Zhao Mengfu and Yuan Mingshan.",
                "ko": "조선 후기 이유원(李裕元, 1814~1888)은 이 완위각의 유래가 이하곤의 조상인 이제현(李齊賢, 1287~1367)의 고사에서 유래하였다고 하였다. 이제현은 원나라 연경에 있을 때 만권당(萬卷堂)이라는 독서당을 세워 고금의 많은 서적을 비치하였다. 이곳에서 조맹부, 원명선 등 원나라의 유명한 학자들과 학술을 토론하고 연구하였다."
            },
            {
                "en": "Instead of simply owning books, Yi Ha-gon carefully proofread and critiqued each volume, and whenever he encountered a book he wanted, particularly one not already in his collection, he spared no means or effort to acquire it. This extraordinary devotion ultimately gave rise to the rich and diverse collection of books at Wanwigak.",
                "ko": "이하곤은 소유에 그치지 않고 일일이 교정하고 비평하면서 무작정 책이 좋아 있으면 보고 없는 것은 수단과 방법을 가리지 않고 사들였다. 이러한 집착의 결과 다양하면서도 풍부한 완위각의 전적이 형성되었다고 하겠다."
            }
        ]
    },
    {
        "id": 6,
        "badge": "Exhibition Section 06",
        "title_en": "Records of Wanwigak by Distinguished Figures of the Joseon Dynasty",
        "title_ko": "조선시대 명사의 완위각 기록",
        "type": "article",
        "paragraphs": [
            {
                "en": "As Wanwigak became known for its extensive collection of rare and valuable books, its reputation spread widely, attracting distinguished figures both during Yi Ha-gon’s lifetime and in later generations.",
                "ko": "완위각에 진귀한 서적이 많이 소장되면서 그 존재가 알려졌고, 당시는 물론 이후에도 많은 명사가 방문하여 완위각의 명성이 더욱 퍼져나갔다."
            },
            {
                "en": "The renowned calligrapher Yun Sun (1680–1741) wrote the plaque inscription “Wanwigak,” while his disciple Yi Gwang-sa (1705–1777) wrote the plaque inscription “Mangwollu.” During Yi Ha-gon’s lifetime, Kim Chang-heup and Yi Byeong-yeon, who were closely associated with him, mentioned Wanwigak in their writings. In later generations, figures including Sim Yuk (1685–1753), Yi Chung-ik (1744–1816), and Yi Yu-won (1814–1888) left poems and prose about the pavilion.",
                "ko": "조선시대 명필인 윤순(尹淳, 1680~1741)이 ‘완위각(宛委閣)’이라는 편액을 썼으며, 그의 제자인 이광사(李匡師, 1705~1777)가 ‘만권루(萬卷樓)’의 편액을 썼다. 당대에 김창흡, 이병연 등이 이하곤과 교유하면서 완위각을 언급하고, 심육(1685~1753), 이충익(1744~1816), 이유원(1814~1888) 등이 시문을 남겼다."
            },
            {
                "en": "When Yi Jip-du, Yi Ha-gon’s grandson, was appointed magistrate of Jincheon County and brought his father, Yi Seok-no, to live with him, Yi Chung-ik composed a poem for the occasion. In it, he noted that Wanwigak contained a remarkably rich collection of books and that Yi Jip-du planned to remain there after completing his term in office to preserve the scholarly legacy of his ancestors.",
                "ko": "이충익은 이하곤의 손자인 이집두가 진천현감이 되어 그 부친인 이석노를 모시자 시를 지어 주었다. 여기에서 이충익은 완위각에는 책이 매우 풍부하다고 하면서 이집두가 임기가 끝나면 머물며 선대의 유업을 지킬 것을 계획하였다고 하였다."
            },
            {
                "is_quote": True,
                "en": "Yi Yu-won (1814–1888) wrote in his essay Mangwollu:\n\n“In Chopyeong, there is Mangwollu, which was established by Yi Ha-gon.”\n\nHe explained that it was given this name because it housed a large collection of books covering a wide range of subjects.",
                "ko": "이유원(1814~1888)도 <만권루>라는 글에서 다음과 같이 기록하였다.\n\n“초평에 만권루가 있는데, 이는 이하곤이 지은 것이다.”\n\n그는 여러 분야의 많은 책을 소장하고 있어서 그렇게 이름을 삼았다고 설명하였다."
            }
        ]
    },
    {
        "id": 7,
        "badge": "Exhibition Section 07",
        "title_en": "Visits and Legacy of Eminent Figures in the Late Joseon Period",
        "title_ko": "한말 명사의 방문과 자취",
        "type": "article",
        "paragraphs": [
            {
                "en": "Amid the political turmoil caused by foreign incursions in the final years of the Joseon dynasty, Chopyeong in Jincheon was a suitable place for intellectuals to live in seclusion. Not only was the area home to the Gyeongju Yi clan, but Wanwigak, with its extensive collection of books, also provided an ideal setting for cultivating their scholarship. Scholar-officials who had served in government in Seoul, particularly prominent figures of the Soron political faction, gathered in Chopyeong.",
                "ko": "외세의 침략에 어수선한 정국에서 진천 초평은 지식인들이 은거하기에 적당하였다. 여기에는 경주이씨가 자리하고 있을 뿐만 아니라 많은 서적을 소장한 완위각이 있어서 자신들의 학문적 소양을 연마하기에 적합하였다. 서울에서 벼슬 생활하던 사대부, 특히 소론의 명사들은 초평으로 모여들었다."
            },
            {
                "en": "A substantial collection of books remained carefully preserved at Wanwigak even until the end of the Joseon dynasty. In a poem written in 1922, Jeong In-pyo wrote, “Ten thousand volumes, bound in silk, fill the bookshelves.” The verse reflects how Wanwigak continued to be regarded as a place where intellectuals could pursue scholarship and cultivate themselves.",
                "ko": "당시 완위각은 한말까지도 상당량의 전적이 잘 보관되어 있었다. 1922년 지은 시에서 정인표는 “장물 서책 만권이 비단으로 장정되어 서가에 가득하네”라고 하여 완위각이 여전히 지식인들이 학문하며 수양하는 공간으로 인식하고 있었다."
            },
            {
                "en": "Among the distinguished figures who resigned from government positions in Seoul and moved to Chopyeong were Hong Seung-heon (1854–?), Jeong Won-ha (1855–?), Jeong Eun-jo (1856–?), Jeong In-pyo, Yi Jong-hyeong, and Jeong In-bo. They were leading intellectuals of their time and prominent figures of the Soron faction, and shared a connection with the Ganghwa School. Hong Seung-heon, a fifth-generation descendant of Hong Yang-ho (1724–1802), resigned from his post as Vice Minister of Personnel and moved to Jincheon. Jeong Won-ha, a sixth-generation descendant of Jeong Je-du (1649–1736), regarded as a founder of Yangmingism in Joseon, resigned from his post as Inspector General and withdrew to Jincheon. Yi Jong-hyeong, the eldest male-line descendant of Yi Si-bal, left his position as Royal Secretary and returned to his ancestral home in Chopyeong. His close friend, Jeong In-pyo, moved from Anseong to Chopyeong in 1898. Jeong Eun-jo, who had also served as Royal Secretary, later moved to Chopyeong with his son, Jeong In-bo. These figures helped guide and educate Jeong In-bo, who was still in his teens at the time.",
                "ko": "한말 서울에서 벼슬을 그만두고 진천 초평으로 옮겨 살았던 명사로 홍승헌(1854~?), 정원하(1855~?), 정은조(1856~?), 정인표, 이종형, 정인보 등이 있다. 이들은 당대를 대표하는 지식인이자 소론의 명사들로 강화학파 학인이라는 공통점을 지닌다. 홍양호(1724~1802)의 5대손인 홍승헌은 이조참판을 사직하고 진천으로 내려왔으며, 조선 양명학의 비조인 정제두(1649~1736)의 6대손인 정원하도 대사헌을 사직하고 진천으로 내려와 은거하였다. 경주이씨 이시발의 종손인 이종형이 비서승을 그만두고 고향인 초평으로 왔으며, 친한 벗인 정인표도 1898년 안성에서 초평으로 옮겨 살았다. 비서승을 지낸 정은조도 아들인 정인보를 데리고 초평으로 이거하여 10대였던 정인보를 훈도하였다."
            },
            {
                "en": "Thus, in the final years of the Joseon dynasty, Wanwigak was more than a repository for books. It served as an important cultural space for intellectuals of the Soron tradition and as an academic and intellectual center for prominent scholars and literati.",
                "ko": "이처럼 한말 완위각은 전적을 수장한 서고의 의미를 넘어 당대 소론계 지식인들의 문화적 공간이었다. 완위각은 소론의 명사나 문한들에게 학문적, 정신적 구심점으로 자리하였다."
            }
        ]
    },
    {
        "id": 8,
        "badge": "Exhibition Section 08",
        "title_en": "Genealogy of the Gyeongju Yi Clan of Chopyeong, Jincheon",
        "title_ko": "진천 초평 경주이씨 가계도",
        "type": "genealogy",
        "sections": [
            {
                "ref_title_en": "Reference 1: The Origin of Palbyeol",
                "ref_title_ko": "참고 자료 1: 팔별(八鼈)의 유래",
                "content_en": "The Gyeongju Yi clan of Chopyeong traces its lineage to the eight sons of Yi Gong-rin, collectively known as the Palbyeol (八鼈, Eight Turtles). Yi Gong-rin, a sixth-generation descendant of Yi Je-hyeon, married a daughter of Bak Paeng-nyeon. According to legend, he dreamed of eight turtles, said to be the sons of the Dragon King. When his eight sons were born, he named them after aquatic creatures: O (鰲, Giant Turtle), Gu (龜, Turtle), Won (黿, Softshell Turtle), Ta (鼉, Crocodile), Byeol (鼈, Softshell Turtle), Byeok (鼊, Turtle), Gyeong (鯨, Whale), and Gon (鯤, Giant Fish).",
                "content_ko": "진천 초평의 경주이씨는 이공린(李公麟)의 여덟 아들인 팔별(八鼈)에서 시작된다. 이제현(李齊賢)의 6대손인 이공린은 박팽년(朴彭年)의 사위가 되어 용왕의 아들인 여덟 자라를 꿈꾸고, 태어나는 여덟 명의 아들 이름을 물에 사는 ‘자라(鰲)’, ‘거북이(龜)’, ‘자라(黿)’, ‘악어(鼉)’, ‘자라(鼈)’, ‘거북이(鼊)’, ‘고래(鯨)’, ‘곤이(鯤)’라고 하였다."
            },
            {
                "ref_title_en": "Reference 2: Succession to Yi Ha-gon",
                "ref_title_ko": "참고 자료 2: 이하곤으로 이어지는 계보",
                "content_en": "The third of the eight brothers, Yi Won, was an ancestor of Yi Ha-gon. Yi Won’s third son, Yi Gyeong-yun, had three sons. Through Yi Dae-geon, one of his descendants, the family line reached Yi Si-bal, who settled in Chopyeong, Jincheon. The lineage continued through Yi Si-bal’s son, Yi Gyeong-eok, and his grandson, Yi In-yeop, eventually leading to Yi Ha-gon. After Yi Ha-gon, the family line continued through Yi Seok-pyo, Yi Hu-won, and Yi Jip-ro.",
                "content_ko": "여덟 형제 중 셋째인 이원(李黿)이 이하곤의 선조이다. 그의 3남인 이경윤(李憬胤)은 아들 세 명을 두었는데, 이대건(李大建)의 아들인 이시발(李時發)에 이르러 경주이씨가 진천 초평에 정착하였다. 이시발의 아들인 이경억(李慶億)과 손자인 이인엽(李寅燁)을 거쳐 이하곤에 이르렀다. 이하곤 이후의 가계는 이석표(李錫杓), 이후원(李厚源), 이집로(李集魯)로 계승되었다."
            }
        ],
        "lineage_chart": [
            {"generation": "G1", "name": "Yi Je-hyeon (이제현)", "role": "Ancestor / Mangwondang Founder"},
            {"generation": "G7", "name": "Yi Gong-rin (이공린)", "role": "Father of the Eight Turtles (Palbyeol)"},
            {"generation": "G8", "name": "Yi Won (이원 - 黿)", "role": "3rd Son of Yi Gong-rin"},
            {"generation": "G9", "name": "Yi Gyeong-yun (이경윤)", "role": "3rd Son of Yi Won"},
            {"generation": "G11", "name": "Yi Si-bal (이시발)", "role": "Settled in Chopyeong, Jincheon"},
            {"generation": "G12", "name": "Yi Gyeong-eok (이경억)", "role": "Son of Yi Si-bal"},
            {"generation": "G13", "name": "Yi In-yeop (이인엽)", "role": "Grandson of Yi Si-bal"},
            {"generation": "G14", "name": "Yi Ha-gon (이하곤)", "role": "Master of Wanwigak (1677–1724)"},
            {"generation": "G15+", "name": "Yi Seok-pyo → Yi Hu-won → Yi Jip-ro", "role": "Later Generations"}
        ]
    },
    {
        "id": 9,
        "badge": "Exhibition Section 09",
        "title_en": "Donor Yi Jeong-hui",
        "title_ko": "기증자 이정희 코너",
        "type": "donor",
        "meta_en": "October 22, 1931 – August 4, 2019 / Gyeongju Yi Clan",
        "meta_ko": "1931년 10월 22일 ~ 2019년 8월 4일 | 경주이씨",
        "content_en": "Born in Yongjeong-ri, Chopyeong-myeon, Jincheon-gun, Chungcheongbuk-do Province, Yi Jeong-hui was a tenth-generation descendant of Yi In-yeop of the Gyeongju Yi clan. To support the restoration of Wanwigak and the development of Chopyeong Book Village, he donated some 800 old books that had been preserved by his family. Some of the books in the original collection were destroyed in a fire in the late Joseon period. The surviving volumes continued to be preserved in the family’s sarangchae, the traditional men’s quarters of the house, and were kept even after the family moved to Seoul. At one point, the collection was also entrusted to the Jangseogak Archives of the Academy of Korean Studies. The donated books will be permanently preserved by Jincheon County and continue to serve as valuable resources for exhibitions and academic research.",
        "content_ko": "충북 진천군 초평면 용정리 출신으로 경주이씨 이인엽(회와공)의 10대 후손이다. 완위각 복원과 초평 책마을 조성사업을 위해 집안에서 보존해온 고서 약 800권을 기증하였다. 이 고서들은 구한말 화재로 일부가 소실된 뒤 사랑채와 서울 이주 후에도 계속 보관되었으며, 한때 한국학중앙연구원 장서각에 위탁된 기록도 있다. 기증된 고서는 진천군에서 영구히 보존하며, 다양한 전시와 학술연구 자료로 꾸준히 활용될 예정이다."
    }
]

with open('exhibition_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("exhibition_data.json created successfully!")
