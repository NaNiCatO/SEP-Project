def test():
    input_str = "create task test detail testing due date M7 2024 time 10:30 urgent"

    if "task" in input_str:
        name_index = input_str.find("task")
    elif "name" in input_str:
        name_index = input_str.find("name")

    if "detail" in input_str:
        detail_index = input_str.find("detail")
    elif "details" in input_str:
        detail_index = input_str.find("details")

    if "due" in input_str:
        due_date_index = input_str.find("due")
    elif "date" in input_str:
        due_date_index = input_str.find("date")


    if "time" in input_str:
        time_index = input_str.find("time")
    elif "at" in input_str:
        time_index = input_str.find("at")

    print("name :", input_str[name_index + 5: detail_index])
    print("detail :", input_str[detail_index + 7: due_date_index])
    print("due date :", input_str[due_date_index + 4: time_index])
    print("time :", input_str[time_index + 4:])