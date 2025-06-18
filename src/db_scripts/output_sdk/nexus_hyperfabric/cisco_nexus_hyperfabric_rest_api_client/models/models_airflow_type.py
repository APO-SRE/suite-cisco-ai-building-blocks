from enum import Enum


class ModelsAirflowType(str, Enum):
    AIRFLOW_TYPE_PORT_SIDE_EXHAUST = "AIRFLOW_TYPE_PORT_SIDE_EXHAUST"
    AIRFLOW_TYPE_PORT_SIDE_INTAKE = "AIRFLOW_TYPE_PORT_SIDE_INTAKE"

    def __str__(self) -> str:
        return str(self.value)
