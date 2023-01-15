from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
import winsound


#--------------------------------------------------------------------------------------------------------------------

email = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input'
confirm = '//*[@id="i10"]/div[2]'
f_name = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
l_name = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
gender = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]'
gender_female = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]'
x_facebook = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_mobile = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_insta = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_house = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_street = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_brgy = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_city = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input'
region = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div[1]/div[1]'
region_calabarzon = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[2]/div[8]/span'
email_2 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div[1]/div/div[1]/input'
checkbox = '//*[@id="i68"]/div[2]'
size = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[3]/div/div[1]/div[1]/div[1]'
size_option = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[3]/div/div[2]/div[11]/span'
ship = '//*[@id="i85"]/div[3]/div'
submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div/span'

#--------------------------------------------------------------------------------------------------------------------
#Email Database
a_emails = ['bry.punzalan06@gmail.com', 'punzalanbren@gmail.com', 'villlclarenzzz@gmail.com', 'neon023456@gmail.com', 'erikdelacruz739@gmail.com', 'bryanpunzalan.yt@gmail.com', 'emma.marquez031@gmail.com', 'punzalanprescilla5@gmail.com', 'elmerpunzalan206@gmail.com', 'punzalanbraulio@gmail.com' ]
b_emails = ['regina.punzalan11@gmail.com', 'reckadelacruz3@gmail.com', 'bllclrnc@gmail.com', 'regineericka.delacruz7@gmail.com', 'regina.delacruz163@gmail.com', 'prescilla.punzalan07@gmail.com', 'lyellamae.delgado@lspu.edu.ph', 'lyellamaedelgado07@gmail.com', 'jokubas.gordon@gmail.com', 'edfrye482@gmail.com' ]
c_emails = ['jozel.felix@gmail.com', 'cresswellkory@gmail.com', 'nazim.valdez@gmail.com', 'roxie.lindsey123@gmail.com', 'rudye4417@gmail.com', 'kateynorman6@gmail.com', 'mabelmckinney51@gmail.com', 'whitworthhattie3@gmail.com', 'nabila.joyner@gmail.com', 'clementsdivine@gmail.com' ]
d_emails = ['rittercheyanne@gmail.com', 'mccalllylah@gmail.com', 'dolliemarkham60@gmail.com', 'dayjenny681@gmail.com', 'stonedarci7@gmail.com', 'laciemcintyre66@gmail.com', 'emilyjonesemily54@gmail.com', 'lovekameron49@gmail.com', 'haydnjeffery@gmail.com', 'mellors819@gmail.com' ]
e_emails = ['wrenpierce112@gmail.com', 'jeannemerrill32@gmail.com', 'celinebowen8@gmail.com', 'kelsiecobb34@gmail.com', 'teliyapugh@gmail.com', 'iqravega4@gmail.com', 'lillianhead98@gmail.com', 'lugob0008@gmail.com', 'marthamac237@gmail.com', 'irenecardenas357@gmail.com']
f_emails = ['bodhispence@gmail.com', 'esmayrayner@gmail.com', 'brookstasmin@gmail.com', 'masumaparra@gmail.com', 'kelisedonovan@gmail.com', 'imaniwhitmore2@gmail.com', 'madge.elsabeth01@gmail.com', 'lois.elfrida01@gmail.com', 'jacquelyn.belle01@gmail.com', 'adria.gabby01@gmail.com']
g_emails = ['zoie.bea01@gmail.com', 'taylor.liliana01@gmail.com', 'laci.bronte01@gmail.com', 'gytha.lise01@gmail.com', 'rheanna.candis01@gmail.com', 'andi.alannis01@gmail.com', 'hayley.gift01@gmail.com', 'stacie.nelly01@gmail.com', 'jenae.kilie01@gmail.com', 'alita.elizabeth01@gmail.com']
h_emails = ['azure.tegan01@gmail.com', 'rosanne.merle01@gmail.com', 'elnora.kate01@gmail.com', 'raelyn.davinia01@gmail.com', 'katlyn.chris01@gmail.com', 'odetta.ronda01@gmail.com', 'vale.posie01@gmail.com', 'addilyn.jeannette01@gmail.com', 'judi.kalyn01@gmail.com', 'barbie.rebeccah01@gmail.com']
i_emails = ['katrina.nellie01@gmail.com', 'misti.elsabeth01@gmail.com', 'tammy.madelynn01@gmail.com', 'lucinda.bobbie01@gmail.com', 'isabel.natalee01@gmail.com', 'tori.sara01@gmail.com', 'detta.marge01@gmail.com', 'cat.bethel01@gmail.com', 'kinsey.charisse01@gmail.com', 'cherry.ibbie01@gmail.com']
j_emails = ['susan.samara01@gmail.com', 'kilie.dolores01@gmail.com', 'gracie.randy01@gmail.com', 'aretha.evette01@gmail.com', 'meridith.jacinth01@gmail.com', 'marcie.annika01@gmail.com', 'blythe.bronwyn01@gmail.com', 'wilda.annalise01@gmail.com', 'katheryn.ibbie01@gmail.com', 'neva.cruz01@gmail.com'] 
emails = a_emails + b_emails + c_emails + d_emails + e_emails + f_emails + g_emails + h_emails + i_emails + j_emails

