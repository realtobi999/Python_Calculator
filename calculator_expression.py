from calculator_expression_processor import CalculatorExpressionProcessor


class CalculatorExpression:
    def __init__(self, expression_str: str, processor: CalculatorExpressionProcessor):
        self.expression_str = expression_str.replace(" ", "")
        self.processor = processor

    def _tokenize_expression(self):
        """
        Parses the input expression string into a list of numbers and operators.

        Returns:
            list: A list of numbers and operators extracted from the expression.
        """
        tokens = []
        i = 0
        while i < len(self.expression_str):
            if self.expression_str[i].isdigit():
                number = ""
                while i < len(self.expression_str) and self.expression_str[i].isdigit():
                    number += self.expression_str[i]
                    i += 1
                tokens.append(int(number))
            elif self.expression_str[i] in CalculatorExpressionProcessor.OPERATORS:
                tokens.append(self.expression_str[i])
                i += 1
            elif self.expression_str[i] in CalculatorExpressionProcessor.MISC:
                tokens.append(self.expression_str[i])
                i += 1
            else:
                raise Exception(
                    f"SYNTAX ERROR! '{
                        self.expression_str[i]}' is not valid syntax!"
                )
        return tokens

    def calculate(self):
        """
        Tokenizes the expression, processes it, and calculates the result.

        Returns:
            float: The result of the expression.
        """
        tokens = self._tokenize_expression()
        return self.processor.process_expression_tokens(tokens)
