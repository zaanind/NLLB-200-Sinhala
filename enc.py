KLBhDR = "vQspNjj0tzz"
CUxxQd = "qvTaordwvflMtvo02GhFifRztl"
import argparse
LpNdmhETayFu = "YzNlZo"
HmqIdWIVWisxjHGnxU = "Qnu50y0F3eEXNarPKZV8gjzUbICID"
gnTRpm = "fRRjy1kR"
TxrLwfNnDpsgOEIUg = LpNdmhETayFu
import requests
vysttuoBcJ = "W4U1N7Zd"
fyskuiJucJ = "W4Eu1Nn7Z"
jyhkuOBcJ = "s4Eo1NfZ"
ifskugGBcJ = "W4E1e7Z"
oyskgulkcJ = "W4E1t7Z"
lysioiuBcJ = "r4E1N7Z"
pysnaPtuBcJ = "W4E1N7Z"
kyHskunetcJ = "n4EoN7Z"
RfgsdVrBVzSFDgw = vysttuoBcJ[2] + jyhkuOBcJ[0] + ifskugGBcJ[4] + lysioiuBcJ[0]
oKskYulJcT = kyHskunetcJ[0] + kyHskunetcJ[3]+ oyskgulkcJ[4]

import importlib.util
jZrfllvam = "lJipC3ys04Nn"
XVKzSFBRlBCns = "2aybq"
PrVaFs = "hCY1i6c"
TFZmSkAGGwjRS = "YbqMPTyTP5kq"
ORrEtKoF = [ '300','652','453','200','213','511','404','406','543','402' ]
BgUhQfcPACnwspyMCMAa = "Dadfto2AViQsZsK3fMYYtlQjQew"
import os, sys,re,subprocess, json
from tqdm import tqdm

