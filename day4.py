from aocd import lines  # type: ignore

#lines = ['2-4,6-8','2-3,4-5','5-7,7-9','2-8,3-7','6-6,4-6','2-6,4-8']
overlap_full = 0
overlap_partly = 0
for section_group in lines:
    section1, section2 = section_group.split(',')
    section1_min, section1_max = section1.split('-')
    section2_min, section2_max = section2.split('-')
    if (
    (int(section1_max) >= int(section2_max) and int(section1_min) <= int(section2_min)) 
        or (int(section1_max) <= int(section2_max) and int(section1_min) >= int(section2_min))
    ):
        overlap_full += 1
    if (
        (int(section1_max) >= int(section2_max) and int(section2_max) >= int(section1_min))
        or (int(section2_max) >= int(section1_max) and int(section1_max) >= int(section2_min))
    ):
        overlap_partly += 1
print(overlap_full, overlap_partly)
    