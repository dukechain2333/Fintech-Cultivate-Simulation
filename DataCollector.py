#  @author ZHChain
#  @File:DataCollector.py
#  @createTime 2021/05/03 02:03:03

from Student import *
import numpy as np


class DataCollector:
    def __init__(self):
        self.densityFinance = self.knowledgeFinance()
        self.densityCS = self.knowledgeCS()
        self.densityFintech = self.knowledgeFintech()
        self.densityFamily = self.relatedFamilyMembers()
        self.densityFintechProduct = self.productFintech()

    def generateStudent(self, studentNumber):
        studentList = []
        for i in range(studentNumber):
            major = self.generateMajor()
            basic = self.generateChoice(major)
            relatedFamily = self.generateFamily()
            finProduct = self.generateFinProduct()
            interest = self.basicInterest(major)
            patience = self.basicPatience(major)
            selfLearning = self.basicSelfLearning(major)
            focus = self.basicFocus(major)
            basicInfo = [basic, relatedFamily, finProduct, patience, interest, selfLearning, focus]
            s = Student(major, basicInfo)
            studentList.append(s)
        print('Student generate complete!')

        return studentList

    def runStudent(self, studentNumber, duration):
        """
        Simulation on student
        :param studentNumber:Input the number of student you want to simulate
        :param duration: Input the duration you want to simulate
        :return: data that contains student simulation
        """
        studentList = self.generateStudent(studentNumber)
        dataList = []
        print('Processing')
        for s in studentList:
            for t in range(1, duration + 1):
                s.updateKnowledge(t)
            dataList.append(s.data)
            # print(s.data)
        dataList = np.array(dataList)
        # save the result to local
        np.save('data', dataList, allow_pickle=True, fix_imports=True)
        return dataList

    @staticmethod
    def basicPatience(major):
        """
        Patience Curve at time 0
        :param major: Input a major
        :return: the value of patience curve refers to time 0
        """
        if major == '0':
            patience = 4.796
        elif major == '1':
            patience = 6.08
        else:
            patience = 2.99 * (np.sin(0 - np.pi)) + 0.02013 * ((0 - 10) ** 2) + 4.003

        return patience

    @staticmethod
    def basicInterest(major):
        """
        Interest Curve at time 0
        :param major: Input a major
        :return: the value of interest curve refers to time 0
        """
        if major == '0':
            interest = 4.559
        elif major == '1':
            interest = 3.891
        else:
            interest = 6.576

        return interest

    @staticmethod
    def basicSelfLearning(major):
        """
        Self-Learning Curve at time 0
        :param major: Input a major
        :return: the value of self-learning curve refers to time 0
        """
        if major == '0':
            selfLearning = 3.966
        elif major == '1':
            selfLearning = 4.888
        else:
            selfLearning = 1.628

        return selfLearning

    @staticmethod
    def basicFocus(major):
        """
        Focus Curve
        :param major: Input a major
        :return: the value of focus curve refers to time 0
        """
        if major == "0":
            focus = 4.48
        elif major == '1':
            focus = 6.126
        else:
            focus = 6.028

        return focus

    def generateChoice(self, major):
        if major == "0":
            return int(random.choice(
                ['1'] * int(self.densityFinance[0] * 100) + ['2'] * int(self.densityFinance[1] * 100) + ['3'] * int(
                    self.densityFinance[2] * 100) + ['4'] * int(self.densityFinance[3] * 100) + ['5'] * int(
                    self.densityFinance[4] * 100)))
        elif major == "1":
            return int(random.choice(
                ['1'] * int(self.densityCS[0] * 100) + ['2'] * int(self.densityCS[1] * 100) + ['3'] * int(
                    self.densityCS[2] * 100) + ['4'] * int(self.densityCS[3] * 100) + ['5'] * int(
                    self.densityCS[4] * 100)))
        else:
            return int(random.choice(
                ['1'] * int(self.densityFintech[0] * 100) + ['2'] * int(self.densityFintech[1] * 100) + ['3'] * int(
                    self.densityFintech[2] * 100) + ['4'] * int(self.densityFintech[3] * 100) + ['5'] * int(
                    self.densityFintech[4] * 100)))

    def generateFamily(self):
        return int(random.choice(
            ['1'] * int(self.densityFamily[0] * 100) + ['2'] * int(self.densityFamily[1] * 100) + ['3'] * int(
                self.densityFamily[2] * 100) + ['4'] * int(self.densityFamily[3] * 100) + ['5'] * int(
                self.densityFamily[4] * 100)))

    def generateFinProduct(self):
        return int(random.choice(
            ['1'] * int(self.densityFintechProduct[0] * 100) + ['2'] * int(self.densityFintechProduct[1] * 100) + [
                '3'] * int(
                self.densityFintechProduct[2] * 100) + ['4'] * int(self.densityFintechProduct[3] * 100) + ['5'] * int(
                self.densityFintechProduct[4] * 100)))

    @staticmethod
    def knowledgeFinance():
        densityFinance = []
        for i in range(1, 6):
            density = (1 / (((np.pi * 2) ** 0.5) * 3.47416)) * (np.e ** (-((i - 1.60976) ** 2) / (2 * (3.47416 ** 2))))
            densityFinance.append(density)

        return densityFinance

    @staticmethod
    def knowledgeCS():
        densityCS = []
        for i in range(1, 6):
            density = (1 / (((np.pi * 2) ** 0.5) * 3.47416)) * (np.e ** (-((i - 1.60976) ** 2) / (2 * (3.47416 ** 2))))
            densityCS.append(density)

        return densityCS

    @staticmethod
    def knowledgeFintech():
        densityFintech = []
        for i in range(1, 6):
            density = (1 / (((np.pi * 2) ** 0.5) * 3.21981)) * (np.e ** (-((i - 1.40224) ** 2) / (2 * (3.21981 ** 2))))
            densityFintech.append(density)

        return densityFintech

    @staticmethod
    def relatedFamilyMembers():
        densityFamily = []
        for i in range(1, 6):
            density = (1 / (((np.pi * 2) ** 0.5) * 2.86044)) * (np.e ** (-((i - 1.3811) ** 2) / (2 * (2.86044 ** 2))))
            densityFamily.append(density)

        return densityFamily

    @staticmethod
    def productFintech():
        densityFintech = []
        for i in range(1, 6):
            density = (1 / (((np.pi * 2) ** 0.5) * 3.85037)) * (np.e ** (-((i - 1.59451) ** 2) / (2 * (3.85037 ** 2))))
            densityFintech.append(density)

        return densityFintech

    @staticmethod
    def generateMajor():
        """
        Generate student's major
        0 means Finance
        1 means CS
        2 means Fintech
        :return: major
        """
        # Fin:CS:Fintech = 38:38:24
        return random.choice(['0'] * 38 + ['1'] * 38 + ['2'] * 24)
