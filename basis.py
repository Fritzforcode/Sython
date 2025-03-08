# Global memory dictionary to store objects
_memory_dict = {}
_next_id = 1  # Unique ID counter

class PyTypeObject:
    def __init__(self, tp_name: str):
        self.tp_name = tp_name
    def __repr__(self) -> str:
        from str import MyStr
        return MyStr.from_python("<class '__main__." + self.tp_name + "'>")

class PyObject_HEAD:
    good_repr_compatible = True # For debugging
    _fields = ["ob_refcnt", "ob_type"]
    def __init__(self, ob_type):
        self.ob_refcnt = 0
        self.ob_type = ob_type

    def make_reference_compatible(self):
        global _next_id
        self.ref_id = _next_id
        _memory_dict[self.ref_id] = self
        _next_id += 1        

class PyObject_VAR_HEAD(PyObject_HEAD):
    _fields = PyObject_HEAD._fields + []
    def __init__(self, ob_type):
        super().__init__(ob_type=ob_type)

class Reference:
    good_repr_compatible = True # For debugging
    _fields = ["ref_id"]
    def __init__(self, obj: PyObject_HEAD):
        assert hasattr(obj, "ref_id")
        self.ref_id = obj.ref_id
    
    def deref(self):
        return _memory_dict.get(self.ref_id, None)


def my_repr(obj):
    print(type(obj))
    if hasattr(obj, "__repr__"):
        s = obj.__repr__()
        return s if isinstance(s, str) else s.to_python()
    elif hasattr(obj, "__str__"):
        s = obj.__str__()
        return s if isinstance(s, str) else s.to_python()
    else:
        return repr(obj)

