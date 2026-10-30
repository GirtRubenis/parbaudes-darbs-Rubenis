# ----------------------------------------------------------------------
# C1. Python — rīks, kas atlasa un saglabā
# ----------------------------------------------------------------------

# Uzraksti skriptu, kuram līmeni padod kā argumentu komandrindā. Skripts izvada, cik tāda līmeņa rindu žurnālā ir, un saglabā visas šīs rindas failā, kura nosaukums sākas ar līmeņa nosaukumu. Ja arguments nav padots, skripts izvada pamācību un neavarē.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Mainīgo, kurā glabā līmeni, nosauc ar vārdu meklejamais.
import sys

if len(sys.argv) < 2:
    print("Usage: C1_uzraksti.py ")
    sys.exit()

level = sys.argv[1]
lines = []

with open("system.log", encoding="utf-8") as f:
    for line in f:
        if level in line:
            lines.append(line)

print(len(lines))

with open(f"{level}.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
