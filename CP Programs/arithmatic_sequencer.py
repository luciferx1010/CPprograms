def arithmetic_arranger(problems, show_result=False):
    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        # Split the problem into operands and operator
        operand1, operator, operand2 = problem.split()

        # Check if the operands are numeric
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Only numeric values are allowed."

        # Check if the operator is valid
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        # Calculate the result if requested
        result = str(int(operand1) + int(operand2)) if operator == '+' else str(int(operand1) - int(operand2))

        # Determine the maximum length of operands for alignment
        max_length = max(len(operand1), len(operand2))

        # Build the lines of the arranged problem
        line1 += operand1.rjust(max_length + 2)
        line2 += operator + operand2.rjust(max_length + 1)
        line3 += '-' * (max_length + 2)
        line4 += result.rjust(max_length + 2) if show_result else ' ' * (max_length + 2)

        # Add spacing between problems
        line1 += '    '
        line2 += '    '
        line3 += '    '
        line4 += '    '

    # Combine the lines into the final arrangement
    arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() + '\n' + line4.rstrip()

    return arranged_problems
