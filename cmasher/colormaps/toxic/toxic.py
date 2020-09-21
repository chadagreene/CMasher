# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"

# Package declaration
__package__ = 'cmasher'


# %% GLOBALS AND DEFINITIONS
# Type of this colormap
cm_type = 'sequential'

# RGB-values of this colormap
cm_data = [[0.00000000, 0.00000000, 0.00000000],
           [0.00021919, 0.00017738, 0.00025640],
           [0.00076896, 0.00060812, 0.00092866],
           [0.00160931, 0.00124648, 0.00200351],
           [0.00272383, 0.00207079, 0.00349008],
           [0.00410240, 0.00306677, 0.00540349],
           [0.00573772, 0.00422381, 0.00776200],
           [0.00762399, 0.00553359, 0.01058584],
           [0.00975629, 0.00698924, 0.01389684],
           [0.01213021, 0.00858496, 0.01771836],
           [0.01474165, 0.01031573, 0.02207488],
           [0.01758664, 0.01217717, 0.02699213],
           [0.02066129, 0.01416537, 0.03249706],
           [0.02396169, 0.01627681, 0.03861805],
           [0.02748381, 0.01850834, 0.04513914],
           [0.03122350, 0.02085710, 0.05167956],
           [0.03517643, 0.02332047, 0.05825140],
           [0.03933804, 0.02589607, 0.06485967],
           [0.04357683, 0.02858173, 0.07150882],
           [0.04774246, 0.03137546, 0.07820284],
           [0.05184652, 0.03427550, 0.08494531],
           [0.05589043, 0.03728026, 0.09173945],
           [0.05987518, 0.04038835, 0.09858821],
           [0.06380141, 0.04347816, 0.10549426],
           [0.06766941, 0.04652830, 0.11246002],
           [0.07147914, 0.04954228, 0.11948764],
           [0.07523026, 0.05252246, 0.12657944],
           [0.07892209, 0.05547124, 0.13373712],
           [0.08255360, 0.05839101, 0.14096191],
           [0.08612349, 0.06128398, 0.14825578],
           [0.08963006, 0.06415261, 0.15561935],
           [0.09307128, 0.06699927, 0.16305391],
           [0.09644471, 0.06982659, 0.17055942],
           [0.09974746, 0.07263707, 0.17813719],
           [0.10297622, 0.07543371, 0.18578627],
           [0.10612712, 0.07821961, 0.19350623],
           [0.10919575, 0.08099812, 0.20129608],
           [0.11217702, 0.08377298, 0.20915415],
           [0.11506515, 0.08654834, 0.21707793],
           [0.11785356, 0.08932889, 0.22506389],
           [0.12053468, 0.09211976, 0.23310813],
           [0.12310000, 0.09492694, 0.24120452],
           [0.12553979, 0.09775708, 0.24934595],
           [0.12784309, 0.10061786, 0.25752278],
           [0.12999741, 0.10351790, 0.26572370],
           [0.13198869, 0.10646703, 0.27393420],
           [0.13380132, 0.10947643, 0.28213598],
           [0.13541800, 0.11255863, 0.29030642],
           [0.13681950, 0.11572749, 0.29841890],
           [0.13798571, 0.11899831, 0.30643958],
           [0.13889563, 0.12238729, 0.31432859],
           [0.13952863, 0.12591107, 0.32203906],
           [0.13986561, 0.12958571, 0.32951799],
           [0.13989230, 0.13342530, 0.33670574],
           [0.13960042, 0.13744012, 0.34354116],
           [0.13899107, 0.14163478, 0.34996459],
           [0.13807666, 0.14600650, 0.35592376],
           [0.13688113, 0.15054446, 0.36137976],
           [0.13543870, 0.15523031, 0.36631131],
           [0.13379086, 0.16004001, 0.37071651],
           [0.13198234, 0.16494642, 0.37461143],
           [0.13005804, 0.16992188, 0.37802641],
           [0.12805913, 0.17494065, 0.38100128],
           [0.12602301, 0.17997986, 0.38358068],
           [0.12398152, 0.18502046, 0.38581040],
           [0.12196071, 0.19004743, 0.38773450],
           [0.11998242, 0.19504906, 0.38939398],
           [0.11806439, 0.20001669, 0.39082594],
           [0.11622142, 0.20494404, 0.39206356],
           [0.11446495, 0.20982699, 0.39313586],
           [0.11280358, 0.21466317, 0.39406788],
           [0.11124498, 0.21945113, 0.39488180],
           [0.10979390, 0.22419074, 0.39559620],
           [0.10845574, 0.22888195, 0.39622823],
           [0.10723217, 0.23352600, 0.39679141],
           [0.10612488, 0.23812416, 0.39729795],
           [0.10513489, 0.24267787, 0.39775861],
           [0.10426193, 0.24718892, 0.39818247],
           [0.10350392, 0.25165945, 0.39857674],
           [0.10286002, 0.25609113, 0.39894888],
           [0.10232628, 0.26048635, 0.39930380],
           [0.10190091, 0.26484673, 0.39964753],
           [0.10157861, 0.26917466, 0.39998341],
           [0.10135508, 0.27347213, 0.40031518],
           [0.10122541, 0.27774108, 0.40064596],
           [0.10118418, 0.28198348, 0.40097836],
           [0.10122553, 0.28620125, 0.40131446],
           [0.10134322, 0.29039626, 0.40165595],
           [0.10153075, 0.29457037, 0.40200411],
           [0.10178135, 0.29872536, 0.40235992],
           [0.10208812, 0.30286298, 0.40272402],
           [0.10244481, 0.30698475, 0.40309739],
           [0.10284399, 0.31109237, 0.40347991],
           [0.10327822, 0.31518751, 0.40387123],
           [0.10374182, 0.31927140, 0.40427210],
           [0.10422656, 0.32334577, 0.40468111],
           [0.10472674, 0.32741180, 0.40509851],
           [0.10523468, 0.33147102, 0.40552279],
           [0.10574510, 0.33552448, 0.40595398],
           [0.10625047, 0.33957366, 0.40639017],
           [0.10674537, 0.34361958, 0.40683072],
           [0.10722377, 0.34766339, 0.40727428],
           [0.10767949, 0.35170624, 0.40771914],
           [0.10810727, 0.35574910, 0.40816396],
           [0.10850226, 0.35979284, 0.40860744],
           [0.10885879, 0.36383850, 0.40904744],
           [0.10917209, 0.36788691, 0.40948222],
           [0.10943758, 0.37193887, 0.40990992],
           [0.10965093, 0.37599513, 0.41032864],
           [0.10980836, 0.38005632, 0.41073660],
           [0.10990563, 0.38412313, 0.41113153],
           [0.10993904, 0.38819616, 0.41151133],
           [0.10990517, 0.39227594, 0.41187388],
           [0.10980078, 0.39636296, 0.41221702],
           [0.10962288, 0.40045764, 0.41253859],
           [0.10936866, 0.40456037, 0.41283639],
           [0.10903552, 0.40867148, 0.41310823],
           [0.10862105, 0.41279126, 0.41335191],
           [0.10812304, 0.41691995, 0.41356525],
           [0.10753945, 0.42105773, 0.41374607],
           [0.10686841, 0.42520478, 0.41389220],
           [0.10610825, 0.42936118, 0.41400153],
           [0.10525742, 0.43352702, 0.41407193],
           [0.10431456, 0.43770232, 0.41410135],
           [0.10327866, 0.44188706, 0.41408785],
           [0.10214849, 0.44608122, 0.41402935],
           [0.10092305, 0.45028473, 0.41392388],
           [0.09960155, 0.45449750, 0.41376952],
           [0.09818331, 0.45871939, 0.41356440],
           [0.09666780, 0.46295026, 0.41330672],
           [0.09505462, 0.46718992, 0.41299469],
           [0.09334361, 0.47143817, 0.41262663],
           [0.09153477, 0.47569477, 0.41220093],
           [0.08962790, 0.47995950, 0.41171583],
           [0.08762319, 0.48423211, 0.41116976],
           [0.08552104, 0.48851232, 0.41056117],
           [0.08332203, 0.49279985, 0.40988855],
           [0.08102712, 0.49709438, 0.40915050],
           [0.07863734, 0.50139561, 0.40834555],
           [0.07615401, 0.50570323, 0.40747227],
           [0.07357896, 0.51001689, 0.40652929],
           [0.07091446, 0.51433627, 0.40551528],
           [0.06816340, 0.51866100, 0.40442893],
           [0.06532926, 0.52299074, 0.40326893],
           [0.06241641, 0.52732512, 0.40203398],
           [0.05943032, 0.53166379, 0.40072282],
           [0.05637778, 0.53600635, 0.39933420],
           [0.05326717, 0.54035244, 0.39786686],
           [0.05010861, 0.54470167, 0.39631945],
           [0.04691527, 0.54905366, 0.39469079],
           [0.04370324, 0.55340800, 0.39297962],
           [0.04049251, 0.55776429, 0.39118466],
           [0.03732758, 0.56212213, 0.38930462],
           [0.03436328, 0.56648111, 0.38733806],
           [0.03162373, 0.57084082, 0.38528362],
           [0.02913353, 0.57520082, 0.38314000],
           [0.02691783, 0.57956067, 0.38090581],
           [0.02500275, 0.58391993, 0.37857956],
           [0.02341539, 0.58827816, 0.37615975],
           [0.02218389, 0.59263488, 0.37364479],
           [0.02133729, 0.59698964, 0.37103295],
           [0.02090583, 0.60134198, 0.36832241],
           [0.02092167, 0.60569136, 0.36551156],
           [0.02141786, 0.61003727, 0.36259853],
           [0.02242889, 0.61437920, 0.35958134],
           [0.02399079, 0.61871658, 0.35645790],
           [0.02614124, 0.62304886, 0.35322603],
           [0.02891968, 0.62737545, 0.34988339],
           [0.03236745, 0.63169574, 0.34642754],
           [0.03652797, 0.63600907, 0.34285586],
           [0.04142314, 0.64031480, 0.33916559],
           [0.04676428, 0.64461220, 0.33535378],
           [0.05245640, 0.64890055, 0.33141730],
           [0.05846070, 0.65317905, 0.32735282],
           [0.06474496, 0.65744690, 0.32315657],
           [0.07128286, 0.66170327, 0.31882407],
           [0.07805400, 0.66594717, 0.31435186],
           [0.08504197, 0.67017760, 0.30973557],
           [0.09223413, 0.67439352, 0.30497053],
           [0.09962094, 0.67859382, 0.30005046],
           [0.10719583, 0.68277729, 0.29496970],
           [0.11495440, 0.68694255, 0.28972355],
           [0.12289438, 0.69108825, 0.28430336],
           [0.13101515, 0.69521280, 0.27870279],
           [0.13931769, 0.69931452, 0.27291388],
           [0.14780462, 0.70339158, 0.26692724],
           [0.15647987, 0.70744194, 0.26073327],
           [0.16534811, 0.71146337, 0.25432315],
           [0.17441719, 0.71545342, 0.24768165],
           [0.18369431, 0.71940933, 0.24079846],
           [0.19318886, 0.72332804, 0.23365958],
           [0.20291198, 0.72720612, 0.22624922],
           [0.21287640, 0.73103971, 0.21855038],
           [0.22309648, 0.73482446, 0.21054490],
           [0.23358823, 0.73855542, 0.20221375],
           [0.24437119, 0.74222692, 0.19353389],
           [0.25546570, 0.74583253, 0.18448442],
           [0.26689443, 0.74936490, 0.17504465],
           [0.27868216, 0.75281565, 0.16519620],
           [0.29085725, 0.75617505, 0.15492332],
           [0.30344826, 0.75943220, 0.14422336],
           [0.31648159, 0.76257503, 0.13311818],
           [0.32997771, 0.76559080, 0.12167266],
           [0.34395332, 0.76846588, 0.11001182],
           [0.35839862, 0.77118878, 0.09839083],
           [0.37327650, 0.77375138, 0.08724270],
           [0.38850526, 0.77615284, 0.07725599],
           [0.40395292, 0.77840295, 0.06938992],
           [0.41944119, 0.78052427, 0.06473030],
           [0.43477585, 0.78254937, 0.06409972],
           [0.44977785, 0.78451593, 0.06764048],
           [0.46431715, 0.78645901, 0.07475662],
           [0.47831864, 0.78840714, 0.08448216],
           [0.49176080, 0.79037960, 0.09588826],
           [0.50465158, 0.79238932, 0.10826766],
           [0.51702182, 0.79444304, 0.12114762],
           [0.52891244, 0.79654352, 0.13423414],
           [0.54036553, 0.79869148, 0.14735063],
           [0.55142076, 0.80088662, 0.16039351],
           [0.56211741, 0.80312725, 0.17330769],
           [0.57249138, 0.80541120, 0.18606628],
           [0.58257846, 0.80773509, 0.19866405],
           [0.59239777, 0.81009935, 0.21108764],
           [0.60198087, 0.81249995, 0.22335058],
           [0.61134812, 0.81493537, 0.23545816],
           [0.62051811, 0.81740406, 0.24741809],
           [0.62950804, 0.81990436, 0.25923983],
           [0.63833376, 0.82243455, 0.27093381],
           [0.64700982, 0.82499292, 0.28251092],
           [0.65554293, 0.82758007, 0.29397086],
           [0.66395021, 0.83019272, 0.30533222],
           [0.67223796, 0.83283107, 0.31659675],
           [0.68041720, 0.83549339, 0.32777532],
           [0.68849224, 0.83818019, 0.33886785],
           [0.69647457, 0.84088912, 0.34988797],
           [0.70436906, 0.84362014, 0.36083807],
           [0.71217877, 0.84637379, 0.37171749],
           [0.71991237, 0.84914828, 0.38253679],
           [0.72757442, 0.85194329, 0.39329924],
           [0.73516924, 0.85475850, 0.40400805],
           [0.74270088, 0.85759359, 0.41466630],
           [0.75017319, 0.86044826, 0.42527694],
           [0.75758977, 0.86332219, 0.43584282],
           [0.76495404, 0.86621509, 0.44636669],
           [0.77226924, 0.86912668, 0.45685117],
           [0.77953840, 0.87205668, 0.46729879],
           [0.78676327, 0.87500535, 0.47770945],
           [0.79394549, 0.87797296, 0.48808296],
           [0.80108952, 0.88095841, 0.49842559],
           [0.80819782, 0.88396148, 0.50873950],
           [0.81527094, 0.88698280, 0.51902261],
           [0.82230991, 0.89002279, 0.52927401],
           [0.82931959, 0.89307990, 0.53950184],
           [0.83629942, 0.89615525, 0.54970182],
           [0.84325086, 0.89924894, 0.55987438],
           [0.85017860, 0.90235935, 0.57002798]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.toxic', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
