#  @author ZHChain
#  @File:Student.py
#  @createTime 2021/05/03 02:00:03

import random
import numpy as np


class Student:
    def __init__(self, major, basicInfo):
        self.major = major
        self.basicInfo = basicInfo
        self.fundaments = self.generateBasicKnowledge()
        self.coefficientEffect = self.generateCoefficientEffect()
        self.forgetMatrix = []
        self.patienceMatrix = []
        self.interestMatrix = []
        self.selfLearningMatrix = []
        self.focusMatrix = []
        self.data = [np.dot(self.coefficientEffect, self.fundaments)]

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

    def generateBasicKnowledge(self):
        """
        Generate Basic Knowledge.
        coefficient of basic is 0.3,
        coefficient of relatedFamily is 0.5,
        coefficient of finProduct is 0.2,
        coefficient of patience is 0.4,
        coefficient of interest is 0.3,
        coefficient of selfLearning is 0.2,
        coefficient of focus is 0.1 .
        :return: basic knowledge
        """
        basicKnowledge = 0.3 * self.basicInfo[0] + 0.5 * self.basicInfo[1] + 0.2 * self.basicInfo[2] + 0.4 * \
                         self.basicInfo[3] + 0.3 * self.basicInfo[4] + 0.2 * self.basicInfo[5] + 0.1 * self.basicInfo[6]
        return basicKnowledge

    def generateCoefficientEffect(self):
        """
        Generate Coefficient of Effect
        :return: coefficient of Effect
        """
        if self.major == '0':
            coefficientEffect = np.array([6.73, 0])
        elif self.major == '1':
            coefficientEffect = np.array([0, 8.04])
        else:
            coefficientEffect = np.array([2, 3])

        return coefficientEffect

    def getForgetPoint(self, timePoint):
        """
        Forget Curve
        :param timePoint:Input a time point
        :return: the area of forget curve refers to the zero point to timePoint
        """
        if self.major == '0':
            forget = 34.84 * (timePoint ** (-0.2034)) + 12.78 + 4 * (
                    0.0056 * (timePoint ** 2) - 0.1997 * timePoint + 4.796) + 3 * (
                             0.004151 * (timePoint ** 2) - 0.1469 * timePoint + 4.559) + 2 * (
                             0.001208 * (timePoint ** 2) - 0.03826 * timePoint + 3.966) + 0.003468 * (
                             timePoint ** 2) - 0.1228 * timePoint + 4.48
        elif self.major == '1':
            forget = 34.84 * (timePoint ** (-0.2034)) + 12.78 + 4 * (
                    0.009684 * (timePoint ** 2) - 0.3725 * timePoint + 6.08) + 3 * (
                             (-0.3418) * (timePoint ** 2) - 0.1127 * timePoint + 3.891) + 2 * (
                             0.005575 * (timePoint ** 2) - 0.2055 * timePoint + 4.888) + 0.00769 * (
                             timePoint ** 2) - 0.3146 * timePoint + 6.126
        else:
            forget = 34.84 * (timePoint ** (-0.2034)) + 12.78 + 4 * (
                    2.99 * np.sin(timePoint - np.pi) + 0.02013 * ((timePoint - 10) ** 2) + 4.003) + 3 * (
                             0.01066 * (timePoint ** 2) - 0.4039 * timePoint + 6.576) + 2 * (
                             (-0.006938) * (timePoint ** 2) + 0.2858 * timePoint + 1.628) + 0.00483 * (
                             timePoint ** 2) - 0.2245 * timePoint + 6.028

        if len(self.forgetMatrix) == 0:
            tmp = forget + float(np.random.rand(1) * 100)
            self.forgetMatrix.append(tmp)
        else:
            tmp = forget + self.forgetMatrix[-1] + float(np.random.rand(1) * 100)
            self.forgetMatrix.append(tmp)

        return tmp

    def getPatience(self, timePoint):
        """
        Patience Curve
        :param timePoint: Input a time point
        :return: the area of patience curve refers to the zero point to timePoint
        """
        if self.major == '0':
            patience = 0.0056 * (timePoint ** 2) - 0.1997 * timePoint + 4.796
        elif self.major == '1':
            # patience = 0.009684 * (timePoint ** 2) - 0.3725 * timePoint + 6.08
            patience = 0.0002152 * ((timePoint - 5) ** 3) - 0.1519 * timePoint + 4.815
        else:
            patience = 2.99 * (np.sin(timePoint - np.pi)) + 0.02013 * ((timePoint - 10) ** 2) + 4.003

        if len(self.patienceMatrix) == 0:
            tmp = patience + float(np.random.rand(1) * 100)
            self.patienceMatrix.append(tmp)
        else:
            tmp = patience + self.patienceMatrix[-1] + float(np.random.rand(1) * 100)
            self.patienceMatrix.append(tmp)

        return tmp

    def getInterest(self, timePoint):
        """
        Interest Curve
        :param timePoint: Input a time point
        :return: the area of interest curve refers to the zero point to timePoint
        """
        if self.major == '0':
            interest = 0.00415 * (timePoint ** 2) - 0.1469 * timePoint + 4.559
        elif self.major == '1':
            # interest = (-0.3418) * (timePoint ** 2) + 0.1127 * timePoint + 3.891
            interest = 2.145 * (timePoint ** 0.2019)
        else:
            interest = 0.01066 * (timePoint ** 2) - 0.4039 * timePoint + 6.576

        if len(self.interestMatrix) == 0:
            tmp = interest + float(np.random.rand(1) * 100)
            self.interestMatrix.append(tmp)
        else:
            tmp = interest + self.interestMatrix[-1] + float(np.random.rand(1) * 100)
            self.interestMatrix.append(tmp)

        return tmp

    def getSelfLearning(self, timePoint):
        """
        Self-Learning Curve
        :param timePoint: Input a time point
        :return: the area of self-learning curve refers to the zero point to timePoint
        """
        if self.major == '0':
            selfLearning = 0.001208 * (timePoint ** 2) - 0.03826 * timePoint + 3.966
        elif self.major == '1':
            selfLearning = 0.005575 * (timePoint ** 2) - 0.2055 * timePoint + 4.888
        else:
            selfLearning = (-0.006938) * (timePoint ** 2) + 0.2858 * timePoint + 1.628

        if len(self.selfLearningMatrix) == 0:
            tmp = selfLearning + float(np.random.rand(1) * 100)
            self.selfLearningMatrix.append(tmp)
        else:
            tmp = selfLearning + self.selfLearningMatrix[-1] + float(np.random.rand(1) * 100)
            self.selfLearningMatrix.append(tmp)

        return tmp

    def getFocus(self, timePoint):
        """
        Focus Curve
        :param timePoint: Input a time point
        :return: the area of focus curve refers to the zero point to timePoint
        """
        if self.major == "0":
            focus = 0.003468 * (timePoint ** 2) - 0.1228 * timePoint + 4.48
        elif self.major == '1':
            focus = 0.00769 * (timePoint ** 2) - 0.3146 * timePoint + 6.126
        else:
            focus = 0.00483 * (timePoint ** 2) - 0.2245 * timePoint + 6.028

        if len(self.focusMatrix) == 0:
            tmp = focus + float(np.random.rand(1) * 100)
            self.focusMatrix.append(tmp)
        else:
            tmp = focus + self.focusMatrix[-1] + float(np.random.rand(1) * 100)
            self.focusMatrix.append(tmp)

        return tmp

    def updateKnowledge(self, timePoint):
        """
        Update the latest knowledge
        :param timePoint: Input a time point
        :return: the latest knowledge
        """
        patience = self.getPatience(timePoint)
        interest = self.getInterest(timePoint)
        selfLearning = self.getSelfLearning(timePoint)
        focus = self.getFocus(timePoint)

        knowledge = np.dot(self.coefficientEffect, 0.4 * patience + 0.3 * interest + 0.2 * selfLearning + 0.1 * focus) \
                    + np.dot(self.coefficientEffect / np.sum(np.dot(self.coefficientEffect, self.fundaments)),
                             self.fundaments)
        self.data.append(knowledge)
        return knowledge

    def getMajor(self):
        """
        Get student's major
        :return: major
        """
        return self.major

    def getFundaments(self):
        """
        Get student's fundaments
        :return: student's fundaments
        """
        return self.fundaments

    def getCoefficientEffect(self):
        """
        Get coefficient of Effect
        :return: coefficient of Effect
        """
        return self.coefficientEffect
