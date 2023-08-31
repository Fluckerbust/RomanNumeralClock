roman = {
  "I" : "1",
  "II" : "2",
  "III" : " 3",
  "IV" : " 4",
  "V" : " 5",
  "VI" : " 6", 
  "VII" : "7",
  "VIII" : "8",
  "IX" : "9",
  "X" : "10",
  "XI" : "11",
  "XII" : "12",
  "XIII" : "13",
  "XIV" : "14",
  "XV" : "15",
  "XVI" : "16",
  "XVII" : "17",
  "XVIII": "18",
  "XIX":"19",
  "XX" : "20",
  "XXI" : "21",
  "XXII" : "22",
  "XXIII" : "23",
  "XXIV" : "24",
  "XXV" : "25",
  "XXVI" : "26",
  "XXVII" : "27",
  "XXVIII" : "28",
  "XXIX" : "29",
  "XXX" : "30",
  "XXXI" : "31",
  "XXXII" : "32",
  "XXXIII" : "33",
  "XXXIV" : "34",
  "XXXV" : "35",
  "XXXVI" : "36",
  "XXXVII" : "37",
  "XXXVIII" : "38",
  "XXXIX" : "39",
  "XL" : "40",
  "XLI" : "41",
  "XLII" : "42",
  "XLIII" : "43",
  "XLIV" : "44",
  "XLV" : "45",
  "XLVI" : "46",
  "XLVII" : "47",
  "XLVIII" : "48",
  "XLIX" : "49",
  "L" : "50",
  "LI" : "51",
  "LII" : "52",
  "LIII" : "53",
  "LIV" : "54",
  "LV" : "55",
  "LVI" : "56",
  "LVII" : "57",
  "LVIII" : "58",
  "LIX" : "59",
  
 
}

nums = {
  "1" : "I",
  "2" : "II",
  "3" : "III",
  "4" : "IV",
  "5" : "V",
  "6" : "VI",
  "7" : "VII",
  "8" : "VIII",
  "9" : "IX",
  "10" : "X",
  "11" : "XI",
  "12" : "XII",
  "13" : "XIII",
  "14" : "XIV",
  "15" : "XV",
  "16" : "XVI",
  "17" : "XVII",
  "18" : "XVIII",
  "19" : "XIX",
  "20" : "XX",
  "21" : "XXI",
  "22" : "XXII",
  "23" : "XXIII",
  "24" : "XXIVXX",
  "25" : "XXV",
  "26" : "XXVI",
  "27" : "XXVII",
  "28" : "XXVIII",
  "29" : "XXIX",
  "30" : "XXX",
  "31" : "XXXI",
  "32" : "XXXII",
  "33" : "XXXIII",
  "34" : "XXXIV",
  "35" : "XXXV",
  "36" : "XXXVI",
  "37" : "XXXVII",
  "38" : "XXXVIII",
  "39" : "XXXIX",
  "40" : "XL" ,
  "41" : "XLI",
  "42" : "XLII" ,
  "44" : "XLIV ",
  "45" : "XLV ",
  "47" : "XLVII ",
  "48" : "XLVIII ",
  "50" : "L ",
  "51" : "LI ",
  "52" : "LII ",
  "53" : "LIII ",
  "54" : "LIV" ,
  "55" : "LV ",
  "56" : "LVI ",
  "57" : "LVII ",
  "58" : "LVIII ",
  "59" : "LIX ",
  
} 
def roman_numerals(hr, min):
  lowhour = str(hr)
  lowminute = str(min)
  hour = lowhour.upper()
  minute = lowminute.upper()
  if hour in roman.keys():
    print(roman[hour] + ":" + roman[minute])
  else:  print(nums[hour] + ":" + nums[minute])
    
          
          

roman_numerals(5,20)

roman_numerals(15, 59)
roman_numerals(10, 50)

roman_numerals(1, 4)

roman_numerals("XII", "LIX")
roman_numerals("XIV", "XV")
roman_numerals("IV", "xx")

