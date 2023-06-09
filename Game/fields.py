import pygame

WIDTH,HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)

fields_list = []

class Field:
    def __init__(self, size, center, next=[]):
        self.size = size
        self.center = center
        self.next_fields = next
        fields_list.append(self)
        self.rect = pygame.Rect((self.center[0]-(self.size/2),self.center[1]-(self.size/2)), (self.size, self.size))
        self.gym = False
        self.shining = False

    def shine(self):
        self.shining = True
        pygame.draw.circle(SCREEN, (0,255,0), self.center, self.size+2, width=3)
        pygame.display.update()

class ChanceField(Field):
    def __init__(self, location, size, center, next = []):
        self.location = location
        super().__init__(size, center, next = [])

class GymField(Field):
    def __init__(self, location, size, center, next = []):
        self.location = location
        super().__init__(size, center, next = [])
        self.gym = True

class PokeField(Field):
    def __init__(self, location, size, center, next = []):
        self.location = location
        super().__init__(size, center, next = [])

class RocketField(Field):
    pass

class BattleField(Field):
    pass

class MegaField(Field):
    pass
    
field1 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 227,112), [])
field2 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 248,106), [])
field3 = ChanceField('orange',10, ((SCREEN.get_width() - 1094) / 2 + 270,118), [])
field4 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 285,102), [])
field5 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 297,84), [])
field6 = GymField('orange',22, ((SCREEN.get_width() - 1094) / 2 + 272,49), [])
field7 = PokeField('orange',12, ((SCREEN.get_width() - 1094) / 2 + 323,96), [])
field8 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 351,104), [])
field9 = PokeField('orange',12, ((SCREEN.get_width() - 1094) / 2 + 377,111), [])
field10 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 403,109), [])
field11 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 413,134), [])
field12 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 438,134), [])
field13 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 458,125), [])
field14 = PokeField('gray',12, ((SCREEN.get_width() - 1094) / 2 + 477,111), [])
field15 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 492,88), [])
field16 = PokeField('gray',12, ((SCREEN.get_width() - 1094) / 2 + 512,72), [])
field17 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 533,57), [])
field18 = ChanceField('gray',10, ((SCREEN.get_width() - 1094) / 2 + 560,48), [])
field19 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 587,54), [])
field20 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 618,49), [])
field21 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 622,75), [])
field22 = PokeField('gray',12, ((SCREEN.get_width() - 1094) / 2 + 613,99), [])
field23 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 594,110), [])
field24 = GymField('gray',22, ((SCREEN.get_width() - 1094) / 2 + 560,104), [])
field25 = PokeField('gray',12, ((SCREEN.get_width() - 1094) / 2 + 648,79), [])
field26 = RocketField(10, ((SCREEN.get_width() - 1094) / 2 + 657,102), [])
field27 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 663,124), [])
field28 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 676,148), [])
field29 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 688,170), [])
field30 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 711,161), [])
field31 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 733,145), [])
field32 = PokeField('gray',12, ((SCREEN.get_width() - 1094) / 2 + 760,139), [])
field33 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 788,139), [])
field34 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 815,127), [])
field35 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 844,117), [])
field36 = MegaField(30, ((SCREEN.get_width() - 1094) / 2 + 895,126), [])
field37 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 876,167), [])
field38 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 866,188), [])
field39 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 848,207), [])
field40 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 870,227), [])
field41 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 899,233), [])
field42 = PokeField('green',12, ((SCREEN.get_width() - 1094) / 2 + 928,234), [])
field43 = RocketField(10, ((SCREEN.get_width() - 1094) / 2 + 958,237), [])
field44 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 964,265), [])
field45 = PokeField('green',12, ((SCREEN.get_width() - 1094) / 2 + 946,290), [])
field46 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 935,315), [])
field47 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 917,338), [])
field48 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 889,353), [])
field49 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 855,357), [])
field50 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 855,386), [])
field51 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 880,402), [])
field52 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 895,423), [])
field53 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 884,447), [])
field54 = RocketField(10, ((SCREEN.get_width() - 1094) / 2 + 872,471), [])
field55 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 897,482), [])
field56 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 924,484), [])
field57 = ChanceField('brown',10, ((SCREEN.get_width() - 1094) / 2 + 957,491), [])
field58 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 969,519), [])
field59 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 937,528), [])
field60 = PokeField('brown',12, ((SCREEN.get_width() - 1094) / 2 + 912,538), [])
field61 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 887,533), [])
field62 = GymField('brown',27, ((SCREEN.get_width() - 1094) / 2 + 843,531), [])
field63 = PokeField('brown',12, ((SCREEN.get_width() - 1094) / 2 + 976,547), [])
field64 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 978,574), [])
field65 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 952,587), [])
field66 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 923,588), [])
field67 = PokeField('brown',12, ((SCREEN.get_width() - 1094) / 2 + 896,591), [])
field68 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 865,593), [])
field69 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 833,589), [])
field70 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 804,585), [])
field71 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 779,569), [])
field72 = PokeField('brown',12, ((SCREEN.get_width() - 1094) / 2 + 764,547), [])
field73 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 753,519), [])
field74 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 727,519), [])
field75 = PokeField('yellow',12, ((SCREEN.get_width() - 1094) / 2 + 702,534), [])
field76 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 677,535), [])
field77 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 675,559), [])
field78 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 652,571), [])
field79 = PokeField('yellow',12, ((SCREEN.get_width() - 1094) / 2 + 626,580), [])
field80 = RocketField(10, ((SCREEN.get_width() - 1094) / 2 + 598,580), [])
field81 = PokeField('yellow',12, ((SCREEN.get_width() - 1094) / 2 + 571,578), [])
field82 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 542,571), [])
field83 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 517,554), [])
field84 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 503,532), [])
field85 = PokeField('yellow',12, ((SCREEN.get_width() - 1094) / 2 + 475,533), [])
field86 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 477,558), [])
field87 = GymField('yellow',27, ((SCREEN.get_width() - 1094) / 2 + 441,581), [])
field88 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 451,521), [])
field89 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 429,511), [])
field90 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 417,489), [])
field91 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 404,465), [])
field92 = PokeField('purple',12, ((SCREEN.get_width() - 1094) / 2 + 379,447), [])
field93 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 356,428), [])
field94 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 325,434), [])
field95 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 292,441), [])
field96 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 265,447), [])
field97 = PokeField('purple',12, ((SCREEN.get_width() - 1094) / 2 + 239,444), [])
field98 = RocketField(10, ((SCREEN.get_width() - 1094) / 2 + 214,449), [])
field99 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 189,448), [])
field100 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 165,436), [])
field101 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 144,422), [])
field102 = PokeField('purple',12, ((SCREEN.get_width() - 1094) / 2 + 161,404), [])
field103 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 179,390), [])
field104 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 200,382), [])
field105 = GymField('purple',22, ((SCREEN.get_width() - 1094) / 2 + 233,358), [])
field106 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 121,414), [])
field107 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 110,394), [])
field108 = PokeField('purple',12, ((SCREEN.get_width() - 1094) / 2 + 110,371), [])
field109 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 116,348), [])
field110 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 130,328), [])
field111 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 148,311), [])
field112 = PokeField('purple',12, ((SCREEN.get_width() - 1094) / 2 + 157,290), [])
field113 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 177,273), [])
field114 = PokeField('purple',12, ((SCREEN.get_width() - 1094) / 2 + 200,262), [])
field115 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 224,249), [])
field116 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 226,228), [])
field117 = PokeField('orange',12, ((SCREEN.get_width() - 1094) / 2 + 228,203), [])
field118 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 205,194), [])
field119 = PokeField('orange',12, ((SCREEN.get_width() - 1094) / 2 + 186,176), [])
field120 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 196,150), [])
field121 = RocketField(10, ((SCREEN.get_width() - 1094) / 2 + 218,134), [])
field122 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 254,195), [])
field123 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 281,195), [])
field124 = PokeField('orange',12, ((SCREEN.get_width() - 1094) / 2 + 306,184), [])
field125 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 330,172), [])
field126 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 347,152), [])
field127 = PokeField('orange',12, ((SCREEN.get_width() - 1094) / 2 + 373,156), [])
field128 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 397,151), [])
field129 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 318,207), [])
field130 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 340,222), [])
field131 = PokeField('white',12, ((SCREEN.get_width() - 1094) / 2 + 365,229), [])
field132 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 391,218), [])
field133 = PokeField('white',12, ((SCREEN.get_width() - 1094) / 2 + 419,210), [])
field134 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 449,210), [])
field135 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 473,197), [])
field136 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 483,172), [])
field137 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 486,151), [])
field138 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 493,130), [])
field139 = PokeField('gray',12, ((SCREEN.get_width() - 1094) / 2 + 507,181), [])
field140 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 527,169), [])
field141 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 551,176), [])
field142 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 569,160), [])
field143 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 590,164), [])
field144 = PokeField('gray',12, ((SCREEN.get_width() - 1094) / 2 + 610,175), [])
field145 = PokeField('gray',12, ((SCREEN.get_width() - 1094) / 2 + 625,154), [])
field146 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 641,135), [])
field147 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 245,260), [])
field148 = PokeField('purple',12, ((SCREEN.get_width() - 1094) / 2 + 251,285), [])
field149 = ChanceField('purple',10, ((SCREEN.get_width() - 1094) / 2 + 277,296), [])
field150 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 301,311), [])
field151 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 327,323), [])
field152 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 356,331), [])
field153 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 381,328), [])
field154 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 407,339), [])
field155 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 434,327), [])
field156 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 460,332), [])
field157 = ChanceField('white',10, ((SCREEN.get_width() - 1094) / 2 + 484,320), [])
field158 = GymField('white',25, ((SCREEN.get_width() - 1094) / 2 + 503,285), [])
field159 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 462,270), [])
field160 = PokeField('white',12, ((SCREEN.get_width() - 1094) / 2 + 435,266), [])
field161 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 412,272), [])
field162 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 390,283), [])
field163 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 365,278), [])
field164 = PokeField('white',12, ((SCREEN.get_width() - 1094) / 2 + 363,255), [])
field165 = PokeField('purple',12, ((SCREEN.get_width() - 1094) / 2 + 374,407), [])
field166 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 388,385), [])
field167 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 398,362), [])
field168 = PokeField('white',12, ((SCREEN.get_width() - 1094) / 2 + 545,284), [])
field169 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 565,264), [])
field170 = PokeField('white',12, ((SCREEN.get_width() - 1094) / 2 + 575,245), [])
field171 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 566,221), [])
field172 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 558,199), [])
field173 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 528,318), [])
field174 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 526,343), [])
field175 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 507,361), [])
field176 = PokeField('blue',12, ((SCREEN.get_width() - 1094) / 2 + 489,384), [])
field177 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 473,408), [])
field178 = PokeField('blue',12, ((SCREEN.get_width() - 1094) / 2 + 489,431), [])
field179 = RocketField(10, ((SCREEN.get_width() - 1094) / 2 + 513,445), [])
field180 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 536,455), [])
field181 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 566,458), [])
field182 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 595,452), [])
field183 = PokeField('blue',12, ((SCREEN.get_width() - 1094) / 2 + 585,430), [])
field184 = GymField('blue',25, ((SCREEN.get_width() - 1094) / 2 + 556,398), [])
field185 = PokeField('blue',12, ((SCREEN.get_width() - 1094) / 2 + 619,444), [])
field186 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 642,430), [])
field187 = ChanceField('blue',10, ((SCREEN.get_width() - 1094) / 2 + 649,402), [])
field188 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 676,405), [])
field189 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 700,412), [])
field190 = PokeField('blue',12, ((SCREEN.get_width() - 1094) / 2 + 714,438), [])
field191 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 720,462), [])
field192 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 746,468), [])
field193 = PokeField('brown',12, ((SCREEN.get_width() - 1094) / 2 + 755,493), [])
field194 = PokeField('blue',12, ((SCREEN.get_width() - 1094) / 2 + 553,347), [])
field195 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 578,341), [])
field196 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 606,344), [])
field197 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 629,329), [])
field198 = PokeField('blue',12, ((SCREEN.get_width() - 1094) / 2 + 649,351), [])
field199 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 647,375), [])
field200 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 768,455), [])
field201 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 795,450), [])
field202 = PokeField('brown',12, ((SCREEN.get_width() - 1094) / 2 + 821,457), [])
field203 = PokeField('brown',12, ((SCREEN.get_width() - 1094) / 2 + 845,466), [])
field204 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 601,240), [])
field205 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 626,240), [])
field206 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 653,242), [])
field207 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 679,248), [])
field208 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 705,254), [])
field209 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 718,234), [])
field210 = PokeField('green',12, ((SCREEN.get_width() - 1094) / 2 + 719,212), [])
field211 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 702,192), [])
field212 = BattleField(10, ((SCREEN.get_width() - 1094) / 2 + 742,232), [])
field213 = ChanceField('green',10, ((SCREEN.get_width() - 1094) / 2 + 768,228), [])
field214 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 791,218), [])
field215 = PokeField('green',12, ((SCREEN.get_width() - 1094) / 2 + 818,208), [])
field216 = PokeField('blue',12, ((SCREEN.get_width() - 1094) / 2 + 716,396), [])
field217 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 725,372), [])
field218 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 726,348), [])
field219 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 733,324), [])
field220 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 751,306), [])
field221 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 779,298), [])
field222 = PokeField('green',12, ((SCREEN.get_width() - 1094) / 2 + 804,288), [])
field223 = GymField('green',25, ((SCREEN.get_width() - 1094) / 2 + 847,281), [])
field224 = PokeField('green',12, ((SCREEN.get_width() - 1094) / 2 + 713,280), [])
field225 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 734,290), [])
field226 = PokeField('green',12, ((SCREEN.get_width() - 1094) / 2 + 770,331), [])
field227 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 792,347), [])
field228 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 822,355), [])
field229 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 462,498), [])
field230 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 480,482), [])
field231 = ChanceField('yellow',10, ((SCREEN.get_width() - 1094) / 2 + 503,488), [])
field232 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 526,498), [])
field233 = PokeField('yellow',12, ((SCREEN.get_width() - 1094) / 2 + 550,507), [])
field234 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 573,513), [])
field235 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 598,508), [])
field236 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 617,493), [])
field237 = Field(10, ((SCREEN.get_width() - 1094) / 2 + 641,502), [])
field238 = PokeField('yellow',12, ((SCREEN.get_width() - 1094) / 2 + 663,515), [])

