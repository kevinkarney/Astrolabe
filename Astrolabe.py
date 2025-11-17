# SPDX-License-Identifier: CC0-1.0
# this software released into the public domain under CC0 1.0

# It follows the equations in the previous chapter.
# It prints - to the Python console - tab-delimited output that can be
# copy and pasted into any spreadsheet.

from math import degrees, radians, tan, sin, asin, cos, sqrt
Obliquity             = 23.43  # degrees
Latitude              = 51.75  # degrees
Capric_r              = 10     # radius of Tympanum
Amulcantar_division   = 15     # Amulcantar every n degrees
Azimuth_division      = 15     # Azimuth every n degree
Ecliptic_Circle_Width = 1      #  something around 5-10% of Capric_r 

# These are the Right Ascension & Declinations of the 14 brightest stars 
# in the Northern Hemishpere
Stars = [
['Altair',297.695827,8.868321],['Algol',47.042218,40.955646],
['Aldebaran',68.980163,16.509302],['Baten Kaitos',26.017354,-10.335044],
['Procyon',114.825497,5.224987],['Sirius',101.287155,-16.716116],
['Alphard',141.896847,-8.658602],['Deneb',310.357979,45.280338],
['Diphda',10.897379,-17.986606],['Vega',279.234735,38.783689],
['Alkaid',206.885157,49.313268],['Alphecca',233.672213,26.714693],
['Spica',201.298247,-11.161319],['Capella',79.172328,45.997991]]
    
def Calculate():
    print('BASIC CIRCLES')
    print('\tx\ty\tr')

    Scale             = (1 - sind(Obliquity)) / cosd(Obliquity)
    Equator_r         = Capric_r * Scale
    Cancer_r          = Capric_r * Scale**2
    
    Horizon_x         = 0
    Horizon_y         = Capric_r * Scale / tand(Latitude)
    Horizon_r         = Capric_r * Scale / sind(Latitude)
    
    Zenith_x          = 0
    Zenith_y          = Capric_r * Scale * tand((90-Latitude)/2)
    print('Capricorn\t0\t0'+ abc(Capric_r)) 
    print('Equator\t0\t0'  + abc(Equator_r)) 
    print('Cancer\t0\t0'   + abc(Cancer_r))
    print('Horizon\t0'     + abc(Horizon_y) + abc(Horizon_r)) 
    print('Zenith\t0'      + abc(Zenith_y)  + abc(0)) 
    
    print('ALMUCANTARS')
    print('Altitude\tx\ty\tr')
    for altitude in range(0,89,Amulcantar_division):
        aaa = sind(Latitude) + sind(altitude)
        Alt_x = 0
        Alt_y = Equator_r * cosd(Latitude)  / aaa
        Alt_r = Equator_r * cosd(altitude ) / aaa
        
        print(str(altitude) + abc(Alt_x) + abc(Alt_y) + abc(Alt_r))

    print('AZIMUTHS')
    print('Azimuth\tx\ty\tr')
    for i in range(0,180,Azimuth_division):
        Azimuth_y = Zenith_y/2 - Equator_r**2/(2*Zenith_y)
        Azimuth_x = (Zenith_y - Azimuth_y)* tand(i)
        Azimuth_r = (Zenith_y - Azimuth_y)/cosd(i)
        if i != 90:
            print(str(i) + abc(Azimuth_x) + abc(Azimuth_y) + abc(Azimuth_r))
        else:
            print(str(i) + '\t vertical line through origin')
            

    print('UNEQUAL HOURS')
    print('Hour from Noon\tx\ty\tr')
    bbb                      = (Horizon_r**2 - Cancer_r**2 + Horizon_y**2) / (2*Horizon_y)
    ccc                      = sqrt(Horizon_r**2 - bbb**2)
    Arc_Noon_to_Cancer       = degrees(asin(ccc/Cancer_r))
    Angle_per_Hour_Cancer    = Arc_Noon_to_Cancer/6
    for Hours_from_Noon in range(-5,6,1):
        if Hours_from_Noon != 0:
            ddd           = (Equator_r**2 - Cancer_r**2)/(2 * Cancer_r * sind(Hours_from_Noon*(15 - Angle_per_Hour_Cancer)))
            Unequal_x     = ddd*cosd(15*Hours_from_Noon)
            Unequal_y     = ddd*sind(15*Hours_from_Noon)
            Unequal_r     = sqrt(Equator_r**2+ddd**2)
            print(str(Hours_from_Noon) + abc(Unequal_x) + abc(Unequal_y) + abc(Unequal_r))
    
    print('RETE ECLIPTIC CIRCLE')
    Rete_x                   = 0   
    Rete_y                   = (Capric_r - Cancer_r)/2
    Rete_r                   = (Capric_r + Cancer_r)/2
    print('\tx\ty\tr')
    print(abc(Rete_x) + abc(Rete_y) +abc(Rete_r))
    print('ECLIPTIC CIRCLE ZODIAC LINES')
    print('Zodiac Angle\touter-x\touter-y\tinner-x\tinner-y')
    for i in range(0,360,30):
        sig = 1 if i <= 90 or i > 270 else -1
        for j in range(2):
            radius = Rete_r if j == 0 else Rete_r - Ecliptic_Circle_Width
            eee                      = tand(i)
            fff                      = 1 + eee**2
            ggg                      = -2 * Rete_y * eee
            hhh                      = Rete_y**2 - radius**2
            iii                      = sqrt(ggg**2 - 4 * fff * hhh)
            ZodiacCircle_x           = (-ggg + sig * iii)/(2*fff)
            ZodiacCircle_y           = eee*ZodiacCircle_x
            if j == 0 :
                x_outer,y_innner          = ZodiacCircle_x,ZodiacCircle_x
                Record = str(i) + abc(ZodiacCircle_x) + abc(ZodiacCircle_y)
            else:
                Record = Record + abc(ZodiacCircle_x) + abc(ZodiacCircle_y)+'\r'
        print(Record)

    print('STAR POINTERS')
    print('Name\tx\ty')
    for i in range(len(Stars)):
        this_star = Stars[i]
        Name = this_star[0]
        RA   = this_star[1]
        Decl = this_star[2]
        jjj                      = -tand(45 - Decl/2) / tand(45+Obliquity/2)
        Star_x                   = Capric_r * jjj * cosd(RA)
        Star_y                   = Capric_r * jjj * sind(RA)
        print(Name + abc(Star_x) + abc(Star_y))

def abc(val):
    # Subroutine to produce tab-delimited printed 
    # output that can be copied direcetly into
    # a spreadsheet
    return('\t' + str(round(val,3)))
def tand(a):
    return tan(radians(a))
def cosd(a):
    return cos(radians(a))
def sind(a):
    return sin(radians(a))
 
Calculate()

