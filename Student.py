#  @author ZHChain
#  @File:Student.py
#  @createTime 2021/05/03 02:00:03

import random
import numpy as np
from sympy import *


class Student:
    def __init__(self, basicInfo):
        self.major = self.generateMajor()
        self.basicInfo = basicInfo
        self.fundaments = self.generateBasicKnowledge()
        self.coefficientEffect = self.generateCoefficientEffect()
        self.data = [self.fundaments]

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
        x = symbols("x")
        if self.major == '0':
            forget = 34.84 * (x ** (-0.2034)) + 12.78 + 4 * (
                    0.0056 * (x ** 2) - 0.1997 * x + 4.796) + 3 * (
                             0.004151 * (x ** 2) - 0.1469 * x + 4.559) + 2 * (
                             0.001208 * (x ** 2) - 0.03826 * x + 3.966) + 0.003468 * (
                             x ** 2) - 0.1228 * x + 4.48
        elif self.major == '1':
            forget = 34.84 * (x ** (-0.2034)) + 12.78 + 4 * (
                    0.009684 * (x ** 2) - 0.3725 * x + 6.08) + 3 * (
                             (-0.3418) * (x ** 2) - 0.1127 * x + 3.891) + 2 * (
                             0.005575 * (x ** 2) - 0.2055 * x + 4.888) + 0.00769 * (
                             x ** 2) - 0.3146 * x + 6.126
        else:
            forget = 34.84 * (x ** (-0.2034)) + 12.78 + 4 * (
                    2.99 * np.sin(x - np.pi) + 0.02013 * ((x - 10) ** 2) + 4.003) + 3 * (
                             0.01066 * (x ** 2) - 0.4039 * x + 6.576) + 2 * (
                             (-0.006938) * (x ** 2) + 0.2858 * x + 1.628) + 0.00483 * (
                             x ** 2) - 0.2245 * x + 6.028

        return integrate(forget, (x, 0, timePoint))

    def getPatience(self, timePoint):
        """
        Patience Curve
        :param timePoint: Input a time point
        :return: the area of patience curve refers to the zero point to timePoint
        """
        x = symbols("x")
        if self.major == '0':
            patience = 0.0056 * (x ** 2) - 0.1997 * x + 4.796
        elif self.major == '1':
            patience = 0.009684 * (x ** 2) - 0.3725 * x + 6.08
        else:
            patience = 2.99 * (np.sin(x - np.pi)) + 0.02013 * ((x - 10) ** 2) + 4.003

        return integrate(patience, (x, 0, timePoint))

    def getInterest(self, timePoint):
        """
        Interest Curve
        :param timePoint: Input a time point
        :return: the area of interest curve refers to the zero point to timePoint
        """
        x = symbols("x")
        if self.major == '0':
            interest = 0.00415 * (x ** 2) - 0.1469 * x + 4.559
        elif self.major == '1':
            interest = (-0.3418) * (x ** 2) + 0.1127 * x + 3.891
        else:
            interest = 0.01066 * (x ** 2) - 0.4039 * x + 6.576

        return integrate(interest, (x, 0, timePoint))

    def getSelfLearning(self, timePoint):
        """
        Self-Learning Curve
        :param timePoint: Input a time point
        :return: the area of self-learning curve refers to the zero point to timePoint
        """
        x = symbols("x")
        if self.major == '0':
            selfLearning = 0.001208 * (x ** 2) - 0.03826 * x + 3.966
        elif self.major == '1':
            selfLearning = 0.005575 * (x ** 2) - 0.2055 * x + 4.888
        else:
            selfLearning = (-0.006938) * (x ** 2) + 0.2858 * x + 1.628

        return integrate(selfLearning, (x, 0, timePoint))

    def getFocus(self, timePoint):
        """
        Focus Curve
        :param timePoint: Input a time point
        :return: the area of focus curve refers to the zero point to timePoint
        """
        x = symbols("x")
        if self.major == "0":
            focus = 0.003468 * (x ** 2) - 0.1228 * x + 4.48
        elif self.major == '1':
            focus = 0.00769 * (x ** 2) - 0.3146 * x + 6.126
        else:
            focus = 0.00483 * (x ** 2) - 0.2245 * x + 6.028

        return integrate(focus, (x, 0, timePoint))

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

        knowledge = np.sum(np.dot(self.coefficientEffect,
                                  0.4 * patience + 0.3 * interest + 0.2 * selfLearning + 0.1 * focus)) + self.fundaments
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
