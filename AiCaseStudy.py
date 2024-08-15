class CompanyReport:
    def __init__(self, title, overview, Business_activities, landscape, results, recommendations):
        self.title =title
        self.overview =overview
        self.business_activities =Business_activities
        self.landscape =landscape
        self.results = results
        self.recommendations =recommendations

    def display(self):
        print(f"# {self.title}**\n")

        print("n## Overview and Origin\n")
        for key, value in self.overview.items():
            print(f"* **{key}:** {value}")

        print("\n## business.activities\n")
        for key, value in self.business.activities.items():
            print(f"* **{key}:** {value}")

        print("\n## landscape\n")
        for key, value in self.landscape.items():
            print(f"* **{key}:** {value}")

        print("\n## results\n")
        for key, value in self.results.items():
            print(f"* **{key}:** {value}")

        print("\n## recommendations\n")
        for key, value in self.recommendations.items():
            print(F"* **{key}:** {value}")

CompanyReport = CompanyReport("OpenAI Case Study")

CompanyReport.set_overview(
    name="OpenAI",
    incorporation_date="December 11, 2015",
    founders=["Elon Musk", "Sam Altman", "Greg Brockman", "Ilya Sutskever", "John Schulman", "Wojciech Zaremba"],
    idea_origin="The idea of OpenAI was born out of concerns about the potential dangers of artificial intelligence (AI) if misaligned with human values. The founders wanted to ensure that AI would be developed safely and benefit all of humanity.",
    funding_sources="Initially funded by private investors, including Elon Musk and other tech industry leaders. Later, it transitioned into a capped-profit model and recieved significant investments, including $1 billion from microsoft in 2019",
)