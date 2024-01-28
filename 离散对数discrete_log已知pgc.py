p = 173383907346370188246634353442514171630882212643019826706575120637048836061602034776136960080336351252616860522273644431927909101923807914940397420063587913080793842100264484222211278105783220210128152062330954876427406484701993115395306434064667136148361558851998019806319799444970703714594938822660931343299
g = 5
c = 105956730578629949992232286714779776923846577007389446302378719229216496867835280661431342821159505656015790792811649783966417989318584221840008436316642333656736724414761508478750342102083967959048112859470526771487533503436337125728018422740023680376681927932966058904269005466550073181194896860353202252854
from Crypto.Util.number import *
from tqdm import *

table = "0123456789abcdef"

ii=12
lengthpad = 128-ii-6
padding = bytes_to_long(b"flag{"+b'x00'*ii+b"}"+(chr(lengthpad)*lengthpad).encode())
#pad_inv = inverse(padding，p-1)
ctmp = c * (pow(g,-padding,p))%p
for _ in range(lengthpad*8+8):
    ctmp = pow(ctmp,(p+3)//4,p)

mh={}
for i in tqdm(table):
    for j in table:
        for k in table:
            for l in table:
                for m in table:
                    for n in table:
                        mm = i+j+k+l+m+n
                        mm = mm.encode()
                        mm = bytes_to_long(mm)*1<<((ii//2)*8)
                        mh[pow(g,mm,p)] = mm

ml={}
for i in tqdm(table):
    for j in table:
        for k in table:
            for l in table:
                for m in table:
                    for n in table:
                        mm = i+j+k+l+m+n
                        mm = mm.encode()
                        mm = bytes_to_long(mm)
                        if ctmp*pow(g,-mm,p) in mh:
                            print(mh[ctmp*pow(g,-mm,p)])
                            print(mm)
