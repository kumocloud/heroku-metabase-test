class PredictionResult:

    def __init__(self, date, model_version, valid_race,
                 win_count, win_winning_amount, place_count, place_winning_amount,
                 exacta_count, exacta_winning_amount, quinella_count, quinella_winning_amount,
                 quinella_place_count, quinella_place_winning_amount,
                 trio_count, trio_winning_amount, trifecta_count, trifecta_winning_amount):
        self.date = date
        self.model_version = model_version
        self.valid_race = valid_race
        self.win_count = win_count
        self.win_winning_amount = win_winning_amount
        self.place_count = place_count
        self.place_winning_amount = place_winning_amount
        self.exacta_count = exacta_count
        self.exacta_winning_amount = exacta_winning_amount
        self.quinella_count = quinella_count
        self.quinella_winning_amount = quinella_winning_amount
        self.quinella_place_count = quinella_place_count
        self.quinella_place_winning_amount = quinella_place_winning_amount
        self.trio_count = trio_count
        self.trio_winning_amount = trio_winning_amount
        self.trifecta_count = trifecta_count
        self.trifecta_winning_amount = trifecta_winning_amount