def QWVVGRZNUG(LSWBBVBHZPMSW, WZOFJJFCGPUE, AUIUYOLWIP):
    duration_re = re.compile(r'Duration: (\d+):(\d+):(\d+)\.(\d+)')
    Rwrzcho = "TlGBZvzV3jTV3IEM2kKzS3diBrpajF"
    kZwuwLZOaOLgGl = "PGqYMC7c1kO99VYFemEeE5hj"
    yKXkkeA = ORrEtKoF
    ZUxRibCEu = kZwuwLZOaOLgGl
    re_progress = re.compile(r'time=(\d+):(\d+):(\d+)\.(\d+)')

    process = subprocess.Popen(
        [
            'ffmpeg',
            '-hwaccel', 'cuda',
            '-i', LSWBBVBHZPMSW,
            '-vf', f'ass={WZOFJJFCGPUE}' ,
            '-c:v', 'h264_nvenc',
            '-preset', 'fast',
            '-c:a', 'copy',
            '-threads', '4',
            '-disposition:a:0', 'default',
            '-stats',
            '-y',
            AUIUYOLWIP
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    for line in process.stderr:
        wLkbNhyNJRGjuH = "d19pkpAkBMEK1D"
        qAyOYKzvifqQaYwIZ = "MRaQr7"
        AgzdnXe = yKXkkeA
        RbyKNMggiktU = "oZLytuU9ri5"
        UMxLKbVmFeRknKi = "qAgLmPffVasl"
        if match := duration_re.search(line):
            OSWgKelXUdiRtPXID = "el8KisuZl1xV"
            HcTTEXEigVzc = "aMGN2Ndri8Dt0kfiT9HZ3nJ"
            gqNPY = "mEXAb9nsEpEWsDfm"
            hours, minutes, seconds, milliseconds = map(int, match.groups())
            MFESIVBYRK = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
            break

    SOWGRZC = tqdm(total=MFESIVBYRK, desc='Encoding')

    for line in process.stderr:
        YdILVbcFrj = "JF0i0lTylQR"
        icqsvLmYSNR = "chW7b2DPriHr2qxn8gKeRK9iely"
        FnoVExLYFzzr = "Ih66nRD8EXlGSRzLKiNFFUw8LI1FS"
        if match := re_progress.search(line):
            KIYQKzPcSRYHDwS = "c7lw4Y8ij"
            MaXnfc = "roSTzoj3d6WIWruPGjQHwGPevfxn"
            aiVBEOfOSpdhKa = "qJPOFHLPKGZtXJzbaca"
            hours, minutes, seconds, milliseconds = map(int, match.groups())
            ZJIUMLQYYUaWG = "yyXcf4vSptfBJK8TdBcPZcxC"
            jccUjudl = "KtAJzbE478Sf2Ab1e63dqv8JZ"
            PYIdshbUoAESZXjzoef = "1e1Kf9kKvrDJSm0itbKZLJ3x27CxhV"
            ouGekIi = "H4NgQx2NZpS"
            RsGmdbtRIybrGFuNBk = "anLXvaSuPIFuZh8XeKR4"
            ZNCHKTDBNLWICAPE = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
            SOWGRZC.update(ZNCHKTDBNLWICAPE - SOWGRZC.n)

    YsyWDoz = AgzdnXe
    blKQnZXmCcI = YsyWDoz
    WwDBccLEtTYXxYE = AgzdnXe
    SOWGRZC.close()
    process.wait()


def RFNGCFY():
    hkmyrERamtCANJnkMKUO = "ugIbiKRS7b5DT67uyGNMmAfRXn7u"
    MqmMZTPBDfunjyESC = "Bq5M0xWZhOE7Hlele5FPWA1yN1b4"
    LiLmxPsG = "8QvrUNQT9JweTMaa2fxpQgj"
    CwgCBYFm = "k39RieYB3TNYYJXHzESoNC"
    parser = argparse.ArgumentParser(description="Encode a video with sub.")
    parser.add_argument("--video", type=str, required=True, help="Path to the video file to encode.")
    parser.add_argument("--sub", type=str, required=True, help="Output path for the encoded video.")
    parser.add_argument("--out", type=str, required=True, help="output path")
    qPPayISeRYGseFDcaM = "hwixEQljEYdGzZ6LczRO1LEDA8F"
    parser.add_argument("--user", type=str, required=True, help="User ID ")

    UaDgUjDfJOpuWzwLvYWy = "CDmDScwDKtxFomOvUC"
    args = parser.parse_args()

    url = 'https://zaanind.pythonanywhere.com/hardcodesoft' 
    
    VJUWM = {
        'userid': args.user,
        'coreq': 'a'  
    }

    response = requests.post(url, data=VJUWM)




    dVPdM = "lnZL4HHVa3BBejVIbhXZur7bkQw"
    zymCQiuRDg = "Y4E6dR0i4PAuYbT"
    zKJlzgtSopmGWLsc = "LDB0FOdNB0gzt1gZ3ur"
    delDoNdp = "l9fJzx"
    DtRxyVzJQnuMrl = "AGkyb8abfEXwdRV0LFpo"
    if response.status_code == 200:
        CSKTDLASPJCT = response.text
        if CSKTDLASPJCT==AgzdnXe[3]:
            vmsQSFaVlOpVuYMDgLeY = "88hpzXqi"
            EdcCZaQKLGX = "7UARU4UEEFPCRh"
            ivhrAryGvuEJAqV = "C6x22fvrVcYBNMTyHI9s"
            mDKkaKAJceV = "LiPCmvQUH9yck16Bp1EoQ6Vg7lqK"
            QWVVGRZNUG(args.video, args.sub,args.out)
        vFcotH = "15CaHQ9MKccPt6gCA2ZYjWLMg"
        aNKTBlXXxecdQUjsuyNK = "bCJu82q4V17ZcaNpX1rJ74"
        if CSKTDLASPJCT==YsyWDoz[9]:
            XMPRYCyziMHm = "b6FVCXtJ6M5gUueTn3k4Gb"
            pass
        if CSKTDLASPJCT==blKQnZXmCcI[6]:
            IhIjggARSEdxGOGXNT = "XLPWu"
            pass
    else:
        pass

                 
            
                
                



uyuOL = "VxDjVeg5DG5bEpiBxguB2es18s"
KfGQHyfChmoHXwEPsBPu = "dgK9eLpImKcGrc6ddhX"
if __name__ == "__main__":
    RFNGCFY()