#--------------------------------------------------------------------------------------------------------------------
#name Database
a_name = ['BRYAN CEDRIC', 'BREN', 'BILL CLARENCE ', 'CARL', 'ERIK', 'CEDRIC', 'EMMA', 'PRESCILLA', 'ELMER', 'BRAULIO']
b_name = ['REGINA', 'RECKA', 'CLARENCE', 'REGINE ERICKA', 'REGINA', 'PRECY', 'MAE', 'LYELLA', 'JOKUBAS', 'ED']
c_name = ['JOZEL', 'KORY', 'NAZIM', 'ROXIE', 'RUDY', 'KATEY', 'MABEL', 'HATTIE', 'NABILA', 'DIVINE']
d_name = ['CHEYANNE', 'LYLAH', 'DOLLIE', 'JENNY', 'DARCI', 'LACIE', 'EMILY', 'KAMERON', 'HAYDN', 'SAM']
e_name = ['WREN', 'JEANNE', 'CELINE', 'KELSIE', 'TELIYA', 'IQRA', 'LILLIAN', 'BEATRIZ', 'MARTHA', 'IRENE']
fs_name = ['BODHI', 'ESMAY', 'TASMIN', 'MASUMA', 'KELISE', 'IMANI', 'MADGE', 'LOIS', 'JACQUELYN', 'ADRIA']
g_name = ['ZOIE', 'TAYLOR', 'LACI', 'GYTHA', 'RHEANNA', 'ANDI', 'HAYLEY', 'STACIE', 'JENAE', 'ALITA']
h_name = ['AZURE', 'ROSANNE', 'ELNORA', 'RAELYN', 'KATLYN', 'ODETTA', 'VALE', 'ADDILYN', 'JUDI', 'BARBIE']
i_name = ['KATRINA', 'MISTI', 'TAMMY', 'LUCINDA', 'ISABEL', 'TORI', 'DETTA', 'CAT', 'KINSEY', 'CHERRY']
j_name = ['SUSAN', 'KILIE', 'GRACIE', 'ARETHA', 'MERIDITH', 'MARCIE', 'BLYTHE', 'WILDA', 'KATHERYN', 'NEVA'] 

name = a_name + b_name + c_name + d_name + e_name + fs_name + g_name + h_name + i_name + j_name

