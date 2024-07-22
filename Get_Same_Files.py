

import os
import shutil
import Get_Just_Name

def Same(contents):
    names=[]
    for i in range(len(contents)):
        names.append(Get_Just_Name.name(contents[i]))
    print(len(names))
    duplicates=[]
    for i in range(len(contents)):
        for j in range (i+1,len(names)):
            if Get_Just_Name.name(contents[i])==names[j]:
                duplicates.append(contents[i])
                break

    return duplicates

# m=['Other/20230819_124950.jpg', 'Other/20230819_130115.jpg', 'Other/20230819_142337.jpg', 'Other/20230819_150256.jpg', 'Other/20230819_150309.jpg', 'Other/20230819_150322.jpg', 'Other/20230819_153258.jpg', 'Other/20230819_154311.jpg', 'Other/20230819_154326.jpg', 'Other/20230819_194213.jpg', 'Other/20230819_194300.jpg', 'Other/20230819_194346.jpg', 'Other/20230819_194410.jpg', 'Other/20230819_194437.jpg', 'Other/20230820_091501.jpg', 'Other/20230820_091546.jpg', 'Other/20230820_091557.jpg', 'Other/20230820_133805.jpg', 'Other/20230820_133816.jpg', 'Other/20230820_133832.jpg', 'Other/20230820_185018.jpg', 'Other/20230820_185045.jpg', 'Other/20230820_185233.jpg', 'Other/20230820_185259.jpg', 'Other/20230820_185301.jpg', 'Other/20230820_185312.jpg', 'Other/20230820_185320.jpg', 'Other/20230820_185402.jpg', 'Other/20230820_185404.jpg', 'Other/20230820_185422.jpg', 'Other/20230820_185513.jpg', 'Other/20230820_185514.jpg', 'Other/20230821_112832.jpg', 'Other/20230822_165012.mp4', 'Other/20230822_170443.jpg', 'Other/20230823_155037.jpg', 'Other/20230916_032644.jpg', 'Other/20230916_032845.jpg', 'Other/20230916_032848.mp4', 'Other/20230916_032944.jpg', 'Other/20230916_032947.jpg', 'Other/20230916_032953.jpg', 'Other/20230916_032957.jpg', 'Other/20230916_033000.jpg', 'Other/20230916_033004.jpg', 'Other/20230916_033118.jpg', 'Other/20230916_033131.jpg', 'Other/20230916_033135.jpg', 'Other/20230916_033139.jpg', 'Other/20230916_033142.jpg', 'Other/20230916_033150.jpg', 'Other/20230916_033202.jpg', 'Other/20230916_033206.jpg', 'Other/20230916_033214.jpg', 'Other/20230916_033235.jpg', 'Other/20230916_033321.jpg', 'Other/20230916_033345.jpg', 'Other/20230916_033347.jpg', 'Other/20230916_033349.jpg', 'Other/20230916_033355.jpg', 'Other/20230916_033400.jpg', 'Other/20230916_033407.jpg', 'Other/20230916_033408.jpg', 'Other/20230916_033735.jpg', 'Other/20230916_033740.jpg', 'Other/20230916_033753.jpg', 'Other/20230916_033756.jpg', 'Other/20230916_033758.jpg', 'Other/20230916_033801.jpg', 'Other/20230916_033806.jpg', 'Other/20230916_033818.jpg', 'Other/20230916_033846.jpg', 'Other/20230916_033938.jpg', 'Other/20230916_033944.jpg', 'Other/20230916_034000.jpg', 'Other/20230916_034007.jpg', 'Other/20230916_034010.jpg', 'Other/20230916_034027.jpg', 'Other/20230916_034030.jpg', 'Other/20230916_034042.jpg', 'Other/20230916_034044.jpg', 'Other/20230916_034456.jpg', 'Other/20230916_034619.jpg', 'Other/20230916_034655.jpg', 'Other/20230916_034802.jpg', 'Other/20230916_034809.jpg', 'Other/20230916_034816.jpg', 'Other/20230916_034820.jpg', 'Other/20230916_034844_001.jpg', 'Other/20230916_034847.jpg', 'Other/20230916_034848.jpg', 'Other/20230916_034850.jpg', 'Other/20230916_034859.jpg', 'Other/20230916_034901.jpg', 'Other/20230916_034904.jpg', 'Other/20230916_040946.jpg', 'Other/20230916_040959.jpg', 'Other/20230916_041009.jpg', 'Other/CS02/20230819_124950.jpg', 'Other/CS02/IMG-20230927-WA0006.jpg', 'Other/CS02/IMG-20230927-WA0007.jpg', 'Other/CS02/IMG-20230927-WA0008.jpg', 'Other/CS02/IMG-20230927-WA0009.jpg', 'Other/CS02/IMG-20230927-WA0010.jpg', 'Other/CS02/IMG-20231108-WA0003.jpg', 'Other/CS02/IMG-20231108-WA0004.jpg', 'Other/CS02/IMG-20231108-WA0005.jpg', 'Other/CS02/IMG-20231108-WA0006.jpg', 'Other/CS02/IMG-20231108-WA0007.jpg', 'Other/CS02/IMG-20231108-WA0008.jpg', 'Other/CS02/IMG-20231108-WA0009.jpg', 'Other/CS02/IMG-20231108-WA0010.jpg', 'Other/CS02/IMG-20231108-WA0011.jpg', 'Other/CS02/IMG-20231108-WA0012.jpg', 'Other/CS02/IMG-20231211-WA0040.jpg', 'Other/CS02/IMG-20231211-WA0043.jpg', 'Other/CS02/IMG-20231211-WA0049.jpg', 'Other/CS02/IMG-20231211-WA0061.jpg', 'Other/CS02/IMG-20231211-WA0062.jpg', 'Other/CS02/IMG-20231211-WA0066.jpg', 'Other/CS02/IMG-20231211-WA0070.jpg', 'Other/CS02/IMG-20231211-WA0073.jpg', 'Other/CS02/IMG-20231211-WA0074.jpg', 'Other/CS02/IMG-20231211-WA0075.jpg', 'Other/CS02/IMG-20231211-WA0077.jpg', 'Other/CS02/IMG-20231211-WA0079.jpg', 'Other/CS02/IMG-20231211-WA0080.jpg', 'Other/CS02/IMG-20231211-WA0081.jpg', 'Other/CS02/IMG-20231211-WA0083.jpg', 'Other/CS02/IMG-20231211-WA0084.jpg', 'Other/CS02/IMG-20231211-WA0086.jpg', 'Other/CS02/IMG-20231211-WA0087.jpg', 'Other/CS02/IMG-20231211-WA0090.jpg', 'Other/CS02/IMG-20231211-WA0091.jpg', 'Other/CS02/IMG-20231211-WA0092.jpg', 'Other/CS02/IMG-20231211-WA0093.jpg', 'Other/CS02/IMG-20231211-WA0094.jpg', 'Other/CS02/IMG-20231211-WA0095.jpg', 'Other/CS02/IMG-20231211-WA0096.jpg', 'Other/CS02/VID-20231211-WA0098.mp4', 'Other/CS02/WhatsApp Image 2023-10-10 at 06.01.36 (1).jpeg', 'Other/CS02/Xmas/PXL_20231220_094055840.mp4', 'Other/CS02/Xmas/PXL_20231220_121940084.mp4', 'Other/CS02/Xmas/PXL_20231220_122443007.mp4', 'Other/CS02/Xmas/PXL_20231220_122907303.mp4', 'Other/CS02/Xmas/PXL_20231220_124647152.jpg', 'Other/CS02/Xmas/PXL_20231220_124650686.MP.jpg', 'Other/CS02/Xmas/PXL_20231220_124652030.jpg', 'Other/CS02/Xmas/PXL_20231220_125656679.mp4', 'Other/CS02/Xmas/VID-20231220-WA0006.mp4', 'Other/CS02/Xmas/VID-20231221-WA0002.mp4', 'Other/IMG-20231027-WA0010.jpg', 'Other/IMG-20231027-WA0011.jpg', 'Other/IMG-20231027-WA0012.jpg', 'Other/IMG-20231027-WA0013.jpg', 'Other/IMG-20231110-WA0017.jpg', 'Other/IMG-20231110-WA0018.jpg', 'Other/IMG-20231110-WA0019.jpg', 'Other/IMG-20231110-WA0020.jpg', 'Other/IMG-20231110-WA0021.jpg', 'Other/IMG-20231110-WA0022.jpg', 'Other/IMG-20231110-WA0023.jpg', 'Other/IMG-20231110-WA0024.jpg', 'Other/IMG-20231211-WA0006.jpeg', 'Other/IMG-20231211-WA0008.jpg', 'Other/IMG-20231211-WA0016.jpeg', 'Other/New folder/IMG-20231208-WA0000.jpg', 'Other/New folder/IMG-20231209-WA0057.jpg', 'Other/New folder/IMG-20231209-WA0058.jpg', 'Other/New folder/IMG-20231209-WA0063.jpg', 'Other/PXL_20231025_130636732.jpg', 'Other/PXL_20231025_130638141.jpg', 'Other/PXL_20231025_130640196.jpg', 'Other/PXL_20231025_130646169.NIGHT.jpg', 'Other/PXL_20231025_130651440.NIGHT.jpg', 'Other/PXL_20231025_131217601.jpg', 'Other/PXL_20231028_184310550.MP.jpg', 'Other/PXL_20231028_184313429.jpg', 'Other/PXL_20231028_184323107.jpg', 'Other/PXL_20231109_095432265.mp4', 'Other/PXL_20231109_095442981.mp4', 'Other/PXL_20231109_101940481.MP.jpg', 'Other/PXL_20231112_065345973.jpg', 'Other/PXL_20231112_065421037.jpg', 'Other/PXL_20231112_065520046.MP.jpg', 'Other/PXL_20231112_065539859.jpg', 'Other/PXL_20231124_155842092.NIGHT.jpg', 'Other/PXL_20231124_155848079.NIGHT.jpg', 'Other/PXL_20231124_155848079.NIGHT~2.jpg', 'Other/PXL_20231124_155903261.NIGHT.jpg', 'Other/PXL_20231124_155921283.NIGHT.jpg', 'Other/PXL_20231210_182440256.jpg', 'Other/PXL_20231210_182443717.jpg', 'Other/PXL_20231210_185044918.jpg', 'Other/PXL_20231210_200428860.jpg', 'Other/PXL_20231210_200430047.jpg', 'Other/PXL_20231210_200430873.jpg', 'Other/PXL_20231210_200517176.jpg', 'Other/PXL_20231210_200518506.MP.jpg', 'Other/PXL_20231210_200519769.jpg', 'Other/PXL_20231210_200548734.jpg', 'Other/PXL_20231210_200549144.jpg', 'Other/PXL_20231210_200549452.jpg', 'Other/VID-20231017-WA0032.mp4', 'Other/VID-20231203-WA0000.mp4', 'Other/VID-20231216-WA0004.mp4']

# print(len(m))
# print(Same(m))

