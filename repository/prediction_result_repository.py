from repository.client.pg_client import pg_client


class PredictionResultRepository:

    def __init__(self, client):
        self.client = client

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS prediction_results (
            date date,
            model_version text,
            valid_race integer,
            win_count integer,
            win_winning_amount integer,
            place_count integer,
            place_winning_amount integer,
            exacta_count integer,
            exacta_winning_amount integer,
            quinella_count integer,
            quinella_winning_amount integer,
            quinella_place_count integer,
            quinella_place_winning_amount integer,
            trio_count integer,
            trio_winning_amount integer,
            trifecta_count integer,
            trifecta_winning_amount integer
        )
        """
        self.client.execute(sql)
        print('prediction_results table created (or already exists).')

    def insert(self, prediction_result):
        sql = "INSERT INTO prediction_results VALUES %s"
        insert = (prediction_result.date,
                  prediction_result.model_version,
                  prediction_result.valid_race,
                  prediction_result.win_count,
                  prediction_result.win_winning_amount,
                  prediction_result.place_count,
                  prediction_result.place_winning_amount,
                  prediction_result.exacta_count,
                  prediction_result.exacta_winning_amount,
                  prediction_result.quinella_count,
                  prediction_result.quinella_winning_amount,
                  prediction_result.quinella_place_count,
                  prediction_result.quinella_place_winning_amount,
                  prediction_result.trio_count,
                  prediction_result.trio_winning_amount,
                  prediction_result.trifecta_count,
                  prediction_result.trifecta_winning_amount)

        self.client.execute(sql, (insert, ))
        print('prediction result data are inserted.')


prediction_result_repository = PredictionResultRepository(pg_client)