field1.next_fields = [field2, field121]
field2.next_fields = [field1, field3]
field3.next_fields = [field2, field4]
field4.next_fields = [field3, field5]
field5.next_fields = [field4, field6, field7]
field6.next_fields = [field5]
field7.next_fields = [field5, field8]
field8.next_fields = [field7, field9]
field9.next_fields = [field8, field10]
field10.next_fields = [field9, field11]
field11.next_fields = [field10, field12, field128]
field12.next_fields = [field11, field13]
field13.next_fields = [field12, field14]
field14.next_fields = [field13, field15, field138]
field15.next_fields = [field14, field16]
field16.next_fields = [field15, field17]
field17.next_fields = [field16, field18]
field18.next_fields = [field17, field19]
field19.next_fields = [field18, field20]
field20.next_fields = [field19, field21]
field21.next_fields = [field20, field22, field25]
field22.next_fields = [field21, field23]
field23.next_fields = [field22, field24]
field24.next_fields = [field23]
field25.next_fields = [field21, field26]
field26.next_fields = [field25, field27]
field27.next_fields = [field26, field28, field146]
field28.next_fields = [field27, field29]
field29.next_fields = [field28, field30, field211]
field30.next_fields = [field29, field31]
field31.next_fields = [field30, field32]
field32.next_fields = [field31, field33]
field33.next_fields = [field32, field34]
field34.next_fields = [field33, field35]
field35.next_fields = [field34, field36]
field36.next_fields = [field35, field37]
field37.next_fields = [field36, field38]
field38.next_fields = [field37, field39]
field39.next_fields = [field38, field40, field215]
field40.next_fields = [field39, field41]
field41.next_fields = [field40, field42]
field42.next_fields = [field41, field43]
field43.next_fields = [field42, field44]
field44.next_fields = [field43, field45]
field45.next_fields = [field44, field46]
field46.next_fields = [field45, field47]
field47.next_fields = [field46, field48]
field48.next_fields = [field47, field49]
field49.next_fields = [field48, field50, field228]
field50.next_fields = [field49, field51]
field51.next_fields = [field50, field52]
field52.next_fields = [field51, field53]
field53.next_fields = [field52, field54]
field54.next_fields = [field53, field55, field203]
field55.next_fields = [field54, field56]
field56.next_fields = [field55, field57]
field57.next_fields = [field56, field58]
field58.next_fields = [field57, field59, field63]
field59.next_fields = [field58, field60]
field60.next_fields = [field59, field61]
field61.next_fields = [field60, field62]
field62.next_fields = [field61]
field63.next_fields = [field58, field64]
field64.next_fields = [field63, field65]
field65.next_fields = [field64, field66]
field66.next_fields = [field65, field67]
field67.next_fields = [field66, field68]
field68.next_fields = [field67, field69]
field69.next_fields = [field68, field70]
field70.next_fields = [field69, field71]
field71.next_fields = [field70, field72]
field72.next_fields = [field71, field73]
field73.next_fields = [field72, field74, field193]
field74.next_fields = [field73, field75]
field75.next_fields = [field74, field76]
field76.next_fields = [field75, field77, field238]
field77.next_fields = [field76, field78]
field78.next_fields = [field77, field79]
field79.next_fields = [field78, field80]
field80.next_fields = [field79, field81]
field81.next_fields = [field80, field82]
field82.next_fields = [field81, field83]
field83.next_fields = [field82, field84]
field84.next_fields = [field83, field85]
field85.next_fields = [field84, field86, field88]
field86.next_fields = [field85, field87]
field87.next_fields = [field86]
field88.next_fields = [field85, field89, field229]
field89.next_fields = [field88, field90]
field90.next_fields = [field89, field91]
field91.next_fields = [field90, field92]
field92.next_fields = [field91, field93]
field93.next_fields = [field92, field94, field165]
field94.next_fields = [field93, field95]
field95.next_fields = [field94, field96]
field96.next_fields = [field95, field97]
field97.next_fields = [field96, field98]
field98.next_fields = [field97, field99]
field99.next_fields = [field98, field100]
field100.next_fields = [field99, field101]
field101.next_fields = [field100, field102, field106]
field102.next_fields = [field101, field103]
field103.next_fields = [field102, field104]
field104.next_fields = [field103, field105]
field105.next_fields = [field104]
field106.next_fields = [field101, field107]
field107.next_fields = [field106, field108]
field108.next_fields = [field107, field109]
field109.next_fields = [field108, field110]
field110.next_fields = [field109, field111]
field111.next_fields = [field110, field112]
field112.next_fields = [field111, field113]
field113.next_fields = [field112, field114]
field114.next_fields = [field113, field115]
field115.next_fields = [field114, field116, field147]
field116.next_fields = [field115, field117]
field117.next_fields = [field116, field118, field122]
field118.next_fields = [field117, field119]
field119.next_fields = [field118, field120]
field120.next_fields = [field119, field121]
field121.next_fields = [field120, field1]
field122.next_fields = [field117, field123]
field123.next_fields = [field122, field124]
field124.next_fields = [field123, field125, field129]
field125.next_fields = [field124, field126]
field126.next_fields = [field125, field127]
field127.next_fields = [field126, field128]
field128.next_fields = [field127, field11]
field129.next_fields = [field124, field130]
field130.next_fields = [field129, field131]
field131.next_fields = [field130, field132, field164]
field132.next_fields = [field131, field133]
field133.next_fields = [field132, field134]
field134.next_fields = [field133, field135]
field135.next_fields = [field134, field136]
field136.next_fields = [field135, field137, field139]
field137.next_fields = [field136, field138]
field138.next_fields = [field137, field14]
field139.next_fields = [field136, field140]
field140.next_fields = [field139, field141]
field141.next_fields = [field140, field142, field172]
field142.next_fields = [field141, field143]
field143.next_fields = [field142, field144]
field144.next_fields = [field143, field145]
field145.next_fields = [field144, field146]
field146.next_fields = [field145, field27]
field147.next_fields = [field115, field148]
field148.next_fields = [field147, field149]
field149.next_fields = [field148, field150]
field150.next_fields = [field149, field151]
field151.next_fields = [field150, field152]
field152.next_fields = [field151, field153]
field153.next_fields = [field152, field154]
field154.next_fields = [field153, field155, field167]
field155.next_fields = [field154, field156]
field156.next_fields = [field155, field157]
field157.next_fields = [field156, field158]
field158.next_fields = [field157, field159, field168, field173]
field159.next_fields = [field158, field160]
field160.next_fields = [field159, field161]
field161.next_fields = [field160, field162]
field162.next_fields = [field161, field163]
field163.next_fields = [field162, field164]
field164.next_fields = [field163, field131]
field165.next_fields = [field93, field166]
field166.next_fields = [field165, field167]
field167.next_fields = [field166, field154]
field168.next_fields = [field158, field169]
field169.next_fields = [field168, field170]
field170.next_fields = [field169, field171, field204]
field171.next_fields = [field170, field172]
field172.next_fields = [field171, field141]
field173.next_fields = [field158, field174]
field174.next_fields = [field173, field175, field194]
field175.next_fields = [field174, field176]
field176.next_fields = [field175, field177]
field177.next_fields = [field176, field178]
field178.next_fields = [field177, field179]
field179.next_fields = [field178, field180]
field180.next_fields = [field179, field181]
field181.next_fields = [field180, field182]
field182.next_fields = [field181, field183, field185]
field183.next_fields = [field182, field184]
field184.next_fields = [field183]
field185.next_fields = [field182, field186]
field186.next_fields = [field185, field187]
field187.next_fields = [field186, field188, field199]
field188.next_fields = [field187, field189]
field189.next_fields = [field188, field190, field216]
field190.next_fields = [field189, field191]
field191.next_fields = [field190, field192]
field192.next_fields = [field191, field193, field200]
field193.next_fields = [field192, field73]
field194.next_fields = [field174, field195]
field195.next_fields = [field194, field196]
field196.next_fields = [field195, field197]
field197.next_fields = [field196, field198]
field198.next_fields = [field197, field199]
field199.next_fields = [field198, field187]
field200.next_fields = [field192, field201]
field201.next_fields = [field200, field202]
field202.next_fields = [field201, field203]
field203.next_fields = [field202, field54]
field204.next_fields = [field170, field205]
field205.next_fields = [field204, field206]
field206.next_fields = [field205, field207]
field207.next_fields = [field206, field208]
field208.next_fields = [field207, field209, field224]
field209.next_fields = [field208, field210, field212]
field210.next_fields = [field209, field211]
field211.next_fields = [field210, field29]
field212.next_fields = [field209, field213]
field213.next_fields = [field212, field214]
field214.next_fields = [field213, field215]
field215.next_fields = [field214, field39]
field216.next_fields = [field189, field217]
field217.next_fields = [field216, field218]
field218.next_fields = [field217, field219]
field219.next_fields = [field218, field220]
field220.next_fields = [field219, field221, field225, field226]
field221.next_fields = [field220, field222]
field222.next_fields = [field221, field223]
field223.next_fields = [field222]
field224.next_fields = [field208, field225]
field225.next_fields = [field224, field220]
field226.next_fields = [field220, field227]
field227.next_fields = [field226, field228]
field228.next_fields = [field227, field49]
field229.next_fields = [field88, field230]
field230.next_fields = [field229, field231]
field231.next_fields = [field230, field232]
field232.next_fields = [field231, field233]
field233.next_fields = [field232, field234]
field234.next_fields = [field233, field235]
field235.next_fields = [field234, field236]
field236.next_fields = [field235, field237]
field237.next_fields = [field236, field238]
field238.next_fields = [field237, field76]