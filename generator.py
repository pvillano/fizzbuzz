#!/usr/bin/env python
# preamble, line start, line end, post-amble
c = ("fizzbuzz.c", "#include<stdio.h>\n\nint main(){\n", "    printf(\"", "\");\n", "}")
cplusplus = ("fizzbuzz.cpp", "#include <iostream>\n\nint main(){\n", "    std::cout << \"", "\";\n", "}")
java = ("FizzBuzz.java", "public class fizzbuzz {\n    public static void main(String[] args) {\n",
        "        System.out.println(\"", "\");\n", "    }\n}")
javascript = ("FizzBuzz.js", "", "console.log(\"", "\");\n", "")
kotlin = ("FizzBuzz.kt", "fun main(args : Array<String>) {\n", "    println(\"", "\")\n", "}")
python27 = ("FizzBuzz27.py", "#!/usr/bin/env python\n", "print \"", "\"\n", "")
python35 = ("FizzBuzz35.py", "#!/usr/bin/env python\n", "print(\"", "\")\n", "")

languages = [c, cplusplus, java, javascript, kotlin, python27, python35]

for language in languages:
    with open(language[0], mode='w') as f:
        f.write(language[1])
        for i in range(1, 10001):
            f.write(language[2])
            if i % 3 == 0: f.write("fizz")
            if i % 5 == 0: f.write("buzz")
            if i % 3 and i % 5: f.write(str(i))
            f.write(language[3])
        f.write(language[4])
