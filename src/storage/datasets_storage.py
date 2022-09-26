import pandas as pd

def get_data_from_storage(dataset_id: str) -> pd.DataFrame:
    """Gets data given dataset_id

    Args:
        dataset_id (str): Dataset ID

    Returns:
        pd.DataFrame: Pandas Dataframe
    """
    return pd.read_hdf(dataset_id + '.h5', key='dataset', mode='r')