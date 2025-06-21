class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        loss_count = defaultdict(int)

        for winner, loser in matches:
            if winner not in loss_count:
                loss_count[winner] = 0
            loss_count[loser] += 1

        zero_losses = []
        one_loss = []

        for player in loss_count:
            if loss_count[player] == 0:
                zero_losses.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)

        return [sorted(zero_losses), sorted(one_loss)]
