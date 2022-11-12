import datetime

def lam_net_anh(link, so):

    # link = //upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/23px-Flag_of_Serbia.svg.png
    # so = 500

    a = link.split('/')[-1]  # a = 23px-Flag_of_Serbia.svg.png

    b = a.split('px')  # b = [23, -Flag_of_Serbia.svg.png]
    b[0] = so  # b = [500, -Flag_of_Serbia.svg.png]
    b = b[0] + 'px' + b[1]  # b = 500px-Flag_of_Serbia.svg.png

    link_moi = link.replace(a, b)
    # link_moi = //upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/500px-Flag_of_Serbia.svg.png

    return link_moi

def formatTime(date,time,utc):
    date=date.split('-')
    time=time.split(':')
    cr=datetime.datetime( int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]))
    cr=cr+datetime.timedelta(hours=+(7-int(utc[3:])))
    return str(cr)