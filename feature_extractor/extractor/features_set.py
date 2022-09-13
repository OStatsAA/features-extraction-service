"""FeaturesSet Module"""

from dataclasses import dataclass

@dataclass(init=False)
class FeaturesSet:
    """Class to hold features extracted from a dataset."""
    rows_count: int = 0
    total_variables_count: int = 0
    explanatory_variables_count: int = 0
    ratio_of_continous_variables: float = 0
    ratio_of_categorical_variables: float = 0
    response_variables_count: int = 0
    is_response_continous: bool = False
    is_response_dichotomous: bool = False
