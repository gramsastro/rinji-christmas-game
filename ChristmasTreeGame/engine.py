import random

class ChristmasTreeGame:
    def __init__(self):
        # Numbers on the Christmas tree (1–25)
        self.tree_numbers = list(range(1, 26))

        # Prize distribution
        self.prizes = {
            "CASH_1000": 1,   # One ₦1,000 cash prize
            "CASH_500": 2,    # Two ₦500 cash prizes
            "CASH_200": 4,    # Four ₦200 cash prizes
            "DATA_1GB": 5,    # Five 1GB MTN data prizes
            "DATA_500MB": 6,  # Six 500MB MTN data prizes
            "TRY_AGAIN": 7    # Seven "Try Again" slots
        }

        # Game board and player tracking
        self.board = {}
        self.players = {}

        # Generate the board with randomized prizes
        self._generate_board()

    def _generate_board(self):
        prize_pool = []
        for prize, count in self.prizes.items():
            prize_pool += [prize] * count
        random.shuffle(prize_pool)

        for i, number in enumerate(self.tree_numbers):
            self.board[number] = prize_pool[i]

    def pick_number(self, player_id, number):
        # Validate number
        if number not in self.tree_numbers:
            return "Invalid number. Choose between 1 and 25."

        # Prevent duplicate picks
        if number in self.players.get(player_id, []):
            return "You already picked this number."

        # Reveal prize
        prize = self.board[number]

        # Track player’s choice
        if player_id not in self.players:
            self.players[player_id] = []
        self.players[player_id].append(number)

        return f"You picked 🎄 {number}! Prize: {self._format_prize(prize)}"

    def _format_prize(self, prize):
        mapping = {
            "CASH_1000": "₦1,000 CASH",
            "CASH_500": "₦500 CASH",
            "CASH_200": "₦200 CASH",
            "DATA_1GB": "1GB MTN DATA",
            "DATA_500MB": "500MB MTN DATA",
            "TRY_AGAIN": "Try Again 😅"
        }
        return mapping.get(prize, prize)

    def reveal_board(self):
        # Debugging: see all prizes behind numbers
        return self.board

