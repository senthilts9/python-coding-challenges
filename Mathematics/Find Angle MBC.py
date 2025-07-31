# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def find_angle_mbc(ab,bc):
    angle_acb_rad = math.atan2(ab,bc)
    
    angle_mbc_rad = angle_acb_rad  
    
    angle_mbc_deg = math.degrees(angle_mbc_rad)
    
    return round(angle_mbc_deg)
    

ab = int(input())
bc = int(input())

angle_mbc = find_angle_mbc(ab,bc)
print(f"{angle_mbc}\u00B0")
