def countPath(mat, src, des):
    if(src == des):
        return 0
    if(src[0] == des[0]):
        return 1
    if(src[1] == des[1]):
        return 1
    downWays = countPath(mat, [src[0]+1, src[1]], des)
    rightWays = countPath(mat, [src[0], src[1]+1], des)
    return downWays+rightWays
    pass


def path(mat, src, des, org, p):
    if(src[0] == des[0] and src[1] == des[1]):
        print("Path: ", p)
        return p
    if(src[0] < des[0]):
        downPath = path(mat, [src[0]+1, src[1]], des, False, p+"D")
    if(src[1] < des[1]):
        rightPath = path(mat, [src[0], src[1]+1], des, False, p + "R")
    
    

mat = [3,3]
src = [0, 0]
des = [2,2]
if(des[0] < mat[0] and des[0] >= 0 and des[1] < mat[1] and des[1] >= 0):
    print("Ways: ", countPath(mat, src, des))
    path(mat, src, des, True, "")
else:
    print("Please enter valid Source and Destination")
