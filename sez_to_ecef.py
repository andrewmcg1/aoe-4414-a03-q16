# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Andrew McGrellis
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv
import numpy as np

# "constants"
R_E_KM = 6378.1363
EE_E    = 0.081819221456

# helper functions


## function description
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
if len(sys.argv)==7:
  o_lat_deg = float(sys.argv[1])
  o_lon_deg = float(sys.argv[2])
  o_hae_km = float(sys.argv[3])
  s_km = float(sys.argv[4])
  e_km = float(sys.argv[5])
  z_km = float(sys.argv[6])
  ...
else:
  print(\
   'Usage: '\
   'python3 arg1 arg2 ...'\
  )
  exit()

# write script below this line

o_lat_rad = math.radians(o_lat_deg)
o_lon_rad = math.radians(o_lon_deg)

r_y_km = np.array([[math.sin(o_lat_rad),   0, math.cos(o_lat_rad)], 
                   [0,                     1, 0                  ],    
                   [-math.cos(o_lat_rad),  0, math.sin(o_lat_rad)]])
r_z_km = np.array([[math.cos(o_lon_rad),  -math.sin(o_lon_rad), 0],
                   [math.sin(o_lon_rad),   math.cos(o_lon_rad), 0],
                   [0,                     0,                   1]])

r_ecef = np.array([[s_km], [e_km], [z_km]])
r_ecef = r_y_km.dot(r_ecef)
r_ecef = r_z_km.dot(r_ecef)

c_e = R_E_KM / calc_denom(EE_E, o_lat_rad)
s_e = c_e * (1.0 - EE_E**2)

ecef_x_km = (c_e + o_hae_km) * math.cos(o_lat_rad) * math.cos(o_lon_rad) + r_ecef[0]
ecef_y_km = (c_e + o_hae_km) * math.cos(o_lat_rad) * math.sin(o_lon_rad) + r_ecef[1]
ecef_z_km = (s_e + o_hae_km) * math.sin(o_lat_rad) + r_ecef[2]

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)


