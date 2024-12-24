# from typing import List


def numberOfTeams(ratings:List[int])->int:

    count = 0
    for i in range(len(ratings)):
        for j in range(i+1, len(ratings)):
            for k in range(j+1, len(ratings)):
                if((ratings[i]<ratings[j] and ratings[j]<ratings[k]) or 
                   (ratings[i]>ratings[j] and ratings[j]>ratings[k])):
                    count+=1

    # print(count)
    return(count)


# numberOfTeams([9,2,6,5,7])