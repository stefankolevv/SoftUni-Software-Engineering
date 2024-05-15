from influencers.base_influencer import BaseInfluencer

class PremiumInfluencer(BaseInfluencer):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)
        self.payment_percentage = 0.85

    def calculate_payment(self, campaign):
        return campaign.budget * self.payment_percentage

    def reached_followers(self, campaign_type):
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.5)
        elif campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.8)