_UPPER_TRANSLATION = {97:65,98:66,99:67,100:68,101:69,102:70,103:71,104:72,105:73,106:74,107:75,108:76,109:77,110:78,111:79,112:80,113:81,114:82,115:83,116:84,117:85,118:86,119:87,120:88,121:89,122:90,181:924,223:[83,83],224:192,225:193,226:194,227:195,228:196,229:197,230:198,231:199,232:200,233:201,234:202,235:203,236:204,237:205,238:206,239:207,240:208,241:209,242:210,243:211,244:212,245:213,246:214,248:216,249:217,250:218,251:219,252:220,253:221,254:222,255:376,257:256,259:258,261:260,263:262,265:264,267:266,269:268,271:270,273:272,275:274,277:276,279:278,281:280,283:282,285:284,287:286,289:288,291:290,293:292,295:294,297:296,299:298,301:300,303:302,305:73,307:306,309:308,311:310,314:313,316:315,318:317,320:319,322:321,324:323,326:325,328:327,329:[700,78],331:330,333:332,335:334,337:336,339:338,341:340,343:342,345:344,347:346,349:348,351:350,353:352,355:354,357:356,359:358,361:360,363:362,365:364,367:366,369:368,371:370,373:372,375:374,378:377,380:379,382:381,383:83,384:579,387:386,389:388,392:391,396:395,402:401,405:502,409:408,410:573,414:544,417:416,419:418,421:420,424:423,429:428,432:431,436:435,438:437,441:440,445:444,447:503,453:452,454:452,456:455,457:455,459:458,460:458,462:461,464:463,466:465,468:467,470:469,472:471,474:473,476:475,477:398,479:478,481:480,483:482,485:484,487:486,489:488,491:490,493:492,495:494,496:[74,780],498:497,499:497,501:500,505:504,507:506,509:508,511:510,513:512,515:514,517:516,519:518,521:520,523:522,525:524,527:526,529:528,531:530,533:532,535:534,537:536,539:538,541:540,543:542,547:546,549:548,551:550,553:552,555:554,557:556,559:558,561:560,563:562,572:571,575:11390,576:11391,578:577,583:582,585:584,587:586,589:588,591:590,592:11375,593:11373,594:11376,595:385,596:390,598:393,599:394,601:399,603:400,604:42923,608:403,609:42924,611:404,613:42893,614:42922,616:407,617:406,618:42926,619:11362,620:42925,623:412,625:11374,626:413,629:415,637:11364,640:422,642:42949,643:425,647:42929,648:430,649:580,650:433,651:434,652:581,658:439,669:42930,670:42928,837:921,881:880,883:882,887:886,891:1021,892:1022,893:1023,912:[921,776,769],940:902,941:904,942:905,943:906,944:[933,776,769],945:913,946:914,947:915,948:916,949:917,950:918,951:919,952:920,953:921,954:922,955:923,956:924,957:925,958:926,959:927,960:928,961:929,962:931,963:931,964:932,965:933,966:934,967:935,968:936,969:937,970:938,971:939,972:908,973:910,974:911,976:914,977:920,981:934,982:928,983:975,985:984,987:986,989:988,991:990,993:992,995:994,997:996,999:998,1001:1000,1003:1002,1005:1004,1007:1006,1008:922,1009:929,1010:1017,1011:895,1013:917,1016:1015,1019:1018,1072:1040,1073:1041,1074:1042,1075:1043,1076:1044,1077:1045,1078:1046,1079:1047,1080:1048,1081:1049,1082:1050,1083:1051,1084:1052,1085:1053,1086:1054,1087:1055,1088:1056,1089:1057,1090:1058,1091:1059,1092:1060,1093:1061,1094:1062,1095:1063,1096:1064,1097:1065,1098:1066,1099:1067,1100:1068,1101:1069,1102:1070,1103:1071,1104:1024,1105:1025,1106:1026,1107:1027,1108:1028,1109:1029,1110:1030,1111:1031,1112:1032,1113:1033,1114:1034,1115:1035,1116:1036,1117:1037,1118:1038,1119:1039,1121:1120,1123:1122,1125:1124,1127:1126,1129:1128,1131:1130,1133:1132,1135:1134,1137:1136,1139:1138,1141:1140,1143:1142,1145:1144,1147:1146,1149:1148,1151:1150,1153:1152,1163:1162,1165:1164,1167:1166,1169:1168,1171:1170,1173:1172,1175:1174,1177:1176,1179:1178,1181:1180,1183:1182,1185:1184,1187:1186,1189:1188,1191:1190,1193:1192,1195:1194,1197:1196,1199:1198,1201:1200,1203:1202,1205:1204,1207:1206,1209:1208,1211:1210,1213:1212,1215:1214,1218:1217,1220:1219,1222:1221,1224:1223,1226:1225,1228:1227,1230:1229,1231:1216,1233:1232,1235:1234,1237:1236,1239:1238,1241:1240,1243:1242,1245:1244,1247:1246,1249:1248,1251:1250,1253:1252,1255:1254,1257:1256,1259:1258,1261:1260,1263:1262,1265:1264,1267:1266,1269:1268,1271:1270,1273:1272,1275:1274,1277:1276,1279:1278,1281:1280,1283:1282,1285:1284,1287:1286,1289:1288,1291:1290,1293:1292,1295:1294,1297:1296,1299:1298,1301:1300,1303:1302,1305:1304,1307:1306,1309:1308,1311:1310,1313:1312,1315:1314,1317:1316,1319:1318,1321:1320,1323:1322,1325:1324,1327:1326,1377:1329,1378:1330,1379:1331,1380:1332,1381:1333,1382:1334,1383:1335,1384:1336,1385:1337,1386:1338,1387:1339,1388:1340,1389:1341,1390:1342,1391:1343,1392:1344,1393:1345,1394:1346,1395:1347,1396:1348,1397:1349,1398:1350,1399:1351,1400:1352,1401:1353,1402:1354,1403:1355,1404:1356,1405:1357,1406:1358,1407:1359,1408:1360,1409:1361,1410:1362,1411:1363,1412:1364,1413:1365,1414:1366,1415:[1333,1362],4304:7312,4305:7313,4306:7314,4307:7315,4308:7316,4309:7317,4310:7318,4311:7319,4312:7320,4313:7321,4314:7322,4315:7323,4316:7324,4317:7325,4318:7326,4319:7327,4320:7328,4321:7329,4322:7330,4323:7331,4324:7332,4325:7333,4326:7334,4327:7335,4328:7336,4329:7337,4330:7338,4331:7339,4332:7340,4333:7341,4334:7342,4335:7343,4336:7344,4337:7345,4338:7346,4339:7347,4340:7348,4341:7349,4342:7350,4343:7351,4344:7352,4345:7353,4346:7354,4349:7357,4350:7358,4351:7359,5112:5104,5113:5105,5114:5106,5115:5107,5116:5108,5117:5109,7296:1042,7297:1044,7298:1054,7299:1057,7300:1058,7301:1058,7302:1066,7303:1122,7304:42570,7545:42877,7549:11363,7566:42950,7681:7680,7683:7682,7685:7684,7687:7686,7689:7688,7691:7690,7693:7692,7695:7694,7697:7696,7699:7698,7701:7700,7703:7702,7705:7704,7707:7706,7709:7708,7711:7710,7713:7712,7715:7714,7717:7716,7719:7718,7721:7720,7723:7722,7725:7724,7727:7726,7729:7728,7731:7730,7733:7732,7735:7734,7737:7736,7739:7738,7741:7740,7743:7742,7745:7744,7747:7746,7749:7748,7751:7750,7753:7752,7755:7754,7757:7756,7759:7758,7761:7760,7763:7762,7765:7764,7767:7766,7769:7768,7771:7770,7773:7772,7775:7774,7777:7776,7779:7778,7781:7780,7783:7782,7785:7784,7787:7786,7789:7788,7791:7790,7793:7792,7795:7794,7797:7796,7799:7798,7801:7800,7803:7802,7805:7804,7807:7806,7809:7808,7811:7810,7813:7812,7815:7814,7817:7816,7819:7818,7821:7820,7823:7822,7825:7824,7827:7826,7829:7828,7830:[72,817],7831:[84,776],7832:[87,778],7833:[89,778],7834:[65,702],7835:7776,7841:7840,7843:7842,7845:7844,7847:7846,7849:7848,7851:7850,7853:7852,7855:7854,7857:7856,7859:7858,7861:7860,7863:7862,7865:7864,7867:7866,7869:7868,7871:7870,7873:7872,7875:7874,7877:7876,7879:7878,7881:7880,7883:7882,7885:7884,7887:7886,7889:7888,7891:7890,7893:7892,7895:7894,7897:7896,7899:7898,7901:7900,7903:7902,7905:7904,7907:7906,7909:7908,7911:7910,7913:7912,7915:7914,7917:7916,7919:7918,7921:7920,7923:7922,7925:7924,7927:7926,7929:7928,7931:7930,7933:7932,7935:7934,7936:7944,7937:7945,7938:7946,7939:7947,7940:7948,7941:7949,7942:7950,7943:7951,7952:7960,7953:7961,7954:7962,7955:7963,7956:7964,7957:7965,7968:7976,7969:7977,7970:7978,7971:7979,7972:7980,7973:7981,7974:7982,7975:7983,7984:7992,7985:7993,7986:7994,7987:7995,7988:7996,7989:7997,7990:7998,7991:7999,8000:8008,8001:8009,8002:8010,8003:8011,8004:8012,8005:8013,8016:[933,787],8017:8025,8018:[933,787,768],8019:8027,8020:[933,787,769],8021:8029,8022:[933,787,834],8023:8031,8032:8040,8033:8041,8034:8042,8035:8043,8036:8044,8037:8045,8038:8046,8039:8047,8048:8122,8049:8123,8050:8136,8051:8137,8052:8138,8053:8139,8054:8154,8055:8155,8056:8184,8057:8185,8058:8170,8059:8171,8060:8186,8061:8187,8064:[7944,921],8065:[7945,921],8066:[7946,921],8067:[7947,921],8068:[7948,921],8069:[7949,921],8070:[7950,921],8071:[7951,921],8072:[7944,921],8073:[7945,921],8074:[7946,921],8075:[7947,921],8076:[7948,921],8077:[7949,921],8078:[7950,921],8079:[7951,921],8080:[7976,921],8081:[7977,921],8082:[7978,921],8083:[7979,921],8084:[7980,921],8085:[7981,921],8086:[7982,921],8087:[7983,921],8088:[7976,921],8089:[7977,921],8090:[7978,921],8091:[7979,921],8092:[7980,921],8093:[7981,921],8094:[7982,921],8095:[7983,921],8096:[8040,921],8097:[8041,921],8098:[8042,921],8099:[8043,921],8100:[8044,921],8101:[8045,921],8102:[8046,921],8103:[8047,921],8104:[8040,921],8105:[8041,921],8106:[8042,921],8107:[8043,921],8108:[8044,921],8109:[8045,921],8110:[8046,921],8111:[8047,921],8112:8120,8113:8121,8114:[8122,921],8115:[913,921],8116:[902,921],8118:[913,834],8119:[913,834,921],8124:[913,921],8126:921,8130:[8138,921],8131:[919,921],8132:[905,921],8134:[919,834],8135:[919,834,921],8140:[919,921],8144:8152,8145:8153,8146:[921,776,768],8147:[921,776,769],8150:[921,834],8151:[921,776,834],8160:8168,8161:8169,8162:[933,776,768],8163:[933,776,769],8164:[929,787],8165:8172,8166:[933,834],8167:[933,776,834],8178:[8186,921],8179:[937,921],8180:[911,921],8182:[937,834],8183:[937,834,921],8188:[937,921],8526:8498,8560:8544,8561:8545,8562:8546,8563:8547,8564:8548,8565:8549,8566:8550,8567:8551,8568:8552,8569:8553,8570:8554,8571:8555,8572:8556,8573:8557,8574:8558,8575:8559,8580:8579,9424:9398,9425:9399,9426:9400,9427:9401,9428:9402,9429:9403,9430:9404,9431:9405,9432:9406,9433:9407,9434:9408,9435:9409,9436:9410,9437:9411,9438:9412,9439:9413,9440:9414,9441:9415,9442:9416,9443:9417,9444:9418,9445:9419,9446:9420,9447:9421,9448:9422,9449:9423,11312:11264,11313:11265,11314:11266,11315:11267,11316:11268,11317:11269,11318:11270,11319:11271,11320:11272,11321:11273,11322:11274,11323:11275,11324:11276,11325:11277,11326:11278,11327:11279,11328:11280,11329:11281,11330:11282,11331:11283,11332:11284,11333:11285,11334:11286,11335:11287,11336:11288,11337:11289,11338:11290,11339:11291,11340:11292,11341:11293,11342:11294,11343:11295,11344:11296,11345:11297,11346:11298,11347:11299,11348:11300,11349:11301,11350:11302,11351:11303,11352:11304,11353:11305,11354:11306,11355:11307,11356:11308,11357:11309,11358:11310,11359:11311,11361:11360,11365:570,11366:574,11368:11367,11370:11369,11372:11371,11379:11378,11382:11381,11393:11392,11395:11394,11397:11396,11399:11398,11401:11400,11403:11402,11405:11404,11407:11406,11409:11408,11411:11410,11413:11412,11415:11414,11417:11416,11419:11418,11421:11420,11423:11422,11425:11424,11427:11426,11429:11428,11431:11430,11433:11432,11435:11434,11437:11436,11439:11438,11441:11440,11443:11442,11445:11444,11447:11446,11449:11448,11451:11450,11453:11452,11455:11454,11457:11456,11459:11458,11461:11460,11463:11462,11465:11464,11467:11466,11469:11468,11471:11470,11473:11472,11475:11474,11477:11476,11479:11478,11481:11480,11483:11482,11485:11484,11487:11486,11489:11488,11491:11490,11500:11499,11502:11501,11507:11506,11520:4256,11521:4257,11522:4258,11523:4259,11524:4260,11525:4261,11526:4262,11527:4263,11528:4264,11529:4265,11530:4266,11531:4267,11532:4268,11533:4269,11534:4270,11535:4271,11536:4272,11537:4273,11538:4274,11539:4275,11540:4276,11541:4277,11542:4278,11543:4279,11544:4280,11545:4281,11546:4282,11547:4283,11548:4284,11549:4285,11550:4286,11551:4287,11552:4288,11553:4289,11554:4290,11555:4291,11556:4292,11557:4293,11559:4295,11565:4301,42561:42560,42563:42562,42565:42564,42567:42566,42569:42568,42571:42570,42573:42572,42575:42574,42577:42576,42579:42578,42581:42580,42583:42582,42585:42584,42587:42586,42589:42588,42591:42590,42593:42592,42595:42594,42597:42596,42599:42598,42601:42600,42603:42602,42605:42604,42625:42624,42627:42626,42629:42628,42631:42630,42633:42632,42635:42634,42637:42636,42639:42638,42641:42640,42643:42642,42645:42644,42647:42646,42649:42648,42651:42650,42787:42786,42789:42788,42791:42790,42793:42792,42795:42794,42797:42796,42799:42798,42803:42802,42805:42804,42807:42806,42809:42808,42811:42810,42813:42812,42815:42814,42817:42816,42819:42818,42821:42820,42823:42822,42825:42824,42827:42826,42829:42828,42831:42830,42833:42832,42835:42834,42837:42836,42839:42838,42841:42840,42843:42842,42845:42844,42847:42846,42849:42848,42851:42850,42853:42852,42855:42854,42857:42856,42859:42858,42861:42860,42863:42862,42874:42873,42876:42875,42879:42878,42881:42880,42883:42882,42885:42884,42887:42886,42892:42891,42897:42896,42899:42898,42900:42948,42903:42902,42905:42904,42907:42906,42909:42908,42911:42910,42913:42912,42915:42914,42917:42916,42919:42918,42921:42920,42933:42932,42935:42934,42937:42936,42939:42938,42941:42940,42943:42942,42945:42944,42947:42946,42952:42951,42954:42953,42961:42960,42967:42966,42969:42968,42998:42997,43859:42931,43888:5024,43889:5025,43890:5026,43891:5027,43892:5028,43893:5029,43894:5030,43895:5031,43896:5032,43897:5033,43898:5034,43899:5035,43900:5036,43901:5037,43902:5038,43903:5039,43904:5040,43905:5041,43906:5042,43907:5043,43908:5044,43909:5045,43910:5046,43911:5047,43912:5048,43913:5049,43914:5050,43915:5051,43916:5052,43917:5053,43918:5054,43919:5055,43920:5056,43921:5057,43922:5058,43923:5059,43924:5060,43925:5061,43926:5062,43927:5063,43928:5064,43929:5065,43930:5066,43931:5067,43932:5068,43933:5069,43934:5070,43935:5071,43936:5072,43937:5073,43938:5074,43939:5075,43940:5076,43941:5077,43942:5078,43943:5079,43944:5080,43945:5081,43946:5082,43947:5083,43948:5084,43949:5085,43950:5086,43951:5087,43952:5088,43953:5089,43954:5090,43955:5091,43956:5092,43957:5093,43958:5094,43959:5095,43960:5096,43961:5097,43962:5098,43963:5099,43964:5100,43965:5101,43966:5102,43967:5103,64256:[70,70],64257:[70,73],64258:[70,76],64259:[70,70,73],64260:[70,70,76],64261:[83,84],64262:[83,84],64275:[1348,1350],64276:[1348,1333],64277:[1348,1339],64278:[1358,1350],64279:[1348,1341],65345:65313,65346:65314,65347:65315,65348:65316,65349:65317,65350:65318,65351:65319,65352:65320,65353:65321,65354:65322,65355:65323,65356:65324,65357:65325,65358:65326,65359:65327,65360:65328,65361:65329,65362:65330,65363:65331,65364:65332,65365:65333,65366:65334,65367:65335,65368:65336,65369:65337,65370:65338,66600:66560,66601:66561,66602:66562,66603:66563,66604:66564,66605:66565,66606:66566,66607:66567,66608:66568,66609:66569,66610:66570,66611:66571,66612:66572,66613:66573,66614:66574,66615:66575,66616:66576,66617:66577,66618:66578,66619:66579,66620:66580,66621:66581,66622:66582,66623:66583,66624:66584,66625:66585,66626:66586,66627:66587,66628:66588,66629:66589,66630:66590,66631:66591,66632:66592,66633:66593,66634:66594,66635:66595,66636:66596,66637:66597,66638:66598,66639:66599,66776:66736,66777:66737,66778:66738,66779:66739,66780:66740,66781:66741,66782:66742,66783:66743,66784:66744,66785:66745,66786:66746,66787:66747,66788:66748,66789:66749,66790:66750,66791:66751,66792:66752,66793:66753,66794:66754,66795:66755,66796:66756,66797:66757,66798:66758,66799:66759,66800:66760,66801:66761,66802:66762,66803:66763,66804:66764,66805:66765,66806:66766,66807:66767,66808:66768,66809:66769,66810:66770,66811:66771,66967:66928,66968:66929,66969:66930,66970:66931,66971:66932,66972:66933,66973:66934,66974:66935,66975:66936,66976:66937,66977:66938,66979:66940,66980:66941,66981:66942,66982:66943,66983:66944,66984:66945,66985:66946,66986:66947,66987:66948,66988:66949,66989:66950,66990:66951,66991:66952,66992:66953,66993:66954,66995:66956,66996:66957,66997:66958,66998:66959,66999:66960,67000:66961,67001:66962,67003:66964,67004:66965,68800:68736,68801:68737,68802:68738,68803:68739,68804:68740,68805:68741,68806:68742,68807:68743,68808:68744,68809:68745,68810:68746,68811:68747,68812:68748,68813:68749,68814:68750,68815:68751,68816:68752,68817:68753,68818:68754,68819:68755,68820:68756,68821:68757,68822:68758,68823:68759,68824:68760,68825:68761,68826:68762,68827:68763,68828:68764,68829:68765,68830:68766,68831:68767,68832:68768,68833:68769,68834:68770,68835:68771,68836:68772,68837:68773,68838:68774,68839:68775,68840:68776,68841:68777,68842:68778,68843:68779,68844:68780,68845:68781,68846:68782,68847:68783,68848:68784,68849:68785,68850:68786,71872:71840,71873:71841,71874:71842,71875:71843,71876:71844,71877:71845,71878:71846,71879:71847,71880:71848,71881:71849,71882:71850,71883:71851,71884:71852,71885:71853,71886:71854,71887:71855,71888:71856,71889:71857,71890:71858,71891:71859,71892:71860,71893:71861,71894:71862,71895:71863,71896:71864,71897:71865,71898:71866,71899:71867,71900:71868,71901:71869,71902:71870,71903:71871,93792:93760,93793:93761,93794:93762,93795:93763,93796:93764,93797:93765,93798:93766,93799:93767,93800:93768,93801:93769,93802:93770,93803:93771,93804:93772,93805:93773,93806:93774,93807:93775,93808:93776,93809:93777,93810:93778,93811:93779,93812:93780,93813:93781,93814:93782,93815:93783,93816:93784,93817:93785,93818:93786,93819:93787,93820:93788,93821:93789,93822:93790,93823:93791,125218:125184,125219:125185,125220:125186,125221:125187,125222:125188,125223:125189,125224:125190,125225:125191,125226:125192,125227:125193,125228:125194,125229:125195,125230:125196,125231:125197,125232:125198,125233:125199,125234:125200,125235:125201,125236:125202,125237:125203,125238:125204,125239:125205,125240:125206,125241:125207,125242:125208,125243:125209,125244:125210,125245:125211,125246:125212,125247:125213,125248:125214,125249:125215,125250:125216,125251:125217}

