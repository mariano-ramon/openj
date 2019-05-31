import cProfile


from utils import calculate_distance

allpoints = [(29.917048,-90.103161,1),
(30.481936,-90.056539,2),
(29.948378,-90.072162,3),
(29.945513,-90.125303,4),
(29.947748,-90.130409,5),
(29.946603,-90.052116,6),
(29.948285,-90.071762,7),
(29.975471,-90.099094,8),
(29.956740,-90.066400,9),
(29.956740,-90.066400,10),
(29.955716,-90.068780,11),
(30.003969,-90.173947,12),
(29.975766,-90.098763,13),
(29.951844,-90.066435,14),
(29.978083,-90.048038,15),
(29.960458,-90.088372,16),
(29.938903,-90.068684,17),
(29.939027,-90.068728,18),
(29.963458,-90.050701,19),
(29.961669,-90.032227,20),
(29.961663,-90.067389,21),
(29.957365,-90.068093,22),
(29.971988,-90.091615,23),
(29.976209,-90.156595,24),
(29.929003,-90.097314,25),
(29.929003,-90.097314,26),
(29.982082,-90.067147,27),
(29.980509,-90.093602,28),
(30.005436,-90.177161,29),
(29.949822,-90.127839,30),
(29.954563,-90.069129,31),
(29.951276,-90.134816,32),
(29.956131,-90.066641,33),
(29.945678,-90.134748,34),
(29.920547,-90.103327,35),
(29.956643,-90.068057,36),
(29.983375,-90.105958,37),
(29.920845,-90.102600,38),
(29.965480,-90.062589,39),
(29.954489,-90.066357,40),
(29.962965,-90.039181,41),
(29.963084,-90.039171,42),
(29.979325,-90.152120,43),
(29.957464,-90.061881,44),
(29.960170,-90.059827,45),
(29.967048,-90.042701,46),
(29.951897,-90.073079,47),
(29.922204,-90.091899,48),
(29.955793,-90.068693,49),
(29.943928,-90.078735,50),
(29.958752,-90.061031,51),
(30.425732,-90.044318,52),
(29.954272,-90.066499,53),
(29.962254,-90.057967,54),
(29.943658,-90.071310,55),
(29.954936,-90.069020,56),
(30.012860,-90.160108,57),
(29.950621,-90.068031,58),
(29.960287,-90.064017,59),
(29.942142,-90.066974,60),
(29.942192,-90.067120,61),
(29.942185,-90.067008,62),
(29.928774,-90.084262,63),
(29.928784,-90.084219,64),
(29.928784,-90.084219,65),
(29.942380,-90.134363,66),
(30.477758,-90.096753,67),
(29.964712,-90.135511,68),
(29.924473,-90.108502,69),
(29.954026,-90.067925,70),
(29.960936,-90.061218,71),
(29.965146,-90.051450,72),
(29.951241,-90.070010,73),
(30.439373,-90.083723,74),
(29.934863,-90.109104,75),
(30.018746,-90.122708,76),
(29.948297,-90.130707,77),
(29.956920,-90.068477,78),
(30.475452,-90.095515,79),
(30.475440,-90.095512,80),
(29.947430,-90.071087,81),
(29.954345,-90.068733,82),
(29.929480,-90.077160,83),
(29.937881,-90.081385,84),
(29.917398,-90.112367,85),
(29.917493,-90.112341,86),
(30.035786,-89.914977,87),
(30.035795,-89.914910,88),
(30.035795,-89.914910,89),
(29.968136,-90.078423,90),
(29.942394,-90.078653,91),
(29.948297,-90.130707,92),
(29.969436,-90.052175,93),
(29.944616,-90.067286,94),
(29.956400,-90.067953,95),
(29.969436,-90.099126,96),
(29.955889,-90.063023,97),
(29.969181,-90.060339,98),
(29.964409,-90.110836,99),
(29.944059,-90.069797,100),
(29.954034,-90.071751,101),
(29.964050,-90.042554,102),
(29.964050,-90.042554,103),
(29.977562,-90.099593,104),
(29.959208,-90.065140,105),
(29.954920,-90.068931,106),
(29.890917,-90.017917,107),
(29.963457,-90.065437,108),
(29.968443,-90.057155,109),
(29.968443,-90.057155,110),
(29.968443,-90.057155,111),
(29.924545,-90.085393,112),
(29.962680,-90.060679,113),
(29.924393,-90.108595,114),
(29.920624,-90.112607,115),
(30.316175,-92.345779,116),
(29.962112,-90.168350,117),
(32.494056,-93.762933,118),
(29.965986,-90.037818,119),
(29.954347,-90.067868,120),
(29.934487,-90.080476,121),
(29.954144,-90.126034,122),
(29.974785,-90.089264,123),
(29.974164,-90.097448,124),
(29.925068,-90.085016,125),
(29.968480,-90.055092,126),
(30.542364,-91.757265,127),
(29.950752,-90.075051,128),
(29.955758,-90.069937,129),
(29.920529,-90.103977,130),
(29.973653,-90.090308,131),
(29.948270,-90.213366,132),
(30.333250,-89.992812,133),
(30.333287,-89.992667,134),
(29.961038,-90.063608,135),
(29.951623,-90.099821,136),
(29.935065,-90.109156,137),
(29.932086,-90.073438,138),
(30.025326,-90.238385,139),
(29.980318,-90.083159,140),
(30.478320,-90.096439,141),
(29.938033,-90.076577,142),
(29.969881,-90.068687,143),
(29.969881,-90.068687,144),
(29.947371,-90.065614,145),
(29.941645,-90.129503,146),
(29.964311,-90.050229,147),
(29.966985,-90.052095,148),
(29.963057,-90.043832,149),
(29.962761,-90.066128,150),
(29.973038,-90.056445,151),
(29.973038,-90.056445,152),
(30.477106,-90.091896,153),
(29.975274,-90.109784,154),
(30.289542,-90.401475,155),
(30.020636,-90.114916,156),
(29.960029,-90.059882,157),
(29.985445,-90.095178,158),
(29.911172,-90.229284,159),
(29.954274,-90.068231,160),
(29.958937,-90.117648,161),
(29.920711,-90.101216,162),
(29.958384,-90.063105,163),
(29.958384,-90.063105,164),
(29.956000,-90.064970,165),
(29.963692,-90.052939,166),
(29.915798,-90.045184,167),
(29.922178,-90.081210,168),
(29.922625,-90.122402,169),
(30.360613,-90.063334,170),
(29.972410,-90.084786,171),
(30.475586,-90.095745,172),
(30.475580,-90.095797,173),
(30.475580,-90.095797,174),
(29.976773,-90.086452,175),
(29.952895,-90.068212,176),
(30.277387,-89.784970,177),
(29.890268,-90.017697,178),
(29.926439,-90.080136,179),
(29.926439,-90.080136,180),
(29.973654,-90.090257,181),
(29.963435,-90.153897,182),
(30.306191,-92.027729,183),
(30.019664,-90.123943,184),
(29.964106,-90.059509,185),
(29.990298,-90.129141,186),
(29.983441,-90.098098,187),
(29.983441,-90.098098,188),
(29.966684,-90.062702,189),
(29.941044,-90.093010,190),
(29.941044,-90.093010,191),
(29.967620,-90.045270,192),
(29.924624,-90.085677,193),
(29.949969,-90.066673,194),
(29.956441,-90.066014,195),
(29.939236,-89.970876,196),
(30.001109,-90.128722,197),
(29.975348,-90.100274,198),
(29.955244,-90.066689,199),
(29.988965,-90.058768,200),
(29.967947,-90.044246,201),
(29.975327,-92.142176,202),
(29.948256,-90.130877,203),
(29.935200,-90.132385,204),
(29.944128,-90.126056,205),
(29.954543,-90.066427,206),
(29.954489,-90.066357,207),
(29.954489,-90.066357,208),
(29.924589,-90.109088,209),
(29.924792,-90.085221,210),
(29.940818,-90.069245,211),
(29.947960,-92.282970,212),
(29.906984,-90.053741,213),
(29.982447,-90.180421,214),
(29.946923,-90.113641,215),
(29.954990,-90.069337,216),
(29.957191,-90.066951,217),
(29.960499,-90.068379,218),
(29.956522,-90.068465,219),
(29.935113,-90.079718,220),
(29.955793,-90.068693,221),
(29.983613,-90.110149,222),
(29.954204,-90.068092,223),
(29.927392,-90.096105,224),
(29.934932,-90.105659,225),
(29.962937,-90.043945,226),
(29.963820,-90.055024,227),
(29.949617,-90.066243,228),
(29.949617,-90.066243,229),
(29.966320,-90.058097,230),
(29.942264,-90.067242,231),
(29.947913,-90.067307,232),
(29.940818,-90.069245,233),
(29.931134,-90.073223,234),
(29.954319,-90.072095,235),
(29.921861,-90.076217,236),
(29.947879,-90.072208,237),
(29.928784,-90.084219,238),
(29.957531,-90.069358,239),
(29.945031,-90.067366,240),
(29.980572,-90.094389,241),
(29.940973,-90.079205,242),
(29.926955,-90.080942,243),
(30.373693,-90.093048,244),
(29.935711,-90.078844,245),
(29.927207,-90.074389,246),
(29.960317,-90.059704,247),
(29.961940,-90.033667,248),
(29.962097,-90.061168,249),
(29.962097,-90.061168,250),
(29.941824,-90.132370,251),
(30.051673,-89.978871,252),
(29.948317,-90.075121,253),
(29.969151,-90.078860,254),
(29.924325,-90.107384,255)]


def main():
	alldistances = []
	mindist, maxdist = 99999999999,-1 
	for point1 in allpoints:
		for point2 in allpoints:
			if point2[2] > point1[2]: 
				distance = calculate_distance((point1[0],point1[1]), (point2[0],point2[1]))
				if distance > maxdist:
					maxdist = distance
				if distance < mindist:
					mindist = distance
				#print('{},{},{}'.format(point1[2],point2[2],distance))
				alldistances.append((point1[2],point2[2],distance))
	
	print(maxdist)
	print(mindist)

## min max
#196	118	459.145973825005
#79	80	0.001365388750302



if __name__ == '__main__':
	cProfile.run('main()')