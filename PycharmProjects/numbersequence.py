def convert_to_list_and_tuple():

    user_input = input("Enter numbers separated by comma: ")

    try:
        data = [int(number) for number in user_input.split(",")]

        data_list = [str(number) for number in data]

        data_tuple = tuple(data_list)

        print(data_list)
        print(data_tuple)

    except ValueError:
        print("Error: Invalid input. Please enter numbers separated by spaces.")

convert_to_list_and_tuple()


