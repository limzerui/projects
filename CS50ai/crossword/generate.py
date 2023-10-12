import sys
from collections import deque

from crossword import *

class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        } # note that self.domains is a dictionary

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]: #note that .structure returns true or false depends if sth is there
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        for var in self.domains:
            for value in self.domains[var].copy():
                if len(value) != var.length:
                    self.domains[var].remove(value)

    def revise(self, x, y):
        revised=False

        overlap = self.crossword.overlaps[x,y] 

        if overlap:
            i, j = overlap
            for word_x in self.domains[x].copy():
                check_if_overlap=False
                for word_y in self.domains[y]:
                    if word_x[i]==word_y[j]:
                        check_if_overlap=True
                if not check_if_overlap: #so if check_if_overlap is true, then it wont run.only if its false whereby the letters(where they overlap) are not the same
                    self.domains[x].remove(word_x)
                    revised=True

        return revised
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

    def ac3(self, arcs=None):

        # if arcs is none
        if arcs is None:
            arcs=[]
            for var in self.crossword.variables:
                for neighbor in self.crossword.neighbors(var):
                    arcs.append((var, neighbor))
        else:
            arcs=deque(arcs) #note: explaination of deque: if arcs parameter is provided, the code converts the arcs list into a deque using arcs = deque(arcs). This is done to enable efficient append and pop operations from both ends of the queue.allows for easy addition and removal of elements from both ends of the collection. This helps in efficiently exploring and enforcing arc-consistency in constraint satisfaction problems
        
        while arcs:
            x,y = arcs.pop()
            if self.revise(x,y):
                if len(self.domains[x]) == 0:
                    return False
                for z in self.crossword.neighbors(x) - {y}:
                    arcs.append((z,x))
        return True


        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

    def assignment_complete(self, assignment):
        for variable in self.crossword.variables:
            if variable not in assignment.keys():
                return False
            if assignment[variable] not in self.crossword.words:
                return False
        return True
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

    def consistent(self, assignment):
        #values of a variable are distinct, correct length, no conflicts between neighboring
        for var, word in assignment.items():
            #check correct length
            if var.length != len(word):
                return False
            #check if all values are distinct
            for key, value in assignment.items():
                if key != var:
                    if word ==value:
                        return False
            #check if there are no conflicts between neighboring variables
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment.keys():
                    i, j = self.crossword.overlaps[var, neighbor]
                    if neighbor in assignment:
                        if word[i] != assignment[neighbor][j]:
                            return False
                        
        return True
    

        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        raise NotImplementedError

    def order_domain_values(self, var, assignment):
        heuristics = {}
        for word in self.domains[var]:
            if word not in assignment:
                ruled_out=0
                for neighbor in self.crossword.neighbors(var):
                    if word in self.domains[neighbor]:
                        ruled_out+=1
                
                heuristics[word] = ruled_out
        return sorted(heuristics, key=lambda x: heuristics[x])

        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        #degree would mean the most neighbours
        def degree(var):
            return len(self.crossword.neighbors(var))
        def domain(var):
            return len(self.domains[var])
        
        unassigned=[]
        for var in self.crossword.variables:
            if var not in assignment:
                unassigned.append(var)
        
        result_var=unassigned[0]
        for var in unassigned:
            if result_var != var:
                if domain(result_var) > domain(var):
                    result_var=var
                elif domain(result_var) == domain(var):
                    if degree(var) >= degree(result_var):
                        result_var=var
        return result_var
        
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

    def backtrack(self, assignment):


        if self.assignment_complete(assignment):
            return assignment

        unassigned_var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(unassigned_var, assignment):
            assignment[unassigned_var]=value
            if self.consistent(assignment):
                result = self.backtrack(assignment)
            if result:
                return result
            del assignment[unassigned_var]
        return None
        




        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
