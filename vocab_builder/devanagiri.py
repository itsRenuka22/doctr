devangiri_start, devangiri_end = int("0900",16), int("097F",16)
devangiri_main = [chr(i) for i in range(devangiri_start,devangiri_end + 1)]

print(*devangiri_main,sep="")

devangiri_ext_start, devangiri_ext_end = int("A8E0",16),int("A8FF",16)
devangiri_ext = [chr(i) for i in range(devangiri_ext_start,devangiri_ext_end + 1)]

print(*devangiri_ext,sep="")

devangiri_ext_a_start, devangiri_ext_a_end = int("11B00",16),int("11B09",16)
devangiri_ext_a = [chr(i) for i in range(devangiri_ext_a_start,devangiri_ext_a_end + 1)]

print(*devangiri_ext_a,sep="")

with open("dvocab.txt","w",encoding='utf-8') as f:
    f.write("".join(devangiri_main+devangiri_ext))