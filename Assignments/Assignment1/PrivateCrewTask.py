def findPowerLevels(powerLevels: list[int]) -> list[int]:

    result = list()
    prefProd = 1
    # print(powerLevels)

    #first for loop prefix product
    for i in range(0, len(powerLevels)):
        #mistake - dont swap positions of below 2 statements
        result.append(prefProd)
        prefProd = prefProd * powerLevels[i]
    # print(result)

    sufProd = 1
    #seconf for loop - suffix product
    for i in range(len(powerLevels)-1, -1, -1):
        result[i] = result[i]*sufProd
        sufProd = sufProd * powerLevels[i]
    # print(result)

    return(result)

# findPowerLevels([1,2,3,4])