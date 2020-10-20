# beautiful_year.py
# Valeria Lucio Rangel
# A01411381

def btfl_yr(yr):
    if 1000 <= yr <= 9000:
        while True:
            yr += 1
            byr = str(yr)
            if byr[0] != byr[1] and byr[0] != byr[2] and byr[0] != byr[3] and byr[1] != byr[2] and byr[1] != byr[3] and byr[2] != byr[3]:
                return byr
            else:
                int(byr)
                
yr = int(input())
print(btfl_yr(yr))