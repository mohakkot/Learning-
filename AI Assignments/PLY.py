import ply.lex
import ply.yacc

def ply_parse(text):

    keywords = {"true": "TRUE", "false": "FALSE"}
    tokens = (["SYMBOL", "COMMA", "LPAREN", "RPAREN",
               "EQUALS", "NOT", "AND", "OR", "IMPLIES"] +
              list(keywords.values()))

    def t_SYMBOL(t):
        r"[a-zA-Z]\w*"
        t.type = keywords.get(t.value, "SYMBOL")
        return t

    t_EQUALS = r"="
    t_NOT = r"~"
    t_AND = r"&"
    t_OR = r"\|"
    t_IMPLIES = r"=>"
#    t_COLON = r":"
    t_COMMA = r","
    t_LPAREN = r"\("
    t_RPAREN = r"\)"

    t_ignore = " \t\n"

    def t_newline(t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_error(t):
        line = t.value.lstrip()
        i = line.find("\n")
        line = line if i == -1 else line[:i]
        raise ValueError("Syntax error, line {0}: {1}"
                         .format(t.lineno + 1, line))

#    def p_formula_quantifier(p):
#        """FORMULA : FORALL SYMBOL COLON FORMULA
#                   | EXISTS SYMBOL COLON FORMULA"""
#        p[0] = [p[1], p[2], p[4]]

    def p_formula_binary(p):
        """FORMULA : FORMULA IMPLIES FORMULA
                   | FORMULA OR FORMULA
                   | FORMULA AND FORMULA"""
        p[0] = [p[1], p[3]]

    def p_formula_not(p):
        "FORMULA : NOT FORMULA"
        p[0] = [p[1], p[2]]

    def p_formula_boolean(p):
        """FORMULA : FALSE
                   | TRUE"""
        p[0] = p[1]

    def p_formula_group(p):
        "FORMULA : LPAREN FORMULA RPAREN"
        p[0] = p[2]

    def p_formula_symbol(p):
        "FORMULA : SYMBOL"
        p[0] = p[1]

    def p_formula_equals(p):
        "FORMULA : TERM EQUALS TERM"
        p[0] = [p[1], p[2], p[3]]

    def p_formula_or(p):
        "FORMULA : TERM OR TERM"
        p[0] = [p[1], p[2], p[3]]

    def p_formula_and(p):
        "FORMULA : TERM AND TERM"
        p[0] = [p[1], p[2], p[3]]

    def p_term(p):
        """TERM : LPAREN SYMBOL LPAREN TERMLIST RPAREN RPAREN
                | SYMBOL"""
        p[0] = p[1] if len(p) == 2 else [p[1], p[3]]

    def p_termlist(p):
        """TERMLIST : TERM COMMA TERMLIST
                    | TERM"""
        p[0] = p[1] if len(p) == 2 else [p[1], p[3]]

    def p_error(p):
        if p is None:
            raise ValueError("Unknown error")
        raise ValueError("Syntax error, line {0}: {1}".format(
            p.lineno + 1, p.type))

    # from lowest to highest precedence!
    precedence = (("right", "IMPLIES"),
                  ("left", "OR"),
                  ("left", "AND"),
                  ("right", "NOT"),
                  ("nonassoc", "EQUALS"))

    lexer = ply.lex.lex()
    parser = ply.yacc.yacc()
    try:
        return parser.parse(text, lexer=lexer)
    except ValueError as err:
        print(err)
        return []


print(ply_parse("C(m) & (A(x,y) | B(z))"))