from deferred_acceptance.deferred_acceptance import deferred_acceptance
from deferred_acceptance.utils import create_dataframes


def simple_school_choice() -> None:
    """
    Here is a minimalistic example of deferred acceptance algorithm for school choice.
    """
    # Prepare the dataframes
    students_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    schools_list = ["BRW", "COL", "CRN", "DRT", "HAR", "PEN", "PTN", "YLE"]
    students_preferences = {
        "a": [3, 1, 6, 7, 5, 8, 4, 2],
        "b": [6, 5, 1, 7, 2, 4, 3, 8],
        "c": [3, 2, 4, 6, 8, 7, 5, 1],
        "d": [7, 5, 4, 6, 8, 2, 1, 3],
        "e": [7, 4, 5, 3, 2, 6, 1, 8],
        "f": [2, 5, 3, 8, 1, 7, 6, 4].
        "g": [5, 1, 3, 2, 8, 7, 4, 6], 
        "h": [1, 8, 2, 6, 7, 4, 3, 5]
    }
    schools_preferences = {"BRW": [2, 6, 4, 1, 7, 8, 5, 3], 
                           "COL": [8, 7, 3, 6, 5, 2, 1, 4], 
                           "CRN": [3, 8, 1, 4, 5, 7, 2, 6], 
                           "DRT": [8, 2, 6, 7, 3, 4, 1, 5], 
                           "HAR": [8, 4, 6, 2, 3, 5, 1, 7], 
                           "PEN": [4, 1, 3, 8, 2, 6, 5, 7], 
                           "PTN": [1, 8, 4, 7, 3, 6, 2, 5], 
                           "YLE": [5, 3, 1, 7, 4, 6, 2, 8]}

    students_df, schools_df = create_dataframes(
        students_list=students_list,
        students_preferences=students_preferences,
        schools_list=schools_list,
        schools_preferences=schools_preferences,
    )

    # Run the algorithm
    schools_quota = {"A": 1, "B": 2, "C": 1}
    matches = deferred_acceptance(
        students_df=students_df, schools_df=schools_df, schools_quota=schools_quota
    )

    print(matches)


if __name__ == "__main__":
    simple_school_choice()
