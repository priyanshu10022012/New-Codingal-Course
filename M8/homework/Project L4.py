class ExpressionSolver:
    def __init__(self, expression):
        self._expression = expression
    def set_expression(self, expression):
        self._expression = expression
    def get_expression(self):
        return self._expression
    def solve(self):
        try:
            result = eval(self._expression)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
if __name__ == "__main__":
    exp = input("Enter a mathematical expression : ")
    solver = ExpressionSolver(exp)
    print("Expression:", solver.get_expression())
    print("Result:", solver.solve())
