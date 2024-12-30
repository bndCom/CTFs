from math import gcd
n=14796477939003611775208041290348339020936676002454717224646251311708293201469184897483873509941865693809473126459329421641681364023167948749968330703736720102973359063469333188059740821023029754734348790951000190344725434181826714146206341535759458897968330526467533482043059528899390103382667493810391462225262830839080650123020531330437922519352683752900562956790917167821286707566070945501977829889638290916396721583750493508694371199246172248676755456956867908139894047255712093824958695471469193986023590431653571458714419577768587744910333974014399293363573408883808909700956297360313208260851637982241566005049
c=7834381455537086069556470828674580173937271064256312815617230923582264273260067511896680320170885743343862894164014864043792487985706669274975353978277862462944814782646749746217479200710773218743409525658958249817055354592575831865920206596021699022326281524908299055420849742148757177093582285192053105592180465511200588277457610702671508363048935552446809692594715753573724603294565113603946429767347234628199252177612170759392617992009035004668823723769453952068616628571785811538463850603629779083508146990944772896050051747702814005551146368404685501836088557927084895438654990821206561992369510510301944786242
p=95035264145462998106373959950852388512916398417336694051973007035267892127571038290551358518210018988802168144062568058000141570285306734135476955708641860308084865175837570650537276267265396611644179740194499506782555051319215145789689879081854479885459274078337276115880870922739027746148771680782305865397

e = 65537
q = n // p
phi = (p-1)*(q-1)

for e in range(1, 51):
    if gcd(e, phi) != 1:
        print("not coprimes phi and e.")
        continue

    d = pow(e, -1, phi)
    m = pow(c, d, n)

    flag = bytes.fromhex(hex(m)[2:])

    print(f"{e} -> {flag}")

# csd{V3sA_R3sa_RSa?_1D3k}
    