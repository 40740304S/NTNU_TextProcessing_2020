#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(txtFile):
    with open(txtFile, encoding="utf-8") as f:
        txtSTR = f.read()
    return txtSTR



if __name__=="main":
    fileTUPLE = ("example\dbp.txt", "example\pbd.txt")
    
    result = main(fileTUPLE[0])
    xINT = resultSTR.count("婦人")
    yINT = resultSTR.count("土狗")
    zINT = resultSTR.count("男")
    dbpLIST = [("婦人", xINT),("土狗", yINT), ("男", zINT)]
    print(fileTUPLE[0].split("/")[1], dbpLIST)
    
    resultSTR = main(fileTUPLE[1])
    xINT = resultSTR.count("婦人")
    yINT = resultSTR.count("土狗")
    zINT = resultSTR.count("男")
    dbpLIST = [("婦人", xINT),("土狗", yINT), ("男", zINT)]
    print(fileTUPLE[1].split("/")[1], dbpLIST)