#--------------------------------------------------------------------------------------------------------------------
#lname Database
a_l_names = ['PUNZALAN', 'PUNZALAN', 'PUNZALAN', 'PUNZALAN', 'DELA  CRUZ', 'PUNZALAN', 'MARQUEZ', 'PUNZALAN', 'PUNZALAN', 'PUNZALAN']
b_l_names = ['PUNZALAN', 'PUNZALAN', 'PUNZALAN', 'DELA  CRUZ', 'DELA  CRUZ', 'PUNZALAN', 'DELGADO', 'DELGADO', 'GORDON', 'FRYE']
c_l_names = ['FELIX', 'CRESSWELL', 'VALDEZ', 'LINDSEY', 'ESTRADA', 'NORMAN', 'MCKINNEY', 'WHITWORTH', 'JOYNER', 'CLEMENTS']
d_l_names = ['RITTER', 'MCCALL', 'MARKHAM', 'DAY', 'STONE', 'MCINTYRE', 'JONES', 'LOVE', 'JEFFERY', 'MELLOR']
e_l_names = ['PIERCE', 'MERRILL', 'BOWEN', 'COBB', 'PUGH', 'VEGA', 'HEAD', 'LUGO', 'MAC', 'CARDENAS']
f_l_names = ['SPENCE', 'RAYNER', 'BROOKS', 'PARRA', 'DONOVAN', 'WHITMORE', 'FERNANDEZ', 'CRUZ', 'DE GUZMAN', 'LOPEZ']
g_l_names = ['PEREZ', 'CASTILLO', 'FRANCISCO', 'RIVERA', 'AQUINO', 'CASTRO', 'SANCHEZ', 'TORRES', 'DE LEON', 'MARTINEZ']
h_l_names = ['RODRIGUEZ', 'SANTIAGO', 'SORIANO', 'DELOS SANTOS', 'DIAZ', 'HERNANDEZ', 'TOLENTINO', 'VALDEZ', 'RAMIREZ', 'MORALES']
i_l_names = ['MERCADO', 'TAN', 'AGUILAR', 'NAVARRO', 'MANALO', 'GOMEZ', 'DIZON', 'DEL ROSARIO', 'JAVIER', 'CORPUZ']
j_l_names = ['GUTIERREZ', 'SALVADOR', 'VELASCO', 'MIRANDA', 'DAVID', 'SALAZAR', 'FERRER', 'ALVAREZ', 'SARMIENTO', 'CRUZ'] 

l_names = a_l_names + b_l_names + c_l_names + d_l_names + e_l_names + f_l_names + g_l_names + h_l_names + i_l_names + j_l_names

