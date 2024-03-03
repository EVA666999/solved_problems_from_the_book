mouth_list_no = 'января февраля мартa апреля майа июня июля августа сентября октября ноября декабря'
mouth_list_ye = mouth_list_no.split()
date = '12/05/2018'
real_date = date.split('/')
if '01' in real_date[1]:
    real_date[1] = mouth_list_ye[0]
    nd = date.replace('01', real_date[1])
elif '02' in real_date[1]:
    real_date[1] = mouth_list_ye[1]
    nd = date.replace('02', real_date[1])
elif '03' in real_date[1]:
    real_date[1] = mouth_list_ye[2]
    nd = date.replace('03', real_date[1])
elif '04' in real_date[1]:
    real_date[1] = mouth_list_ye[3]
    nd = date.replace('04', real_date[1])
elif '05' in real_date[1]:
    real_date[1] = mouth_list_ye[4]
    nd = date.replace('05', real_date[1])
elif '06' in real_date[1]:
    real_date[1] = mouth_list_ye[5]
    nd = date.replace('06', real_date[1])
elif '07' in real_date[1]:
    real_date[1] = mouth_list_ye[6]
    nd = date.replace('07', real_date[1])
elif '08' in real_date[1]:
    real_date[1] = mouth_list_ye[7]
    nd = date.replace('08', real_date[1])
elif '09' in real_date[1]:
    real_date[1] = mouth_list_ye[8]
    nd = date.replace('09', real_date[1])
elif '10' in real_date[1]:
    real_date[1] = mouth_list_ye[9]
    nd = date.replace('10', real_date[1])
elif '11' in real_date[1]:
    real_date[1] = mouth_list_ye[10]
    nd = date.replace('11', real_date[1])
elif '12' in real_date[1]:
    real_date[1] = mouth_list_ye[11]
    nd = date.replace('12', real_date[1])
print(nd + 'Г')