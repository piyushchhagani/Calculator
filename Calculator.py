import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler("calculator.log",maxBytes=1000,backupCount=3)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def calculator():
    try:
        a = float(input("Number1: "))
        b = float(input("Number2: "))
        op = input("Operation to Perform (+, -, *, /): ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = divide(a, b)
        else:
            raise ValueError("Invalid operator")

        print("Output:", result)
        logger.info(f"{a} {op} {b} = {result}")

    except ValueError as v:
        print("Value Error:", v)
        logger.error(v)

    except ZeroDivisionError as zero:
        print("Zero Division Error:", zero)
        logger.error(zero)

    except Exception as e:
        print("Unexpected Error:", e)
        logger.error(e)

    finally:
        print("Operation Successfully Done!!")

calculator()
logging.shutdown()
