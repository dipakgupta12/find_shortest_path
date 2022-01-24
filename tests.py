from find_path import FindShortestPath

FILENAME = "graph.csv"
START_NODE = "A"
GOAL_NODE = "D"


def test_with_details():
    print("========= Test with right details =========\n")
    fsp = FindShortestPath(
        start_node=START_NODE,
        goal_node=GOAL_NODE,
        file_name=FILENAME
    )
    assert fsp.result() == True
    print("\n====== Executed Successfully ==============================\n\n")


def test_with_wrong_file_details():
    print("========= Test with wrong filename =========\n")
    fsp = FindShortestPath(
        start_node=START_NODE,
        goal_node=GOAL_NODE,
        file_name="wrong_file.csv"
    )
    assert fsp.result() == False
    print("\n====== Executed Successfully ==============================\n\n")

def test_with_same_goals():
    print("========= Test with same goal values =========\n")
    fsp = FindShortestPath(
        start_node=START_NODE,
        goal_node=START_NODE,
        file_name=FILENAME
    )
    assert fsp.result() == False
    print("\n====== Executed Successfully ==============================\n\n")

def test_with_non_existing_paths():
    print("========= Test with non-existing paths =========\n")
    fsp = FindShortestPath(
        start_node="Z",
        goal_node="L",
        file_name=FILENAME
    )
    assert fsp.result() == False
    print("\n====== Executed Successfully ==============================\n\n")

if __name__ == "__main__":
    test_functions = [
        test_with_details,
        test_with_wrong_file_details,
        test_with_same_goals,
        test_with_non_existing_paths
    ]

    for func in test_functions:
        func()