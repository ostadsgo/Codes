s = """
CS 2xx: Math I

CS 2xx: Physics I

CS 2xx: English for Computing
CS 10x: Fundamentals of Computer Science
CS 11x: Programming Fundamentals

CS 12x: Computer Fundamentals


CS 2xx: Math II

CS 2xx: Physics II

CS 10x: Foundation of Mathematics

CS 11x: Programming in C

CS 12x: Digital Design

CS 2xx: Differential Equation

CS 10x: Foundation of Combinatorics

CS 10x: Introduction to Logic and Set Theory

CS 11x: Data Structures and Algorithms

CS 11x: Object Oriented Programming

CS 12x: Computer Architecture 

CS 10x: Foundation of Matrix and Linear Algebra

CS 10x: Introduction to Theory of Computation 

CS 10x: Foundation of Mathematical (Real) Analysis

CS 11x: Functional Programming

CS 11x: Algorithms Design and Analysis

CS 12x: Microprocessors 

CS 10x: Foundation of Numerical Analysis

CS 10x: Statistics Methods

CS 11x: Operating Systems

CS 11x: Programming Languages

CS 11x: Database Design
CS 14x: Linear Algebra
CS 10x: Foundation of Algebra

CS 10x: Probability Fundamentals

CS 11x: Graph Theory and its Applications

CS 11x: Compiler Construction 

CS 11x: Software Design

CS 2xx: Research Method and Documentation



CS 11x: Linear Optimization 

CS 11x: Software Engineering 

CS 13x: Computer Network

CS 14x: Artificial Intelligence 

CS 14x: Introduction to Data Mining

CS 14x: Computer Graphics

CS 11x: Web Programming

CS 11x: Parallel and Distributed Computing

CS 11x: Human-Computer Interaction

CS 14x: Machine Learning

CS 14x: Natural Language Processing

CS 14x: Modern Information Retrieval

CS 13x: Cybersecurity
"""

courses = [course for course in s.split("\n") if course]

courses = [course.split(":")[-1] for course in courses]
print(courses)
s = "\n".join(courses)
print(s)

print(len(s.split("\n")))
