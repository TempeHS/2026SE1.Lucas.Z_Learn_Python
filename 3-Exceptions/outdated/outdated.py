while True:
    try:
        date = input("MM/DD/YYYY")
        date = date.split('/')
        match date[0]:
            case '01'|'Januart':
                date[0] = '1'
            case '02'|'February':
                date[0] = '2'
            case '03'|'March':
                date[0] = '3'
            case '04'|'April':
                date[0] = '4'
            case '05'|'May':
                date[0] = '5'
            case '06'|'June':
                date[0] = '6'
            case '07'|'July':
                date[0] = '7'
            case '08'|'August':
                date[0] = '8'
            case '09'|'September':
                date[0] = '9'
            case '10'|'October':
                date[0] = '10'
            case '11'|'November':
                date[0] = '11'
            case '12'|'December':
                date[0] = '12'
        if int(date[0])>12 or int(date[1])>31:
            continue
        print(date[2]+'-'+date[0]+'-'+date[1])
        break
    except (ValueError, IndexError):
        pass