#--------------------------------------------------------------------------------------------------------------------
#facebook Database
a_facebook = ['www.facebook.com/bryan cedric.punzalan', 'www.facebook.com/bren.punzalan', 'www.facebook.com/bill clarence .punzalan', 'www.facebook.com/carl.punzalan', 'www.facebook.com/erik.dela  cruz', 'www.facebook.com/cedric.punzalan', 'www.facebook.com/emma.marquez', 'www.facebook.com/prescilla.punzalan', 'www.facebook.com/elmer.punzalan', 'www.facebook.com/braulio.punzalan']
b_facebook = ['www.facebook.com/regina.punzalan', 'www.facebook.com/recka.punzalan', 'www.facebook.com/clarence.punzalan', 'www.facebook.com/regine ericka.dela  cruz', 'www.facebook.com/regina.dela  cruz', 'www.facebook.com/precy.punzalan', 'www.facebook.com/mae.delgado', 'www.facebook.com/lyella.delgado', 'www.facebook.com/jokubas.gordon', 'www.facebook.com/ed.frye']
c_facebook = ['www.facebook.com/jozel.felix', 'www.facebook.com/kory.cresswell', 'www.facebook.com/nazim.valdez', 'www.facebook.com/roxie.lindsey', 'www.facebook.com/rudy.estrada', 'www.facebook.com/katey.norman', 'www.facebook.com/mabel.mckinney', 'www.facebook.com/hattie.whitworth', 'www.facebook.com/nabila.joyner', 'www.facebook.com/divine.clements']
d_facebook = ['www.facebook.com/cheyanne.ritter', 'www.facebook.com/lylah.mccall', 'www.facebook.com/dollie.markham', 'www.facebook.com/jenny.day', 'www.facebook.com/darci.stone', 'www.facebook.com/lacie.mcintyre', 'www.facebook.com/emily.jones', 'www.facebook.com/kameron.love', 'www.facebook.com/haydn.jeffery', 'www.facebook.com/sam.mellor']
e_facebook = ['www.facebook.com/wren.pierce', 'www.facebook.com/jeanne.merrill', 'www.facebook.com/celine.bowen', 'www.facebook.com/kelsie.cobb', 'www.facebook.com/teliya.pugh', 'www.facebook.com/iqra.vega', 'www.facebook.com/lillian.head', 'www.facebook.com/beatriz.lugo', 'www.facebook.com/martha.mac', 'www.facebook.com/irene.cardenas']
f_facebook = ['www.facebook.com/bodhi.spence', 'www.facebook.com/esmay.rayner', 'www.facebook.com/tasmin.brooks', 'www.facebook.com/masuma.parra', 'www.facebook.com/kelise.donovan', 'www.facebook.com/imani.whitmore', 'www.facebook.com/madge.fernandez', 'www.facebook.com/lois.cruz', 'www.facebook.com/jacquelyn.de guzman', 'www.facebook.com/adria.lopez']
g_facebook = ['www.facebook.com/zoie.perez', 'www.facebook.com/taylor.castillo', 'www.facebook.com/laci.francisco', 'www.facebook.com/gytha.rivera', 'www.facebook.com/rheanna.aquino', 'www.facebook.com/andi.castro', 'www.facebook.com/hayley.sanchez', 'www.facebook.com/stacie.torres', 'www.facebook.com/jenae.de leon', 'www.facebook.com/alita.martinez']
h_facebook = ['www.facebook.com/azure.rodriguez', 'www.facebook.com/rosanne.santiago', 'www.facebook.com/elnora.soriano', 'www.facebook.com/raelyn.delos santos', 'www.facebook.com/katlyn.diaz', 'www.facebook.com/odetta.hernandez', 'www.facebook.com/vale.tolentino', 'www.facebook.com/addilyn.valdez', 'www.facebook.com/judi.ramirez', 'www.facebook.com/barbie.morales']
i_facebook = ['www.facebook.com/katrina.mercado', 'www.facebook.com/misti.tan', 'www.facebook.com/tammy.aguilar', 'www.facebook.com/lucinda.navarro', 'www.facebook.com/isabel.manalo', 'www.facebook.com/tori.gomez', 'www.facebook.com/detta.dizon', 'www.facebook.com/cat.del rosario', 'www.facebook.com/kinsey.javier', 'www.facebook.com/cherry.corpuz']
j_facebook = ['www.facebook.com/susan.gutierrez', 'www.facebook.com/kilie.salvador', 'www.facebook.com/gracie.velasco', 'www.facebook.com/aretha.miranda', 'www.facebook.com/meridith.david', 'www.facebook.com/marcie.salazar', 'www.facebook.com/blythe.ferrer', 'www.facebook.com/wilda.alvarez', 'www.facebook.com/katheryn.sarmiento', 'www.facebook.com/neva.cruz'] 

facebook = a_facebook + b_facebook + c_facebook + d_facebook + e_facebook + f_facebook + g_facebook + h_facebook + i_facebook + j_facebook

#--------------------------------------------------------------------------------------------------------------------
#mobile Database
a_mobile = ['9753186362', '9687152768', '9687152769', '9357912758', '9357914221', '9682904479', '9051673672', '9217168610', '9357912718', '9357912435' ]
b_mobile = ['9357912231', '9357912430', '9051929491', '9357914301', '9357916445', '9292217163', '9232627776', '9054880137', '9354319901', '9354316235']
c_mobile = ['9354302822', '9354312155', '9354316202', '9354319236', '9354319864', '9354317971', '9354316131', '9354308292', '9354316929', '9354318703']
d_mobile = ['9354316173', '9354322742', '9976149327', '9754406242', '9354316918', '9754406191', '9533720149', '9754413144', '9533720158', '9533720156']
e_mobile = ['9754406202', '9533750543', '9068009479', '9754404745', '9754406210', '9533720153', '9754413249', '9754425237', '9361846728', '9754426191']
f_mobile = ['9368335468', '9754410761', '9533720203', '9754404669', '9533720219', '9754400867', '9754406017', '9754400852', '9751995166', '9555263663']
g_mobile = ['9751993741', '9751992903', '9555263931', '9751990807', '9751990795', '9555267137', '9751990047', '9555267069', '9751991235', '9751992833']
h_mobile = ['9751989266', '9751991202', '9751990734', '9555267179', '9751992913', '9555267211', '9555275704', '9751990717', '9751990108', '9751993706']
i_mobile = ['9751992734', '9751990019', '9751992810', '9555263874', '9751991198', '9751991195', '9751992671', '9555264989', '9751992864', '9555264992']
j_mobile = ['9751992355', '9555266859', '9751993847', '9751993659', '9751992663', '9555264956', '9751991172', '9555263866', '9555263768', '9751989249'] 
mobile = a_mobile + b_mobile + c_mobile + d_mobile + e_mobile + f_mobile + g_mobile + h_mobile + i_mobile + j_mobile

