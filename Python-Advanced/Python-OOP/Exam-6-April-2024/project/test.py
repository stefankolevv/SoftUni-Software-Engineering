from influencer_manager_app import InfluencerManagerApp

manager = InfluencerManagerApp()

# Register influencers
print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 50000, 4.2))
print(manager.register_influencer("StandardInfluencer", "JaneSmith", 10000, 3.5))
print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 80000, 4.2))
print(manager.register_influencer("InvalidInfluencer", "JohnDoe", 50000, 4.2))
print(manager.register_influencer("StandardInfluencer", "AliceJohnson", 20000, 3.8))
print(manager.register_influencer("PremiumInfluencer", "OliviaBennett", 80000, 4.5))
print(manager.register_influencer("PremiumInfluencer", "DanielRodriguez", 90000, 4.8))
print(manager.register_influencer("PremiumInfluencer", "EmilyTurner", 1000000, 5.0))

# Create campaigns
print(manager.create_campaign("LowBudgetCampaign", 1, "TechGurus", 4.0))
print(manager.create_campaign("HighBudgetCampaign", 2, "FashionTrendz", 3.0))
print(manager.create_campaign("LowBudgetCampaign", 1, "FashionTrendz", 3.0))
print(manager.create_campaign("LowBudgetCampaign", 3, "QuantumFusion", 3.0))
print(manager.create_campaign("InvalidCampaign", 4, "FoodieDelights", 2.5))

# Participate in campaigns
print(manager.participate_in_campaign("JohnDoe", 1))
print(manager.participate_in_campaign("JaneSmith", 2))
print(manager.participate_in_campaign("AliceJohnson", 2))
print(manager.participate_in_campaign("AliceJohnson", 1))
print(manager.participate_in_campaign("NonExistentInfluencer", 1))
print(manager.participate_in_campaign("AliceJohnson", 3))
print(manager.participate_in_campaign("JohnDoe", 2))
print(manager.participate_in_campaign("JaneSmith", 4))
print(manager.participate_in_campaign("JaneSmith", 1))
print(manager.participate_in_campaign("OliviaBennett", 3))
print(manager.participate_in_campaign("DanielRodriguez", 3))
print(manager.participate_in_campaign("EmilyTurner", 3))

# Print influencer campaign reports and campaign statistics
print(manager.influencer_campaign_report("JohnDoe"))
print(manager.influencer_campaign_report("JaneSmith"))
print(manager.campaign_statistics())
