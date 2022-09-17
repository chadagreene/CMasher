# %% IMPORTS
# Package imports
from cmasher.utils import _register_cmap as register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"

# Package declaration
__package__ = 'cmasher'


# %% GLOBALS AND DEFINITIONS
# Type of this colormap
cm_type = 'diverging'

# RGB-values of this colormap
cm_data = [[0.12434357, 0.00588452, 0.21400096],
           [0.12931129, 0.00675787, 0.22011754],
           [0.13427605, 0.00761301, 0.22627813],
           [0.13923743, 0.00844618, 0.23248445],
           [0.14419489, 0.00925374, 0.23873832],
           [0.14914773, 0.01003226, 0.24504157],
           [0.15409628, 0.01077599, 0.25139847],
           [0.15903865, 0.01148361, 0.25780936],
           [0.16397490, 0.01214941, 0.26427895],
           [0.16890307, 0.01277188, 0.27080848],
           [0.17382209, 0.01334730, 0.27740161],
           [0.17873060, 0.01387220, 0.28406219],
           [0.18362636, 0.01434494, 0.29079310],
           [0.18850717, 0.01476335, 0.29759833],
           [0.19336978, 0.01512770, 0.30448066],
           [0.19821038, 0.01543943, 0.31144297],
           [0.20302543, 0.01569841, 0.31849056],
           [0.20780909, 0.01591090, 0.32562507],
           [0.21255503, 0.01608416, 0.33284912],
           [0.21725536, 0.01622978, 0.34016407],
           [0.22190089, 0.01636307, 0.34757095],
           [0.22647956, 0.01650931, 0.35506605],
           [0.23097774, 0.01669935, 0.36264494],
           [0.23537868, 0.01697681, 0.37029727],
           [0.23966261, 0.01740014, 0.37800537],
           [0.24380764, 0.01804107, 0.38574545],
           [0.24778982, 0.01898922, 0.39348282],
           [0.25158529, 0.02034719, 0.40117401],
           [0.25517266, 0.02222479, 0.40876847],
           [0.25853565, 0.02473093, 0.41621127],
           [0.26166567, 0.02795975, 0.42345155],
           [0.26456273, 0.03198252, 0.43044714],
           [0.26723479, 0.03684228, 0.43716929],
           [0.26969569, 0.04248896, 0.44360388],
           [0.27196284, 0.04848981, 0.44974895],
           [0.27405475, 0.05471025, 0.45561291],
           [0.27598966, 0.06106965, 0.46121003],
           [0.27778467, 0.06750507, 0.46655789],
           [0.27945476, 0.07396949, 0.47167607],
           [0.28101352, 0.08042854, 0.47658345],
           [0.28247268, 0.08685793, 0.48129838],
           [0.28384236, 0.09324093, 0.48583798],
           [0.28513137, 0.09956639, 0.49021794],
           [0.28634701, 0.10582750, 0.49445266],
           [0.28749631, 0.11201977, 0.49855477],
           [0.28858462, 0.11814153, 0.50253603],
           [0.28961712, 0.12419213, 0.50640676],
           [0.29059833, 0.13017201, 0.51017629],
           [0.29153215, 0.13608239, 0.51385302],
           [0.29242208, 0.14192500, 0.51744454],
           [0.29327113, 0.14770193, 0.52095768],
           [0.29408197, 0.15341549, 0.52439862],
           [0.29485717, 0.15906795, 0.52777294],
           [0.29559924, 0.16466147, 0.53108570],
           [0.29630976, 0.17019880, 0.53434154],
           [0.29699110, 0.17568189, 0.53754465],
           [0.29764460, 0.18111329, 0.54069888],
           [0.29827178, 0.18649525, 0.54380773],
           [0.29887444, 0.19182963, 0.54687447],
           [0.29945363, 0.19711869, 0.54990205],
           [0.30001054, 0.20236443, 0.55289318],
           [0.30054631, 0.20756873, 0.55585038],
           [0.30106201, 0.21273339, 0.55877600],
           [0.30155859, 0.21786013, 0.56167217],
           [0.30203696, 0.22295063, 0.56454090],
           [0.30249793, 0.22800646, 0.56738403],
           [0.30294227, 0.23302915, 0.57020328],
           [0.30337068, 0.23802016, 0.57300024],
           [0.30378382, 0.24298087, 0.57577639],
           [0.30418229, 0.24791260, 0.57853310],
           [0.30456679, 0.25281657, 0.58127171],
           [0.30493787, 0.25769398, 0.58399340],
           [0.30529589, 0.26254606, 0.58669927],
           [0.30564131, 0.26737393, 0.58939035],
           [0.30597473, 0.27217857, 0.59206767],
           [0.30629654, 0.27696100, 0.59473213],
           [0.30660696, 0.28172230, 0.59738453],
           [0.30690651, 0.28646330, 0.60002572],
           [0.30719552, 0.29118493, 0.60265644],
           [0.30747413, 0.29588812, 0.60527731],
           [0.30774293, 0.30057358, 0.60788908],
           [0.30800193, 0.30524222, 0.61049227],
           [0.30825149, 0.30989477, 0.61308745],
           [0.30849187, 0.31453196, 0.61567516],
           [0.30872319, 0.31915455, 0.61825584],
           [0.30894582, 0.32376318, 0.62082997],
           [0.30915975, 0.32835858, 0.62339790],
           [0.30936539, 0.33294131, 0.62596007],
           [0.30956268, 0.33751209, 0.62851674],
           [0.30975200, 0.34207144, 0.63106829],
           [0.30993331, 0.34662001, 0.63361494],
           [0.31010692, 0.35115830, 0.63615698],
           [0.31027282, 0.35568691, 0.63869459],
           [0.31043127, 0.36020633, 0.64122798],
           [0.31058231, 0.36471711, 0.64375731],
           [0.31072612, 0.36921970, 0.64628271],
           [0.31086280, 0.37371461, 0.64880430],
           [0.31099249, 0.37820230, 0.65132216],
           [0.31111533, 0.38268321, 0.65383636],
           [0.31123142, 0.38715778, 0.65634691],
           [0.31134094, 0.39162643, 0.65885384],
           [0.31144402, 0.39608958, 0.66135714],
           [0.31154081, 0.40054761, 0.66385675],
           [0.31163148, 0.40500090, 0.66635262],
           [0.31171621, 0.40944984, 0.66884467],
           [0.31179520, 0.41389476, 0.67133278],
           [0.31186865, 0.41833603, 0.67381681],
           [0.31193680, 0.42277397, 0.67629662],
           [0.31199992, 0.42720890, 0.67877201],
           [0.31205825, 0.43164113, 0.68124278],
           [0.31211216, 0.43607095, 0.68370870],
           [0.31216189, 0.44049867, 0.68616949],
           [0.31220796, 0.44492453, 0.68862492],
           [0.31225061, 0.44934882, 0.69107462],
           [0.31229048, 0.45377175, 0.69351832],
           [0.31232786, 0.45819361, 0.69595559],
           [0.31236353, 0.46261456, 0.69838612],
           [0.31239787, 0.46703487, 0.70080943],
           [0.31243174, 0.47145469, 0.70322513],
           [0.31246573, 0.47587424, 0.70563272],
           [0.31250071, 0.48029366, 0.70803171],
           [0.31253759, 0.48471311, 0.71042159],
           [0.31257717, 0.48913278, 0.71280175],
           [0.31262078, 0.49355270, 0.71517170],
           [0.31266920, 0.49797308, 0.71753069],
           [0.31272396, 0.50239396, 0.71987816],
           [0.31278644, 0.50681539, 0.72221344],
           [0.31285779, 0.51123752, 0.72453568],
           [0.31293998, 0.51566030, 0.72684425],
           [0.31303476, 0.52008375, 0.72913836],
           [0.31314366, 0.52450796, 0.73141704],
           [0.31326906, 0.52893282, 0.73367953],
           [0.31341322, 0.53335830, 0.73592494],
           [0.31357856, 0.53778430, 0.73815229],
           [0.31376746, 0.54221081, 0.74036052],
           [0.31398291, 0.54663764, 0.74254862],
           [0.31422803, 0.55106464, 0.74471556],
           [0.31450612, 0.55549161, 0.74686019],
           [0.31482075, 0.55991833, 0.74898134],
           [0.31517574, 0.56434455, 0.75107779],
           [0.31557523, 0.56876997, 0.75314825],
           [0.31602366, 0.57319425, 0.75519142],
           [0.31652582, 0.57761700, 0.75720593],
           [0.31708684, 0.58203779, 0.75919038],
           [0.31771222, 0.58645611, 0.76114332],
           [0.31840787, 0.59087143, 0.76306326],
           [0.31918007, 0.59528313, 0.76494869],
           [0.32003532, 0.59969060, 0.76679791],
           [0.32098080, 0.60409308, 0.76860934],
           [0.32202424, 0.60848970, 0.77038148],
           [0.32317357, 0.61287960, 0.77211265],
           [0.32443695, 0.61726187, 0.77380097],
           [0.32582371, 0.62163533, 0.77544516],
           [0.32734269, 0.62599895, 0.77704320],
           [0.32900405, 0.63035134, 0.77859393],
           [0.33081742, 0.63469128, 0.78009540],
           [0.33279358, 0.63901718, 0.78154661],
           [0.33494302, 0.64332754, 0.78294608],
           [0.33727653, 0.64762069, 0.78429266],
           [0.33980514, 0.65189480, 0.78558566],
           [0.34253965, 0.65614801, 0.78682444],
           [0.34549065, 0.66037837, 0.78800872],
           [0.34866835, 0.66458383, 0.78913863],
           [0.35208231, 0.66876231, 0.79021477],
           [0.35574127, 0.67291169, 0.79123827],
           [0.35965281, 0.67702987, 0.79221088],
           [0.36382312, 0.68111477, 0.79313499],
           [0.36825671, 0.68516444, 0.79401368],
           [0.37295618, 0.68917704, 0.79485074],
           [0.37792196, 0.69315094, 0.79565068],
           [0.38315216, 0.69708476, 0.79641869],
           [0.38864250, 0.70097742, 0.79716057],
           [0.39438623, 0.70482817, 0.79788271],
           [0.40037420, 0.70863664, 0.79859195],
           [0.40659514, 0.71240286, 0.79929533],
           [0.41303585, 0.71612724, 0.80000005],
           [0.41968153, 0.71981060, 0.80071327],
           [0.42651620, 0.72345411, 0.80144199],
           [0.43352311, 0.72705927, 0.80219282],
           [0.44068514, 0.73062784, 0.80297193],
           [0.44798499, 0.73416184, 0.80378517],
           [0.45540582, 0.73766347, 0.80463763],
           [0.46293189, 0.74113497, 0.80553339],
           [0.47054756, 0.74457873, 0.80647656],
           [0.47823856, 0.74799715, 0.80747031],
           [0.48599174, 0.75139259, 0.80851720],
           [0.49379555, 0.75476731, 0.80961897],
           [0.50163802, 0.75812375, 0.81077799],
           [0.50951018, 0.76146396, 0.81199484],
           [0.51740343, 0.76479002, 0.81327029],
           [0.52531010, 0.76810393, 0.81460481],
           [0.53322356, 0.77140754, 0.81599852],
           [0.54113819, 0.77470259, 0.81745128],
           [0.54904863, 0.77799078, 0.81896303],
           [0.55695031, 0.78127373, 0.82053353],
           [0.56484078, 0.78455267, 0.82216148],
           [0.57271595, 0.78782912, 0.82384685],
           [0.58057376, 0.79110425, 0.82558859],
           [0.58841174, 0.79437931, 0.82738612],
           [0.59622922, 0.79765517, 0.82923797],
           [0.60402262, 0.80093330, 0.83114456],
           [0.61179265, 0.80421427, 0.83310394],
           [0.61953824, 0.80749903, 0.83511535],
           [0.62725857, 0.81078844, 0.83717801],
           [0.63495307, 0.81408331, 0.83929113],
           [0.64262139, 0.81738440, 0.84145388],
           [0.65026337, 0.82069239, 0.84366540],
           [0.65787900, 0.82400793, 0.84592486],
           [0.66546844, 0.82733162, 0.84823141],
           [0.67303197, 0.83066400, 0.85058419],
           [0.68056996, 0.83400559, 0.85298238],
           [0.68808289, 0.83735685, 0.85542516],
           [0.69557018, 0.84071852, 0.85791228],
           [0.70303254, 0.84409099, 0.86044288],
           [0.71047142, 0.84747442, 0.86301580],
           [0.71788585, 0.85086963, 0.86563112],
           [0.72527708, 0.85427682, 0.86828781],
           [0.73264583, 0.85769631, 0.87098521],
           [0.73999166, 0.86112874, 0.87372319],
           [0.74731621, 0.86457417, 0.87650067],
           [0.75461912, 0.86803319, 0.87931756],
           [0.76190122, 0.87150605, 0.88217322],
           [0.76916383, 0.87499286, 0.88506677],
           [0.77640537, 0.87849452, 0.88799879],
           [0.78362842, 0.88201078, 0.89096784],
           [0.79083329, 0.88554198, 0.89397361],
           [0.79801871, 0.88908894, 0.89701653],
           [0.80518675, 0.89265150, 0.90009549],
           [0.81233783, 0.89622995, 0.90321016],
           [0.81947230, 0.89982462, 0.90636025],
           [0.82659011, 0.90343594, 0.90954568],
           [0.83369156, 0.90706423, 0.91276619],
           [0.84077761, 0.91070961, 0.91602124],
           [0.84784862, 0.91437236, 0.91931059],
           [0.85490492, 0.91805279, 0.92263401],
           [0.86194682, 0.92175119, 0.92599126],
           [0.86897464, 0.92546784, 0.92938214],
           [0.87598869, 0.92920304, 0.93280643],
           [0.88298922, 0.93295708, 0.93626395],
           [0.88997650, 0.93673027, 0.93975451],
           [0.89695077, 0.94052289, 0.94327794],
           [0.90391222, 0.94433526, 0.94683409],
           [0.91086103, 0.94816769, 0.95042279],
           [0.91779733, 0.95202051, 0.95404393],
           [0.92472121, 0.95589406, 0.95769737],
           [0.93163272, 0.95978870, 0.96138299],
           [0.93853161, 0.96370486, 0.96510081],
           [0.94541738, 0.96764310, 0.96885089],
           [0.95229045, 0.97160364, 0.97263292],
           [0.95915055, 0.97558695, 0.97644685],
           [0.96599731, 0.97959353, 0.98029261],
           [0.97283020, 0.98362395, 0.98417016],
           [0.97964739, 0.98767922, 0.98807995],
           [0.98644895, 0.99175974, 0.99202153],
           [0.99323371, 0.99586633, 0.99599488],
           [1.00000000, 1.00000000, 1.00000000],
           [0.99382469, 0.99580955, 0.99432110],
           [0.98760164, 0.99166330, 0.98862986],
           [0.98133740, 0.98755931, 0.98291625],
           [0.97503997, 0.98349458, 0.97717497],
           [0.96871626, 0.97946629, 0.97140333],
           [0.96237164, 0.97547209, 0.96560034],
           [0.95601185, 0.97150923, 0.95976730],
           [0.94963976, 0.96757616, 0.95390497],
           [0.94325909, 0.96367088, 0.94801568],
           [0.93687235, 0.95979187, 0.94210153],
           [0.93048036, 0.95593835, 0.93616375],
           [0.92408561, 0.95210878, 0.93020504],
           [0.91768886, 0.94830240, 0.92422693],
           [0.91129032, 0.94451872, 0.91823051],
           [0.90489147, 0.94075664, 0.91221790],
           [0.89849256, 0.93701566, 0.90619023],
           [0.89209319, 0.93329557, 0.90014800],
           [0.88569452, 0.92959547, 0.89409297],
           [0.87929669, 0.92591493, 0.88802599],
           [0.87289905, 0.92225388, 0.88194719],
           [0.86650216, 0.91861170, 0.87585767],
           [0.86010629, 0.91498793, 0.86975822],
           [0.85371140, 0.91138223, 0.86364935],
           [0.84731670, 0.90779464, 0.85753082],
           [0.84092280, 0.90422454, 0.85140359],
           [0.83452970, 0.90067160, 0.84526808],
           [0.82813733, 0.89713553, 0.83912458],
           [0.82174544, 0.89361612, 0.83297320],
           [0.81535347, 0.89011330, 0.82681372],
           [0.80896190, 0.88662654, 0.82064685],
           [0.80257057, 0.88315559, 0.81447273],
           [0.79617936, 0.87970020, 0.80829144],
           [0.78978811, 0.87626012, 0.80210307],
           [0.78339667, 0.87283512, 0.79590767],
           [0.77700472, 0.86942502, 0.78970513],
           [0.77061205, 0.86602960, 0.78349540],
           [0.76421875, 0.86264852, 0.77727873],
           [0.75782467, 0.85928154, 0.77105510],
           [0.75142964, 0.85592843, 0.76482449],
           [0.74503349, 0.85258894, 0.75858685],
           [0.73863604, 0.84926286, 0.75234213],
           [0.73223714, 0.84594994, 0.74609027],
           [0.72583661, 0.84264994, 0.73983119],
           [0.71943428, 0.83936264, 0.73356480],
           [0.71302998, 0.83608780, 0.72729102],
           [0.70662354, 0.83282518, 0.72100975],
           [0.70021479, 0.82957454, 0.71472089],
           [0.69380357, 0.82633564, 0.70842432],
           [0.68738971, 0.82310825, 0.70211992],
           [0.68097304, 0.81989211, 0.69580759],
           [0.67455294, 0.81668717, 0.68948672],
           [0.66812958, 0.81349304, 0.68315752],
           [0.66170286, 0.81030946, 0.67681990],
           [0.65527262, 0.80713617, 0.67047373],
           [0.64883872, 0.80397291, 0.66411886],
           [0.64240101, 0.80081943, 0.65775515],
           [0.63595841, 0.79767582, 0.65138150],
           [0.62951158, 0.79454151, 0.64499858],
           [0.62306045, 0.79141621, 0.63860627],
           [0.61660476, 0.78829970, 0.63220428],
           [0.61014331, 0.78519209, 0.62579136],
           [0.60367711, 0.78209270, 0.61936849],
           [0.59720594, 0.77900127, 0.61293539],
           [0.59072831, 0.77591802, 0.60649044],
           [0.58424556, 0.77284215, 0.60003495],
           [0.57775664, 0.76977369, 0.59356774],
           [0.57126149, 0.76671233, 0.58708865],
           [0.56476033, 0.76365767, 0.58059777],
           [0.55825218, 0.76060971, 0.57409393],
           [0.55173780, 0.75756786, 0.56757778],
           [0.54521614, 0.75453214, 0.56104804],
           [0.53868762, 0.75150206, 0.55450494],
           [0.53215208, 0.74847735, 0.54794811],
           [0.52560864, 0.74545795, 0.54137634],
           [0.51905823, 0.74244322, 0.53479036],
           [0.51250000, 0.73943309, 0.52818895],
           [0.50593365, 0.73642732, 0.52157144],
           [0.49935973, 0.73342539, 0.51493803],
           [0.49277805, 0.73042701, 0.50828809],
           [0.48618824, 0.72743197, 0.50162076],
           [0.47958991, 0.72444003, 0.49493507],
           [0.47298359, 0.72145070, 0.48823100],
           [0.46636921, 0.71846366, 0.48150783],
           [0.45974679, 0.71547856, 0.47476485],
           [0.45311640, 0.71249506, 0.46800133],
           [0.44647816, 0.70951278, 0.46121648],
           [0.43983228, 0.70653133, 0.45440955],
           [0.43317907, 0.70355031, 0.44757974],
           [0.42651828, 0.70056948, 0.44072551],
           [0.41985059, 0.69758833, 0.43384622],
           [0.41317687, 0.69460632, 0.42694128],
           [0.40649778, 0.69162299, 0.42000968],
           [0.39981272, 0.68863823, 0.41304872],
           [0.39312423, 0.68565110, 0.40605913],
           [0.38643180, 0.68266150, 0.39903778],
           [0.37973812, 0.67966850, 0.39198500],
           [0.37304275, 0.67667203, 0.38489700],
           [0.36634870, 0.67367115, 0.37777377],
           [0.35965765, 0.67066532, 0.37061319],
           [0.35297165, 0.66765394, 0.36341301],
           [0.34629317, 0.66463637, 0.35617090],
           [0.33962524, 0.66161188, 0.34888442],
           [0.33297150, 0.65857969, 0.34155107],
           [0.32633633, 0.65553892, 0.33416823],
           [0.31972491, 0.65248860, 0.32673327],
           [0.31314248, 0.64942789, 0.31924201],
           [0.30659623, 0.64635564, 0.31169136],
           [0.30009369, 0.64327077, 0.30407659],
           [0.29364480, 0.64017187, 0.29639406],
           [0.28726040, 0.63705756, 0.28863847],
           [0.28095360, 0.63392625, 0.28080436],
           [0.27474016, 0.63077607, 0.27288617],
           [0.26863813, 0.62760506, 0.26487647],
           [0.26267002, 0.62441075, 0.25676914],
           [0.25686147, 0.62119053, 0.24855490],
           [0.25124393, 0.61794122, 0.24022510],
           [0.24585511, 0.61465902, 0.23177057],
           [0.24074014, 0.61133945, 0.22318124],
           [0.23595315, 0.60797718, 0.21444629],
           [0.23155932, 0.60456563, 0.20555579],
           [0.22763671, 0.60109683, 0.19649969],
           [0.22427864, 0.59756085, 0.18727215],
           [0.22159446, 0.59394541, 0.17787608],
           [0.21970884, 0.59023557, 0.16832692],
           [0.21875529, 0.58641365, 0.15866581],
           [0.21885793, 0.58246043, 0.14897700],
           [0.22009608, 0.57835850, 0.13940533],
           [0.22245044, 0.57409882, 0.13016467],
           [0.22576171, 0.56968811, 0.12150790],
           [0.22974550, 0.56515118, 0.11365853],
           [0.23407808, 0.56052386, 0.10674215],
           [0.23848634, 0.55584188, 0.10077283],
           [0.24278697, 0.55113355, 0.09568718],
           [0.24687702, 0.54641845, 0.09138767],
           [0.25070795, 0.54170912, 0.08777129],
           [0.25426366, 0.53701323, 0.08474270],
           [0.25754688, 0.53233510, 0.08221878],
           [0.26056796, 0.52767728, 0.08012845],
           [0.26334064, 0.52304119, 0.07841111],
           [0.26588045, 0.51842744, 0.07701528],
           [0.26820294, 0.51383615, 0.07589709],
           [0.27032300, 0.50926715, 0.07501892],
           [0.27225402, 0.50472022, 0.07434809],
           [0.27400849, 0.50019497, 0.07385633],
           [0.27559818, 0.49569090, 0.07351934],
           [0.27703238, 0.49120778, 0.07331473],
           [0.27832162, 0.48674492, 0.07322459],
           [0.27947412, 0.48230192, 0.07323212],
           [0.28049758, 0.47787835, 0.07332273],
           [0.28139919, 0.47347376, 0.07348371],
           [0.28218562, 0.46908766, 0.07370402],
           [0.28286261, 0.46471970, 0.07397352],
           [0.28343564, 0.46036946, 0.07428352],
           [0.28390985, 0.45603654, 0.07462643],
           [0.28429006, 0.45172052, 0.07499567],
           [0.28458007, 0.44742115, 0.07538470],
           [0.28478415, 0.44313801, 0.07578856],
           [0.28490602, 0.43887075, 0.07620262],
           [0.28494907, 0.43461906, 0.07662274],
           [0.28491652, 0.43038262, 0.07704527],
           [0.28481132, 0.42616112, 0.07746700],
           [0.28463599, 0.42195434, 0.07788471],
           [0.28439348, 0.41776190, 0.07829633],
           [0.28408628, 0.41358350, 0.07869974],
           [0.28371630, 0.40941900, 0.07909240],
           [0.28328605, 0.40526800, 0.07947311],
           [0.28279736, 0.40113032, 0.07984003],
           [0.28225231, 0.39700566, 0.08019202],
           [0.28165244, 0.39289384, 0.08052756],
           [0.28099980, 0.38879452, 0.08084604],
           [0.28029571, 0.38470756, 0.08114612],
           [0.27954177, 0.38063269, 0.08142708],
           [0.27873954, 0.37656965, 0.08168838],
           [0.27789035, 0.37251823, 0.08192932],
           [0.27699548, 0.36847822, 0.08214928],
           [0.27605604, 0.36444944, 0.08234761],
           [0.27507335, 0.36043163, 0.08252408],
           [0.27404853, 0.35642457, 0.08267831],
           [0.27298263, 0.35242806, 0.08280996],
           [0.27187665, 0.34844188, 0.08291875],
           [0.27073158, 0.34446585, 0.08300442],
           [0.26954834, 0.34049973, 0.08306678],
           [0.26832781, 0.33654334, 0.08310564],
           [0.26707080, 0.33259648, 0.08312079],
           [0.26577808, 0.32865896, 0.08311205],
           [0.26445049, 0.32473055, 0.08307943],
           [0.26308876, 0.32081105, 0.08302283],
           [0.26169362, 0.31690026, 0.08294219],
           [0.26026570, 0.31299798, 0.08283742],
           [0.25880553, 0.30910406, 0.08270826],
           [0.25731388, 0.30521825, 0.08255493],
           [0.25579133, 0.30134033, 0.08237742],
           [0.25423833, 0.29747015, 0.08217546],
           [0.25265547, 0.29360749, 0.08194916],
           [0.25104334, 0.28975212, 0.08169866],
           [0.24940226, 0.28590390, 0.08142361],
           [0.24773284, 0.28206257, 0.08112428],
           [0.24603549, 0.27822793, 0.08080061],
           [0.24431057, 0.27439981, 0.08045246],
           [0.24255862, 0.27057794, 0.08008011],
           [0.24077983, 0.26676218, 0.07968318],
           [0.23897479, 0.26295224, 0.07926209],
           [0.23714362, 0.25914798, 0.07881643],
           [0.23528689, 0.25534911, 0.07834662],
           [0.23340468, 0.25155548, 0.07785225],
           [0.23149749, 0.24776679, 0.07733371],
           [0.22956545, 0.24398289, 0.07679069],
           [0.22760892, 0.24020347, 0.07622341],
           [0.22562811, 0.23642835, 0.07563177],
           [0.22362324, 0.23265727, 0.07501578],
           [0.22159459, 0.22888997, 0.07437557],
           [0.21954224, 0.22512625, 0.07371087],
           [0.21746649, 0.22136579, 0.07302195],
           [0.21536746, 0.21760838, 0.07230872],
           [0.21324527, 0.21385374, 0.07157112],
           [0.21110013, 0.21010159, 0.07080928],
           [0.20893210, 0.20635167, 0.07002313],
           [0.20674127, 0.20260369, 0.06921265],
           [0.20452777, 0.19885735, 0.06837794],
           [0.20229165, 0.19511235, 0.06751901],
           [0.20003290, 0.19136842, 0.06663574],
           [0.19775160, 0.18762521, 0.06572831],
           [0.19544775, 0.18388240, 0.06479672],
           [0.19312130, 0.18013969, 0.06384095],
           [0.19077219, 0.17639672, 0.06286104],
           [0.18840038, 0.17265315, 0.06185709],
           [0.18600578, 0.16890862, 0.06082917],
           [0.18358823, 0.16516277, 0.05977729],
           [0.18114755, 0.16141524, 0.05870151],
           [0.17868358, 0.15766562, 0.05760198],
           [0.17619607, 0.15391353, 0.05647879],
           [0.17368476, 0.15015856, 0.05533204],
           [0.17114930, 0.14640032, 0.05416183],
           [0.16858932, 0.14263837, 0.05296828],
           [0.16600443, 0.13887229, 0.05175158],
           [0.16339415, 0.13510163, 0.05051188],
           [0.16075793, 0.13132595, 0.04924932],
           [0.15809517, 0.12754478, 0.04796409],
           [0.15540519, 0.12375769, 0.04665629],
           [0.15268725, 0.11996418, 0.04532612],
           [0.14994054, 0.11616378, 0.04397374],
           [0.14716414, 0.11235600, 0.04259926],
           [0.14435705, 0.10854034, 0.04120279],
           [0.14151819, 0.10471630, 0.03977633],
           [0.13864637, 0.10088335, 0.03834104],
           [0.13574030, 0.09704098, 0.03691515],
           [0.13279861, 0.09318862, 0.03549973],
           [0.12981983, 0.08932571, 0.03409578],
           [0.12680239, 0.08545164, 0.03270415],
           [0.12374463, 0.08156576, 0.03132562],
           [0.12064478, 0.07766739, 0.02996087],
           [0.11750102, 0.07375577, 0.02861046],
           [0.11431142, 0.06983006, 0.02727485],
           [0.11107399, 0.06588932, 0.02595442],
           [0.10778667, 0.06193249, 0.02464948]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.waterlily', N=511)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