#--------------------------------------------------------------------------------------------------------------------
#insta Database
a_insta = ['@bryan cedric.punzalan', '@bren.punzalan', '@bill clarence .punzalan', '@carl.punzalan', '@erik.dela  cruz', '@cedric.punzalan', '@emma.marquez', '@prescilla.punzalan', '@elmer.punzalan', '@braulio.punzalan']
b_insta = ['@regina.punzalan', '@recka.punzalan', '@clarence.punzalan', '@regine ericka.dela  cruz', '@regina.dela  cruz', '@precy.punzalan', '@mae.delgado', '@lyella.delgado', '@jokubas.gordon', '@ed.frye']
c_insta = ['@jozel.felix', '@kory.cresswell', '@nazim.valdez', '@roxie.lindsey', '@rudy.estrada', '@katey.norman', '@mabel.mckinney', '@hattie.whitworth', '@nabila.joyner', '@divine.clements']
d_insta = ['@cheyanne.ritter', '@lylah.mccall', '@dollie.markham', '@jenny.day', '@darci.stone', '@lacie.mcintyre', '@emily.jones', '@kameron.love', '@haydn.jeffery', '@sam.mellor']
e_insta = ['@wren.pierce', '@jeanne.merrill', '@celine.bowen', '@kelsie.cobb', '@teliya.pugh', '@iqra.vega', '@lillian.head', '@beatriz.lugo', '@martha.mac', '@irene.cardenas']
f_insta = ['@bodhi.spence', '@esmay.rayner', '@tasmin.brooks', '@masuma.parra', '@kelise.donovan', '@imani.whitmore', '@madge.fernandez', '@lois.cruz', '@jacquelyn.de guzman', '@adria.lopez']
g_insta = ['@zoie.perez', '@taylor.castillo', '@laci.francisco', '@gytha.rivera', '@rheanna.aquino', '@andi.castro', '@hayley.sanchez', '@stacie.torres', '@jenae.de leon', '@alita.martinez']
h_insta = ['@azure.rodriguez', '@rosanne.santiago', '@elnora.soriano', '@raelyn.delos santos', '@katlyn.diaz', '@odetta.hernandez', '@vale.tolentino', '@addilyn.valdez', '@judi.ramirez', '@barbie.morales']
i_insta = ['@katrina.mercado', '@misti.tan', '@tammy.aguilar', '@lucinda.navarro', '@isabel.manalo', '@tori.gomez', '@detta.dizon', '@cat.del rosario', '@kinsey.javier', '@cherry.corpuz']
j_insta = ['@susan.gutierrez', '@kilie.salvador', '@gracie.velasco', '@aretha.miranda', '@meridith.david', '@marcie.salazar', '@blythe.ferrer', '@wilda.alvarez', '@katheryn.sarmiento', '@neva.cruz'] 
insta = a_insta + b_insta + c_insta + d_insta + e_insta + f_insta + g_insta + h_insta + i_insta + j_insta

