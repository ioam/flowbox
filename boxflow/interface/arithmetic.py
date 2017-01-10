# Module offering basic arithmetic classes
#
#
from __future__ import absolute_import
import param

class Percentage(param.Parameterized):
    no_ports = ['percent']

    percent = param.Number(default=50, bounds=(0,100))

    def propagate(self):
        return self.percent


class Magnitude(param.Parameterized):
    no_ports = ['magnitude']

    magnitude = param.Number(default=0.5, bounds=(0,1))

    def propagate(self):
        return self.magnitude


class Multiply(param.Parameterized):

    input = param.Number(default=0)

    multiplier = param.Number(default=1)

    def propagate(self):
        return self.input * self.multiplier


class Divide(param.Parameterized):

    input = param.Number(default=0)

    divisor = param.Number(default=1)

    def propagate(self):
        return self.input / self.divisor


class Add(param.Parameterized):

    lhs = param.Number(default=0)

    rhs = param.Number(default=1)

    def propagate(self):
        return self.lhs + self.rhs


class Subtract(param.Parameterized):

    lhs = param.Number(default=0)

    rhs = param.Number(default=1)

    def propagate(self):
        return self.lhs - self.rhs


def arithmetic_nodes():
    return {'LabelledNode':[Percentage, Magnitude, Multiply, Divide, Add, Subtract]}

def arithmetic_display(instance):
    return {}