_LOWER_TRANSLATION = {65:97,66:98,67:99,68:100,69:101,70:102,71:103,72:104,73:105,74:106,75:107,76:108,77:109,78:110,79:111,80:112,81:113,82:114,83:115,84:116,85:117,86:118,87:119,88:120,89:121,90:122,192:224,193:225,194:226,195:227,196:228,197:229,198:230,199:231,200:232,201:233,202:234,203:235,204:236,205:237,206:238,207:239,208:240,209:241,210:242,211:243,212:244,213:245,214:246,216:248,217:249,218:250,219:251,220:252,221:253,222:254,256:257,258:259,260:261,262:263,264:265,266:267,268:269,270:271,272:273,274:275,276:277,278:279,280:281,282:283,284:285,286:287,288:289,290:291,292:293,294:295,296:297,298:299,300:301,302:303,304:[105,775],306:307,308:309,310:311,313:314,315:316,317:318,319:320,321:322,323:324,325:326,327:328,330:331,332:333,334:335,336:337,338:339,340:341,342:343,344:345,346:347,348:349,350:351,352:353,354:355,356:357,358:359,360:361,362:363,364:365,366:367,368:369,370:371,372:373,374:375,376:255,377:378,379:380,381:382,385:595,386:387,388:389,390:596,391:392,393:598,394:599,395:396,398:477,399:601,400:603,401:402,403:608,404:611,406:617,407:616,408:409,412:623,413:626,415:629,416:417,418:419,420:421,422:640,423:424,425:643,428:429,430:648,431:432,433:650,434:651,435:436,437:438,439:658,440:441,444:445,452:454,453:454,455:457,456:457,458:460,459:460,461:462,463:464,465:466,467:468,469:470,471:472,473:474,475:476,478:479,480:481,482:483,484:485,486:487,488:489,490:491,492:493,494:495,497:499,498:499,500:501,502:405,503:447,504:505,506:507,508:509,510:511,512:513,514:515,516:517,518:519,520:521,522:523,524:525,526:527,528:529,530:531,532:533,534:535,536:537,538:539,540:541,542:543,544:414,546:547,548:549,550:551,552:553,554:555,556:557,558:559,560:561,562:563,570:11365,571:572,573:410,574:11366,577:578,579:384,580:649,581:652,582:583,584:585,586:587,588:589,590:591,880:881,882:883,886:887,895:1011,902:940,904:941,905:942,906:943,908:972,910:973,911:974,913:945,914:946,915:947,916:948,917:949,918:950,919:951,920:952,921:953,922:954,923:955,924:956,925:957,926:958,927:959,928:960,929:961,931:963,932:964,933:965,934:966,935:967,936:968,937:969,938:970,939:971,975:983,984:985,986:987,988:989,990:991,992:993,994:995,996:997,998:999,1000:1001,1002:1003,1004:1005,1006:1007,1012:952,1015:1016,1017:1010,1018:1019,1021:891,1022:892,1023:893,1024:1104,1025:1105,1026:1106,1027:1107,1028:1108,1029:1109,1030:1110,1031:1111,1032:1112,1033:1113,1034:1114,1035:1115,1036:1116,1037:1117,1038:1118,1039:1119,1040:1072,1041:1073,1042:1074,1043:1075,1044:1076,1045:1077,1046:1078,1047:1079,1048:1080,1049:1081,1050:1082,1051:1083,1052:1084,1053:1085,1054:1086,1055:1087,1056:1088,1057:1089,1058:1090,1059:1091,1060:1092,1061:1093,1062:1094,1063:1095,1064:1096,1065:1097,1066:1098,1067:1099,1068:1100,1069:1101,1070:1102,1071:1103,1120:1121,1122:1123,1124:1125,1126:1127,1128:1129,1130:1131,1132:1133,1134:1135,1136:1137,1138:1139,1140:1141,1142:1143,1144:1145,1146:1147,1148:1149,1150:1151,1152:1153,1162:1163,1164:1165,1166:1167,1168:1169,1170:1171,1172:1173,1174:1175,1176:1177,1178:1179,1180:1181,1182:1183,1184:1185,1186:1187,1188:1189,1190:1191,1192:1193,1194:1195,1196:1197,1198:1199,1200:1201,1202:1203,1204:1205,1206:1207,1208:1209,1210:1211,1212:1213,1214:1215,1216:1231,1217:1218,1219:1220,1221:1222,1223:1224,1225:1226,1227:1228,1229:1230,1232:1233,1234:1235,1236:1237,1238:1239,1240:1241,1242:1243,1244:1245,1246:1247,1248:1249,1250:1251,1252:1253,1254:1255,1256:1257,1258:1259,1260:1261,1262:1263,1264:1265,1266:1267,1268:1269,1270:1271,1272:1273,1274:1275,1276:1277,1278:1279,1280:1281,1282:1283,1284:1285,1286:1287,1288:1289,1290:1291,1292:1293,1294:1295,1296:1297,1298:1299,1300:1301,1302:1303,1304:1305,1306:1307,1308:1309,1310:1311,1312:1313,1314:1315,1316:1317,1318:1319,1320:1321,1322:1323,1324:1325,1326:1327,1329:1377,1330:1378,1331:1379,1332:1380,1333:1381,1334:1382,1335:1383,1336:1384,1337:1385,1338:1386,1339:1387,1340:1388,1341:1389,1342:1390,1343:1391,1344:1392,1345:1393,1346:1394,1347:1395,1348:1396,1349:1397,1350:1398,1351:1399,1352:1400,1353:1401,1354:1402,1355:1403,1356:1404,1357:1405,1358:1406,1359:1407,1360:1408,1361:1409,1362:1410,1363:1411,1364:1412,1365:1413,1366:1414,4256:11520,4257:11521,4258:11522,4259:11523,4260:11524,4261:11525,4262:11526,4263:11527,4264:11528,4265:11529,4266:11530,4267:11531,4268:11532,4269:11533,4270:11534,4271:11535,4272:11536,4273:11537,4274:11538,4275:11539,4276:11540,4277:11541,4278:11542,4279:11543,4280:11544,4281:11545,4282:11546,4283:11547,4284:11548,4285:11549,4286:11550,4287:11551,4288:11552,4289:11553,4290:11554,4291:11555,4292:11556,4293:11557,4295:11559,4301:11565,5024:43888,5025:43889,5026:43890,5027:43891,5028:43892,5029:43893,5030:43894,5031:43895,5032:43896,5033:43897,5034:43898,5035:43899,5036:43900,5037:43901,5038:43902,5039:43903,5040:43904,5041:43905,5042:43906,5043:43907,5044:43908,5045:43909,5046:43910,5047:43911,5048:43912,5049:43913,5050:43914,5051:43915,5052:43916,5053:43917,5054:43918,5055:43919,5056:43920,5057:43921,5058:43922,5059:43923,5060:43924,5061:43925,5062:43926,5063:43927,5064:43928,5065:43929,5066:43930,5067:43931,5068:43932,5069:43933,5070:43934,5071:43935,5072:43936,5073:43937,5074:43938,5075:43939,5076:43940,5077:43941,5078:43942,5079:43943,5080:43944,5081:43945,5082:43946,5083:43947,5084:43948,5085:43949,5086:43950,5087:43951,5088:43952,5089:43953,5090:43954,5091:43955,5092:43956,5093:43957,5094:43958,5095:43959,5096:43960,5097:43961,5098:43962,5099:43963,5100:43964,5101:43965,5102:43966,5103:43967,5104:5112,5105:5113,5106:5114,5107:5115,5108:5116,5109:5117,7312:4304,7313:4305,7314:4306,7315:4307,7316:4308,7317:4309,7318:4310,7319:4311,7320:4312,7321:4313,7322:4314,7323:4315,7324:4316,7325:4317,7326:4318,7327:4319,7328:4320,7329:4321,7330:4322,7331:4323,7332:4324,7333:4325,7334:4326,7335:4327,7336:4328,7337:4329,7338:4330,7339:4331,7340:4332,7341:4333,7342:4334,7343:4335,7344:4336,7345:4337,7346:4338,7347:4339,7348:4340,7349:4341,7350:4342,7351:4343,7352:4344,7353:4345,7354:4346,7357:4349,7358:4350,7359:4351,7680:7681,7682:7683,7684:7685,7686:7687,7688:7689,7690:7691,7692:7693,7694:7695,7696:7697,7698:7699,7700:7701,7702:7703,7704:7705,7706:7707,7708:7709,7710:7711,7712:7713,7714:7715,7716:7717,7718:7719,7720:7721,7722:7723,7724:7725,7726:7727,7728:7729,7730:7731,7732:7733,7734:7735,7736:7737,7738:7739,7740:7741,7742:7743,7744:7745,7746:7747,7748:7749,7750:7751,7752:7753,7754:7755,7756:7757,7758:7759,7760:7761,7762:7763,7764:7765,7766:7767,7768:7769,7770:7771,7772:7773,7774:7775,7776:7777,7778:7779,7780:7781,7782:7783,7784:7785,7786:7787,7788:7789,7790:7791,7792:7793,7794:7795,7796:7797,7798:7799,7800:7801,7802:7803,7804:7805,7806:7807,7808:7809,7810:7811,7812:7813,7814:7815,7816:7817,7818:7819,7820:7821,7822:7823,7824:7825,7826:7827,7828:7829,7838:223,7840:7841,7842:7843,7844:7845,7846:7847,7848:7849,7850:7851,7852:7853,7854:7855,7856:7857,7858:7859,7860:7861,7862:7863,7864:7865,7866:7867,7868:7869,7870:7871,7872:7873,7874:7875,7876:7877,7878:7879,7880:7881,7882:7883,7884:7885,7886:7887,7888:7889,7890:7891,7892:7893,7894:7895,7896:7897,7898:7899,7900:7901,7902:7903,7904:7905,7906:7907,7908:7909,7910:7911,7912:7913,7914:7915,7916:7917,7918:7919,7920:7921,7922:7923,7924:7925,7926:7927,7928:7929,7930:7931,7932:7933,7934:7935,7944:7936,7945:7937,7946:7938,7947:7939,7948:7940,7949:7941,7950:7942,7951:7943,7960:7952,7961:7953,7962:7954,7963:7955,7964:7956,7965:7957,7976:7968,7977:7969,7978:7970,7979:7971,7980:7972,7981:7973,7982:7974,7983:7975,7992:7984,7993:7985,7994:7986,7995:7987,7996:7988,7997:7989,7998:7990,7999:7991,8008:8000,8009:8001,8010:8002,8011:8003,8012:8004,8013:8005,8025:8017,8027:8019,8029:8021,8031:8023,8040:8032,8041:8033,8042:8034,8043:8035,8044:8036,8045:8037,8046:8038,8047:8039,8072:8064,8073:8065,8074:8066,8075:8067,8076:8068,8077:8069,8078:8070,8079:8071,8088:8080,8089:8081,8090:8082,8091:8083,8092:8084,8093:8085,8094:8086,8095:8087,8104:8096,8105:8097,8106:8098,8107:8099,8108:8100,8109:8101,8110:8102,8111:8103,8120:8112,8121:8113,8122:8048,8123:8049,8124:8115,8136:8050,8137:8051,8138:8052,8139:8053,8140:8131,8152:8144,8153:8145,8154:8054,8155:8055,8168:8160,8169:8161,8170:8058,8171:8059,8172:8165,8184:8056,8185:8057,8186:8060,8187:8061,8188:8179,8486:969,8490:107,8491:229,8498:8526,8544:8560,8545:8561,8546:8562,8547:8563,8548:8564,8549:8565,8550:8566,8551:8567,8552:8568,8553:8569,8554:8570,8555:8571,8556:8572,8557:8573,8558:8574,8559:8575,8579:8580,9398:9424,9399:9425,9400:9426,9401:9427,9402:9428,9403:9429,9404:9430,9405:9431,9406:9432,9407:9433,9408:9434,9409:9435,9410:9436,9411:9437,9412:9438,9413:9439,9414:9440,9415:9441,9416:9442,9417:9443,9418:9444,9419:9445,9420:9446,9421:9447,9422:9448,9423:9449,11264:11312,11265:11313,11266:11314,11267:11315,11268:11316,11269:11317,11270:11318,11271:11319,11272:11320,11273:11321,11274:11322,11275:11323,11276:11324,11277:11325,11278:11326,11279:11327,11280:11328,11281:11329,11282:11330,11283:11331,11284:11332,11285:11333,11286:11334,11287:11335,11288:11336,11289:11337,11290:11338,11291:11339,11292:11340,11293:11341,11294:11342,11295:11343,11296:11344,11297:11345,11298:11346,11299:11347,11300:11348,11301:11349,11302:11350,11303:11351,11304:11352,11305:11353,11306:11354,11307:11355,11308:11356,11309:11357,11310:11358,11311:11359,11360:11361,11362:619,11363:7549,11364:637,11367:11368,11369:11370,11371:11372,11373:593,11374:625,11375:592,11376:594,11378:11379,11381:11382,11390:575,11391:576,11392:11393,11394:11395,11396:11397,11398:11399,11400:11401,11402:11403,11404:11405,11406:11407,11408:11409,11410:11411,11412:11413,11414:11415,11416:11417,11418:11419,11420:11421,11422:11423,11424:11425,11426:11427,11428:11429,11430:11431,11432:11433,11434:11435,11436:11437,11438:11439,11440:11441,11442:11443,11444:11445,11446:11447,11448:11449,11450:11451,11452:11453,11454:11455,11456:11457,11458:11459,11460:11461,11462:11463,11464:11465,11466:11467,11468:11469,11470:11471,11472:11473,11474:11475,11476:11477,11478:11479,11480:11481,11482:11483,11484:11485,11486:11487,11488:11489,11490:11491,11499:11500,11501:11502,11506:11507,42560:42561,42562:42563,42564:42565,42566:42567,42568:42569,42570:42571,42572:42573,42574:42575,42576:42577,42578:42579,42580:42581,42582:42583,42584:42585,42586:42587,42588:42589,42590:42591,42592:42593,42594:42595,42596:42597,42598:42599,42600:42601,42602:42603,42604:42605,42624:42625,42626:42627,42628:42629,42630:42631,42632:42633,42634:42635,42636:42637,42638:42639,42640:42641,42642:42643,42644:42645,42646:42647,42648:42649,42650:42651,42786:42787,42788:42789,42790:42791,42792:42793,42794:42795,42796:42797,42798:42799,42802:42803,42804:42805,42806:42807,42808:42809,42810:42811,42812:42813,42814:42815,42816:42817,42818:42819,42820:42821,42822:42823,42824:42825,42826:42827,42828:42829,42830:42831,42832:42833,42834:42835,42836:42837,42838:42839,42840:42841,42842:42843,42844:42845,42846:42847,42848:42849,42850:42851,42852:42853,42854:42855,42856:42857,42858:42859,42860:42861,42862:42863,42873:42874,42875:42876,42877:7545,42878:42879,42880:42881,42882:42883,42884:42885,42886:42887,42891:42892,42893:613,42896:42897,42898:42899,42902:42903,42904:42905,42906:42907,42908:42909,42910:42911,42912:42913,42914:42915,42916:42917,42918:42919,42920:42921,42922:614,42923:604,42924:609,42925:620,42926:618,42928:670,42929:647,42930:669,42931:43859,42932:42933,42934:42935,42936:42937,42938:42939,42940:42941,42942:42943,42944:42945,42946:42947,42948:42900,42949:642,42950:7566,42951:42952,42953:42954,42960:42961,42966:42967,42968:42969,42997:42998,65313:65345,65314:65346,65315:65347,65316:65348,65317:65349,65318:65350,65319:65351,65320:65352,65321:65353,65322:65354,65323:65355,65324:65356,65325:65357,65326:65358,65327:65359,65328:65360,65329:65361,65330:65362,65331:65363,65332:65364,65333:65365,65334:65366,65335:65367,65336:65368,65337:65369,65338:65370,66560:66600,66561:66601,66562:66602,66563:66603,66564:66604,66565:66605,66566:66606,66567:66607,66568:66608,66569:66609,66570:66610,66571:66611,66572:66612,66573:66613,66574:66614,66575:66615,66576:66616,66577:66617,66578:66618,66579:66619,66580:66620,66581:66621,66582:66622,66583:66623,66584:66624,66585:66625,66586:66626,66587:66627,66588:66628,66589:66629,66590:66630,66591:66631,66592:66632,66593:66633,66594:66634,66595:66635,66596:66636,66597:66637,66598:66638,66599:66639,66736:66776,66737:66777,66738:66778,66739:66779,66740:66780,66741:66781,66742:66782,66743:66783,66744:66784,66745:66785,66746:66786,66747:66787,66748:66788,66749:66789,66750:66790,66751:66791,66752:66792,66753:66793,66754:66794,66755:66795,66756:66796,66757:66797,66758:66798,66759:66799,66760:66800,66761:66801,66762:66802,66763:66803,66764:66804,66765:66805,66766:66806,66767:66807,66768:66808,66769:66809,66770:66810,66771:66811,66928:66967,66929:66968,66930:66969,66931:66970,66932:66971,66933:66972,66934:66973,66935:66974,66936:66975,66937:66976,66938:66977,66940:66979,66941:66980,66942:66981,66943:66982,66944:66983,66945:66984,66946:66985,66947:66986,66948:66987,66949:66988,66950:66989,66951:66990,66952:66991,66953:66992,66954:66993,66956:66995,66957:66996,66958:66997,66959:66998,66960:66999,66961:67000,66962:67001,66964:67003,66965:67004,68736:68800,68737:68801,68738:68802,68739:68803,68740:68804,68741:68805,68742:68806,68743:68807,68744:68808,68745:68809,68746:68810,68747:68811,68748:68812,68749:68813,68750:68814,68751:68815,68752:68816,68753:68817,68754:68818,68755:68819,68756:68820,68757:68821,68758:68822,68759:68823,68760:68824,68761:68825,68762:68826,68763:68827,68764:68828,68765:68829,68766:68830,68767:68831,68768:68832,68769:68833,68770:68834,68771:68835,68772:68836,68773:68837,68774:68838,68775:68839,68776:68840,68777:68841,68778:68842,68779:68843,68780:68844,68781:68845,68782:68846,68783:68847,68784:68848,68785:68849,68786:68850,71840:71872,71841:71873,71842:71874,71843:71875,71844:71876,71845:71877,71846:71878,71847:71879,71848:71880,71849:71881,71850:71882,71851:71883,71852:71884,71853:71885,71854:71886,71855:71887,71856:71888,71857:71889,71858:71890,71859:71891,71860:71892,71861:71893,71862:71894,71863:71895,71864:71896,71865:71897,71866:71898,71867:71899,71868:71900,71869:71901,71870:71902,71871:71903,93760:93792,93761:93793,93762:93794,93763:93795,93764:93796,93765:93797,93766:93798,93767:93799,93768:93800,93769:93801,93770:93802,93771:93803,93772:93804,93773:93805,93774:93806,93775:93807,93776:93808,93777:93809,93778:93810,93779:93811,93780:93812,93781:93813,93782:93814,93783:93815,93784:93816,93785:93817,93786:93818,93787:93819,93788:93820,93789:93821,93790:93822,93791:93823,125184:125218,125185:125219,125186:125220,125187:125221,125188:125222,125189:125223,125190:125224,125191:125225,125192:125226,125193:125227,125194:125228,125195:125229,125196:125230,125197:125231,125198:125232,125199:125233,125200:125234,125201:125235,125202:125236,125203:125237,125204:125238,125205:125239,125206:125240,125207:125241,125208:125242,125209:125243,125210:125244,125211:125245,125212:125246,125213:125247,125214:125248,125215:125249,125216:125250,125217:125251}
