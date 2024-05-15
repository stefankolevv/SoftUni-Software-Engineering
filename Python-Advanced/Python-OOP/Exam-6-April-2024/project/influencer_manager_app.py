from campaigns.high_budget_campaign import HighBudgetCampaign
from campaigns.low_budget_campaign import LowBudgetCampaign
from influencers.premium_influencer import PremiumInfluencer
from influencers.standard_influencer import StandardInfluencer

class InfluencerManagerApp:
    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in ("PremiumInfluencer", "StandardInfluencer"):
            return f"{influencer_type} is not an allowed influencer type."
        for influencer in self.influencers:
            if influencer.username == username:
                return f"{username} is already registered."
        influencer = PremiumInfluencer(username, followers, engagement_rate) if influencer_type == "PremiumInfluencer" else \
                    StandardInfluencer(username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in ("HighBudgetCampaign", "LowBudgetCampaign"):
            return f"{campaign_type} is not a valid campaign type."
        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."
        campaign = HighBudgetCampaign(campaign_id, brand, required_engagement) if campaign_type == "HighBudgetCampaign" else \
                   LowBudgetCampaign(campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = next((inf for inf in self.influencers if inf.username == influencer_username), None)
        if influencer is None:
            return f"Influencer '{influencer_username}' not found."
        campaign = next((camp for camp in self.campaigns if camp.campaign_id == campaign_id), None)
        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."
        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."
        payment = influencer.calculate_payment(campaign)
        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."
        else:
            return ""

    def calculate_total_reached_followers(self):
        total_followers = {}
        for campaign in self.campaigns:
            reached_followers = sum(inf.reached_followers(type(campaign).__name__) for inf in campaign.approved_influencers)
            if reached_followers > 0:
                total_followers[campaign] = reached_followers
        return total_followers

    def influencer_campaign_report(self, username: str):
        influencer = next((inf for inf in self.influencers if inf.username == username), None)
        if influencer is None:
            return ""
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda camp: (len(camp.approved_influencers), -camp.budget))
        report = ""
        for campaign in sorted_campaigns:
            total_followers = sum(inf.reached_followers(type(campaign).__name__) for inf in campaign.approved_influencers)
            report += f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, " \
                      f"Total budget: ${campaign.budget:.2f}, Total reached followers: {total_followers}\n"
        return f"$$ Campaign Statistics $$\n{report}"