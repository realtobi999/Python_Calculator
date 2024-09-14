from calculator_expression import CalculatorExpression
from calculator_expression_processor import CalculatorExpressionProcessor

class Calculator:
    def solve(self, expression: CalculatorExpression) -> float:
        return expression.calculate()
    
    def solve(self, expression_str: str) -> float:
        return CalculatorExpression(expression_str, CalculatorExpressionProcessor()).calculate()