#--------------------------------------------------------------------------------------------------------------------
#house Database
a_house = ['7EF 195', '4FG 195', 'D3A 195', '287 195', '50H 195', 'ABC 195', 'J80 195', '85B 195', 'G49 195', '36E 195']
b_house = ['96E 195', 'ED9 195', 'SFW 195', 'D2H 195', '344 195', '70B 195', '06G 195', '62I 195', '4B4 195', 'SFE 195']
c_house = ['1JG 195', '3D9 195', '5A5 195', 'BSW 195', '1H7 195', '6I1 195', '642 195', '5E2 195', 'BXX 195', '2A9 195']
d_house = ['H56 195', '2JC 195', '7F7 195', '81D 195', 'ZQW 195', '52G 195', 'CBE 195', '14F 195', 'BEG 195', 'BNR 195']
e_house = ['XSW 195', '0CJ 195', '7F1 195', 'GE9 195', 'H9J 195', 'JJC 195', '03I 195', 'BCE 195', 'A90 195', '8DG 195']
f_house = ['D57 195', 'C5C 195', '77C 195', 'E52 195', '7D3 195', '39B 195', 'G46 195', '20F 195', '32J 195', 'A98 195']
g_house = ['D0G 195', '0I8 195', '0HG 195', 'E1E 195', 'BBF 195', 'VBF 195', '1B5 195', 'C48 195', 'XEG 195', 'CE0 195']
h_house = ['NNG 195', '62F 195', 'G00 195', 'F32 195', '078 195', 'GD6 195', '68C 195', '2D6 195', 'B50 195', 'CN8 195']
i_house = ['8A5 195', '9EF 195', '35E 195', 'JC5 195', 'C41 195', 'NHU 195', 'E63 195', 'J38 195', '426 195', 'F43 195']
j_house = ['ASW 195', 'DEH 195', 'ZSQ 195', 'A17 195', 'BMJ 195', 'NHY 195', 'G1C 195', '99F 195', '7E7 195', '3JI 195'] 
house = a_house + b_house + c_house + d_house + e_house + f_house + g_house + h_house + i_house + j_house

#--------------------------------------------------------------------------------------------------------------------
#street Database
a_street = ['Llamas Subdivision', 'lLAmAs SUBDVISION', 'LlamAS SUBD.', 'llAMAS subd.', 'lLaMAs SUBDVSION', 'lLaMAS subdivsion', 'llamAs Subdvi', 'llamas Street', 'LlaMas Strts', 'lLAMAs st.']
b_street = ['lLaMAS STREET', 'lLamaS Stret', 'lLAMas Strt.', 'LLAMaS ST.', 'llAmaS Subdivision', 'LlaMAS SUBDVISION', 'lLAMaS SUBD.', 'LLamaS subd.', 'Llamas SUBDVSION', 'llAMaS subdivsion']
c_street = ['LlAMas Subdvi', 'lLAMAS Street', 'LLamaS Strts', 'LlamAS st.', 'LlAMAS STREET', 'lLAMas Stret', 'llamAS Strt.', 'llamAS ST.', 'LlamAS Subdivision', 'LlAmaS SUBDVISION']
d_street = ['llaMas SUBD.', 'LlaMaS subd.', 'Llamas SUBDVSION', 'llamas subdivsion', 'LLAmAs Subdvi', 'llaMaS Street', 'LLAMAs Strts', 'llAMaS st.', 'llamaS STREET', 'lLAMAs Stret']
e_street = ['lLAMaS Strt.', 'LLamaS ST.', 'Llamas Subdivision', 'llAMaS SUBDVISION', 'LlAMas SUBD.', 'lLAMAS subd.', 'LLamaS SUBDVSION', 'LlamAS subdivsion', 'LlAMAS Subdvi', 'Llamas Subdivision']
f_street = ['lLAmAs SUBDVISION', 'LlamAS SUBD.', 'llAMAS subd.', 'lLaMAs SUBDVSION', 'lLaMAS subdivsion', 'llamAs Subdvi', 'llamas Street', 'LlaMas Strts', 'lLAMAs st.', 'lLaMAS STREET']
g_street = ['lLamaS Stret', 'lLAMas Strt.', 'LLAMaS ST.', 'llAmaS Subdivision', 'LlaMAS SUBDVISION', 'lLAMaS SUBD.', 'LLamaS subd.', 'Llamas SUBDVSION', 'llAMaS subdivsion', 'LlAMas Subdvi']
h_street = ['lLAMAS Street', 'LLamaS Strts', 'LlamAS st.', 'LlAMAS STREET', 'lLAMas Stret', 'llamAS Strt.', 'llamAS ST.', 'LlamAS Subdivision', 'LlAmaS SUBDVISION', 'llaMas SUBD.']
i_street = ['LlaMaS subd.', 'Llamas SUBDVSION', 'llamas subdivsion', 'LLAmAs Subdvi', 'llaMaS Street', 'LLAMAs Strts', 'llAMaS st.', 'llamaS STREET', 'lLAMAs Stret', 'lLAMaS Strt.']
j_street = ['LLamaS ST.', 'Llamas Subdivision', 'llAMaS SUBDVISION', 'LlAMas SUBD.', 'lLAMAS subd.', 'LLamaS SUBDVSION', 'LlamAS subdivsion', 'LlAMAS Subdvi', 'Llamas Subdivision', 'lLAmAs SUBDVISION'] 
street = a_street + b_street + c_street + d_street + e_house + f_house + g_street + h_street + i_street + j_street

