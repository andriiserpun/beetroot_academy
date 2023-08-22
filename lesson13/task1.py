import inspect
import keyword

def count_local_variables(func):
    source_lines = inspect.getsourcelines(func)[0]
    variable_count = 0
    for line in source_lines:
        line = line.strip()
        if line.startswith("def "):
            continue
        if not line or line.startswith("#"):
            continue
        if line.startswith(("class ", "if ", "else ", "while ", "for ", "with ", "try ", "except ", "return ")):
            continue
        words = line.split()
        for word in words:
            if word.isidentifier() and not keyword.iskeyword(word):
                variable_count += 1
    return variable_count

def example_function():
    a = 10
    b = 20
    c = a + b
    print(c)

def main():
    func = example_function
    var_count = count_local_variables(func)
    print(f"Estimated number of local variables in '{func.__name__}': {var_count}")

if __name__ == "__main__":
    main()
