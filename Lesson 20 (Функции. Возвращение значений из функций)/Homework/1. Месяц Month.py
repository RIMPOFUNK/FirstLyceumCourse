def month_name(num, lang):
    rus = {0: "январь",
           1: "февраль",
           2: "март",
           3: "апрель",
           4: "май",
           5: "июнь",
           6: "июль",
           7: "август",
           8: "сентябрь",
           9: "октябрь",
           10: "ноябрь",
           11: "декабрь"}
    
    eng = {0: "january",
           1: "February",
           2: "March",
           3: "April",
           4: "May",
           5: "June",
           6: "July",
           7: "August",
           8: "september",
           9: "october ",
           10: "november",
           11: "december"}
    
    if lang == "ru":
        return rus[num - 1]
    return eng[num - 1].lower()
