import ephem

gatech = ephem.Observer()
gatech.lon, gatech.lat = '-84.39733', '33.775867'
gatech.date = '1984/5/30 16:22:56'
iss = ephem.readtle("ISS (ZARYA)",
 "1 25544U 98067A   03097.78853147  .00021906  00000-0  28403-3 0  8652",
 "2 25544  51.6361  13.7980 0004256  35.6671  59.2566 15.58778559250029")
gatech.date = '2003/3/23'
iss.compute(gatech)
print('%s %s' % (iss.alt, iss.az))
info = gatech.next_pass(iss)
print("Rise time: %s azimuth: %s" % (info[0], info[1]))
