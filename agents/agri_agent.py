from agents.tools.rag_tool import rag_tool
from agents.tools.predict_tool import predict_yield
from agents.tools.eda_tool import eda_summary

class YieldAgent:
    def route(self, query):
        """
        Simple intent routing
        """
        q = query.lower()

        if "predict" in q or "forecast" in q:
            return "predict"

        if "summary" in q or "overview" in q or "eda" in q:
            return "eda"

        return "rag"

    def run(self, query, features= None):
        intent = self.route(query)

        if intent == "predict":
            if not features:
                raise ValueError("Features required for prediction")
            return predict_yield(features)

        """if intent == "eda":
            return eda_summary()"""

        return rag_tool(query)


if __name__ == "__main__":
    agent = YieldAgent()

    print(agent.run("What is the yield of wheat in the north?"))

    print(agent.run(
        "Predict yield for this season",
        features={
            "rainfall": 110,
            "temperature": 23,
            "region": 1,
            "crop": 0
        }
    ))

    print(agent.run("Give me a dataset overview"))