#--------------------------------------------------------------------------------------------------------------------
#brgy Database
a_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3']
b_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3']
c_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3']
d_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3']
e_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3']
f_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3']
g_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3']
h_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3']
i_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3']
j_brgy = ['Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3', 'Barangay 3'] 
brgy = a_brgy + b_brgy + c_brgy + d_brgy + e_brgy + f_brgy + g_brgy + h_brgy + i_brgy + j_brgy

#city Database
a_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City']
b_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City']
c_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City']
d_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City']
e_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City']
f_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City']
g_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City']
h_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City']
i_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City']
j_city = ['Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City', 'Calamba City'] 
city = a_city + b_city + c_city + d_city + e_city + f_city + g_city + h_city + i_city + j_city






for (a, b, c, d, e, f, g, h, i, j) in zip(emails, name, l_names, facebook, mobile, insta, house, street, brgy, city):
    # py = '45.56.97.74:20201'
    # chrome_options = webdriver.ChromeOptions()
    # #proxy parameter to options
    # chrome_options.add_argument('--proxy-server=%s' % py)
    # #options to Chrome()
    # driver = webdriver.Chrome(options= chrome_options)
    # driver.implicitly_wait(0.6)

    duration = 1000  # milliseconds
    freq = 1600  # Hz
    freq2 = 2000  # Hz
    winsound.Beep(freq, duration)

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser = webdriver.Chrome(executable_path=r'C:\Users\Bren Punzalan\Downloads\Chrome Driver\chromedriver.exe', options=options)
    # link
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSeuF9eBQLHWs3Aoq-OMq1bZbNmBf8OmHcmq1obV5SAK0BddHg/viewform')
    
    
    #email
    browser.find_element(By.XPATH, email).send_keys(a)
    #confirm checkbox
    browser.find_element(By.XPATH, confirm).click()

    #first_name
    browser.find_element(By.XPATH, f_name).send_keys(b)
    #last-name
    browser.find_element(By.XPATH, l_name).send_keys(c)
   
    # gender
    time.sleep(1)
    browser.find_element(By.XPATH, gender).click()
    time.sleep(3)
    browser.find_element(By.XPATH, gender_female).click()
    

    #facebook
    browser.find_element(By.XPATH, x_facebook).send_keys(d)

    #mobile
    browser.find_element(By.XPATH, x_mobile).send_keys(e)
    
    #insta
    browser.find_element(By.XPATH, x_insta).send_keys(f)

    #house
    browser.find_element(By.XPATH, x_house).send_keys(g)

    #street
    browser.find_element(By.XPATH, x_street).send_keys(h)

    #brgy
    browser.find_element(By.XPATH, x_brgy).send_keys(i)

    #city
    browser.find_element(By.XPATH, x_city).send_keys(j)

    #calabarzon
    browser.find_element(By.XPATH, region).click()
    time.sleep(3)
    browser.find_element(By.XPATH, region_calabarzon).click()
   

    #email2
    browser.find_element(By.XPATH, email_2).send_keys(a)

    #confirm checkbox
        #browser.find_element(By.XPATH, checkbox).click()

    #size
    browser.find_element(By.XPATH, size).click()
    time.sleep(3)
    browser.find_element(By.XPATH, size_option).click()
   
    winsound.Beep(freq2, duration)
    #confirm checkbox
    #browser.find_element(By.XPATH, ship).click()
   
    browser.find_element(By.XPATH, submit).click()
    
    print(b + '' + c)
    time.sleep(5)
    print('15')
    time.sleep(5)
    print('10')
    time.sleep(5)
    print('5')
    time.sleep(5)
    print('0')
    
   

