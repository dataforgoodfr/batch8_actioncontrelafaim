# inspired from: https://stackoverflow.com/a/38409774/8086033
from pathlib import Path
import inspect

import yaml

class sources:
    def __init__(self, abs_root):
        # WFP Hunger Covid Snapshots
        self.wfp_hunger_covid_snapshots_overview_url = "https://static.hungermapdata.org/hungermap/reports/hunger_covid_weekly_snapshot.pdf"
        self.wpf_hunger_covid_snapshots_overview_path = abs_root / "./data/sources/hunger_covid_weekly_snapshot.pdf"
        self.wfp_hunger_covid_snapshots_hyperlinks_mapping_path = abs_root / "./data/meta/wfp_hunger_covid_snapshots_hyperlinks_mapping.csv"
        self.wfp_hunger_covid_weekly_snapshots_folder_path = abs_root / "./data/clean/wfp_hunger_covid_weekly_snapshots/"
        self.wfp_hunger_covid_weekly_snapshots_metadata_path = self.wfp_hunger_covid_weekly_snapshots_folder_path / "snapshots_metadata.csv"

        # IPC Alerts Acute Food Insecurity
        self.ipc_alerts_url = "http://www.ipcinfo.org/ipcinfo-website/resources/alerts-archive/en/"
        self.ipc_alerts_folder_path = abs_root / "./data/clean/ipc_alerts_acute_food_insecurity/"
        self.ipc_alerts_metadata_path = self.ipc_alerts_folder_path / "ipc_alerts_metadata.csv"

        # WAS6.11 diarrhoea cases below five years old
        self.was611_diarrhoea_cases_output_path = abs_root / "./data/clean/indic_was611_diarrhoea_careseeking_below_five.csv"
        self.was611_diarrhoea_output_folder_path = abs_root / "./data/sources/"
        self.was611_diarrhoea_dataset_name = "unicef-mnch-diarcare"
        self.was611_diarrhoea_ressource_index = 1

        # Food Security Portal API
        self.food_security_api_url = "http://www.foodsecurityportal.org/api/about/"
        self.food_security_url = "www.foodsecurityportal.org/"
        self.food_security_output_folder_path = abs_root / "./data/clean/food_security/"

        # Food and Agriculture Organization FAO
        self.fao_api_bulk_url = "http://fenixservices.fao.org/faostat/static/bulkdownloads/datasets_E.xml"
        self.fao_output_folder = abs_root / "./data/clean/FAO/"
        self.fao_metadata_csv_path = abs_root / "./data/meta/FAO_metadata.csv"


class meta:
    def __init__(self, abs_root):
        self.countries_ISO_3166_1_csv_path = abs_root / "./data/meta/countries - ISO 3166-1.csv"

class Config:
    def __init__(self, abs_root):
        self.notebooks_collection_path = abs_root / "src/notebooks/collection/"
        self.sources = sources(abs_root)
        self.meta = meta(abs_root)


project_absolute_root = Path(inspect.getfile(inspect.currentframe())).absolute().parent.parent
config = Config(project_absolute_root)
