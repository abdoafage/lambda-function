import time


def execute_python_code(code, nameOfFunction, params):
    # print("code:", code)
    try:
        # Create a dictionary to hold the global and local variables
        namespace = {}

        start_time = time.time()

        # Execute the code within the given namespace
        exec(code, namespace)
        # print(namespace)
        # Get the output from the namespace
        func = namespace.get(f"{nameOfFunction}", "")

        # run the functionand pass the params.
        output = func(**params)

        end_time = time.time()

        # Calculate the execution time
        execution_time = end_time - start_time

        # print(output)

        return {"status": True, "message": output, "execution_time": execution_time}

    except Exception as e:
        print(e)
        return {"status": False, "message": str(e), "execution_time": 0}
