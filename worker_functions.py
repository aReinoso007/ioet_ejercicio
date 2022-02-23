import sys


class WorkerFunctions():
    def __init__(self, file):
        self.file = file

    def readFile(self):
        lines, newLine = [], []
        with open(self.file, encoding='utf8') as f:
            lines = f.readlines()
        for l in lines:
            ln = l.replace("=", ",").replace(" ", "")
            ln = ln.strip()
            ln = ln.split(',')[0:]
            newLine.append(ln)
        return newLine

    def calculateOverlappingHours(self, list):
        counter, result = 0, dict()
        for i in range(0, len(list)):
            for j in range(i+1, len(list)):
                arrA = list[i][1:]
                arrB = list[j][1:]
                for e in arrA:
                    for e2 in arrB:
                        if (e[:2] == e2[:2]):
                            start1, end1, start2, end2 = int(e[2:4]), int(
                                e[8:10]), int(e2[2:4]), int(e2[8:10])
                            if (start1 <= end2) & (start2 <= end1):
                                counter += 1
                if counter > 0:
                    key = "" + str(list[i][:1]) + "-" + str(list[j][:1])
                    key = key.replace('[', '').replace(']', '')
                    result[key] = counter
                counter = 0
        return result

    def runProcess(self):
        fileInput = self.readFile()
        result = self.calculateOverlappingHours(fileInput)
        return result
