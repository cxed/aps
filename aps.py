#!/usr/bin/python3
'''Takes input from the `iwlist wlan0 scanning` command and sorts it out.'''

import subprocess

# Interface
IF='wlp2s0b1'
#IF='wlan0'
CMD=['/sbin/iwlist', IF, 'scanning']

class AP:
    def __init__(self,C,A):
        self.cellnum= C     # 17
        self.address= A.replace(':','') # No need for MAC colons.
        self.channel= '?'    # "11"
        self.freq= '?'       # "2.462 GHz"
        self.quality= '?'    # "23/70"
        self.sig_lvl= '?'    #"-87 dBm"
        self.essid= '?'      # "UCSD-GUEST"
        self.mode= '?'       # "Master"
        self.bitrates= '?'   # "6 Mb/s; 9Mb/s; 12 Mb/s; ... 54 Mb/s"
        self.enckey= '?'     # "on"

    def __repr__(self):
        o= list()
        o.append(self.cellnum)
        o.append(self.address)
        o.append(self.channel)
        o.append(self.freq)
        o.append(self.quality)
        o.append(self.sig_lvl)
        o.append(self.enckey)
        o.append(self.mode)
        o.append(self.essid)
        return '|'.join(o)

    def build(self,l):
        '''Takes a line of input and properly adds it to object.'''
        if 'Channel:' in l:
            self.channel= l.split(':')[1]
        if 'Frequency:' in l:
            self.freq= l.split(':')[1].split(' ')[0]
        if 'Quality=' in l:
            qparts= l.strip().split(' ')
            self.quality= qparts[0].split('=')[1]
            if 'Signal level=' in l:
                self.sig_lvl= qparts[3].split('=')[1]+'dBm'
        if 'ESSID:' in l:
            self.essid= l.split(':')[1].replace('"','')
        if 'Encryption key:' in l:
            self.enckey= l.split(':')[1]
            if 'on' in self.enckey:
                self.enckey= 'E'
            else:
                self.enckey= 'e'
        if 'Mode:' in l:
            self.mode= l.split(':')[1]
            
if __name__ == '__main__':
    cell= None # Start with no objects to signal none in progress.
    import io
    proc= subprocess.Popen(CMD,stdout=subprocess.PIPE)
    for oo in io.TextIOWrapper(proc.stdout, encoding="utf-8"): 
        o= oo.strip()
        if 'Cell' in o: # Output shows a new "Cell ##" record?
            if cell: # Need to close out the previous one if extant.
                print(cell)
            parts= o.strip().split(' ')    # Parse this line.
            cell= AP( parts[1], parts[4] ) # Start a new cell object.
        if cell:
            cell.build(o)
    print(cell)
