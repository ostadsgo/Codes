s = """
Python: Known for its readability and versatility, Python is widely used in data science, web development, machine learning, and automation.\n
JavaScript: The language of the web, JavaScript is essential for front-end development, server-side programming (Node.js), and game development.\n
Java: A versatile language used for enterprise applications, Android development, and web services.\n
C++: A powerful language for system programming, game development, and high-performance computing.\n
C: A low-level language often used for operating systems, embedded systems, and device drivers.\n
C#: A general-purpose language developed by Microsoft, primarily used for Windows applications, game development (Unity), and web development.\n
PHP: A popular language for web development, especially for creating dynamic websites and web applications.\n
SQL: A specialized language for interacting with databases, used for data management and retrieval.\n
Go (Golang): A modern language developed by Google, known for its simplicity, efficiency, and concurrency.\n
Ruby: A dynamic language often used for web development, especially with the Ruby on Rails framework.\n
Swift: Apple's programming language for iOS, macOS, watchOS, and tvOS development.\n
Kotlin: A modern language that can interoperate with Java, often used for Android development.\n
R: A statistical computing language widely used in data analysis, machine learning, and statistics.\n
Rust: A systems programming language known for its safety, speed, and memory efficiency.\n
TypeScript: A typed superset of JavaScript, often used for large-scale web applications.\n
Objective-C: A superset of C, used for iOS and macOS development before Swift became the primary language.\n
Perl: A general-purpose language often used for system administration and web development.\n
Scala: A functional programming language that runs on the JVM, often used for large-scale data processing and web applications.\n
Julia: A high-performance language designed for scientific computing and technical computing.\n
MATLAB: A proprietary language used for numerical computing, data analysis, and algorithm development.\n
Assembly Language: A low-level language that provides direct control over hardware, used for performance-critical applications.\n
Visual Basic .NET: A Microsoft language used for Windows applications, web development, and database access.\n
Dart: A language developed by Google, used for creating cross-platform applications with Flutter.\n
COBOL: A legacy language still used in many mainframe systems, especially in finance and government.\n
Fortran: A language used for scientific computing, especially in engineering and physics.\n
Pascal: A general-purpose language that influenced many other languages, including Modula-2 and Ada.\n
Delphi/Object Pascal: A modern version of Pascal, often used for Windows applications and database development.\n
Lisp: A family of functional programming languages, including Common Lisp and Scheme.\n
Prolog: A logic programming language used for artificial intelligence and natural language processing.\n
Lua: A lightweight language often embedded in other applications for scripting and customization.\n
Haskell: A pure functional programming language known for its type system and lazy evaluation.\n
F#: A functional programming language that runs on the .NET platform.\n
Erlang: A functional programming language designed for distributed and fault-tolerant systems.\n
Clojure: A functional programming language that runs on the JVM, often used for web development and data processing.\n
Groovy: A dynamic language that runs on the JVM, often used for scripting and web development.\n
APL: A language designed for array programming, often used for mathematical calculations and data analysis.\n
Smalltalk: A dynamic language that influenced many other object-oriented languages, including Java and Python.\n
Ada: A general-purpose language designed for embedded systems and real-time applications.\n
VHDL: A hardware description language used for designing digital circuits.\n
Verilog: Another hardware description language used for designing digital circuits.\n
ABAP: A language used for SAP ERP systems.\n
PL/SQL: A procedural language used for extending SQL with procedural constructs.\n
SAS: A statistical software suite that includes a programming language.\n
LabVIEW: A graphical programming language used for data acquisition, instrumentation, and control systems.\n
Bash: A shell scripting language used for automating tasks in Unix-like operating systems.\n
PowerShell: A scripting language used for automating tasks in Windows.\n
MATLAB: A proprietary language used for numerical computing, data analysis, and algorithm development.\n
Julia: A high-performance language designed for scientific computing and technical computing.\n
Rust: A systems programming language known for its safety, speed, and memory efficiency.\n
TypeScript: A typed superset of JavaScript, often used for large-scale web applications."""

f = open("lang.txt", "w")
for line in s.split("\n\n"):
    lang = line.split(":")[0]
    f.write(lang.strip()+"\n")
f.close()
