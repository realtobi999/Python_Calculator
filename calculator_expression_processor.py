class CalculatorExpressionProcessor:
    OPERATORS = ["+", "-", "*", "/"]
    MISC = ["(", ")"]

    def _handle_subtraction_addition(self, tokens):
        """
        Processes addition and subtraction operators in the tokenized expression.
        It updates the tokens list in place by replacing the operands
        and operator with their calculated result.

        Args:
            tokens (list): A list of numbers and operators.
        """
        i = 0
        while i < len(tokens):
            if tokens[i] == "-":
                temp = tokens[i - 1] - tokens[i + 1]
                tokens[i - 1: i + 2] = [temp]
            elif tokens[i] == "+":
                temp = tokens[i - 1] + tokens[i + 1]
                tokens[i - 1: i + 2] = [temp]
            else:
                i += 1

    def _handle_multiplication_division(self, tokens):
        """
        Processes multiplication and division operators in the tokenized expression.
        It updates the tokens list in place by replacing the operands
        and operator with their calculated result.

        Args:
            tokens (list): A list of numbers and operators.

        Raises:
            Exception: If there is a division by zero.
        """
        i = 0
        while i < len(tokens):
            if tokens[i] == "*":
                temp = tokens[i - 1] * tokens[i + 1]
                tokens[i - 1: i + 2] = [temp]
            elif tokens[i] == "/":
                if tokens[i + 1] == 0:
                    raise Exception(
                        "MATH ERROR! Division by zero is not allowed.")
                temp = tokens[i - 1] / tokens[i + 1]
                tokens[i - 1: i + 2] = [temp]
            else:
                i += 1

    def _handle_parentheses(self, tokens):
        """
        Processes parentheses in the tokenized expression.
        It evaluates the expression inside each pair of parentheses
        and replaces the parentheses and their contents with the result.

        Args:
            tokens (list): A list of numbers, operators, and parentheses.

        Returns:
            list: The modified list of tokens with parentheses processed.

        Raises:
            Exception: If there are unclosed parentheses.
        """
        i = 0
        while i < len(tokens):
            if tokens[i] == ")":
                raise Exception(
                    "SYNTAX ERROR! Cannot have unclosed parentheses!")

            elif tokens[i] == "(":
                for j in range(i + 1, len(tokens)):
                    if tokens[j] == ")":
                        # Process the tokens inside the parentheses
                        tokens[i: j + 1] = [
                            self.process_expression_tokens(
                                tokens[i + 1: j], False)
                        ]
                        break
                else:
                    raise Exception(
                        "SYNTAX ERROR! Cannot have unclosed parentheses!")
            else:
                i += 1

        return tokens

    def process_expression_tokens(self, tokens, should_handle_parentheses=True):
        """
        Processes the tokenized expression by handling parentheses, 
        multiplication, division, addition, and subtraction.

        Args:
            tokens (list): A list of numbers and operators.
            should_handle_parentheses (bool): Whether to process parentheses.

        Returns:
            The result of the processed expression.
        """
        if should_handle_parentheses:
            tokens = self._handle_parentheses(tokens)

        # Handle multiplication and division
        self._handle_multiplication_division(tokens)

        # Handle addition and subtraction
        self._handle_subtraction_addition(tokens)

        return tokens[0]  # The only thing left should be the result
