if __name__=="__main__":
    import os
    import Get_All_Files
    import Duplicates_Diff_Folder
    import Get_Same_Files    
    
    def Final(string):
        Duplicates_Diff_Folder.Duplicates(Get_Same_Files.Same(Get_All_Files.Store_Files(string)))

    Final(input())