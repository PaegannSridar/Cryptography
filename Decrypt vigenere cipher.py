from collections import Counter

def caesar_decrypt(text, shift):
    decrypted = []
    for char in text:
        if 'A' <= char <= 'Z':
            decrypted.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        elif 'a' <= char <= 'z':
            decrypted.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def vigenere_decrypt(ciphertext, key_length):
    def guess_caesar_shift(segment):
        frequency = Counter(segment)
        most_common_char = frequency.most_common(1)[0][0]
        shift = (ord(most_common_char) - ord('E')) % 26
        return shift

    segments = ['' for _ in range(key_length)]
    for i, char in enumerate(ciphertext):
        segments[i % key_length] += char

    all_shifts = []
    for segment in segments:
        possible_shifts = []
        for shift in range(26):
            shifted_segment = caesar_decrypt(segment, shift)
            possible_shifts.append((shift, shifted_segment))
        all_shifts.append(possible_shifts)

    return all_shifts

ciphertext = "MZDFP OCFFO YFQZY ZMXDE CTCWZ HOWCS OCYTX DSPCD WOEUC UUCNO PZDEW OKFZI ODEOC EFPZD EWOKE GDDOK OYNWC YTXKT OCDSZ GYFOE EXDUC UUCNO QPCHO SZXAW OFOTX KQYHO EFQNC FQZYE CFFPO QXAOD QCWCD XESGE FZXEI CDOPZ GEOCY TIQWW DOFGD YMZDF PIQFP UGFVY ZIQYN RGEFP ZIWZY NFPCF RZGDY OKXCK FCVOC YTPZI DOXCD VCUWK EIQMF KZGDD ZKCWX CQWSC YUOQF PZGNP FQFUO EFFZE OYTKZ GXKDO AZDFU KWOFF ODXKY OIMDQ OYTEQ YWQHO DAZZW IODOD OCWPO WAMGW CYTAD ZHQTO TXOIQ FPFPO EPQAA QYNAC AODEC WFPZG NPQCX YZFEG DOPZI XGSPC EEQEF CYSOF POKIQ WWADZ HQTOC WWQSC YEOOQ EFPCF FPOSD CFOEC WWWOM FFPOG YQFOT EFCFO EFZNO FPODC YTOCS PIOQN POTFP OECXO EGNNO EFQYN FPCFY ZFPQY NPCTU OOYFC VOYQM QYTQF XQNPF KGYWQ VOWKF PCFCY KZYOQ YFODO EFOTQ YEFOC WQYNF POSZY FOYFE ZMCEQ YNWOS DCFOI ZGWTF CVOFP OFDZG UWOFZ DOAWC SOFPO XIQFP CSCDO MGWWK SCWQU DCFOT IOQNP FZMDG UUWOZ DZFPO DYZYE OYEOC YTQYC YKSCE OFPOE OCWPC TUOOY DOAWC SOTFP CFEOO XEWQV OCYCI MGWWZ FZMFD ZGUWO MZDCM OIDQM WOECY TUZJO EZMCX XGYQF QZYIQ FPFPO SDCFO EQYEF ZDCNO FPOEO CWEPC HOUOO YDOXZ HOTAD OEGXC UWKFZ CWWZI KZGDS GEFZX EZMMQ SQCWE FZQYE AOSFF POXCY TFPCF NCHOX OCYZA AZDFG YQFKF ZOJCX QYOFP OSZYF OYFEQ FFZZV XOCWZ YNFQX OFZIZ DVFPD ZGNPF POXCW WUGFQ FEFPO TCDYO TOEFF PQYNF PODOQ EYZFP QYNXQ EEQYN CYTQX OCYYZ FPQYN YZFOH OYCEQ YNWOU GWWOF CYTIO VYZIF PCFCF WOCEF ZYOIC EWOMF ZYFPO MWZZD ZMFPO ICDOP ZGEOQ YODQY XKMDQ OYTEF OWWXO FPCFC PQYTG NOYFW OXCYP CTUOO YEOOY QYFPO HQSQY QFKZM FPOEP OTQYF POACE FYQNP FUGFQ CXXQY TOTFZ FPQYV FPCFQ ERGEF ESGFF WOUGF FMZWV EQYOD QYFCW VWQVO FPCFC UZGFE FDCYN ODECW WFPOF QXOCY TIQFP YZFPQ YNFZS ZYYOS FPQXF ZFPOS CDNZC YTYZI CKFZF DCSVP QXTZI YQFPQ YVIOS CYQNY ZDOQM YZFMZ DNOFF PONZE EQAQP ZAOFZ UOIQF PKZGC NCQYQ YFPDO OTCKE CYTWZ ZVMZD ICDTF ZTQES GEEQY NFPQE XKEFO DKIQF PKZGF POYXQ EEVCF OICDY O"

key_length = 6
decrypted_shifts = vigenere_decrypt(ciphertext, key_length)

for i, shifts in enumerate(decrypted_shifts):
    print(f"Segment {i+1}:")
    for shift, text in shifts:
        print(f"Shift {shift}: {text}")
