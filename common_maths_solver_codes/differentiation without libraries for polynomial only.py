def differentiate(expr):
    terms = expr.split("+")
    deriv_terms = []
    for term in terms:
        if "x" in term:
            coef, exp = term.split("x")
            if coef == "":
                coef = "1"
            if exp == "":
                exp = "1"
            coef = int(coef)
            exp = int(exp[1:]) if len(exp) > 1 else 1
            deriv_coef = coef * exp
            deriv_exp = exp - 1
            if deriv_coef != 0:
                if deriv_coef == 1:
                    deriv_term = (
                        "x^{}".format(deriv_exp)
                        if deriv_exp > 1
                        else "x"
                        if deriv_exp == 1
                        else "1"
                    )
                else:
                    deriv_term = (
                        "{}x^{}".format(deriv_coef, deriv_exp)
                        if deriv_exp > 1
                        else "{}x".format(deriv_coef)
                        if deriv_exp == 1
                        else "{}".format(deriv_coef)
                    )
                deriv_terms.append(deriv_term)
    return " + ".join(deriv_terms) if deriv_terms else "0"


expr = "6^4 + 7x^2 + 23x + 1"
deriv_expr = differentiate(expr)
print("The derivative of {} is {}".format(expr, deriv_expr))
