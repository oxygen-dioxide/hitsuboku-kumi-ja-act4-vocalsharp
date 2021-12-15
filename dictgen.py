orig={"あ":"a",
"い":"i",
"う":"u",
"え":"e",
"お":"o",
"か":"ka",
"き":"ki",
"く":"ku",
"け":"ke",
"こ":"ko",
"さ":"sa",
"すぃ":"si",
"す":"su",
"せ":"se",
"そ":"so",
"た":"ta",
"てぃ":"ti",
"とぅ":"tu",
"て":"te",
"と":"to",
"な":"na",
"に":"ni",
"ぬ":"nu",
"ね":"ne",
"の":"no",
"は":"ha",
"ひ":"hi",
"ふ":"hu",
"へ":"he",
"ほ":"ho",
"ま":"ma",
"み":"mi",
"む":"mu",
"め":"me",
"も":"mo",
"や":"ya",
"ゆ":"yu",
"よ":"yo",
"ら":"ra",
"り":"ri",
"る":"ru",
"れ":"re",
"ろ":"ro",
"わ":"wa",
"うぉ":"wo",
"を":"o",
"が":"ga",
"ぎ":"gi",
"ぐ":"gu",
"げ":"ge",
"ご":"go",
"ざ":"za",
"ずぃ":"zi",
"ず":"zu",
"ぜ":"ze",
"ぞ":"zo",
"だ":"da",
"でぃ":"di",
"どぅ":"du",
"で":"de",
"ど":"do",
"ば":"ba",
"び":"bi",
"ぶ":"bu",
"べ":"be",
"ぼ":"bo",
"ぱ":"pa",
"ぴ":"pi",
"ぷ":"pu",
"ぺ":"pe",
"ぽ":"po",
"きゃ":"kya",
"きゅ":"kyu",
"きょ":"kyo",
"しゃ":"sha",
"し":"shi",
"しゅ":"shu",
"しょ":"sho",
"ちゃ":"cha",
"ち":"chi",
"ちゅ":"chu",
"ちょ":"cho",
"つぁ":"tsa",
"つぃ":"tsi",
"つ":"tsu",
"つぇ":"tse",
"つぉ":"tso",
"にゃ":"nya",
"にゅ":"nyu",
"にょ":"nyo",
"ひゃ":"hya",
"ひゅ":"hyu",
"ひょ":"hyo",
"ふぁ":"fa",
"ふぃ":"fi",
"ふぇ":"fe",
"ふぉ":"fo",
"みゃ":"mya",
"みゅ":"myu",
"みょ":"myo",
"りゃ":"rya",
"りゅ":"ryu",
"りょ":"ryo",
"ぎゃ":"gya",
"ぎゅ":"gyu",
"ぎょ":"gyo",
"じゃ":"ja",
"じ":"ji",
"じゅ":"ju",
"じょ":"jo",
"びゃ":"bya",
"びゅ":"byu",
"びょ":"byo",
"ぴゃ":"pya",
"ぴゅ":"pyu",
"ぴょ":"pyo",
"ん":"n",
}
import json
exp=orig.copy()
for i in list(exp.values()):
    if(not(i in exp)):
        exp[i]=i
with open("main.lsd","w",encoding="utf8") as dictfile:
    for(key,value) in exp.items():
        dictfile.write("{}\n#{}\n".format(key,value))
#生成替换表
vmconvert={
    "Calias":{value:key for (key,value) in orig.items()}|{"":"-"},
    "Valias":{i:i[-1] for i in list(orig.values())}|{"":"-"}
}
with open("vmconvert.json","w",encoding="utf8") as vmconvertfile:
    json.dump(vmconvert,vmconvertfile,ensure_ascii=False,indent=4)     