import streamlit as st

st.title("Simple Calculator")

st.write("Select an operation from below:")

operator = st.selectbox(
    "Choose Operator",
    ["+", "-", "*", "/"]
)

# ADDITION
if operator == "+":
    values = st.text_input(
        "Enter values separated by comma",
        placeholder="Example: 10,20,30,40"
    )

    if st.button("Calculate Addition"):
        try:
            splitted_vals = values.split(",")

            result = sum([
                float(val.strip())
                for val in splitted_vals
            ])

            st.success(
                f"Addition of all the given values = {result}"
            )

        except ValueError:
            st.error("Please enter valid numbers separated by commas.")


# SUBTRACTION
elif operator == "-":

    num1 = st.number_input(
        "Enter first number",
        value=0.0
    )

    num2 = st.number_input(
        "Enter second number",
        value=0.0
    )

    if st.button("Calculate Subtraction"):

        st.success(
            f"{num1} - {num2} = {num1 - num2}"
        )

        st.success(
            f"{num2} - {num1} = {num2 - num1}"
        )


# MULTIPLICATION
elif operator == "*":

    values = st.text_input(
        "Enter values separated by comma",
        placeholder="Example: 2,3,4,5"
    )

    if st.button("Calculate Multiplication"):

        try:
            splitted_vals = values.split(",")

            val_list = [
                float(val.strip())
                for val in splitted_vals
            ]

            result = 1

            for i in val_list:
                result = result * i

            st.success(
                f"Multiplication of all the given values = {result}"
            )

        except ValueError:
            st.error(
                "Please enter valid numbers separated by commas."
            )


# DIVISION
elif operator == "/":

    num1 = st.number_input(
        "Enter first number",
        value=0.0,
        key="division_num1"
    )

    num2 = st.number_input(
        "Enter second number",
        value=0.0,
        key="division_num2"
    )

    if st.button("Calculate Division"):

        if num2 != 0:

            st.success(
                f"{num1} / {num2} = {num1 / num2}"
            )

        else:

            st.error(
                "You cannot divide by zero. Please try again."
            )


st.divider()

st.write("Thank you for using the calculator.")